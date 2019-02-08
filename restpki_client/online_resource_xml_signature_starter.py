from .xml_signature_starter import XmlSignatureStarter
from .signature_start_result import SignatureStartResult


class OnlineResourceXmlSignatureStarter(XmlSignatureStarter):

    def __init__(self, client):
        XmlSignatureStarter.__init__(self, client)
        self._resource_uri = None

    def start_with_webpki(self):
        XmlSignatureStarter._verify_common_parameters(self, True)

        if not self._resource_uri or len(self._resource_uri) == 0:
            raise Exception('The online resource URI to sign was not set')

        request = XmlSignatureStarter._get_request(self)
        request['resourceToSignUri'] = self._resource_uri

        response = self._client.post(
            'Api/XmlSignatures/OnlineResourceXmlSignature', data=request)

        return SignatureStartResult(response.get('token', None),
                                    response.get('certificate', None))


__all__ = ['OnlineResourceXmlSignatureStarter']
