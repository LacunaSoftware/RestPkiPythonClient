from .xml_signature_starter import XmlSignatureStarter
from .signature_start_result import SignatureStartResult


class FullXmlSignatureStarter(XmlSignatureStarter):

    def __init__(self, client):
        XmlSignatureStarter.__init__(self, client)

    def start_with_webpki(self):
        XmlSignatureStarter._verify_common_parameters(self, True)

        if not self._xml_to_sign_content:
            raise Exception('The XML to sign was not set')

        request = XmlSignatureStarter._get_request(self)
        response = self._client.post('Api/XmlSignatures/FullXmlSignature',
                                     data=request)

        return SignatureStartResult(response.get('token', None),
                                    response.get('certificate', None))


__all__ = ['FullXmlSignatureStarter']
