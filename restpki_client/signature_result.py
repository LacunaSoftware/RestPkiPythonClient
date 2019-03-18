from .file_result import FileResult
from .pk_certificate import PKCertificate


class SignatureResult(FileResult):

    def __init__(self,
                 client,
                 file_model,
                 certificate,
                 callback_argument=None):

        super(SignatureResult, self).__init__(client, file_model)
        self._certificate = None
        if certificate is not None:
            self._certificate = PKCertificate(certificate)
        self._callback_argument = callback_argument

    @property
    def certificate(self):
        return self._certificate

    @certificate.setter
    def certificate(self, value):
        self._certificate = value

    @property
    def callback_argument(self):
        return self._callback_argument

    @callback_argument.setter
    def callback_argument(self, value):
        self._callback_argument = value


__all__ = ['SignatureResult']
