from .rest_base_error import RestBaseError


class RestUnreachableError(RestBaseError):

    def __init__(self, verb, url):
        RestBaseError.__init__(self,
                               __name__,
                               "REST action %s %s unreachable" % (verb, url),
                               verb,
                               url)


__all__ = ['RestUnreachableError']
