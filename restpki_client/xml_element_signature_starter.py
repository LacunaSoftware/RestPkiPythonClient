from .xml_signature_starter import XmlSignatureStarter
from .signature_start_result import SignatureStartResult


class XmlElementSignatureStarter(XmlSignatureStarter):

    def __init__(self, client):
        XmlSignatureStarter.__init__(self, client)
        self.__to_sign_element_id = None
        self.__id_resolution_table = None

    @property
    def to_sign_element_id(self):
        return self.__to_sign_element_id

    @to_sign_element_id.setter
    def to_sign_element_id(self, value):
        self.__to_sign_element_id = value

    @property
    def id_resolution_table(self):
        return self.__id_resolution_table

    @id_resolution_table.setter
    def id_resolution_table(self, value):
        self.__id_resolution_table = value

    def start(self):
        return self.__start_common()

    def start_with_web_pki(self):
        return self.__start_common(True)

    def start_with_webpki(self):
        return self.start_with_web_pki()

    def __start_common(self, is_with_web_pki=False):
        request = self.__get_start_common_request(is_with_web_pki)
        response = self._client.post('Api/XmlSignatures/XmlElementSignature',
                                     request)
        return SignatureStartResult(response)

    def __get_start_common_request(self, is_with_web_pki=False):
        self._verify_common_parameters(is_with_web_pki)
        if self.__to_sign_element_id is None:
            raise Exception('The XML element id to sign was not set')
        request = {}
        self._fill_request(request)
        request['elementToSignId'] = self.__to_sign_element_id
        if self.__id_resolution_table is not None:
            request['idResolutionTable'] = self.__id_resolution_table.to_model()
        return request


__all__ = ['XmlElementSignatureStarter']
