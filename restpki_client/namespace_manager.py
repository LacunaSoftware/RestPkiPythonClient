class NamespaceManager:
    _namespaces = []

    def __init__(self):
        pass

    def add_namespace(self, prefix, uri):
        if not prefix or not uri:
            raise Exception('Prefix and uri parameters can not be null')

        ns = {'prefix': prefix, 'uri': uri}
        self._namespaces.append(ns)

    @property
    def namespaces(self):
        return self._namespaces


__all__ = ['NamespaceManager']
