import re


class PKCertificate:
    _email_address = None
    _serial_number = None
    _validity_start = None
    _validity_end = None
    _subject_name = None
    _issuer_name = None
    _pki_brazil = None
    _pki_italy = None
    _issuer = None

    def __init__(self, model):
        self._email_address = model.get('emailAddress', None)
        self._serial_number = model.get('serialNumber', None)
        self._validity_start = model.get('validityStart', None)
        self._validity_end = model.get('validityEnd', None)

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

    @property
    def serial_number(self):
        return self._serial_number

    @property
    def validity_start(self):
        return self._validity_start

    @property
    def validity_end(self):
        return self._validity_end

    @property
    def subject_name(self):
        return self._subject_name

    @property
    def issuer_name(self):
        return self._issuer_name

    @property
    def pki_brazil(self):
        return self._pki_brazil

    @property
    def pki_italy(self):
        return self._pki_italy

    @property
    def issuer(self):
        return self._issuer


class PkiItalyCertificateFields:
    _certificate_type = None
    _codice_fiscale = None
    _id_carta = None

    def __init__(self, model):
        self._certificate_type = model.get('certificateType', None)
        self._codice_fiscale = model.get('codiceFiscale', None)
        self._id_carta = model.get('idCarta', None)

    @property
    def certificate_type(self):
        return self._certificate_type

    @property
    def codice_fiscale(self):
        return self._codice_fiscale

    @property
    def id_carta(self):
        return self._id_carta


class PkiBrazilCertificateFields:
    _certificate_type = None
    _cpf = None
    _cnpj = None
    _responsavel = None
    _company_name = None
    _oab_uf = None
    _oab_numero = None
    _rg_numero = None
    _rg_emissor = None
    _rg_emissor_uf = None
    _date_of_birth = None

    def __init__(self, model):
        self._certificate_type = model.get('certificateType', None)
        self._cpf = model.get('cpf', None)
        self._cnpj = model.get('cnpj', None)
        self._responsavel = model.get('responsavel', None)
        self._company_name = model.get('companyName', None)
        self._oab_uf = model.get('oabUF', None)
        self._oab_numero = model.get('oabNumero', None)
        self._rg_numero = model.get('rgNumero', None)
        self._rg_emissor = model.get('rgEmissor', None)
        self._rg_emissor_uf = model.get('rgEmissorUF', None)
        self._date_of_birth = model.get('dateOfBirth', None)

    @property
    def certificate_type(self):
        return self._certificate_type

    @property
    def cpf(self):
        return self._cpf

    @property
    def cpf_formatted(self):
        if self._cpf is None:
            return ''
        if not re.match('^\d{11}$', self._cpf):
            return self._cpf
        return "%s.%s.%s-%s" % (self._cpf[:3], self._cpf[3:6], self._cpf[6:9],
                                self._cpf[9:])

    @property
    def cnpj(self):
        return self._cnpj

    @property
    def cnpj_formatted(self):
        if self._cnpj is None:
            return ''
        if not re.match('^\d{14}', self._cnpj):
            return self._cnpj
        return "%s.%s.%s/%s-%s" % (self._cnpj[:2], self._cnpj[2:5],
                                   self._cnpj[5:8], self._cnpj[8:12],
                                   self._cnpj[12:])

    @property
    def responsavel(self):
        return self._responsavel

    @property
    def company_name(self):
        return self._company_name

    @property
    def oab_uf(self):
        return self._oab_uf

    @property
    def oab_numero(self):
        return self._oab_numero

    @property
    def rg_numero(self):
        return self._rg_numero

    @property
    def rg_emissor(self):
        return self._rg_emissor

    @property
    def rg_emissor_uf(self):
        return self._rg_emissor_uf

    @property
    def date_of_birth(self):
        return self._date_of_birth


class Name:
    _common_name = None
    _country = None
    _dn_qualifier = None
    _email_address = None
    _generation_qualifier = None
    _given_name = None
    _initials = None
    _locality = None
    _organization = None
    _organization_unit = None
    _pseudonym = None
    _serial_number = None
    _state_name = None
    _surname = None
    _title = None

    def __init__(self, model):
        self._common_name = model.get('commonName', None)
        self._country = model.get('country', None)
        self._dn_qualifier = model.get('dnQualifier', None)
        self._email_address = model.get('emailAddress', None)
        self._generation_qualifier = model.get('generationQualifier', None)
        self._given_name = model.get('givenName', None)
        self._initials = model.get('initials', None)
        self._locality = model.get('locality', None)
        self._organization = model.get('organization', None)
        self._organization_unit = model.get('organizationUnit', None)
        self._pseudonym = model.get('pseudonym', None)
        self._serial_number = model.get('serialNumber', None)
        self._state_name = model.get('stateName', None)
        self._surname = model.get('surname', None)
        self._title = model.get('title', None)

    @property
    def common_name(self):
        return self._common_name

    @property
    def country(self):
        return self._country

    @property
    def dn_qualifier(self):
        return self._dn_qualifier

    @property
    def email_address(self):
        return self._email_address

    @property
    def generation_qualifier(self):
        return self._generation_qualifier

    @property
    def given_name(self):
        return self._given_name

    @property
    def initials(self):
        return self._initials

    @property
    def locality(self):
        return self._locality

    @property
    def organization(self):
        return self._organization

    @property
    def organization_unit(self):
        return self._organization_unit

    @property
    def pseudonym(self):
        return self._pseudonym

    @property
    def serial_number(self):
        return self._serial_number

    @property
    def state_name(self):
        return self._state_name

    @property
    def surname(self):
        return self._surname

    @property
    def title(self):
        return self._title


__all__ = [
    'PKCertificate',
    'PkiItalyCertificateFields',
    'PkiBrazilCertificateFields',
    'Name'
]
