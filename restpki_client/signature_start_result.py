from .digest_algorithm import DigestAlgorithm
from .pk_certificate import PKCertificate


class SignatureStartResult(object):

    def __init__(self, response):
        certificate = response.get('certificate', None)
        if certificate is not None:
            self.__certificate = PKCertificate(certificate)
        self.__token = response.get('token', None)
        self.__to_sign_data = response.get('toSignData', None)
        self.__to_sign_hash = response.get('toSignHash', None)
        self.__digest_algorithm_oid = response.get('digestAlgorithmOid', None)
        self.__digest_algorithm = None

    # region "certificate" accessors

    @property
    def certificate(self):
        return self.__get_certificate()

    def __get_certificate(self):
        return self.__certificate

    @certificate.setter
    def certificate(self, value):
        self.__set_certificate(value)

    def __set_certificate(self, value):
        if value is None:
            raise Exception('The provided "certificate" is not valid')
        self.__certificate = value

    # endregion

    # region "token" accessors

    @property
    def token(self):
        return self.__get_token()

    def __get_token(self):
        return self.__token

    @token.setter
    def token(self, value):
        self.__set_token(value)

    def __set_token(self, value):
        if value is None:
            raise Exception('The provided "token" is not valid')
        self.__token = value

    # endregion

    # region "to_sign_data" accessors

    @property
    def to_sign_data(self):
        return self.__get_to_sign_data()

    def __get_to_sign_data(self):
        return self.__to_sign_data

    @to_sign_data.setter
    def to_sign_data(self, value):
        self.__set_to_sign_data(value)

    def __set_to_sign_data(self, value):
        if value is None:
            raise Exception('The provided "to_sign_data" is not valid')
        self.__to_sign_data = value

    # endregion

    # region "to_sign_hash" accessors

    @property
    def to_sign_hash(self):
        return self.__get_to_sign_hash()

    def __get_to_sign_hash(self):
        return self.__to_sign_hash

    @to_sign_hash.setter
    def to_sign_hash(self, value):
        self.__set_to_sign_hash(value)

    def __set_to_sign_hash(self, value):
        if value is None:
            raise Exception('The provided "to_sign_hash" is not valid')
        self.__to_sign_hash = value

    # endregion

    # region "digest_algorithm_oid" accessors

    @property
    def digest_algorithm_oid(self):
        return self.__get_digest_algorithm_oid()

    def __get_digest_algorithm_oid(self):
        return self.__digest_algorithm_oid

    @digest_algorithm_oid.setter
    def digest_algorithm_oid(self, value):
        self.__set_digest_algorithm_oid(value)

    def __set_digest_algorithm_oid(self, value):
        if value is None:
            raise Exception(
                'The provided "digest_algorithm_oid" is not valid')
        self.__digest_algorithm_oid = value

    # endregion

    @property
    def digest_algorithm(self):
        if self.__digest_algorithm is None:
            if self.__digest_algorithm_oid is None:
                return None
            self.__digest_algorithm = DigestAlgorithm\
                .get_instance_by_oid(self.__digest_algorithm_oid)
        return self.__digest_algorithm


__all__ = ['SignatureStartResult']
