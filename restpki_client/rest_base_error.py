class RestBaseError(Exception):

    def __init__(self, name, message, verb, url):
        super(RestBaseError, self).__init__(message)
        self._name = name
        self._verb = verb
        self._url = url

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def verb(self):
        return self._verb

    @verb.setter
    def verb(self, value):
        self._verb = value

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value


__all__ = ['RestBaseError']
