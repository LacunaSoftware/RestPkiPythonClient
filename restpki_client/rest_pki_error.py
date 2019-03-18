from .rest_base_error import RestBaseError


class RestPkiError(RestBaseError):

    def __init__(self, verb, url, error_code, detail):
        message = "REST PKI action %s %s error: %s" % (verb, url, error_code)
        if detail and len(detail) > 0:
            message += " (%s)" % detail
        RestBaseError.__init__(self, __name__, message, verb, url)

        self._error_code = error_code
        self._detail = detail

    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value

    @property
    def detail(self):
        return self._detail

    @detail.setter
    def detail(self, value):
        self._detail = value


__all__ = ['RestPkiError']
