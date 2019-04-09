class Name(object):

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


__all__ = ['Name']
