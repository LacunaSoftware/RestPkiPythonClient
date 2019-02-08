import base64

from .signature_starter import SignatureStarter
from .signature_start_result import SignatureStartResult


class PadesSignatureStarter(SignatureStarter):

    def __init__(self, client):
        SignatureStarter.__init__(self, client)
        self._bypass_marks_if_signed = True
        self._pdf_marks = []
        self._pdf_to_sign_content = None
        self._measurement_units = None
        self._page_optimization = None
        self._visual_representation = None

    @property
    def pdf_to_sign_content(self):
        return self._pdf_to_sign_content

    # region set_pdf_to_sign

    def set_pdf_to_sign_from_path(self, path):
        with open(path, 'rb') as f:
            self._pdf_to_sign_content = f.read()

    def set_pdf_to_sign_from_content_raw(self, content_raw):
        self._pdf_to_sign_content = content_raw

    def set_pdf_to_sign_from_content_base64(self, content_base64):
        self._pdf_to_sign_content = base64.b64decode(content_base64)

    def set_pdf_to_sign_path(self, path):
        self.set_pdf_to_sign_from_path(path)

    def set_pdf_to_sign(self, path):
        self.set_pdf_to_sign_path(path)

    def set_pdf_to_sign_content(self, content_raw):
        self.set_pdf_to_sign_from_content_raw(content_raw)

    # endregion

    @property
    def bypass_marks_if_signed(self):
        return self._bypass_marks_if_signed

    @bypass_marks_if_signed.setter
    def bypass_marks_if_signed(self, value):
        self._bypass_marks_if_signed = value

    @property
    def pdf_marks(self):
        return self._pdf_marks

    @pdf_marks.setter
    def pdf_marks(self, value):
        self._pdf_marks = value

    @property
    def measurement_units(self):
        return self._measurement_units

    @measurement_units.setter
    def measurement_units(self, value):
        self._measurement_units = value

    @property
    def page_optimization(self):
        return self._page_optimization

    @page_optimization.setter
    def page_optimization(self, value):
        self._page_optimization = value

    @property
    def visual_representation(self):
        return self._visual_representation

    @visual_representation.setter
    def visual_representation(self, value):
        self._visual_representation = value

    def start_with_webpki(self):
        response = self._start_common()
        return SignatureStartResult(response.get('token', None),
                                    response.get('certificate', None))

    def _start_common(self):

        if not self._pdf_to_sign_content:
            raise Exception('The PDF to sign was not set')

        if not self._signature_policy_id:
            raise Exception('The signature policy was not set')

        request = {
            'signaturePolicyId': self._signature_policy_id,
            'securityContextId': self._security_context_id,
            'pdfToSign': base64.b64encode(self._pdf_to_sign_content),
            'bypassMarksIfSigned': self._bypass_marks_if_signed,
            'measurementUnits': self._measurement_units,
            'pageOptimization': self._page_optimization,
            'visualRepresentation': self._visual_representation
        }

        if self._signer_certificate:
            request['certificate'] = base64.b64encode(self._signer_certificate)

        return self._client.post('Api/PadesSignatures', data=request)


__all__ = ['PadesSignatureStarter']
