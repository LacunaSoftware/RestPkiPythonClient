# pylint: disable=missing-docstring
import hashlib
import requests
import simplejson as json

from distutils.version import StrictVersion
from six import BytesIO

from .apis import Apis
from .authentication import Authentication
from .blob_reference import BlobReference
from .rest_error import RestError
from .rest_pki_error import RestPkiError
from .rest_unreachable_error import RestUnreachableError
from .utils import _base64_encode_string
from .validation import ValidationResults
from .validation_error import ValidationError
from .version import __version__


def _get_api_version(client, api):
    v = client.rest_pki_version
    if v is None:
        v = client.try_get_endpoint_version(client.endpoint_url)

    if api == Apis.START_CADES:
        if v > StrictVersion("1.11"):
            return 3
        elif v > StrictVersion("1.10"):
            return 2
        else:
            return 1
    elif api == Apis.COMPLETE_CADES:
        if v > StrictVersion("1.11"):
            return 2
        else:
            return 1
    elif api == Apis.START_PADES:
        if v > StrictVersion("1.11"):
            return 2
        else:
            return 1
    elif api == Apis.COMPLETE_PADES:
        if v > StrictVersion("1.11"):
            return 2
        else:
            return 1
    elif api == Apis.MULTIPART_UPLOAD:
        if v > StrictVersion("1.11"):
            return 1
        else:
            return 0
    elif api == Apis.ADD_PDF_MARKS:
        if v > StrictVersion("1.13"):
            return 1
        else:
            return 0
    else:
        raise Exception("Unsupported operation.")


class RestPkiClient(object):

    def __init__(self, endpoint_url, access_token):
        self.__endpoint_url = endpoint_url
        self.__auth_token = access_token
        self.__multipart_upload_double_check = None
        self.__multipart_upload_threshold = 5 * 1024 * 1024  # 5 MB
        self.__rest_pki_version = None
        self.__endpoint_versions = {}

    def upload_or_read(self, file_desc):
        api_version = _get_api_version(self, Apis.MULTIPART_UPLOAD)
        if api_version == 0:
            return RestPkiClient._read(file_desc)
        return self._upload(file_desc)

    @staticmethod
    def _read(file_desc):
        return file_desc.read()

    def _upload(self, file_desc):

        # Begin the upload

        begin_url = self.__endpoint_url + 'Api/MultipartUploads'
        begin_response = requests.post(begin_url,
                                       headers=self.get_request_headers())
        self._check_response('GET', begin_url, begin_response)

        blob_token = begin_response.json().get('blobToken')
        blob_uri = "Api/MultipartUploads/%s" % blob_token
        part_size = begin_response.json().get('partSize')

        # Read the file part by part

        part_e_tags = []
        part_number = 0

        # Return to the start of the stream.
        file_desc.seek(0, 0)
        while True:
            buffer = file_desc.read(part_size)
            if buffer is None or len(buffer) == 0:
                # Reached end-of-file.
                break
            headers = self.get_request_headers()
            part_hash = hashlib.md5(buffer)
            headers['Content-MD5'] = _base64_encode_string(part_hash.digest())
            headers['Content-Type'] = 'application/octet-stream'
            part_url = '%s/%s' % (blob_uri, part_number)
            response = requests.post(self.__endpoint_url + part_url,
                                     data=buffer,
                                     headers=headers)
            self._check_response('POST', part_url, response)

            e_tag = response.headers['ETag']
            part_e_tags.append(e_tag)
            part_number += 1

        # Finish upload

        end_request = {
            'partETags': part_e_tags,
            'completeMD5': None
        }
        if self.__multipart_upload_double_check:
            file_desc.seek(0, 0)
            md5 = hashlib.md5(file_desc.read())
            digest = md5.digest()
            end_request['completeMD5'] = _base64_encode_string(digest)
        finish_url = self.__endpoint_url + blob_uri
        finish_response = requests.post(finish_url,
                                        data=json.dumps(end_request),
                                        headers=self.get_request_headers())
        self._check_response('POST', finish_url, finish_response)

        return blob_token

    def upload_file(self, file_desc):
        blob_token = self._upload(file_desc)
        return BlobReference(blob_token)

    def upload_file_from_path(self, path):
        with open(path, 'rb') as file_desc:
            return self.upload_file(file_desc)

    def upload_file_from_raw(self, content_raw):
        stream = BytesIO()
        stream.write(content_raw)
        stream.seek(0, 0)
        return self.upload_file(stream)

    def try_get_endpoint_version(self, endpoint_uri):
        if endpoint_uri in self.__endpoint_versions:
            return self.__endpoint_versions.get(endpoint_uri)

        try:
            response = requests.get('%sApi/System/Info' % self.__endpoint_url,
                                    headers=self.get_request_headers())
            version = StrictVersion(response.json().get('productVersion'))
        except RestError as e:
            return None

        self.__endpoint_versions[endpoint_uri] = version
        return version

    def get_request_headers(self):
        headers = {
            'Authorization': 'Bearer %s' % self.__auth_token,
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'X-RestPki-Client': 'Python %s' % __version__
        }
        return headers

    def post(self, url, data=None):
        verb = 'POST'
        try:

            if data:
                response = requests.post('%s%s' % (self.__endpoint_url, url),
                                         data=json.dumps(data),
                                         headers=self.get_request_headers())
            else:
                response = requests.post('%s%s' % (self.__endpoint_url, url),
                                         headers=self.get_request_headers())
        except Exception as e:
            raise RestUnreachableError(verb, url)

        self._check_response(verb, url, response)
        return response.json()

    def get(self, url, params=None):
        verb = 'GET'
        try:
            response = requests.get('%s%s' % (self.__endpoint_url, url),
                                    params=params,
                                    headers=self.get_request_headers())
        except Exception as e:
            raise RestUnreachableError(verb, url)

        self._check_response(verb, url, response)
        return response.json()

    def get_raw(self, url):
        request_url = '%s%s' % (self.__endpoint_url, url)
        res = requests.get(request_url,
                           stream=True,
                           headers=self.get_request_headers())
        return res

    @staticmethod
    def _check_response(verb, url, response):
        status_code = response.status_code
        if status_code < 200 or status_code > 299:
            try:
                response_body = response.json()
                if status_code == 422 and response_body.get('code', None):
                    if response_body.get('code', None) == 'ValidationError':
                        vr = ValidationResults(
                            response_body.get('validationResults', None))
                        error = ValidationError(verb, url, vr)
                    else:
                        error = RestPkiError(verb,
                                             url,
                                             response_body.get('code', None),
                                             response_body.get('detail', None))
                else:
                    error = RestError(verb,
                                      url,
                                      status_code,
                                      response_body.get('message', None))
            except Exception as e:
                error = RestError(verb, url, status_code)

            raise error

    def get_authentication(self):
        return Authentication(self)

    # region "endpoint_url" accessors

    @property
    def endpoint_url(self):
        return self.__get_endpoint_url()

    def __get_endpoint_url(self):
        return self.__endpoint_url

    @endpoint_url.setter
    def endpoint_url(self, value):
        self.__set_endpoint_url(value)

    def __set_endpoint_url(self, value):
        if value is None:
            raise Exception('The provided "endpoint_url" is not valid')
        self.__endpoint_url = value

    # endregion

    # region "auth_token" accessors

    @property
    def auth_token(self):
        return self.__get_auth_token()

    def __get_auth_token(self):
        return self.__auth_token

    @auth_token.setter
    def auth_token(self, value):
        self.__set_auth_token(value)

    def __set_auth_token(self, value):
        if value is None:
            raise Exception('The provided "auth_token" is not valid')
        self.__auth_token = value

    # endregion

    # region "multipart_upload_double_check" accessors

    @property
    def multipart_upload_double_check(self):
        return self.__get_multipart_upload_double_check()

    def __get_multipart_upload_double_check(self):
        return self.__multipart_upload_double_check

    @multipart_upload_double_check.setter
    def multipart_upload_double_check(self, value):
        self.__set_multipart_upload_double_check(value)

    def __set_multipart_upload_double_check(self, value):
        if value is None:
            raise Exception(
                'The provided "multipart_upload_double_check" is '
                'not valid')
        self.__multipart_upload_double_check = value

    # endregion

    # region "multipart_upload_threshold" accessors

    @property
    def multipart_upload_threshold(self):
        return self.__get_multipart_upload_threshold()

    def __get_multipart_upload_threshold(self):
        return self.__multipart_upload_threshold

    @multipart_upload_threshold.setter
    def multipart_upload_threshold(self, value):
        self.__set_multipart_upload_threshold(value)

    def __set_multipart_upload_threshold(self, value):
        if value is None:
            raise Exception(
                'The provided "multipart_upload_threshold" is not '
                'valid')
        self.__multipart_upload_threshold = value

    # endregion

    # region "rest_pki_version" accessors

    @property
    def rest_pki_version(self):
        return self.__get_rest_pki_version()

    def __get_rest_pki_version(self):
        return self.__rest_pki_version

    @rest_pki_version.setter
    def rest_pki_version(self, value):
        self.__set_rest_pki_version(value)

    def __set_rest_pki_version(self, value):
        if value is None:
            raise Exception('The provided "rest_pki_version" is not valid')
        self.__rest_pki_version = value

    # endregion


__all__ = [
    '_get_api_version',
    'RestPkiClient'
]
