from .pk_certificate import PKCertificate
from .validation import ValidationResults


class AuthenticationResult(object):

    def __init__(self, model):
        self.__certificate = None
        certificate = model.get('certificate', None)
        if certificate is not None:
            self.__certificate = PKCertificate(certificate)

        self.__validation_results = None
        validation_results = model.get('validationResults', None)
        if validation_results is not None:
            self.__validation_results = ValidationResults(validation_results)

    @property
    def certificate(self):
        return self.__certificate

    @certificate.setter
    def certificate(self, value):
        self.__certificate = value

    @property
    def validation_results(self):
        return self.__validation_results

    @validation_results.setter
    def validation_results(self, value):
        self.__validation_results = value


__all__ = ['AuthenticationResult']
