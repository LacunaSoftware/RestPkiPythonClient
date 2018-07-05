import base64


class XmlSignatureFinisher:
    token = ''
    _client = None
    _done = False
    _signed_xml_content = None
    _certificate = None
    _callback_argument = None

    def __init__(self, restpki_client):
        self._client = restpki_client

    def finish(self):
        if not self.token:
            raise Exception('The token was not set')

        response = self._client.post(
            'Api/XmlSignatures/%s/Finalize' % self.token)
        self._signed_xml_content = base64.b64decode(
            response.json().get('signedXml', None))
        self._certificate = response.json().get('certificate', None)
        self._callback_argument = response.json().get('callbackArgument', None)
        self._done = True

    @property
    def signed_xml_content(self):
        if not self._done:
            raise Exception(
                'The property "signed_xml_content" can only be called after'
                ' calling the finish() method'
            )

        return self._signed_xml_content

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

    def write_signed_xml(self, local_xml_path):
        if not self._done:
            raise Exception(
                'The method write_signed_xml() can only be called after calling'
                ' the finish() method'
            )

        f = open(local_xml_path, 'wb')
        f.write(self._signed_xml_content)
        f.close()


__all__ = ['XmlSignatureFinisher']
