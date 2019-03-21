from .authentication_result import AuthenticationResult


class Authentication(object):

    def __init__(self, client):
        self._client = client

    @property
    def client(self):
        return self._client

    @client.setter
    def client(self, value):
        self._client = value

    def start(self):
        response = self.client.get('Api/Authentication')
        nonce = response.get('nonce', None)
        return nonce

    def start_with_web_pki(self,
                           security_context_id,
                           ignore_revocation_status_unknown=False):
        request = {
            'securityContextId': security_context_id,
            'ignoreRevocationStatusUnknown': ignore_revocation_status_unknown
        }
        response = self._client.post('Api/Authentications', request)
        token = response.get('token', None)
        return token

    def start_with_webpki(self,
                          security_context_id,
                          ignore_revocation_status_unknown=False):
        return self.start_with_web_pki(security_context_id,
                                       ignore_revocation_status_unknown)

    def complete(self,
                 nonce,
                 cert_content,
                 signature,
                 security_content_id,
                 ignore_revocation_status_unknown=False):
        request = {
            'nonce': nonce,
            'certificate': cert_content,
            'signature': signature,
            'securityContextId': security_content_id,
            'ignoreRevocationStatusUnknown': ignore_revocation_status_unknown
        }
        response = self._client.post('Api/Authentication', request)
        return AuthenticationResult(response)

    def complete_with_web_pki(self, token):
        response = self._client.post('Api/Authentications/%s/Finalize' % token)
        return AuthenticationResult(response)

    def complete_with_webpki(self, token):
        return self.complete_with_web_pki(token)


__all__ = ['Authentication']
