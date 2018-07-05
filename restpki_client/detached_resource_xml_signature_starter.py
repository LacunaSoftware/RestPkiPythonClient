from .xml_signature_starter import XmlSignatureStarter


class DetachedResourceXmlSignatureStarter(XmlSignatureStarter):
    resource_content = None
    resource_uri = None

    def __init__(self, client):
        super(DetachedResourceXmlSignatureStarter, self).__init__(client)

    def set_tosign_detached_resource(self, resource_path, resource_uri=None):
        self.resource_uri = resource_uri
        f = open(resource_path, 'rb')
        self.resource_content = f.read()
        f.close()

    def start_with_webpki(self):
        if self.resource_content is None or len(self.resource_content) == 0:
            raise Exception('The detached resource to sign was not set')

        data = super(DetachedResourceXmlSignatureStarter,
                     self).get_common_request_data()
        data['detachedResourceToSignContent'] = self.resource_content
        data['detachedResourceReferenceUri'] = self.resource_uri
        response = self._client.post(
            'Api/XmlSignatures/DetachedResourceXmlSignature', data=data)
        return response.json().get('token', None)


__all__ = ['DetachedResourceXmlSignatureStarter']
