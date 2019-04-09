from .xml_signature_starter import XmlSignatureStarter
from .signature_start_result import SignatureStartResult


class DetachedResourceXmlSignatureStarter(XmlSignatureStarter):

    def __init__(self, client):
        super(DetachedResourceXmlSignatureStarter, self).__init__(client)
        self.__resource_content = None
        self.__resource_uri = None

    @property
    def resource_content(self):
        return self.__resource_content

    @property
    def resource_uri(self):
        return self.__resource_uri

    # region set_to_sign_detached_resource

    def set_to_sign_detached_resource_from_path(self, path, uri=None):
        self.__resource_uri = uri
        with open(path, 'rb') as f:
            self.__resource_content = f.read()

    def set_to_sign_detached_resource_from_content_raw(self, content_raw,
                                                       uri=None):
        if not content_raw:
            raise Exception('Invalid resource content')

        self.__resource_uri = uri
        self.__resource_content = content_raw

    def set_to_sign_detached_resource(self, path, uri=None):
        self.set_to_sign_detached_resource_from_path(path, uri)

    def set_to_sign_detached_resource_content(self,
                                              content_raw,
                                              uri):
        self.set_to_sign_detached_resource_from_content_raw(content_raw, uri)

    # endregion

    def start(self):
        return self.__start_common()

    def start_with_web_pki(self):
        return self.__start_common(True)

    def start_with_webpki(self):
        return self.start_with_web_pki()

    def __start_common(self, is_with_web_pki=False):
        request = self.__get_start_common_request(is_with_web_pki)
        response = \
            self._client.post('Api/XmlSignatures/DetachedResourceXmlSignatures',
                              request)
        return SignatureStartResult(response)

    def __get_start_common_request(self, is_with_web_pki=False):
        self._verify_common_parameters(is_with_web_pki)
        if self.__resource_content is None or len(self.__resource_content) == 0:
            raise Exception('The detached resource to sign was not set')
        request = {}
        self._fill_request(request)
        request['detachedResourceToSignContent'] = self.__resource_content
        request['detachedResourceReferenceUri'] = self.__resource_uri
        return request


__all__ = ['DetachedResourceXmlSignatureStarter']
