import base64


class PadesSignatureStarter:
    pdf_content = None
    security_context_id = None
    signature_policy_id = None
    callback_argument = None
    visual_representation = None
    _client = None

    def __init__(self, client):
        self._client = client

    def set_pdf_path(self, local_pdf_path):
        f = open(local_pdf_path, 'rb')
        self.pdf_content = f.read()
        f.close()

    def start_with_webpki(self):
        if self.pdf_content is None:
            raise Exception('The PDF to sign was not set')

        if self.signature_policy_id is None:
            raise Exception('The signature policy was not set')

        data = dict()
        data['pdfToSign'] = base64.b64encode(self.pdf_content)
        data['signaturePolicyId'] = self.signature_policy_id
        data['securityContextId'] = self.security_context_id
        data['callbackArgument'] = self.callback_argument
        data['visualRepresentation'] = self.visual_representation

        response = self._client.post('Api/PadesSignatures', data=data)
        return response.json().get('token', None)


__all__ = ['PadesSignatureStarter']
