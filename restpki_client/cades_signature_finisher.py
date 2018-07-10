from .signature_finisher import SignatureFinisher
from .signature_result import SignatureResult


class CadesSignatureFinisher(SignatureFinisher):

    def __init__(self, client):
        SignatureFinisher.__init__(self, client)

    def finish(self):

        if not self._token:
            raise Exception('The token was not set')

        if not self._signature:
            response = self._client.post(
                'Api/CadesSignatures/%s/Finalize' % self._token)

            return SignatureResult(
                self._client,
                response.get('cms', None),
                response.get('certificate', None),
                response.get('callbackArgument', None)
            )

        else:
            request = dict()
            request['signature'] = self._signature

            response = self._client.post(
                'Api/CadesSignatures/%s/SignedBytes' % self._token,
                data=request)

            return SignatureResult(
                self._client,
                response.get('cms', None),
                response.get('certificate', None),
                response.get('callbackArgument', None)
            )


__all__ = ['CadesSignatureFinisher']
