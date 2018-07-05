from .xml_signature_starter import XmlSignatureStarter


class FullXmlSignatureStarter(XmlSignatureStarter):
    def __init__(self, client):
        super(FullXmlSignatureStarter, self).__init__(client)

    def start_with_webpki(self):
        if self.xml_content is None:
            raise Exception('The XML to sign was not set')

        data = super(FullXmlSignatureStarter, self).get_common_request_data()
        response = self._client.post('Api/XmlSignatures/FullXmlSignature',
                                     data=data)
        return response.json().get('token', None)


__all__ = ['FullXmlSignatureStarter']
