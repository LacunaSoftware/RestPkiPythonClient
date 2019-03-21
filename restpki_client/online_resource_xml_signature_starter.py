from .xml_signature_starter import XmlSignatureStarter
from .signature_start_result import SignatureStartResult


class OnlineResourceXmlSignatureStarter(XmlSignatureStarter):

    def __init__(self, client):
        super(OnlineResourceXmlSignatureStarter, self).__init__(client)
        self.__resource_uri = None

    # region "resource_uri" accessors

    @property
    def resource_uri(self):
        return self.__get_resource_uri()

    def __get_resource_uri(self):
        return self.__resource_uri

    @resource_uri.setter
    def resource_uri(self, value):
        self.__set_resource_uri(value)

    def __set_resource_uri(self, value):
        if value is None:
            raise Exception('The provided "resource_uri" is not valid')
        self.__resource_uri = value

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
            self._client.post('Api/XmlSignatures/OnlineResourceXmlSignature',
                              request)
        return SignatureStartResult(response)

    def __get_start_common_request(self, is_with_web_pki=False):
        self._verify_common_parameters(is_with_web_pki)
        if self.__resource_uri is None:
            raise Exception('The online resource URI to sign was not set')
        request = {}
        self._fill_request(request)
        request['resourceToSignUri'] = self.__resource_uri
        return request


__all__ = ['OnlineResourceXmlSignatureStarter']
