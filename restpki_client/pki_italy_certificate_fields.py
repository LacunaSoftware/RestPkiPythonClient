class PkiItalyCertificateFields(object):

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


__all__ = ['PkiItalyCertificateFields']
