import requests
import simplejson as json

from .version import __version__
from .authentication import Authentication


class RestPkiClient:

    _endpoint_url = ''
    _auth_token = ''
    _multipart_upload_double_check = False
    _multipart_upload_threshold = 5 * 1024 * 1024  # 5 MB
    _version = None

    def __init__(self, endpoint_url, access_token):
        self._endpointUrl = endpoint_url
        self._auth_token = access_token

    def get_request_headers(self):
        headers = {
            'Authorization': 'Bearer %s' % self._auth_token,
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'X-RestPki-Client': 'Python %s' % __version__
        }
        return headers

    def post(self, url, data=None):
        response = requests.post('%s%s' % (self._endpointUrl, url),
                                 data=json.dumps(data),
                                 headers=self.get_request_headers())
        response.raise_for_status()
        return response

    def get(self, url, params=None):
        response = requests.get('%s%s' % (self._endpointUrl, url),
                                params=params,
                                headers=self.get_request_headers())
        response.raise_for_status()
        return response

    def get_authentication(self):
        return Authentication(self)


__all__ = ['RestPkiClient']
