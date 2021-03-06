import binascii

from .digest_algorithm import DigestAlgorithm
from .utils import _base64_decode


class DigestAlgorithmAndValue(object):

    def __init__(self, model):

        self.__algorithm = None
        algorithm = model.get('algorithm', None)
        if algorithm is not None:
            self.__algorithm = \
                DigestAlgorithm.get_instance_by_api_model(str(algorithm))

        self.__value = None
        value = model.get('value', None)
        if value is not None:
            self.__value = _base64_decode(value)

    @property
    def algorithm(self):
        return self.__algorithm

    @algorithm.setter
    def algorithm(self, value):
        self.__algorithm = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, v):
        self.__value = v

    @property
    def hex_value(self):
        return binascii.hexlify(self.__value)

    @hex_value.setter
    def hex_value(self, value):
        self.__value = binascii.unhexlify(value)

    def to_model(self):
        return {
            'algorithm': self.__algorithm.api_model,
            'value': self.__value
        }


__all__ = ['DigestAlgorithmAndValue']
