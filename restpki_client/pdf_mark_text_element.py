from .pdf_text_section import PdfTextSection
from .pades_horizontal_align import PadesHorizontalAlign
from .pdf_mark_element_type import PdfMarkElementType
from .pdf_mark_element import PdfMarkElement


class PdfMarkTextElement(PdfMarkElement):

    def __init__(self, relative_container=None, text_sections=None):
        super(PdfMarkTextElement, self).__init__(PdfMarkElementType.TEXT,
                                                 relative_container)
        self.__text_sections = text_sections \
            if text_sections is not None else []
        self.__align = PadesHorizontalAlign.LEFT

    # region FluentAPI

    def align_text_left(self):
        self.__align = PadesHorizontalAlign.LEFT
        return self

    def align_text_right(self):
        self.__align = PadesHorizontalAlign.RIGHT
        return self

    def align_text_center(self):
        self.__align = PadesHorizontalAlign.CENTER
        return self

    def add_section_from_text(self, section):
        self.__text_sections.append(PdfTextSection(section))
        return self

    def add_section(self, section):
        self.__text_sections.append(section)
        return self

    # endregion

    @property
    def text_sections(self):
        return self.__text_sections

    @text_sections.setter
    def text_sections(self, value):
        self.__text_sections = value

    @property
    def align(self):
        return self.__align

    @align.setter
    def align(self, value):
        self.__align = value

    def to_model(self):
        model = super(PdfMarkTextElement, self).to_model()
        model['align'] = self.__align
        model['textSections'] = [s.to_model() for s in self.__text_sections]
        return model


__all__ = ['PdfMarkTextElement']
