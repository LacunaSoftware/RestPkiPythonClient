from .pades_signature import PadesSignature
from .signature_explorer import SignatureExplorer


class PadesSignatureExplorer(SignatureExplorer):
    PDF_MIME_TYPE = 'application/pdf'

    def __init__(self, client):
        super(PadesSignatureExplorer, self).__init__(client)

    def open(self):
        if self._signature_file is None:
            raise Exception('The signature file to be opened was not set')

        request = {}
        self._fill_request(request)
        response = self._client.post('Api/PadesSignatures/Open', data=request)
        return PadesSignature(response)


__all__ = ['PadesSignatureExplorer']
