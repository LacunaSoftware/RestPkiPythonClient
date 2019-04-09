from abc import ABCMeta
from abc import abstractmethod

from .signature_result import SignatureResult
from .utils import _base64_encode_string


class SignatureFinisher(object):
    __metaclass__ = ABCMeta

    def __init__(self, client):
        self._client = client
        self._token = None
        self._signature = None

        self.__force_blob_result = None

    # region "client" accessors

    @property
    def client(self):
        return self.__get_client()

    def __get_client(self):
        return self._client

    @client.setter
    def client(self, value):
        self.__set_client(value)

    def __set_client(self, value):
        if value is None:
            raise Exception('The provided "client" is not valid')
        self._client = value

    # endregion

    # region "token" accessors

    @property
    def token(self):
        return self.__get_token()

    def __get_token(self):
        return self._token

    @token.setter
    def token(self, value):
        self.__set_token(value)

    def __set_token(self, value):
        if value is None:
            raise Exception('The provided "token" is not valid')
        self._token = value

    # endregion

    # region "signature" accessors

    @property
    def signature(self):
        return self.__get_signature()

    def __get_signature(self):
        return self._signature

    @signature.setter
    def signature(self, value):
        self.__set_signature(value)

    def __set_signature(self, value):
        if value is None:
            raise Exception('The provided "signature" is not valid')
        self._signature = value

    # endregion

    # region "force_blob_result" accessors

    @property
    def force_blob_result(self):
        return self.__get_force_blob_result()

    def __get_force_blob_result(self):
        return self.__force_blob_result

    @force_blob_result.setter
    def force_blob_result(self, value):
        self.__set_force_blob_result(value)

    def __set_force_blob_result(self, value):
        if value is None:
            raise Exception('The provided "force_blob_result" is not valid')
        self.__force_blob_result = value

    # endregion

    def finish(self):
        if self._token is None:
            raise Exception('The token was not set')

        self._check_compatibility()

        request = {
            'signature': _base64_encode_string(self._signature) if
                         self._signature is not None else None,
            'forceBlobResult': self.__force_blob_result or False
        }
        response = self._client.post(self._get_api_route(), request)
        return SignatureResult(self.client,
                               response.get('signatureFile'),
                               response.get('certificate'),
                               response.get('callbackArgument'))

    @abstractmethod
    def _check_compatibility(self):
        pass

    @abstractmethod
    def _get_api_route(self):
        pass


__all__ = ['SignatureFinisher']
