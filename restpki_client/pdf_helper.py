from .pdf_container_definition import PdfContainerDefinition
from .pdf_text_section import PdfTextSection
from .pdf_mark_qr_code_element import PdfMarkQRCodeElement
from .pdf_mark_image_element import PdfMarkImageElement
from .pdf_mark_text_element import PdfMarkTextElement
from .pdf_mark import PdfMark


class PdfHelper(object):

    @staticmethod
    def container():
        return PdfContainerDefinition.Initial()

    @staticmethod
    def mark():
        return PdfMark()

    @staticmethod
    def text_element():
        return PdfMarkTextElement()

    @staticmethod
    def image_element():
        return PdfMarkImageElement()

    @staticmethod
    def qr_code_element():
        return PdfMarkQRCodeElement()

    @staticmethod
    def text_section(text=None):
        return PdfTextSection(text)


__all__ = ['PdfHelper']
