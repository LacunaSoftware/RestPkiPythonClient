from .color import Color
from .pdf_text_style import PdfTextStyle


class PdfTextSection(object):

    def __init__(self, text=None, color=None, font_size=None):
        self.__style = PdfTextStyle.NORMAL
        self.__text = text
        self.__font_size = font_size
        self.__color = color if color is not None else Color.BLACK

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, value):
        self.__text = value

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value

    @property
    def font_size(self):
        return self.__font_size

    @font_size.setter
    def font_size(self, value):
        self.__font_size = value

    @property
    def style(self):
        return self.__style

    @style.setter
    def style(self, value):
        self.__style = value

    # region FluentAPI

    def with_font_size(self, font_size):
        self.__font_size = font_size
        return self

    def with_text(self, text):
        self.__text = text
        return self

    def bold(self):
        self.__style = PdfTextStyle.BOLD
        return self

    def italic(self):
        self.__style = PdfTextStyle.ITALIC
        return self

    def with_color(self, color):
        self.__color = color
        return self

    # endregion

    def to_model(self):
        return {
            'style': self.__style,
            'text': self.__text,
            'color': self.__color.to_model() if
            self.__color is not None else None,
            'fontSize': self.__font_size
        }


__all__ = ['PdfTextSection']
