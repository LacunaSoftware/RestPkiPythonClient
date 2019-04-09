from .apis import Apis
from .rest_pki_client import _get_api_version
from .signature_finisher import SignatureFinisher


class CadesSignatureFinisher(SignatureFinisher):

    def _check_compatibility(self):
        api_version = _get_api_version(self._client, Apis.COMPLETE_CADES)
        if api_version < 2:
            raise Exception('The CadesSignatureFinisher class can only be used'
                            ' with REST PKI 1.11 or later.')

    def _get_api_route(self):
        return 'Api/v2/CadesSignatures/%s/SignedBytes' % self._token


__all__ = ['CadesSignatureFinisher']
