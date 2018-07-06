import base64
from abc import ABCMeta, abstractmethod

from .signature_starter import SignatureStarter


class XmlSignatureStarter(SignatureStarter):
    __metaclass__ = ABCMeta

    _xml_to_sign_content = None
    _signature_element_id = None
    _signature_element_location_xpath = None
    _signature_element_location_nsm = None
    _signature_element_location_insertion_option = None

    def __init__(self, client):
        SignatureStarter.__init__(self, client)

    # region set_xml_to_sign

    def set_xml_to_sign_from_path(self, path):
        with open(path, 'rb') as f:
            self._xml_to_sign_content = f.read()

    def set_xml_to_sign_from_content_raw(self, content_raw):
        self._xml_to_sign_content = content_raw

    def set_xml_to_sign_from_content_base64(self, content_base64):
        self._xml_to_sign_content = base64.b64decode(content_base64)

    def set_xml_to_sign(self, path):
        self.set_xml_to_sign_from_path(path)

    def set_xml_to_sign_content(self, content_raw):
        self.set_xml_to_sign_from_content_raw(content_raw)

    # endregion

    def set_signature_element_location(self,
                                       xpath,
                                       insertion_option,
                                       namespace_manager):
        self._signature_element_location_xpath = xpath
        self._signature_element_location_insertion_option = insertion_option
        self._signature_element_location_nsm = namespace_manager

    @property
    def signature_element_id(self):
        return self._signature_element_id

    @signature_element_id.setter
    def signature_element_id(self, value):
        self._signature_element_id = value

    def _verify_common_parameters(self, with_webpki=False):
        if not with_webpki and not self._signer_certificate:
            raise Exception('The certificate was not set')

        if not self._xml_to_sign_content:
            raise Exception('The XML was not set')

        if not self._signature_policy_id:
            raise Exception('The signature policy was not set')

    def _get_request(self):
        request = {
            'signaturePolicyId': self._signature_policy_id,
            'securityContextId': self._security_context_id,
            'signatureElementId': self._signature_element_id
        }

        if self._xml_to_sign_content:
            request['xml'] = base64.b64encode(self._xml_to_sign_content)

        if self._signature_element_location_xpath and \
                self._signature_element_location_insertion_option:
            request['signatureElementLocation'] = {
                'xPath': self._signature_element_location_xpath,
                'insertionOption':
                    self._signature_element_location_insertion_option
            }

            if self._signature_element_location_nsm:
                request['signatureElementLocation']['namespaces'] = \
                    self._signature_element_location_nsm.namespaces

        return request

    @abstractmethod
    def start_with_webpki(self):
        pass


__all__ = ['XmlSignatureStarter']
