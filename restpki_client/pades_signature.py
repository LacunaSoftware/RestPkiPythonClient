from .pades_signer_info import PadesSignerInfo


class PadesSignature(object):

    def __init__(self, model):
        self.__signers = []
        signers = model.get('signers', None)
        if signers is not None:
            self.__signers = [PadesSignerInfo(s) for s in signers]

    @property
    def signers(self):
        return self.__signers

    @signers.setter
    def signers(self, value):
        self.__signers = value


__all__ = ['PadesSignature']
