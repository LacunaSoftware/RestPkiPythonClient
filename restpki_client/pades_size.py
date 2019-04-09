class PadesSize(object):

    def __init__(self, width=None, height=None):
        self.__width = width
        self.__height = height

    def to_model(self):
        return {
            'width': self.__width,
            'height': self.__height
        }

    @staticmethod
    def create_from_model(model):
        width = model.get('width', None)
        height = model.get('height', None)
        return PadesSize(width, height)


__all__ = ['PadesSize']
