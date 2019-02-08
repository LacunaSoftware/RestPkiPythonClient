from abc import ABCMeta
from abc import abstractmethod


class SignatureFinisher:
    __metaclass__ = ABCMeta

    def __init__(self, client):
        self._client = client
        self._token = None
        self._signature = None

    @property
    def client(self):
        return self._client

    @client.setter
    def client(self, value):
        self._client = value

    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, value):
        self._token = value

    @property
    def signature(self):
        return self._signature

    @signature.setter
    def signature(self, value):
        self._signature = value

    @abstractmethod
    def finish(self):
        pass


__all__ = ['SignatureFinisher']
