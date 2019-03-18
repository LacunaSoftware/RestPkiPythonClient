from .rest_base_error import RestBaseError


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


__all__ = ['RestError']
