import base64


class CadesSignatureStarter:
    content_to_sign = None
    security_context_id = None
    signature_policy_id = None
    cms_to_cosign_bytes = None
    encapsulate_content = None
    callback_argument = None
    _client = None

    def __init__(self, client):
        self._client = client

    def set_file_to_sign_path(self, path):
        f = open(path, 'rb')
        self.content_to_sign = f.read()
        f.close()

    def set_cms_to_cosign_path(self, path):
        f = open(path, 'rb')
        self.cms_to_cosign_bytes = f.read()
        f.close()

    def start_with_webpki(self):
        if self.content_to_sign is None and self.cms_to_cosign_bytes is None:
            raise Exception(
                'The content to sign was not set and no CMS to be co-signed was'
                ' given'
            )

        if self.signature_policy_id is None:
            raise Exception('The signature policy was not set')

        data = dict()
        data['signaturePolicyId'] = self.signature_policy_id
        data['securityContextId'] = self.security_context_id
        data['callbackArgument'] = self.callback_argument
        data['encapsulateContent'] = self.encapsulate_content
        if self.content_to_sign is not None:
            data['contentToSign'] = base64.b64encode(self.content_to_sign)
        if self.cms_to_cosign_bytes is not None:
            data['cmsToCoSign'] = base64.b64encode(self.cms_to_cosign_bytes)

        response = self._client.post('Api/CadesSignatures', data=data)
        return response.json().get('token', None)


__all__ = ['CadesSignatureStarter']
