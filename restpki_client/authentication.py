from .validation import ValidationResults
from .pk_certificate import PKCertificate


class Authentication:

    def __init__(self, client):
        self._client = client

    @property
    def client(self):
        return self._client

    @client.setter
    def client(self, value):
        self._client = value

    def start_with_webpki(self, security_context_id):
        request = {'securityContextId': security_context_id}
        response = self._client.post('Api/Authentications', data=request)
        return response.get('token', None)

    def complete_with_webpki(self, token):
        response = self._client.post('Api/Authentications/%s/Finalize' % token)
        return AuthenticationResult(response)


class AuthenticationResult:

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


__all__ = ['Authentication', 'AuthenticationResult']
