from .xml_signature_starter import XmlSignatureStarter
from .signature_start_result import SignatureStartResult


class DetachedResourceXmlSignatureStarter(XmlSignatureStarter):
    _resource_content = None
    _resource_uri = None

    def __init__(self, client):
        XmlSignatureStarter.__init__(self, client)

    # region set_to_sign_detached_resource

    def set_to_sign_detached_resource_from_path(self,
                                                resource_path,
                                                resource_uri=None):
        self._resource_uri = resource_uri
        with open(resource_path, 'rb') as f:
            self._resource_content = f.read()

    def set_to_sign_detached_resource_from_content_raw(self,
                                                       resource_content_raw,
                                                       resource_uri=None):
        if not resource_content_raw:
            raise Exception('Invalid resource content')

        self._resource_uri = resource_uri
        self._resource_content = resource_content_raw

    def set_to_sign_detached_resource(self, resource_path, resource_uri=None):
        self.set_to_sign_detached_resource_from_path(resource_path,
                                                     resource_uri)

    def set_to_sign_detached_resource_content(self,
                                              resource_content_raw,
                                              resource_uri):
        self.set_to_sign_detached_resource_from_content_raw(
            resource_content_raw,
            resource_uri)

    # endregion

    def start_with_webpki(self):

        XmlSignatureStarter._verify_common_parameters(self, True)

        if not self._resource_content or len(self._resource_content) == 0:
            raise Exception('The detached resource to sign was not set')

        request = XmlSignatureStarter._get_request(self)
        request['detachedResourceToSignContent'] = self._resource_content
        request['detachedResourceReferenceUri'] = self._resource_uri

        response = self._client.post(
            'Api/XmlSignatures/DetachedResourceXmlSignature', data=request)

        return SignatureStartResult(response.get('token', None),
                                    response.get('certificate', None))


__all__ = ['DetachedResourceXmlSignatureStarter']
