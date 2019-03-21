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
        self._ignore_revocation_status_unknown = None

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

    # region "security_context_id" accessors

    @property
    def security_context_id(self):
        return self.__get_security_context_id()

    def __get_security_context_id(self):
        return self._security_context_id

    @property
    def security_context(self):
        return self.__get_security_context_id()

    @security_context_id.setter
    def security_context_id(self, value):
        self.__set_security_context_id(value)

    def __set_security_context_id(self, value):
        if value is None:
            raise Exception('The provided "security_context_id" is not valid')
        self._security_context_id = value

    @security_context.setter
    def security_context(self, value):
        self.__set_security_context_id(value)

    # endregion

    # region "signature_policy_id" accessors

    @property
    def signature_policy_id(self):
        return self.__get_signature_policy_id()

    def __get_signature_policy_id(self):
        return self._signature_policy_id

    @property
    def signature_policy(self):
        return self.__get_signature_policy_id()

    @signature_policy_id.setter
    def signature_policy_id(self, value):
        self.__set_signature_policy_id(value)

    def __set_signature_policy_id(self, value):
        if value is None:
            raise Exception('The provided "signature_policy_id" is not valid')
        self._signature_policy_id = value

    @signature_policy.setter
    def signature_policy(self, value):
        self.__set_signature_policy_id(value)

    # endregion

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def start_with_web_pki(self):
        pass


__all__ = ['SignatureStarter']
