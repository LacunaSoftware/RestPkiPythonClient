from .utils import _base64_encode_string


class ResourceContentOrReference(object):

    def __init__(self):
        self.__url = None
        self.__mime_type = None
        self.__content = None

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, value):
        self.__url = value

    @property
    def mime_type(self):
        return self.__mime_type

    @mime_type.setter
    def mime_type(self, value):
        self.__mime_type = value

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, value):
        self.__content = value

    def to_model(self):
        return {
            'content': _base64_encode_string(self.__content)
            if self.__content is not None else None,
            'url': self.__url,
            'mimeType': self.__mime_type
        }


__all__ = ['ResourceContentOrReference']
