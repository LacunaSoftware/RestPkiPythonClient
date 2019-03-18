from .pk_certificate import PKCertificate
from .validation import ValidationResults


class AuthenticationResult(object):

    def __init__(self, model):
        self._certificate = None
        self._validation_results = None

        certificate = model.get('certificate', None)
        validation_results = model.get('validationResults', None)
        if certificate is not None:
            self._certificate = PKCertificate(certificate)

        if validation_results is not None:
            self._validation_results = ValidationResults(validation_results)

    @property
    def certificate(self):
        return self._certificate

    @certificate.setter
    def certificate(self, value):
        self._certificate = value

    @property
    def validation_results(self):
        return self._validation_results

    @validation_results.setter
    def validation_results(self, value):
        self._validation_results = value


__all__ = ['AuthenticationResult']
