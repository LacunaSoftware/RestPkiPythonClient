from .rest_base_error import RestBaseError


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


__all__ = ['ValidationError']
