from .standard_signature_policies import StandardSignaturePolicies


class SignaturePolicyCatalog(object):

    def __init__(self, policies=None):
        self.__policies = []
        if policies is not None:
            self.__policies.append(policies)

    @staticmethod
    def get_pki_brazil_cades():
        return SignaturePolicyCatalog([
            StandardSignaturePolicies.PKI_BRAZIL_CADES_ADR_BASICA,
            StandardSignaturePolicies.PKI_BRAZIL_CADES_ADR_TEMPO,
            StandardSignaturePolicies.PKI_BRAZIL_CADES_ADR_COMPLETA
        ])

    @staticmethod
    def get_pki_brazil_cades_with_signer_certificate_protection():
        return SignaturePolicyCatalog([
            StandardSignaturePolicies.PKI_BRAZIL_CADES_ADR_TEMPO,
            StandardSignaturePolicies.PKI_BRAZIL_CADES_ADR_COMPLETA
        ])

    @staticmethod
    def get_pki_brazil_cades_with_ca_certificate_protection():
        return SignaturePolicyCatalog([
            StandardSignaturePolicies.PKI_BRAZIL_CADES_ADR_COMPLETA
        ])

    @staticmethod
    def get_pki_brazil_pades():
        return SignaturePolicyCatalog([
            StandardSignaturePolicies.PKI_BRAZIL_PADES_ADR_BASICA,
            StandardSignaturePolicies.PKI_BRAZIL_PADES_ADR_TEMPO
        ])

    @staticmethod
    def get_pki_brazil_pades_with_signer_certificate_protection():
        return SignaturePolicyCatalog([
            StandardSignaturePolicies.PKI_BRAZIL_PADES_ADR_TEMPO
        ])

    @staticmethod
    def get_pki_brazil_xades():
        return SignaturePolicyCatalog([
            StandardSignaturePolicies.PKI_BRAZIL_XADES_ADR_BASICA,
            StandardSignaturePolicies.PKI_BRAZIL_XADES_ADR_TEMPO
        ])


__all__ = ['SignaturePolicyCatalog']
