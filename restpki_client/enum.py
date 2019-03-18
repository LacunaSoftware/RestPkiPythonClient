class Enum(object):

    def __init__(self, value):
        self.__value = value

    # region "value" accessors

    @property
    def value(self):
        """

        The definition of property "value", which contains the value of the
        enumeration.

        """
        return self.__get_value()

    def __get_value(self):
        return self.__value

    @value.setter
    def value(self, val):
        self.__set_value(val)

    def __set_value(self, val):
        if val is None:
            raise Exception('The provided "value" is not valid')
        self.__value = val

    # endregion


__all__ = ['Enum']
