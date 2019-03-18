from .pdf_mark_image import PdfMarkImage
from .pdf_mark_element import PdfMarkElement
from .pdf_mark_element_type import PdfMarkElementType


class PdfMarkImageElement(PdfMarkElement):

    def __init__(self, relative_container=None, image=None):
        super(PdfMarkImageElement, self).__init__(PdfMarkElementType.IMAGE,
                                                  relative_container)
        self.__image = image

    @property
    def image(self):
        return self.__image

    @image.setter
    def image(self, value):
        self.__image = value

    # region FluentAPI

    def with_image(self, image):
        self.__image = image
        return self

    def with_image_content(self, image_content, mime_type):
        self.__image = PdfMarkImage(image_content, mime_type)
        return self

    # endregion

    def to_model(self):
        model = super(PdfMarkImageElement, self).to_model()
        model['image'] = self.__image.to_model() \
            if self.__image is not None else None
        return model


__all__ = ['PdfMarkImageElement']
