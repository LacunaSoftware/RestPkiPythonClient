from .validation import ValidationResults


class Authentication:

    _ignore_revocation_status_unknown = False
    _client = None

    def __init__(self, client):
        self._client = client

    def start(self):
        response = self._client.get('Api/Authentication')
        return response.nonce

    def start_with_webpki(self, security_context_id):
        request = {
            'securityContextId': security_context_id,
            'ignoreRevocationStatusUnknown':
                self._ignore_revocation_status_unknown
        }
        response = self._client.post('Api/Authentications', data=request)
        return response.json().get('token', None)

    def complete(self,
                 nonce,
                 certificate_content,
                 signature,
                 security_context_id):

        request = {
            'Nonce': nonce,
            'Certificate': certificate_content,
            'Signature': signature,
            'SecurityContextId': security_context_id,
            'IgnoreRevocationStatusUnknwon':
                self._ignore_revocation_status_unknown
        }
        response = self._client.post('Api/Authentication', data=request)
        return AuthenticationResult(response)

    def complete_with_webpki(self, token):
        response = self._client.post('Api/Authentications/%s/Finalize' % token)
        return AuthenticationResult(response)


class AuthenticationResult:

    _certificate = None
    _validation_results = None

    def __init__(self, model):
        self._certificate = model.json().get('certificate', None)
        self._validation_results = ValidationResults(
            model.json().get('validationResults', None))

    @property
    def certificate(self):
        return self._certificate

    @property
    def validation_results(self):
        return self._validation_results


__all__ = ['Authentication', 'AuthenticationResult']
