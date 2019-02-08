class RestBaseError(Exception):

    def __init__(self, name, message, verb, url):
        Exception.__init__(self, message)
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


class RestError(RestBaseError):

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

    @status_code.setter
    def status_code(self, value):
        self._status_code = value

    @property
    def error_message(self):
        return self._error_message

    @error_message.setter
    def error_message(self, value):
        self._error_message = value


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


class RestUnreachableError(RestBaseError):

    def __init__(self, verb, url):
        RestBaseError.__init__(self,
                               __name__,
                               "REST action %s %s unreachable" % (verb, url),
                               verb,
                               url)


class ValidationError(RestBaseError):

    def __init__(self, verb, url, validation_results):
        RestBaseError.__init__(self,
                               __name__,
                               str(validation_results),
                               verb,
                               url)
        self._validation_results = validation_results

    @property
    def validation_results(self):
        return self._validation_results

    @validation_results.setter
    def validation_results(self, value):
        self._validation_results = value


__all__ = [
    'RestBaseError',
    'RestError',
    'RestPkiError',
    'RestUnreachableError',
    'ValidationError'
]
