from .pki_brazil_certificate_fields import PkiBrazilCertificateFields
from .pki_italy_certificate_fields import PkiItalyCertificateFields
from .name import Name


class PKCertificate(object):

    def __init__(self, model):
        self._email_address = model.get('emailAddress', None)
        self._serial_number = model.get('serialNumber', None)
        self._validity_start = model.get('validityStart', None)
        self._validity_end = model.get('validityEnd', None)
        self._subject_name = None
        self._issuer_name = None
        self._pki_brazil = None
        self._pki_italy = None
        self._issuer = None

        subject_name = model.get('subjectName', None)
        if subject_name is not None:
            self._subject_name = Name(subject_name)

        issuer_name = model.get('issuerName', None)
        if issuer_name is not None:
            self._issuer_name = Name(issuer_name)

        pki_brazil = model.get('pkiBrazil', None)
        if pki_brazil is not None:
            self._pki_brazil = PkiBrazilCertificateFields(pki_brazil)

        pki_italy = model.get('pkiItaly', None)
        if pki_italy is not None:
            self._pki_italy = PkiItalyCertificateFields(pki_italy)

        issuer = model.get('issuer', None)
        if issuer is not None:
            self._issuer = PKCertificate(issuer)

    @property
    def email_address(self):
        return self._email_address

    @email_address.setter
    def email_address(self, value):
        self._email_address = value

    @property
    def serial_number(self):
        return self._serial_number

    @serial_number.setter
    def serial_number(self, value):
        self._serial_number = value

    @property
    def validity_start(self):
        return self._validity_start

    @validity_start.setter
    def validity_start(self, value):
        self._validity_start = value

    @property
    def validity_end(self):
        return self._validity_end

    @validity_end.setter
    def validity_end(self, value):
        self._validity_end = value

    @property
    def subject_name(self):
        return self._subject_name

    @subject_name.setter
    def subject_name(self, value):
        self._subject_name = value

    @property
    def issuer_name(self):
        return self._issuer_name

    @issuer_name.setter
    def issuer_name(self, value):
        self._issuer_name = value

    @property
    def pki_brazil(self):
        return self._pki_brazil

    @pki_brazil.setter
    def pki_brazil(self, value):
        self._pki_brazil = value

    @property
    def pki_italy(self):
        return self._pki_italy

    @pki_italy.setter
    def pki_italy(self, value):
        self._pki_italy = value

    @property
    def issuer(self):
        return self._issuer

    @issuer.setter
    def issuer(self, value):
        self._issuer = value


__all__ = ['PKCertificate']
