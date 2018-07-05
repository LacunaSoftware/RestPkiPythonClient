from .xml_signature_starter import XmlSignatureStarter


class XmlElementSignatureStarter(XmlSignatureStarter):
    element_tosign_id = None
    id_resolution_table = None

    def __init__(self, client):
        super(XmlElementSignatureStarter, self).__init__(client)

    def start_with_webpki(self):
        if self.xml_content is None:
            raise Exception('The XML to sign was not set')

        if self.element_tosign_id is None or self.element_tosign_id == '':
            raise Exception('The XML element Id to sign was not set')

        data = super(XmlElementSignatureStarter, self).get_common_request_data()
        data['elementToSignId'] = self.element_tosign_id
        if self.id_resolution_table is not None:
            data['idResolutionTable'] = self.id_resolution_table.to_model()

        response = self._client.post('Api/XmlSignatures/XmlElementSignature',
                                     data=data)
        return response.json().get('token', None)


__all__ = ['XmlElementSignatureStarter']
