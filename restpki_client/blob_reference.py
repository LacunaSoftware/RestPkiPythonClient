class BlobReference(object):

    def __init__(self, token):
        self.__token = token

    # region "token" accessors

    @property
    def token(self):
        return self.__get_token()

    def __get_token(self):
        return self.__token

    @token.setter
    def token(self, value):
        self.__set_token(value)

    def __set_token(self, value):
        if value is None:
            raise Exception('The provided "token" is not valid')
        self.__token = value

    # endregion


__all__ = ['BlobReference']
