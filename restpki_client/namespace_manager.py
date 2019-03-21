class NamespaceManager(object):

    def __init__(self):
        self.__namespaces = []

    @property
    def namespaces(self):
        return self.__namespaces

    @namespaces.setter
    def namespaces(self, value):
        self.__namespaces = value

    def add_namespace(self, prefix, uri):
        if prefix is None or uri is None:
            raise Exception('Prefix and uri parameters cannot be None')
        self.__namespaces.append({'prefix': prefix, 'uri': uri})


__all__ = ['NamespaceManager']
