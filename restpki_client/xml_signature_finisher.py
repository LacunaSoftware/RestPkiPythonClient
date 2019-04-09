from .utils import _base64_encode_string
from .signature_finisher import SignatureFinisher
from .signature_result import SignatureResult


class XmlSignatureFinisher(SignatureFinisher):

    def __init__(self, client):
        super(XmlSignatureFinisher, self).__init__(client)

    def finish(self):
        if not self._token:
            raise Exception('The token was not set')

        if self._signature is None:
            response = self._client.post('Api/XmlSignatures/%s/Finalize' %
                                         self._token)
        else:
            request = {
                'signature': _base64_encode_string(self._signature)
            }
            response = self._client.post('Api/XmlSignatures/%s/SignedBytes' %
                                         self._token)

        return SignatureResult(self._client,
                               {'content': response.get('signedXml')},
                               response.get('certificate', None),
                               response.get('callbackArgument', None))

    def _check_compatibility(self):
        pass

    def _get_api_route(self):
        pass


__all__ = ['XmlSignatureFinisher']
