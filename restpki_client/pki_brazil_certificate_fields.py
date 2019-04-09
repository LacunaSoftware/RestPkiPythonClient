import re


class PkiBrazilCertificateFields(object):

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


__all__ = ['PkiBrazilCertificateFields']
