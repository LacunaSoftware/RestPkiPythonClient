from .pk_certificate import PKCertificate


class SignatureStartResult:
    _token = None
    _certificate = None

    def __init__(self, token, certificate):
        if certificate:
            self._certificate = PKCertificate(certificate)
        self._token = token

    @property
    def token(self):
        return self._token

    @property
    def certificate(self):
        return self._certificate


__all__ = ['SignatureStartResult']
