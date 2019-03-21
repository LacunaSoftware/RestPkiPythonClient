import base64

from .apis import Apis
from .digest_algorithm import DigestAlgorithm
from .file_reference import FileReference
from .rest_pki_client import _get_api_version
from .signature_starter import SignatureStarter
from .signature_start_result import SignatureStartResult


class CadesSignatureStarter(SignatureStarter):

    def __init__(self, client):
        super(CadesSignatureStarter, self).__init__(client)
        self.__file_to_sign = None
        self.__cms_to_cosign = None
        self.__encapsulate_content = True
        self.__digest_algorithms_for_detached_signature = [
            DigestAlgorithm.SHA1,
            DigestAlgorithm.SHA256
        ]

    # region "file_to_sign" accessors

    @property
    def file_to_sign(self):
        return self.__get_file_to_sign()

    def __get_file_to_sign(self):
        return self.__file_to_sign.file_desc

    @file_to_sign.setter
    def file_to_sign(self, value):
        self.__set_file_to_sign(value)

    def __set_file_to_sign(self, value):
        if value is None:
            raise Exception('The provided "file_to_sign" is not valid')
        self.__file_to_sign = FileReference.from_file(value)

    # endregion

    # region "file_to_sign_path" accessors

    @property
    def file_to_sign_path(self):
        return self.__get_file_to_sign_path()

    def __get_file_to_sign_path(self):
        return self.__file_to_sign.path

    @file_to_sign_path.setter
    def file_to_sign_path(self, value):
        self.__set_file_to_sign_path(value)

    def __set_file_to_sign_path(self, value):
        if value is None:
            raise Exception('The provided "file_to_sign_path" is not valid')
        self.__file_to_sign = FileReference.from_path(value)

    def set_file_to_sign_from_path(self, path):
        self.__set_file_to_sign_path(path)

    def set_file_to_sign_path(self, path):
        self.set_file_to_sign_from_path(path)

    def set_file_to_sign(self, path):
        self.set_file_to_sign_path(path)

    # endregion

    # region "file_to_sign_base64" accessors

    @property
    def file_to_sign_base64(self):
        return self.__get_file_to_sign_base64()

    def __get_file_to_sign_base64(self):
        return self.__file_to_sign.content_base64

    @file_to_sign_base64.setter
    def file_to_sign_base64(self, value):
        self.__set_file_to_sign_base64(value)

    def __set_file_to_sign_base64(self, value):
        if value is None:
            raise Exception('The provided "file_to_sign_base64" is not valid')
        self.__file_to_sign_base64 = FileReference.from_content_base64(value)

    def set_file_to_sign_from_content_base64(self, content_base64):
        self.__set_file_to_sign_base64(content_base64)

    # endregion

    # region "file_to_sign_content" accessors

    @property
    def file_to_sign_content(self):
        return self.__get_file_to_sign_content()

    def __get_file_to_sign_content(self):
        return self.__file_to_sign_content

    @file_to_sign_content.setter
    def file_to_sign_content(self, value):
        self.__set_file_to_sign_content(value)

    def __set_file_to_sign_content(self, value):
        if value is None:
            raise Exception('The provided "file_to_sign_content" is not valid')
        self.__file_to_sign_content = value

    def set_file_to_sign_from_content_raw(self, content_raw):
        self.__set_file_to_sign_content(content_raw)

    def set_file_to_sign_content(self, content_raw):
        self.set_file_to_sign_from_content_raw(content_raw)

    # endregion
    
    # region "cms_to_cosign" accessors 
    
    @property
    def cms_to_cosign(self):
        return self.__get_cms_to_cosign()
        
    def __get_cms_to_cosign(self):
        return self.__cms_to_cosign.file_desc
    
    @cms_to_cosign.setter
    def cms_to_cosign(self, value):
        self.__set_cms_to_cosign(value)
        
    def __set_cms_to_cosign(self, value):
        if value is None:
            raise Exception('The provided "cms_to_cosign" is not valid')
        self.__cms_to_cosign = FileReference.from_file(value)
    
    # endregion
    
    # region "cms_to_cosign_path" accessors

    @property
    def cms_to_cosign_path(self):
        return self.__get_cms_to_cosign_path()

    def __get_cms_to_cosign_path(self):
        return self.__cms_to_cosign.path

    @cms_to_cosign_path.setter
    def cms_to_cosign_path(self, value):
        self.__set_cms_to_cosign_path(value)

    def __set_cms_to_cosign_path(self, value):
        if value is None:
            raise Exception('The provided "cms_to_cosign_path" is not valid')
        self.__cms_to_cosign = FileReference.from_path(value)

    def set_cms_to_cosign_from_path(self, path):
        self.__set_cms_to_cosign_path(path)

    def set_cms_to_cosign_path(self, path):
        self.set_cms_to_cosign_from_path(path)

    def set_cms_to_cosign(self, path):
        self.set_cms_to_cosign_path(path)

    # endregion

    # region "cms_to_cosign_content" accessors

    @property
    def cms_to_cosign_content(self):
        return self.__get_cms_to_cosign_content()

    def __get_cms_to_cosign_content(self):
        return self.__cms_to_cosign.content_raw

    @cms_to_cosign_content.setter
    def cms_to_cosign_content(self, value):
        self.__set_cms_to_cosign_content(value)

    def __set_cms_to_cosign_content(self, value):
        if value is None:
            raise Exception('The provided "cms_to_cosign_content" is not valid')
        self.__cms_to_cosign = FileReference.from_content_raw(value)

    def set_cms_to_cosign_from_content_raw(self, content_raw):
        self.__set_cms_to_cosign_content(content_raw)

    def set_cms_to_cosign_content(self, content_raw):
        self.set_cms_to_cosign_from_content_raw(content_raw)

    # endregion

    # region "cms_to_cosign_base64" accessors

    @property
    def cms_to_cosign_base64(self):
        return self.__get_cms_to_cosign_base64()

    def __get_cms_to_cosign_base64(self):
        return self.__cms_to_cosign.content_base64

    @cms_to_cosign_base64.setter
    def cms_to_cosign_base64(self, value):
        self.__set_cms_to_cosign_base64(value)

    def __set_cms_to_cosign_base64(self, value):
        if value is None:
            raise Exception('The provided "cms_to_cosign_base64" is not valid')
        self.__cms_to_cosign = FileReference.from_content_base64(value)

    def set_cms_to_cosign_from_content_base64(self, content_base64):
        self.__set_cms_to_cosign_base64(content_base64)

    # endregion

    # region "cms_to_cosign_result" accessors

    @property
    def cms_to_cosign_result(self):
        return self.__get_cms_to_cosign_result()

    def __get_cms_to_cosign_result(self):
        return self.__cms_to_cosign.result

    @cms_to_cosign_result.setter
    def cms_to_cosign_result(self, value):
        self.__set_cms_to_cosign_result(value)

    def __set_cms_to_cosign_result(self, value):
        if value is None:
            raise Exception('The provided "cms_to_cosign_result" is not valid')
        self.__cms_to_cosign = FileReference.from_result(value)

    # endregion

    @property
    def encapsulate_content(self):
        return self.__encapsulate_content

    @encapsulate_content.setter
    def encapsulate_content(self, value):
        self.__encapsulate_content = value

    def start(self):
        if self._signer_certificate is None:
            raise Exception('The certificate was not set')
        response = self.__start_common()
        return SignatureStartResult(response)

    def start_with_web_pki(self):
        response = self.__start_common()
        return SignatureStartResult(response)

    def start_with_webpki(self):
        return self.start_with_web_pki()

    def __start_common(self):

        if self.__file_to_sign is None and self.__cms_to_cosign is None:
            raise Exception('The content to sign was not set and no CMS to be '
                            'co-signed was given')

        if self._signature_policy_id is None:
            raise Exception('The signature policy was not set')

        api_version = _get_api_version(self._client, Apis.START_CADES)
        if api_version == 1:
            return self.__start_common_v1()
        elif api_version == 1:
            return self.__start_common_v2()
        return self.__start_common_v3()

    def __start_common_v3(self):
        request = self.__get_start_common_request()

        if self.__file_to_sign is not None:
            if not self.__encapsulate_content:
                request['dataHashes'] = self.__file_to_sign.compute_data_hashes(
                    self.__digest_algorithms_for_detached_signature)
            else:
                request['fileToSign'] = \
                    self.__file_to_sign.upload_or_reference(self._client)

        if self.__cms_to_cosign is not None:
            request['cmsToCoSign'] = \
                self.__cms_to_cosign.upload_or_reference(self._client)

        return self._client.post('Api/v3/CadesSignatures', request)

    def __start_common_v2(self):
        request = self.__get_start_common_request()

        if self.__file_to_sign is not None:
            if not self.__encapsulate_content:
                request['dataHashes'] = self.__file_to_sign.compute_data_hashes(
                    self.__digest_algorithms_for_detached_signature)
            else:
                request['contentToSign'] = self.__file_to_sign.content_base64

        if self.__cms_to_cosign is not None:
            request['cmsToCoSign'] = self.__file_to_sign.content_base64

        return self._client.post('Api/v2/CadesSignatures', request)

    def __start_common_v1(self):
        request = self.__get_start_common_request()

        if self.__file_to_sign is not None:
            request['contentToSign'] = self.__file_to_sign.content_base64

        if self.__cms_to_cosign is not None:
            request['cmsToCoSign'] = self.__file_to_sign.content_base64

        return self._client.post('Api/CadesSignatures', request)

    def __get_start_common_request(self):
        return {
            'certificate': self._signer_certificate,
            'signaturePolicyId': self._signature_policy_id,
            'securityContextId': self._security_context_id,
            'ignoreRevocationStatusUnknown':
                self._ignore_revocation_status_unknown,
            'callbackArgument': self._callback_argument,
            'encapsulateContent': self.__encapsulate_content
        }


__all__ = ['CadesSignatureStarter']
