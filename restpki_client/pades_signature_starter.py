from .apis import Apis
from .rest_pki_client import _get_api_version
from .file_reference import FileReference
from .signature_starter import SignatureStarter
from .signature_start_result import SignatureStartResult


class PadesSignatureStarter(SignatureStarter):

    def __init__(self, client):
        super(PadesSignatureStarter, self).__init__(client)
        self.__bypass_marks_if_signed = True
        self.__pdf_marks = []
        self.__pdf_to_sign = None
        self.__measurement_units = None
        self.__page_optimization = None
        self.__visual_representation = None

    # region "pdf_to_sign" accessors

    @property
    def pdf_to_sign(self):
        return self.__get_pdf_to_sign()

    def __get_pdf_to_sign(self):
        return self.__pdf_to_sign.file_desc

    @pdf_to_sign.setter
    def pdf_to_sign(self, value):
        self.__set_pdf_to_sign(value)

    def __set_pdf_to_sign(self, value):
        if value is None:
            raise Exception('The provided "pdf_to_sign" is not valid')
        self.__pdf_to_sign = FileReference.from_file(value)

    # endregion

    # region "pdf_to_sign_path" accessors

    @property
    def pdf_to_sign_path(self):
        return self.__get_pdf_to_sign_path()

    def __get_pdf_to_sign_path(self):
        return self.__pdf_to_sign.path

    @pdf_to_sign_path.setter
    def pdf_to_sign_path(self, value):
        self.__set_pdf_to_sign_path(value)

    def __set_pdf_to_sign_path(self, value):
        if value is None:
            raise Exception('The provided "pdf_to_sign_path" is not valid')
        self.__pdf_to_sign = FileReference.from_path(value)

    def set_pdf_to_sign_from_path(self, path):
        self.__set_pdf_to_sign_path(path)

    def set_pdf_to_sign_path(self, path):
        self.set_pdf_to_sign_from_path(path)

    def set_pdf_to_sign(self, path):
        self.set_pdf_to_sign_path(path)


    # endregion

    # region "pdf_to_sign_content" accessors

    @property
    def pdf_to_sign_content(self):
        return self.__get_pdf_to_sign_content()

    def __get_pdf_to_sign_content(self):
        return self.__pdf_to_sign.content_raw

    @pdf_to_sign_content.setter
    def pdf_to_sign_content(self, value):
        self.__set_pdf_to_sign_content(value)

    def __set_pdf_to_sign_content(self, value):
        if value is None:
            raise Exception('The provided "pdf_to_sign_content" is not valid')
        self.__pdf_to_sign = FileReference.from_content_raw(value)

    def set_pdf_to_sign_from_content_raw(self, content_raw):
        self.__set_pdf_to_sign_content(content_raw)

    def set_pdf_to_sign_content(self, content_raw):
        self.set_pdf_to_sign_from_content_raw(content_raw)

    # endregion

    # region "pdf_to_sign_base64" accessors

    @property
    def pdf_to_sign_base64(self):
        return self.__get_pdf_to_sign_base64()

    def __get_pdf_to_sign_base64(self):
        return self.__pdf_to_sign.content_base64

    @pdf_to_sign_base64.setter
    def pdf_to_sign_base64(self, value):
        self.__set_pdf_to_sign_base64(value)

    def __set_pdf_to_sign_base64(self, value):
        if value is None:
            raise Exception('The provided "pdf_to_sign_base64" is not valid')
        self.__pdf_to_sign = FileReference.from_content_base64(value)

    def set_pdf_to_sign_from_content_base64(self, content_base64):
        self.__set_pdf_to_sign_base64(content_base64)

    # endregion

    @property
    def bypass_marks_if_signed(self):
        return self.__bypass_marks_if_signed

    @bypass_marks_if_signed.setter
    def bypass_marks_if_signed(self, value):
        self.__bypass_marks_if_signed = value

    @property
    def pdf_marks(self):
        return self.__pdf_marks

    @pdf_marks.setter
    def pdf_marks(self, value):
        self.__pdf_marks = value

    def add_mark(self, value):
        if self.__pdf_marks is None:
            self.__pdf_marks = []
        self.__pdf_marks.append(value)

    @property
    def measurement_units(self):
        return self.__measurement_units

    @measurement_units.setter
    def measurement_units(self, value):
        self.__measurement_units = value

    @property
    def page_optimization(self):
        return self.__page_optimization

    @page_optimization.setter
    def page_optimization(self, value):
        self.__page_optimization = value

    @property
    def visual_representation(self):
        return self.__visual_representation

    @visual_representation.setter
    def visual_representation(self, value):
        self.__visual_representation = value

    def start(self):
        if self._signer_certificate is None:
            raise Exception('The certificate was not set')
        response = self.__start_common()
        return SignatureStartResult(response)

    def start_with_web_pki(self):
        response = self.__start_common()
        return SignatureStartResult(response)

    def start_with_webpki(self):
        return self.start_with_web_pki()

    def __start_common(self):

        if not self.__pdf_to_sign:
            raise Exception('The PDF to be signed was not set')

        if not self._signature_policy_id:
            raise Exception('The signature policy was not set')

        api_version = _get_api_version(self._client, Apis.START_PADES)
        if api_version == 1:
            return self.__start_common_v1()
        return self.__start_common_v2()

    def __start_common_v2(self):
        request = self.__get_start_common_request()
        request['pdfToSign'] = \
            self.__pdf_to_sign.upload_or_reference(self._client)
        return self._client.post('Api/v2/PadesSignatures', request)

    def __start_common_v1(self):
        request = self.__get_start_common_request()
        request['pdfToSign'] = self.__pdf_to_sign.content_base64
        return self._client.post('Api/PadesSignatures', request)

    def __get_start_common_request(self):
        return {
            'certificate': self._signer_certificate,
            'signaturePolicyId': self._signature_policy_id,
            'securityContextId': self._security_context_id,
            'ignoreRevocationStatusUnknown':
                self._ignore_revocation_status_unknown,
            'callbackArgument': self._callback_argument,
            'pdfMarks': [m.to_model() for m in self.__pdf_marks],
            'bypassMarksIfSigned': self.__bypass_marks_if_signed,
            'measurementUnits': self.__measurement_units,
            'pageOptimization': self.__page_optimization.to_model()
                                if self.__page_optimization is not None
                                else None,
            'visualRepresentation': self.__visual_representation
        }


__all__ = ['PadesSignatureStarter']
