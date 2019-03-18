class NamespaceManager(object):

    def __init__(self):
        self._namespaces = []

    @property
    def namespaces(self):
        return self._namespaces

    @namespaces.setter
    def namespaces(self, value):
        self._namespaces = value

    def add_namespace(self, prefix, uri):
        if not prefix or not uri:
            raise Exception('Prefix and uri parameters can not be null')

        ns = {'prefix': prefix, 'uri': uri}
        self._namespaces.append(ns)


__all__ = ['NamespaceManager']
