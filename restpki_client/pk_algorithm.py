from .oids import Oids
from .digest_algorithm import DigestAlgorithm


class SignatureAlgorithms(object):
    MD5_WITH_RSA = 'MD5WithRSA'
    SHA1_WITH_RSA = 'SHA1WithRSA'
    SHA256_WITH_RSA = 'SHA256WithRSA'
    SHA384_WITH_RSA = 'SHA384WithRSA'
    SHA512_WITH_RSA = 'SHA512WithRSA'


class SignatureAlgorithm(object):
    MD5_WITH_RSA = None
    SHA1_WITH_RSA = None
    SHA256_WITH_RSA = None
    SHA384_WITH_RSA = None
    SHA512_WITH_RSA = None

    def __init__(self, name, oid, xml_uri, digest_algorithm, pk_algorithm):
        self.__name = name
        self.__oid = oid
        self.__xml_uri = xml_uri
        self.__digest_algorithm = digest_algorithm
        self.__pk_algorithm = pk_algorithm

    def __eq__(self, instance):
        if instance is None:
            return False

        if self == instance:
            return True

        return self.__oid == instance.oid

    @staticmethod
    def _algorithms():
        return [
            SignatureAlgorithm.MD5_WITH_RSA,
            SignatureAlgorithm.SHA1_WITH_RSA,
            SignatureAlgorithm.SHA256_WITH_RSA,
            SignatureAlgorithm.SHA384_WITH_RSA,
            SignatureAlgorithm.SHA512_WITH_RSA
        ]

    @staticmethod
    def _safe_algorithms():
        return [
            SignatureAlgorithm.SHA1_WITH_RSA,
            SignatureAlgorithm.SHA256_WITH_RSA,
            SignatureAlgorithm.SHA384_WITH_RSA,
            SignatureAlgorithm.SHA512_WITH_RSA
        ]

    @staticmethod
    def get_instance_by_name(name):
        filtered_list = list(filter(lambda s: s.name == name,
                                    SignatureAlgorithm._algorithms()))
        alg = filtered_list[0] if len(filtered_list) > 0 else None

        if alg is None:
            raise Exception('Unrecognized signature algorithm name: %s' % name)

        return alg

    @staticmethod
    def get_instance_by_oid(oid):
        filtered_list = list(filter(lambda s: s.oid == oid,
                                    SignatureAlgorithm._algorithms()))
        alg = filtered_list[0] if len(filtered_list) > 0 else None

        if alg is None:
            raise Exception('Unrecognized signature algorithm oid: %s' % oid)

        return alg

    @staticmethod
    def get_instance_by_xml_uri(xml_uri):
        filtered_list = list(filter(lambda s: s.xml_uri == xml_uri,
                                    SignatureAlgorithm._algorithms()))
        alg = filtered_list[0] if len(filtered_list) > 0 else None

        if alg is None:
            raise Exception('Unrecognized signature algorithm XML URI: %s',
                            xml_uri)

        return alg

    @staticmethod
    def get_instance_by_api_model(algorithm):
        if algorithm == SignatureAlgorithms.MD5_WITH_RSA:
            return SignatureAlgorithm.MD5_WITH_RSA
        elif algorithm == SignatureAlgorithms.SHA1_WITH_RSA:
            return SignatureAlgorithm.SHA1_WITH_RSA
        elif algorithm == SignatureAlgorithms.SHA256_WITH_RSA:
            return SignatureAlgorithm.SHA256_WITH_RSA
        elif algorithm == SignatureAlgorithms.SHA384_WITH_RSA:
            return SignatureAlgorithm.SHA384_WITH_RSA
        elif algorithm == SignatureAlgorithms.SHA512_WITH_RSA:
            return SignatureAlgorithm.SHA512_WITH_RSA
        else:
            raise Exception('Unsupported signature algorithm: %s' % algorithm)

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
    def xml_uri(self):
        return self.__xml_uri

    @xml_uri.setter
    def xml_uri(self, value):
        self.__xml_uri = value

    @property
    def digest_algorithm(self):
        return self.__digest_algorithm

    @digest_algorithm.setter
    def digest_algorithm(self, value):
        self.__digest_algorithm = value

    @property
    def pk_algorithm(self):
        return self.__pk_algorithm

    @pk_algorithm.setter
    def pk_algorithm(self, value):
        self.__pk_algorithm = value


class PKAlgorithms(object):
    RSA = 'RSA'


class PKAlgorithm(object):
    RSA = None

    def __init__(self, name, oid):
        self.__name = name
        self.__oid = oid

    def __eq__(self, instance):
        if instance is None:
            return False

        if self == instance:
            return True

        return self.__oid == instance.oid

    @staticmethod
    def _algorithms():
        return [PKAlgorithm.RSA]

    @staticmethod
    def get_instance_by_name(name):
        filtered_list = list(filter(lambda p: p.name == name,
                                    PKAlgorithm._algorithms()))
        alg = filtered_list[0] if len(filtered_list) > 0 else None

        if alg is None:
            raise Exception('Unrecognized private key algorithm name: %s' %
                            name)

        return alg

    @staticmethod
    def get_instance_by_oid(oid):
        filtered_list = list(filter(lambda p: p.oid == oid,
                                    PKAlgorithm._algorithms()))
        alg = filtered_list[0] if len(filtered_list) > 0 else None

        if alg is None:
            raise Exception('Unrecognized private key algorithm oid: %s' % oid)

        return alg

    @staticmethod
    def get_instance_api_model(algorithm):
        if algorithm is PKAlgorithms.RSA:
            return PKAlgorithm.RSA
        else:
            raise Exception('Unsupported private key algorithm: %s' % algorithm)

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


class RSASignatureAlgorithm(SignatureAlgorithm):

    def __init__(self, digest_algorithm):
        name = '%s with RSA' % digest_algorithm
        pk_algorithm = PKAlgorithm.RSA

        if digest_algorithm is DigestAlgorithm.MD5:
            xml_uri = 'http://www.w3.org/2001/04/xmldsig-more#rsa-md5'
            oid = Oids.MD5_WITH_RSA
        elif digest_algorithm is DigestAlgorithm.SHA1:
            xml_uri = 'http://www.w3.org/2000/09/xmldsig#rsa-sha1'
            oid = Oids.SHA1_WITH_RSA
        elif digest_algorithm is DigestAlgorithm.SHA256:
            xml_uri = 'http://www.w3.org/2001/04/xmldsig-more#rsa-sha256'
            oid = Oids.SHA256_WITH_RSA
        elif digest_algorithm is DigestAlgorithm.SHA384:
            xml_uri = 'http://www.w3.org/2001/04/xmldsig-more#rsa-sha384'
            oid = Oids.SHA384_WITH_RSA
        elif digest_algorithm is DigestAlgorithm.SHA512:
            xml_uri = 'http://www.w3.org/2001/04/xmldsig-more#rsa-sha512'
            oid = Oids.SHA512_WITH_RSA
        else:
            raise Exception('Unsupported digest algorithms: %s' %
                            digest_algorithm)

        super(RSASignatureAlgorithm, self).__init__(name, oid, xml_uri,
                                                    digest_algorithm,
                                                    pk_algorithm)


SignatureAlgorithm.MD5_WITH_RSA = RSASignatureAlgorithm(DigestAlgorithm.MD5)
SignatureAlgorithm.SHA1_WITH_RSA = RSASignatureAlgorithm(DigestAlgorithm.SHA1)
SignatureAlgorithm.SHA256_WITH_RSA = \
    RSASignatureAlgorithm(DigestAlgorithm.SHA256)
SignatureAlgorithm.SHA384_WITH_RSA = \
    RSASignatureAlgorithm(DigestAlgorithm.SHA384)
SignatureAlgorithm.SHA512_WITH_RSA = \
    RSASignatureAlgorithm(DigestAlgorithm.SHA512)


class RSAPKAlgorithm(PKAlgorithm):

    def __init__(self):
        name = PKAlgorithms.RSA
        oid = Oids.RSA
        super(RSAPKAlgorithm, self).__init__(name, oid)

    @staticmethod
    def get_signature_algorithm(digest_algorithm):
        return RSASignatureAlgorithm(digest_algorithm)


PKAlgorithm.RSA = RSAPKAlgorithm()

__all__ = [
    'SignatureAlgorithms',
    'SignatureAlgorithm',
    'PKAlgorithms',
    'PKAlgorithm',
    'RSASignatureAlgorithm',
    'RSAPKAlgorithm'
]
