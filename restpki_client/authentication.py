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

    def start_with_webpki(self, security_context_id):
        request = {'securityContextId': security_context_id}
        response = self._client.post('Api/Authentications', data=request)
        return response.get('token', None)

    def complete_with_webpki(self, token):
        response = self._client.post('Api/Authentications/%s/Finalize' % token)
        return AuthenticationResult(response)


__all__ = ['Authentication']
