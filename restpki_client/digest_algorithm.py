from .oids import Oids


class DigestAlgorithms(object):
    """

    Definition of

    """
    MD5 = 'MD5'
    SHA1 = 'SHA1'
    SHA256 = 'SHA256'
    SHA384 = 'SHA384'
    SHA512 = 'SHA512'


class DigestAlgorithm(object):
    MD5 = None
    SHA1 = None
    SHA256 = None
    SHA384 = None
    SHA512 = None

    def __init__(self, name, oid, byte_length, api_model, xml_uri):
        self.__name = name
        self.__oid = oid
        self.__byte_length = byte_length
        self.__api_model = api_model
        self.__xml_uri = xml_uri

    def __eq__(self, instance):
        if instance is None:
            return False

        if self == instance:
            return True

        return self.__oid == instance.oid

    @staticmethod
    def _algorithms():
        return [
            DigestAlgorithm.MD5,
            DigestAlgorithm.SHA1,
            DigestAlgorithm.SHA256,
            DigestAlgorithm.SHA384,
            DigestAlgorithm.SHA512
        ]

    @staticmethod
    def get_instance_by_name(name):
        filtered_list = list(filter(lambda a: a.name == name,
                                    DigestAlgorithm._algorithms()))
        alg = filtered_list[0] if len(filtered_list) > 0 else None

        if alg is None:
            raise Exception('Unrecognized digest algorithm name: %s' % name)

        return alg

    @staticmethod
    def get_instance_by_oid(oid):
        filtered_list = list(filter(lambda a: a.oid == oid,
                                    DigestAlgorithm._algorithms()))
        alg = filtered_list[0] if len(filtered_list) > 0 else None

        if alg is None:
            raise Exception('Unrecognized digest algorithm oid: %s' % oid)

        return alg

    @staticmethod
    def get_instance_by_xml_uri(xml_uri):
        filtered_list = list(filter(lambda a: a.xml_uri == xml_uri,
                                    DigestAlgorithm._algorithms()))
        alg = filtered_list[0] if len(filtered_list) > 0 else None

        if alg is None:
            raise Exception('Unrecognized digest algorithm XML URI: %s' %
                            xml_uri)
        return alg

    @staticmethod
    def get_instance_by_api_model(algorithm):
        if algorithm == DigestAlgorithms.MD5:
            return DigestAlgorithm.MD5
        elif algorithm == DigestAlgorithms.SHA1:
            return DigestAlgorithm.SHA1
        elif algorithm == DigestAlgorithms.SHA256:
            return DigestAlgorithm.SHA256
        elif algorithm == DigestAlgorithms.SHA384:
            return DigestAlgorithm.SHA384
        elif algorithm == DigestAlgorithms.SHA512:
            return DigestAlgorithm.SHA512
        else:
            raise Exception('Unsupported digest algorithm: %s' % algorithm)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def oid(self):
        return self.__oid

    @oid.setter
    def oid(self, value):
        self.__oid = value

    @property
    def byte_length(self):
        return self.__byte_length

    @byte_length.setter
    def byte_length(self, value):
        self.__byte_length = value

    @property
    def api_model(self):
        return self.__api_model

    @api_model.setter
    def api_model(self, value):
        self.__api_model = value

    @property
    def xml_uri(self):
        return self.__xml_uri

    @xml_uri.setter
    def xml_uri(self, value):
        self.__xml_uri = value


class MD5DigestAlgorithm(DigestAlgorithm):

    def __init__(self):
        name = 'MD5'
        oid = Oids.MD5
        byte_length = 16
        api_model = DigestAlgorithms.MD5
        xml_uri = 'http://www.w3.org/2001/04/xmldsig-more#md5'
        super(MD5DigestAlgorithm, self).__init__(name, oid, byte_length,
                                                 api_model, xml_uri)


class SHA1DigestAlgorithm(DigestAlgorithm):

    def __init__(self):
        name = 'SHA-1'
        oid = Oids.SHA1
        byte_length = 20
        api_model = DigestAlgorithms.SHA1
        xml_uri = 'http://www.w3.org/2000/09/xmldsig#sha1'
        super(SHA1DigestAlgorithm, self).__init__(name, oid, byte_length,
                                                  api_model, xml_uri)


class SHA256DigestAlgorithm(DigestAlgorithm):

    def __init__(self):
        name = 'SHA-256'
        oid = Oids.SHA256
        byte_length = 32
        api_model = DigestAlgorithms.SHA256
        xml_uri = 'http://www.w3.org/2001/04/xmlenc#sha256'
        super(SHA256DigestAlgorithm, self).__init__(name, oid, byte_length,
                                                    api_model, xml_uri)


class SHA384DigestAlgorithm(DigestAlgorithm):

    def __init__(self):
        name = 'SHA-384'
        oid = Oids.SHA384
        byte_length = 48
        api_model = DigestAlgorithms.SHA384
        xml_uri = 'http://www.w3.org/2001/04/xmldsig-more#sha384'
        super(SHA384DigestAlgorithm, self).__init__(name, oid, byte_length,
                                                    api_model, xml_uri)


class SHA512DigestAlgorithm(DigestAlgorithm):

    def __init__(self):
        name = 'SHA-512'
        oid = Oids.SHA512
        byte_length = 64
        api_model = DigestAlgorithms.SHA512
        xml_uri = 'http://www.w3.org/2001/04/xmlenc#sha512'
        super(SHA512DigestAlgorithm, self).__init__(name, oid, byte_length,
                                                    api_model, xml_uri)


DigestAlgorithm.MD5 = MD5DigestAlgorithm()
DigestAlgorithm.SHA1 = SHA1DigestAlgorithm()
DigestAlgorithm.SHA256 = SHA256DigestAlgorithm()
DigestAlgorithm.SHA384 = SHA384DigestAlgorithm()
DigestAlgorithm.SHA512 = SHA512DigestAlgorithm()

__all__ = [
    'DigestAlgorithms',
    'DigestAlgorithm',
    'MD5DigestAlgorithm',
    'SHA1DigestAlgorithm',
    'SHA256DigestAlgorithm',
    'SHA384DigestAlgorithm',
    'SHA512DigestAlgorithm'
]
