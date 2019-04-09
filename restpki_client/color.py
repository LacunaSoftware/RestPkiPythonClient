class Color(object):
    TRANSPARENT = None
    WHITE = None
    LIGHT_GRAY = None
    GRAY = None
    DARK_GRAY = None
    BLACK = None
    RED = None
    PINK = None
    ORANGE = None
    YELLOW = None
    GREEN = None
    MAGENTA = None
    CYAN = None
    BLUE = None

    def __init__(self, red, green, blue, alpha=100):
        self.__red = red
        self.__green = green
        self.__blue = blue
        self.__alpha = alpha

    @staticmethod
    def from_rgb(red, green, blue):
        return Color(red, green, blue)

    @staticmethod
    def from_rgba(red, green, blue, alpha):
        return Color(red, green, blue, alpha)

    @property
    def red(self):
        return self.__red

    @red.setter
    def red(self, value):
        self.__red = value

    @property
    def green(self):
        return self.__green

    @green.setter
    def green(self, value):
        self.__green = value

    @property
    def blue(self):
        return self.__blue

    @blue.setter
    def blue(self, value):
        self.__blue = value

    @property
    def alpha(self):
        return self.__alpha

    @alpha.setter
    def alpha(self, value):
        self.__alpha = value

    def to_model(self):
        return {
            'alpha': self.__alpha / 2.55,
            'red': self.__red,
            'green': self.__green,
            'blue': self.__blue
        }


Color.TRANSPARENT = Color(255, 255, 255, 0)
Color.WHITE = Color(255, 255, 255)
Color.LIGHT_GRAY = Color(192, 192, 192)
Color.GRAY = Color(128, 128, 128)
Color.DARK_GRAY = Color(64, 64, 64)
Color.BLACK = Color(0, 0, 0)
Color.RED = Color(255, 0, 0)
Color.PINK = Color(255, 175, 175)
Color.ORANGE = Color(255, 200, 0)
Color.YELLOW = Color(255, 255, 0)
Color.GREEN = Color(0, 255, 0)
Color.MAGENTA = Color(255, 0, 255)
Color.CYAN = Color(0, 255, 255)
Color.BLUE = Color(0, 0, 255)

__all__ = ['Color']
