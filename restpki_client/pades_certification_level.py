class PadesCertificationLevel(object):
    NOT_CERTIFIED = 'NotCertified'
    CERTIFIED_FORM_FILLING = 'CertifiedFormFilling'
    CERTIFIED_FORM_FILLING_AND_ANNOTATIONS = 'CertifiedFormFillingAndAnnotations'
    CERTIFIED_NO_CHANGES_ALLOWED = 'CertifiedNoChangesAllowed'


    def __init__(self):
        pass


__all__ = ['PadesCertificationLevel']
