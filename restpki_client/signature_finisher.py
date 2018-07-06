from abc import ABCMeta
from abc import abstractmethod


class SignatureFinisher:
    __metaclass__ = ABCMeta

    _client = None
    _token = None
    _signature = None

    def __init__(self, client):
        self._client = client

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
