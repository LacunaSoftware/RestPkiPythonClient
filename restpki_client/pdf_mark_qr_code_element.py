from .pdf_mark_element_type import PdfMarkElementType
from .pdf_mark_element import PdfMarkElement


class PdfMarkQRCodeElement(PdfMarkElement):

    def __init__(self, relative_container=None, qr_code_data=None):
        super(PdfMarkQRCodeElement, self).__init__(PdfMarkElementType.QR_CODE,
                                                   relative_container)

        self.__qr_code_data = qr_code_data
        self.__draw_quiet_zones = False

    @property
    def qr_code_data(self):
        return self.__qr_code_data

    @qr_code_data.setter
    def qr_code_data(self, value):
        self.__qr_code_data = value

    # region FluentAPI

    def with_qr_code_data(self, qr_code_data):
        self.__qr_code_data = qr_code_data
        return self

    def draw_quiet_zones(self):
        self.__draw_quiet_zones = True
        return self

    # endregion

    def to_model(self):
        model = super(PdfMarkQRCodeElement, self).to_model()
        model['qrCodeData'] = self.__qr_code_data
        model['qrCddeDrawQuietZones'] = self.__draw_quiet_zones
        return model


__all__ = ['PdfMarkQRCodeElement']
