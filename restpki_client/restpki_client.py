import requests
import simplejson as json

from .version import __version__
from .authentication import Authentication
from .validation import ValidationResults
from .errors import *


class RestPkiClient:
    _endpoint_url = None
    _auth_token = None

    def __init__(self, endpoint_url, access_token):
        self._endpoint_url = endpoint_url
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
        verb = 'POST'
        try:

            if data:
                response = requests.post('%s%s' % (self._endpoint_url, url),
                                         data=json.dumps(data),
                                         headers=self.get_request_headers())
            else:
                response = requests.post('%s%s' % (self._endpoint_url, url),
                                         headers=self.get_request_headers())
        except Exception as e:
            raise RestUnreachableError(verb, url)

        self._check_response(verb, url, response)
        return response.json()

    def get(self, url, params=None):
        verb = 'GET'
        try:
            response = requests.get('%s%s' % (self._endpoint_url, url),
                                    params=params,
                                    headers=self.get_request_headers())
        except Exception as e:
            raise RestUnreachableError(verb, url)

        self._check_response(verb, url, response)
        return response.json()

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


__all__ = ['RestPkiClient']
