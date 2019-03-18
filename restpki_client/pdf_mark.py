from .pdf_mark_page_options import PdfMarkPageOptions
from .color import Color


class PdfMark(object):

    def __init__(self):
        self.__container = None
        self.__border_width = 0.0
        self.__border_color = Color.BLACK
        self.__background_color = Color.TRANSPARENT
        self.__elements = []
        self.__page_option = PdfMarkPageOptions.ALL_PAGES
        self.__page_option_number = None

    @property
    def container(self):
        return self.__container

    @container.setter
    def container(self, value):
        self.__container = value

    @property
    def border_width(self):
        return self.__border_width

    @border_width.setter
    def border_width(self, value):
        self.__border_width = value

    @property
    def border_color(self):
        return self.__border_color

    @border_color.setter
    def border_color(self, value):
        self.__border_color = value

    @property
    def background_color(self):
        return self.__background_color

    @background_color.setter
    def background_color(self, value):
        self.__background_color = value

    @property
    def elements(self):
        return self.__elements

    @elements.setter
    def elements(self, value):
        self.__elements = value

    @property
    def page_option(self):
        return self.__page_option

    @page_option.setter
    def page_option(self, value):
        self.__page_option = value

    @property
    def page_option_number(self):
        return self.__page_option_number

    @page_option_number.setter
    def page_option_number(self, value):
        self.__page_option_number = value

    # region Fluent API

    def on_container(self, container):
        self.__container = container
        return self

    def with_border_width(self, border_width):
        self.__border_width = border_width
        return self

    def on_all_pages(self):
        self.__page_option = PdfMarkPageOptions.ALL_PAGES
        return self

    def on_new_page(self):
        self.__page_option = PdfMarkPageOptions.NEW_PAGE
        return self

    def on_single_page(self, page_number):
        self.__page_option = PdfMarkPageOptions.SINGLE_PAGE
        self.__page_option_number = page_number
        return self

    def on_single_page_from_end(self, page_number):
        self.__page_option = PdfMarkPageOptions.SINGLE_PAGE_FROM_END
        self.__page_option_number = page_number
        return self

    def add_element(self, element):
        self.__elements.append(element)
        return self

    def with_border_color(self, border_color):
        self.__border_color = border_color
        return self

    def with_background_color(self, background_color):
        self.__background_color = background_color
        return self

    # endregion

    def to_model(self):
        return {
            'container': self.__container.to_model()
            if self.__container is not None else None,
            'backgroundColor': self.__background_color.to_model()
            if self.__background_color is not None else None,
            'borderColor': self.__border_color.to_model()
            if self.__border_color is not None else None,
            'borderWidth': self.__border_width,
            'pageOption': self.__page_option,
            'pageOptionNumber': self.__page_option_number,
            'elements': [e.to_model() for e in self.__elements]
        }


__all__ = ['PdfMark']
