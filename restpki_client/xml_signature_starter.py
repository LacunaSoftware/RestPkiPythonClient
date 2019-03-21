from abc import ABCMeta
from abc import abstractmethod

from .file_reference import FileReference
from .namespace_manager import NamespaceManager
from .signature_starter import SignatureStarter


class XmlSignatureStarter(SignatureStarter):
    __metaclass__ = ABCMeta

    def __init__(self, client):
        super(XmlSignatureStarter, self).__init__(client)
        self._xml_to_sign = None
        self._signature_element_id = None
        self._signature_element_location_xpath = None
        self._signature_element_location_nsm = NamespaceManager()
        self._signature_element_location_insertion_option = None

    # region "xml_to_sign" accessors

    @property
    def xml_to_sign(self):
        return self.__get_xml_to_sign()

    def __get_xml_to_sign(self):
        return self._xml_to_sign.file_desc

    @xml_to_sign.setter
    def xml_to_sign(self, value):
        self.__set_xml_to_sign(value)

    def __set_xml_to_sign(self, value):
        if value is None:
            raise Exception('The provided "xml_to_sign" is not valid')
        self._xml_to_sign = FileReference.from_file(value)

    # endregion

    # region "xml_to_sign_path" accessors

    @property
    def xml_to_sign_path(self):
        return self.__get_xml_to_sign_path()

    def __get_xml_to_sign_path(self):
        return self._xml_to_sign.path

    @xml_to_sign_path.setter
    def xml_to_sign_path(self, value):
        self.__set_xml_to_sign_path(value)

    def __set_xml_to_sign_path(self, value):
        if value is None:
            raise Exception('The provided "xml_to_sign_path" is not valid')
        self._xml_to_sign = FileReference.from_path(value)

    def set_xml_to_sign_from_path(self, path):
        self.__set_xml_to_sign_path(path)

    def set_xml_to_sign(self, path):
        self.set_xml_to_sign_from_path(path)

    # endregion

    # region "xml_to_sign_base64" accessors

    @property
    def xml_to_sign_base64(self):
        return self.__get_xml_to_sign_base64()

    def __get_xml_to_sign_base64(self):
        return self._xml_to_sign.content_base64

    @xml_to_sign_base64.setter
    def xml_to_sign_base64(self, value):
        self.__set_xml_to_sign_base64(value)

    def __set_xml_to_sign_base64(self, value):
        if value is None:
            raise Exception('The provided "xml_to_sign_base64" is not valid')
        self._xml_to_sign = FileReference.from_content_base64(value)

    def set_xml_to_sign_from_content_base64(self, content_base64):
        self.__set_xml_to_sign_base64(content_base64)

    # endregion

    # region "xml_to_sign_content" accessors

    @property
    def xml_to_sign_content(self):
        return self.__get_xml_to_sign_content()

    def __get_xml_to_sign_content(self):
        return self._xml_to_sign.content_raw

    @xml_to_sign_content.setter
    def xml_to_sign_content(self, value):
        self.__set_xml_to_sign_content(value)

    def __set_xml_to_sign_content(self, value):
        if value is None:
            raise Exception('The provided "xml_to_sign_content" is not valid')
        self._xml_to_sign = FileReference.from_content_raw(value)

    def set_xml_to_sign_from_content_raw(self, content_raw):
        self.__set_xml_to_sign_content(content_raw)

    def set_xml_to_sign_content(self, content_raw):
        self.set_xml_to_sign_from_content_raw(content_raw)

    # endregion

    @property
    def signature_element_id(self):
        return self._signature_element_id

    @signature_element_id.setter
    def signature_element_id(self, value):
        self._signature_element_id = value

    @property
    def signature_element_location_xpath(self):
        return self._signature_element_location_xpath

    @property
    def signature_element_location_nsm(self):
        return self._signature_element_location_nsm

    @property
    def signature_element_location_insertion_option(self):
        return self._signature_element_location_insertion_option

    def set_signature_element_location(self,
                                       xpath,
                                       insertion_option,
                                       namespace_manager):
        self._signature_element_location_xpath = xpath
        self._signature_element_location_insertion_option = insertion_option
        self._signature_element_location_nsm = namespace_manager

    def _verify_common_parameters(self, is_with_web_pki=False):
        if not is_with_web_pki and self._signer_certificate is None:
            raise Exception('The certificate was not set')

        if self._xml_to_sign is None:
            raise Exception('The XML was not set')

        if self._signature_policy_id is None:
            raise Exception('The signature policy was not set')

    def _fill_request(self, request):
        request['xml'] = self._xml_to_sign.content_base64
        request['certificate'] = self._signer_certificate
        request['signaturePolicyId'] = self._signature_policy_id
        request['securityContextId'] = self._security_context_id
        request['ignoreRevocationStatusUnknown'] = \
            self._ignore_revocation_status_unknown
        request['callbackArgument'] = self._callback_argument
        if self._signature_element_location_xpath is not None and \
                self._signature_element_location_insertion_option is not None:
            request['signatureElementLocation'] = {
                'xPath': self._signature_element_location_xpath,
                'insertionOption':
                    self._signature_element_location_insertion_option,
                'namespaces': self._signature_element_location_nsm.namespaces
                              if self._signature_element_location_nsm is not
                              None else None
            }

        return request

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def start_with_web_pki(self):
        pass


__all__ = ['XmlSignatureStarter']
