class RestBaseError(Exception):
    _name = None
    _verb = None
    _url = None

    def __init__(self, name, message, verb, url):
        Exception.__init__(self, message)
        self._name = name
        self._verb = verb
        self._url = url

    @property
    def name(self):
        return self._name

    @property
    def verb(self):
        return self._verb

    @property
    def url(self):
        return self._url


class RestError(RestBaseError):
    _status_code = None
    _error_message = None

    def __init__(self, verb, url, status_code, error_message=None):
        message = "REST action %s %s returned HTTP error %s" % \
                  (verb, url, status_code)
        if error_message and len(error_message) > 0:
            message += ": %s" % error_message
        RestBaseError.__init__(self, __name__, message, verb, url)

        self._status_code = status_code
        self._error_message = error_message

    @property
    def status_code(self):
        return self._status_code

    @property
    def error_message(self):
        return self._error_message


class RestPkiError(RestBaseError):
    _error_code = None
    _detail = None

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

    @property
    def detail(self):
        return self._detail


class RestUnreachableError(RestBaseError):

    def __init__(self, verb, url):
        RestBaseError.__init__(self,
                               __name__,
                               "REST action %s %s unreachable" % (verb, url),
                               verb,
                               url)


class ValidationError(RestBaseError):
    _validation_results = None

    def __init__(self, verb, url, validation_results):
        RestBaseError.__init__(self,
                               __name__,
                               str(validation_results),
                               verb,
                               url)

    @property
    def validation_results(self):
        return self._validation_results


__all__ = [
    'RestBaseError',
    'RestError',
    'RestPkiError',
    'RestUnreachableError',
    'ValidationError'
]
