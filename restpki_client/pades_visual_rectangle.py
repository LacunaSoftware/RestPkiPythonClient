class PadesVisualRectangle(object):

    def __init__(self):
        self.__left = None
        self.__top = None
        self.__right = None
        self.__bottom = None
        self.__width = None
        self.__height = None

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, value):
        self.__left = value

    @property
    def top(self):
        return self.__top

    @top.setter
    def top(self, value):
        self.__top = value

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, value):
        self.__right = value

    @property
    def bottom(self):
        return self.__bottom

    @bottom.setter
    def bottom(self, value):
        self.__bottom = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    def to_model(self):
        return {
            'left': self.__left,
            'top': self.__top,
            'right': self.__right,
            'bottom': self.__bottom,
            'width': self.__width,
            'height': self.__height
        }


__all__ = ['PadesVisualRectangle']
