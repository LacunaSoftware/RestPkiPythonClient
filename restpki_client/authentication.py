from .validation import ValidationResults
from .pk_certificate import PKCertificate


class Authentication:
    _client = None

    def __init__(self, client):
        self._client = client

    def start_with_webpki(self, security_context_id):
        request = {'securityContextId': security_context_id}
        response = self._client.post('Api/Authentications', data=request)
        return response.get('token', None)

    def complete_with_webpki(self, token):
        response = self._client.post('Api/Authentications/%s/Finalize' % token)
        return AuthenticationResult(response)


class AuthenticationResult:
    _certificate = None
    _validation_results = None

    def __init__(self, model):
        certificate = model.get('certificate', None)
        validation_results = model.get('validationResults', None)
        if certificate is not None:
            self._certificate = PKCertificate(certificate)

        if validation_results is not None:
            self._validation_results = ValidationResults(validation_results)

    @property
    def certificate(self):
        return self._certificate

    @property
    def validation_results(self):
        return self._validation_results


__all__ = ['Authentication', 'AuthenticationResult']
