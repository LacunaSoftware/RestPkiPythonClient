from .xml_signature_starter import XmlSignatureStarter


class OnlineResourceXmlSignatureStarter(XmlSignatureStarter):
    resource_uri = None

    def __init__(self, client):
        super(OnlineResourceXmlSignatureStarter, self).__init__(client)

    def start_with_webpki(self):
        if self.resource_uri is None or self.resource_uri == '':
            raise Exception('The online resource URI to sign was not set')

        data = super(OnlineResourceXmlSignatureStarter,
                     self).get_common_request_data()
        data['resourceToSignUri'] = self.resource_uri
        response = self._client.post(
            'Api/XmlSignatures/OnlineResourceXmlSignature', data=data)
        return response.json().get('token', None)


__all__ = ['OnlineResourceXmlSignatureStarter']
