from .digest_algorithm_and_value import DigestAlgorithmAndValue


class SignaturePolicyIdentifier(object):

    def __init__(self, model):
        self.__digest = None
        digest = model.get('digest', None)
        if digest is not None:
            self.__digest = DigestAlgorithmAndValue(digest)

        self.__oid = model.get('oid', None)
        self.__uri = model.get('uri', None)

    @property
    def digest(self):
        return self.__digest

    @digest.setter
    def digest(self, value):
        self.__digest = value

    @property
    def oid(self):
        return self.__oid

    @oid.setter
    def oid(self, value):
        self.__oid = value

    @property
    def uri(self):
        return self.__uri

    @uri.setter
    def uri(self, value):
        self.__uri = value


__all__ = ['SignaturePolicyIdentifier']
