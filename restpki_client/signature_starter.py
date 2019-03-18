from abc import ABCMeta
from abc import abstractmethod


class SignatureStarter(object):
    __metaclass__ = ABCMeta

    def __init__(self, client):
        self._client = client
        self._signer_certificate = None
        self._signature_policy_id = None
        self._security_context_id = None
        self._callback_argument = None

    @property
    def client(self):
        return self._client

    @client.setter
    def client(self, value):
        self._client = value

    @property
    def signer_certificate(self):
        return self._signer_certificate

    @signer_certificate.setter
    def signer_certificate(self, value):
        self._signer_certificate = value

    @property
    def signature_policy(self):
        return self._signature_policy_id

    @signature_policy.setter
    def signature_policy(self, value):
        self._signature_policy_id = value

    @property
    def security_context(self):
        return self._security_context_id

    @security_context.setter
    def security_context(self, value):
        self._security_context_id = value

    @abstractmethod
    def start_with_webpki(self):
        pass


__all__ = ['SignatureStarter']
