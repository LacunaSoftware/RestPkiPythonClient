from .file_result import FileResult
from .pk_certificate import PKCertificate


class SignatureResult(FileResult):
    _certificate = None
    _callback_argument = None

    def __init__(self, client, file_, certificate, callback_argument=None):
        FileResult.__init__(self, client, file_)
        self._certificate = PKCertificate(certificate)
        self._callback_argument = callback_argument

    @property
    def certificate(self):
        return self._certificate

    @property
    def callback_argument(self):
        return self._callback_argument


__all__ = ['SignatureResult']
