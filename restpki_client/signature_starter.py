from abc import ABCMeta
from abc import abstractmethod


class SignatureStarter:
    __metaclass__ = ABCMeta

    _client = None
    _signer_certificate = None
    _signature_policy_id = None
    _security_context_id = None
    _callback_argument = None

    def __init__(self, client):
        self._client = client

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
