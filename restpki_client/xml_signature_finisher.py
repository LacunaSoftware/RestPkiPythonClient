from .signature_finisher import SignatureFinisher
from .signature_result import SignatureResult


class XmlSignatureFinisher(SignatureFinisher):

    def __init__(self, client):
        SignatureFinisher.__init__(self, client)

    def finish(self):
        if not self._token:
            raise Exception('The token was not set')

        response = self._client.post(
            'Api/XmlSignatures/%s/Finalize' % self.token)

        return SignatureResult(self._client,
                               response.get('signedXml', None),
                               response.get('certificate', None),
                               response.get('callbackArgument', None))


__all__ = ['XmlSignatureFinisher']
