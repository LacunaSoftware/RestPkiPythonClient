import re


class PKCertificate:

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


class PkiItalyCertificateFields:

    def __init__(self, model):
        self._certificate_type = model.get('certificateType', None)
        self._codice_fiscale = model.get('codiceFiscale', None)
        self._id_carta = model.get('idCarta', None)

    @property
    def certificate_type(self):
        return self._certificate_type

    @certificate_type.setter
    def certificate_type(self, value):
        self._certificate_type = value

    @property
    def codice_fiscale(self):
        return self._codice_fiscale

    @codice_fiscale.setter
    def codice_fiscale(self, value):
        self._codice_fiscale = value

    @property
    def id_carta(self):
        return self._id_carta

    @id_carta.setter
    def id_carta(self, value):
        self._id_carta = value


class PkiBrazilCertificateFields:

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

    @certificate_type.setter
    def certificate_type(self, value):
        self._certificate_type = value

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, value):
        self._cpf = value

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

    @cnpj.setter
    def cnpj(self, value):
        self._cnpj = value

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

    @responsavel.setter
    def responsavel(self, value):
        self._responsavel = value

    @property
    def company_name(self):
        return self._company_name

    @company_name.setter
    def company_name(self, value):
        self._company_name = value

    @property
    def oab_uf(self):
        return self._oab_uf

    @oab_uf.setter
    def oab_uf(self, value):
        self._oab_uf = value

    @property
    def oab_numero(self):
        return self._oab_numero

    @oab_numero.setter
    def oab_numero(self, value):
        self._oab_numero = value

    @property
    def rg_numero(self):
        return self._rg_numero

    @rg_numero.setter
    def rg_numero(self, value):
        self._rg_numero = value

    @property
    def rg_emissor(self):
        return self._rg_emissor

    @rg_emissor.setter
    def rg_emissor(self, value):
        self._rg_emissor = value

    @property
    def rg_emissor_uf(self):
        return self._rg_emissor_uf

    @rg_emissor_uf.setter
    def rg_emissor_uf(self, value):
        self._rg_emissor_uf = value

    @property
    def date_of_birth(self):
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, value):
        self._date_of_birth = value


class Name:

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

    @common_name.setter
    def common_name(self, value):
        self._common_name = value

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, value):
        self._country = value

    @property
    def dn_qualifier(self):
        return self._dn_qualifier

    @dn_qualifier.setter
    def dn_qualifier(self, value):
        self._dn_qualifier = value

    @property
    def email_address(self):
        return self._email_address

    @email_address.setter
    def email_address(self, value):
        self._email_address = value

    @property
    def generation_qualifier(self):
        return self._generation_qualifier

    @generation_qualifier.setter
    def generation_qualifier(self, value):
        self._generation_qualifier = value

    @property
    def given_name(self):
        return self._given_name

    @given_name.setter
    def given_name(self, value):
        self._given_name = value

    @property
    def initials(self):
        return self._initials

    @initials.setter
    def initials(self, value):
        self._initials = value

    @property
    def locality(self):
        return self._locality

    @locality.setter
    def locality(self, value):
        self._locality = value

    @property
    def organization(self):
        return self._organization

    @organization.setter
    def organization(self, value):
        self._organization = value

    @property
    def organization_unit(self):
        return self._organization_unit

    @organization_unit.setter
    def organization_unit(self, value):
        self._organization_unit = value

    @property
    def pseudonym(self):
        return self._pseudonym

    @pseudonym.setter
    def pseudonym(self, value):
        self._pseudonym = value

    @property
    def serial_number(self):
        return self._serial_number

    @serial_number.setter
    def serial_number(self, value):
        self._serial_number = value

    @property
    def state_name(self):
        return self._state_name

    @state_name.setter
    def state_name(self, value):
        self._state_name = value

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, value):
        self._surname = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


__all__ = [
    'PKCertificate',
    'PkiItalyCertificateFields',
    'PkiBrazilCertificateFields',
    'Name'
]
