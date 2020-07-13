class PadesCertificationLevel(object):
    NOT_CERTIFIED = 'not-certified'
    CERTIFIED_FORM_FILLING = 'certified-form-filling'
    CERTIFIED_FORM_FILLING_AND_ANNOTATIONS = 'certified-form-filling-annotations'
    CERTIFIED_NO_CHANGES_ALLOWED = 'certified-no-changes-allowed'


    def __init__(self):
        pass


__all__ = ['PadesCertificationLevel']
