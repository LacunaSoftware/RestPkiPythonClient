class PdfMarkElement(object):

    def __init__(self, element_type, relative_container=None):
        self.__element_type = element_type
        self.__relative_container = relative_container
        self.__rotation = 0
        self.__opacity = 100

    @property
    def element_type(self):
        return self.__element_type

    @element_type.setter
    def element_type(self, value):
        self.__element_type = value

    @property
    def relative_container(self):
        return self.__relative_container

    @relative_container.setter
    def relative_container(self, value):
        self.__relative_container = value

    @property
    def rotation(self):
        return self.__rotation

    @rotation.setter
    def rotation(self, value):
        self.__rotation = value

    @property
    def opacity(self):
        return self.__opacity

    @opacity.setter
    def opacity(self, value):
        self.__opacity = value

    # region FluentAPI

    def on_container(self, relative_container):
        self.__relative_container = relative_container
        return self

    def with_rotation(self, rotation):
        self.__rotation = rotation
        return self

    def rotate_90_clockwise(self):
        self.__rotation = 270
        return self

    def rotate_90_counter_clockwise(self):
        self.__rotation = 90
        return self

    def rotate_180(self):
        self.__rotation = 180
        return self

    def with_opacity(self, opacity):
        self.__opacity = opacity
        return self

    # endregion

    def to_model(self):
        return {
            'elementType': self.__element_type,
            'relativeContainer': self.__relative_container.to_model() if
            self.__relative_container is not None else None,
            'rotation': self.__rotation,
            'opacity': self.__opacity
        }


__all__ = ['PdfMarkElement']
