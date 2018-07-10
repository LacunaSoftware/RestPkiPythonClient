from .xml_signature_starter import XmlSignatureStarter
from .signature_start_result import SignatureStartResult


class XmlElementSignatureStarter(XmlSignatureStarter):
    _to_sign_element_id = None
    _id_resolution_table = None

    def __init__(self, client):
        XmlSignatureStarter.__init__(self, client)

    @property
    def to_sign_element_id(self):
        return self._to_sign_element_id

    @to_sign_element_id.setter
    def to_sign_element_id(self, value):
        self._to_sign_element_id = value

    @property
    def id_resolution_table(self):
        return self._id_resolution_table

    @id_resolution_table.setter
    def id_resolution_table(self, value):
        self._id_resolution_table = value

    def start_with_webpki(self):

        XmlSignatureStarter._verify_common_parameters(self, True)

        if not self._xml_to_sign_content:
            raise Exception('The XML to sign was not set')

        if not self._to_sign_element_id or len(self._to_sign_element_id) == 0:
            raise Exception('The XML element id to sign was not set')

        request = XmlSignatureStarter._get_request(self)
        request['elementToSignId'] = self._to_sign_element_id
        if self._id_resolution_table is not None:
            request['idResolutionTable'] = self._id_resolution_table.to_model()

        response = self._client.post('Api/XmlSignatures/XmlElementSignature',
                                     data=request)
        return SignatureStartResult(response.get('token', None),
                                    response.get('certificate', None))


__all__ = ['XmlElementSignatureStarter']
