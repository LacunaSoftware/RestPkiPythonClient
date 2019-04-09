from .resource_content_or_reference import ResourceContentOrReference


class PdfMarkImage(object):

    def __init__(self, image_content=None, mime_type=None):
        self.__resource = ResourceContentOrReference()
        self.__resource.mime_type = mime_type
        self.__resource.content = image_content

    @property
    def resource(self):
        return self.__resource

    @resource.setter
    def resource(self, value):
        self.__resource = value

    def to_model(self):
        return {
            'resource': self.__resource.to_model()
            if self.__resource is not None else None
        }


__all__ = ['PdfMarkImage']
