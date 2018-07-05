import base64


class PadesSignatureFinisher:
    token = ''
    _client = None
    _done = False
    _signed_pdf_content = None
    _certificate = None
    _callback_argument = None

    def __init__(self, restpki_client):
        self._client = restpki_client

    def finish(self):
        if not self.token:
            raise Exception('The token was not set')

        response = self._client.post(
            'Api/PadesSignatures/%s/Finalize' % self.token)
        self._signed_pdf_content = base64.b64decode(
            response.json().get('signedPdf', None))
        self._certificate = response.json().get('certificate', None)
        self._callback_argument = response.json().get('callbackArgument', None)
        self._done = True

    @property
    def signed_pdf_content(self):
        if not self._done:
            raise Exception(
                'The property "signed_pdf_content" can only be called'
                ' after calling the finish() method'
            )

        return self._signed_pdf_content

    @property
    def callback_argument(self):
        if not self._done:
            raise Exception(
                'The property "callback_argument" can only be called after'
                ' calling the finish() method'
            )

        return self._callback_argument

    @property
    def certificate(self):
        if not self._done:
            raise Exception(
                'The property "certificate" can only be called after calling'
                ' the finish() method'
            )

        return self._certificate

    def write_signed_pdf(self, local_pdf_path):
        if not self._done:
            raise Exception(
                'The method write_signed_pdf() can only be called after calling'
                ' the finish() method'
            )

        f = open(local_pdf_path, 'wb')
        f.write(self._signed_pdf_content)
        f.close()


__all__ = ['PadesSignatureFinisher']
