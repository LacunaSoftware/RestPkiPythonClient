from .pk_certificate import PKCertificate


class SignatureStartResult(object):

    def __init__(self, token, certificate):
        if certificate is not None:
            self._certificate = PKCertificate(certificate)
        self._token = token

    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, value):
        self._token = value

    @property
    def certificate(self):
        return self._certificate

    @certificate.setter
    def certificate(self, value):
        self._certificate = value


__all__ = ['SignatureStartResult']
