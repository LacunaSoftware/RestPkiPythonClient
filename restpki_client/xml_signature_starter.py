import base64
from abc import ABCMeta, abstractmethod


class XmlSignatureStarter:
    __metaclass__ = ABCMeta
    
    _client = None
    xml_content = None
    _xpath = None
    _insertion_option = None
    _namespace_manager = None
    signature_element_id = None
    security_context_id = None
    signature_policy_id = None
    callback_argument = None

    @abstractmethod
    def start_with_webpki(self):
        pass

    def __init__(self, client):
        self._client = client

    def set_xml_path(self, local_pdf_path):
        f = open(local_pdf_path, 'rb')
        self.xml_content = f.read()
        f.close()

    def set_signature_element_location(self, xpath, insertion_options,
                                       namespace_manager):
        self._xpath = xpath
        self._insertion_option = insertion_options
        self._namespace_manager = namespace_manager

    def get_common_request_data(self):
        if self.signature_policy_id is None:
            raise Exception('The signature policy was not set')
        data = dict()
        if self.xml_content is not None:
            data['xml'] = base64.b64encode(self.xml_content)

        if self._xpath is not None:
            data['signatureElementLocation'] = {
                'xpath': self._xpath,
                'InsertionOption': None if self._insertion_option is None
                else self._insertion_option,
                'namespaces': None if self._namespace_manager is None
                else self._namespace_manager.namespaces
            }
        data['signatureElementId'] = self.signature_element_id
        data['signaturePolicyId'] = self.signature_policy_id
        data['securityContextId'] = self.security_context_id
        data['callbackArgument'] = self.callback_argument
        return data


__all__ = ['XmlSignatureStarter']
