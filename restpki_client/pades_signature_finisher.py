from .apis import Apis
from .rest_pki_client import _get_api_version
from .signature_finisher import SignatureFinisher


class PadesSignatureFinisher(SignatureFinisher):

    def __init__(self, client):
        super(PadesSignatureFinisher, self).__init__(client)

    def _check_compatibility(self):
        api_version = _get_api_version(self._client, Apis.COMPLETE_PADES)
        if api_version < 2:
            raise Exception('The PadesSignatureFinisher class can only be used'
                            ' with REST PKI 1.11 or later.')

    def _get_api_route(self):
        return 'Api/v2/PadesSignatures/%s/SignedBytes' % self._token


__all__ = ['PadesSignatureFinisher']
