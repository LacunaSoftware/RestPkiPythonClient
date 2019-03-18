from .cades_signature import CadesSignerInfo


class PadesSignerInfo(CadesSignerInfo):

    def __init__(self, model):
        super(PadesSignerInfo, self).__init__(model)
        self.__is_document_timestamp = model.get('isDocumentTimestamp', None)
        self.__signature_field_name = model.get('signatureFieldName', None)

    @property
    def is_document_timestamp(self):
        return self.__is_document_timestamp

    @is_document_timestamp.setter
    def is_document_timestamp(self, value):
        self.__is_document_timestamp = value

    @property
    def signature_file_name(self):
        return self.__signature_field_name

    @signature_file_name.setter
    def signature_file_name(self, value):
        self.__signature_field_name = value


__all__ = ['PadesSignerInfo']
