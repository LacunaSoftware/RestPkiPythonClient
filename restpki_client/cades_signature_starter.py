import base64

from .signature_starter import SignatureStarter
from .signature_start_result import SignatureStartResult


class CadesSignatureStarter(SignatureStarter):
    _file_to_sign_content = None
    _cms_to_cosign_content = None
    _encapsulate_content = True

    def __init__(self, client):
        SignatureStarter.__init__(self, client)

    # region set_file_to_sign

    def set_file_to_sign_from_path(self, path):
        with open(path, 'rb') as f:
            self._file_to_sign_content = f.read()

    def set_file_to_sign_from_content_raw(self, content_raw):
        self._file_to_sign_content = content_raw

    def set_file_to_sign_from_content_base64(self, content_base64):
        self._file_to_sign_content = base64.b64decode(content_base64)

    def set_file_to_sign_path(self, path):
        self.set_file_to_sign_from_path(path)

    def set_file_to_sign(self, path):
        self.set_file_to_sign_path(path)

    def set_file_to_sign_content(self, content_raw):
        self.set_file_to_sign_from_content_raw(content_raw)

    # endregion

    # region set_cms_to_cosign

    def set_cms_to_cosign_from_path(self, path):
        with open(path, 'rb') as f:
            self._cms_to_cosign_content = f.read()

    def set_cms_to_cosign_from_content_raw(self, content_raw):
        self._cms_to_cosign_content = content_raw

    def set_cms_to_cosign_from_content_base64(self, content_base64):
        self._cms_to_cosign_content = base64.b64decode(content_base64)

    def set_cms_to_cosign_path(self, path):
        self.set_cms_to_cosign_from_path(path)

    def set_cms_to_cosign(self, path):
        self.set_cms_to_cosign_path(path)

    def set_cms_to_cosign_content(self, content_raw):
        self.set_cms_to_cosign_from_content_raw(content_raw)

    # endregion

    @property
    def encapsulate_content(self):
        return self._encapsulate_content

    @encapsulate_content.setter
    def encapsulate_content(self, value):
        self._encapsulate_content = value

    def start_with_webpki(self):
        response = self._start_common()

        return SignatureStartResult(response.get('token', None),
                                    response.get('certificate', None))

    def _start_common(self):

        if not self._file_to_sign_content and not self._cms_to_cosign_content:
            raise Exception(
                'The content to sign was not set and no CMS to be co-signed was'
                ' given'
            )

        if not self._signature_policy_id:
            raise Exception('The signature policy was not set')

        request = {
            'signaturePolicyId': self._signature_policy_id,
            'securityContextId': self._security_context_id,
            'callbackArgument': self._callback_argument,
            'encapsulateContent': self._encapsulate_content
        }
        if self._file_to_sign_content:
            request['contentToSign'] = \
                base64.b64encode(self._file_to_sign_content)
        if self._cms_to_cosign_content:
            request['cmsToCoSign'] = \
                base64.b64encode(self._cms_to_cosign_content)
        if self._signer_certificate:
            request['certicate'] = base64.b64encode(self._signer_certificate)

        return self._client.post('Api/CadesSignatures', data=request)


__all__ = ['CadesSignatureStarter']
