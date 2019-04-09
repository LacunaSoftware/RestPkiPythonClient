from .xml_signature_starter import XmlSignatureStarter
from .signature_start_result import SignatureStartResult


class FullXmlSignatureStarter(XmlSignatureStarter):

    def start(self):
        return self.__start_common()

    def start_with_web_pki(self):
        return self.__start_common(True)

    def start_with_webpki(self):
        return self.start_with_web_pki()

    def __start_common(self, is_with_web_pki=False):
        request = self.__get_start_common_request(is_with_web_pki)
        response = self._client.post('Api/XmlSignatures/FullXmlSignature',
                                     request)
        return SignatureStartResult(response)

    def __get_start_common_request(self, is_with_web_pki=False):
        self._verify_common_parameters(is_with_web_pki)
        request = {}
        self._fill_request(request)
        return request


__all__ = ['FullXmlSignatureStarter']
