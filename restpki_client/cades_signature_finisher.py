import base64


class CadesSignatureFinisher:
    token = None
    _client = None
    _done = False
    _cms = None
    _certificate = None
    _callback_argument = None

    def __init__(self, restpki_client):
        self._client = restpki_client

    def finish(self):
        if not self.token:
            raise Exception('The token was not set')

        response = self._client.post(
            'Api/CadesSignatures/%s/Finalize' % self.token).json()
        self._cms = base64.b64decode(response.get('cms', None))
        self._certificate = response.get('certificate', None)
        self._callback_argument = response.get('callbackArgument', None)
        self._done = True

    @property
    def cms(self):
        if not self._done:
            raise Exception(
                'The property "cms" can only be called after calling the'
                ' finish() method'
            )

        return self._cms

    @property
    def certificate(self):
        if not self._done:
            raise Exception(
                'The property "certificate" can only be called after calling'
                ' the finish() method'
            )

        return self._certificate

    @property
    def callback_argument(self):
        if not self._done:
            raise Exception(
                'The property "callback_argument" can only be called after'
                ' calling the finish() method'
            )

        return self._callback_argument

    def write_cms(self, path):
        if not self._done:
            raise Exception(
                'The method write_cms() can only be called after calling the'
                ' finish() method'
            )

        f = open(path, 'wb')
        f.write(self._cms)
        f.close()


__all__ = ['CadesSignatureFinisher']
