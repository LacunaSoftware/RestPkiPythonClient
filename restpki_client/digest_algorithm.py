import hashlib
from abc import ABCMeta
from abc import abstractmethod

from six import BytesIO

from .enum import Enum
from .oids import Oids


class DigestAlgorithms(Enum):
    MD5 = None
    SHA1 = None
    SHA256 = None
    SHA384 = None
    SHA512 = None
    SHA3_256 = None


DigestAlgorithms.MD5 = DigestAlgorithms('MD5')
DigestAlgorithms.SHA1 = DigestAlgorithms('SHA1')
DigestAlgorithms.SHA256 = DigestAlgorithms('SHA256')
DigestAlgorithms.SHA384 = DigestAlgorithms('SHA384')
DigestAlgorithms.SHA512 = DigestAlgorithms('SHA512')
DigestAlgorithms.SHA3_256 = DigestAlgorithms('SHA3_256')


class DigestAlgorithm(object):
    __metaclass__ = ABCMeta

    MD5 = None
    SHA1 = None
    SHA256 = None
    SHA384 = None
    SHA512 = None
    SHA3_256 = None

    def __init__(self, name, oid, xml_uri, byte_length, api_model):
        self.__name = name
        self.__oid = oid
        self.__xml_uri = xml_uri
        self.__byte_length = byte_length
        self.__api_model = api_model

    def __eq__(self, instance):
        if instance is None:
            return False

        return self.__oid == instance.oid

    @staticmethod
    def _algorithms():
        return [
            DigestAlgorithm.MD5,
            DigestAlgorithm.SHA1,
            DigestAlgorithm.SHA256,
            DigestAlgorithm.SHA384,
            DigestAlgorithm.SHA512,
            DigestAlgorithm.SHA3_256
        ]

    @staticmethod
    def _get_safe_algorithms():
        return [
            DigestAlgorithm.SHA256,
            DigestAlgorithm.SHA384,
            DigestAlgorithm.SHA512,
            DigestAlgorithm.SHA3_256
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
        elif algorithm == DigestAlgorithms.SHA3_256:
            return DigestAlgorithm.SHA3_256
        else:
            raise Exception('Unsupported digest algorithm: %s' % algorithm)

    def compute_hash_from_content(self, content, offset=0, count=-1):
        stream = BytesIO(content)
        stream.seek(offset, 0)
        hash_func = self.get_hash_func()
        hash_func.update(stream.read(count))
        return hash_func.digest()

    def compute_hash_from_file(self, file_desc, offset=0, count=-1):
        file_desc.seek(offset, 0)
        hash_func = self.get_hash_func()
        hash_func.update(file_desc.read(count))
        return hash_func.digest()

    def check_length(self, digest_value):
        if len(digest_value) != self.__byte_length:
            raise Exception('A %s digest should contain %s bytes, but a value '
                            'with %s bytes was given' % (self.__name,
                                                         self.__byte_length,
                                                         len(digest_value)))

    @property
    def api_model(self):
        return self.__api_model

    @property
    def name(self):
        return self.__name

    @property
    def oid(self):
        return self.__oid

    @property
    def byte_length(self):
        return self.__byte_length

    @property
    def xml_uri(self):
        return self.__xml_uri

    @abstractmethod
    def get_hash_func(self):
        pass


class MD5DigestAlgorithm(DigestAlgorithm):

    def __init__(self):
        name = 'MD5'
        oid = Oids.MD5
        byte_length = 16
        api_model = DigestAlgorithms.MD5
        xml_uri = 'http://www.w3.org/2001/04/xmldsig-more#md5'
        super(MD5DigestAlgorithm, self)\
            .__init__(name, oid, xml_uri, byte_length, api_model)

    def get_hash_func(self):
        return hashlib.md5()


class SHA1DigestAlgorithm(DigestAlgorithm):

    def __init__(self):
        name = 'SHA-1'
        oid = Oids.SHA1
        byte_length = 20
        api_model = DigestAlgorithms.SHA1
        xml_uri = 'http://www.w3.org/2000/09/xmldsig#sha1'
        super(SHA1DigestAlgorithm, self)\
            .__init__(name, oid, xml_uri, byte_length, api_model)

    def get_hash_func(self):
        return hashlib.sha1()


class SHA256DigestAlgorithm(DigestAlgorithm):

    def __init__(self):
        name = 'SHA-256'
        oid = Oids.SHA256
        byte_length = 32
        api_model = DigestAlgorithms.SHA256
        xml_uri = 'http://www.w3.org/2001/04/xmlenc#sha256'
        super(SHA256DigestAlgorithm, self)\
            .__init__(name, oid, xml_uri, byte_length, api_model)

    def get_hash_func(self):
        return hashlib.sha256()


class SHA384DigestAlgorithm(DigestAlgorithm):

    def __init__(self):
        name = 'SHA-384'
        oid = Oids.SHA384
        byte_length = 48
        api_model = DigestAlgorithms.SHA384
        xml_uri = 'http://www.w3.org/2001/04/xmldsig-more#sha384'
        super(SHA384DigestAlgorithm, self)\
            .__init__(name, oid, xml_uri, byte_length, api_model)

    def get_hash_func(self):
        return hashlib.sha384()


class SHA512DigestAlgorithm(DigestAlgorithm):

    def __init__(self):
        name = 'SHA-512'
        oid = Oids.SHA512
        byte_length = 64
        api_model = DigestAlgorithms.SHA512
        xml_uri = 'http://www.w3.org/2001/04/xmlenc#sha512'
        super(SHA512DigestAlgorithm, self)\
            .__init__(name, oid, xml_uri, byte_length, api_model)

    def get_hash_func(self):
        return hashlib.sha512()


class SHA3DigestAlgorithm(DigestAlgorithm):

    def __init__(self, bit_length):
        if bit_length == 256:
            name = 'SHA3-256'
            oid = Oids.SHA3_256
            byte_length = bit_length / 8
            api_model = DigestAlgorithms.SHA3_256
            xml_uri = 'http://www.w3.org/2007/05/xmldsig-more#sha3-256'
            # https://tools.ietf.org/html/rfc6931#section-2.1.5
            super(SHA3DigestAlgorithm, self)\
                .__init__(name, oid, xml_uri, byte_length, api_model)
        else:
            raise Exception('Bit length not supported')
        self.__bit_length = bit_length

    def get_hash_func(self):
        return hashlib.sha3_256()


DigestAlgorithm.MD5 = MD5DigestAlgorithm()
DigestAlgorithm.SHA1 = SHA1DigestAlgorithm()
DigestAlgorithm.SHA256 = SHA256DigestAlgorithm()
DigestAlgorithm.SHA384 = SHA384DigestAlgorithm()
DigestAlgorithm.SHA512 = SHA512DigestAlgorithm()
DigestAlgorithm.SHA3_256 = SHA3DigestAlgorithm(256)

__all__ = [
    'DigestAlgorithms',
    'DigestAlgorithm',
    'MD5DigestAlgorithm',
    'SHA1DigestAlgorithm',
    'SHA256DigestAlgorithm',
    'SHA384DigestAlgorithm',
    'SHA512DigestAlgorithm'
]
