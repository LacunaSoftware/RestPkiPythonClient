class NamespaceManager:
    namespaces = None

    def __init__(self):
        self.namespaces = []

    def add_namespace(self, prefix, uri):
        ns = {'prefix': prefix, 'uri': uri}
        self.namespaces.append(ns)


__all__ = ['NamespaceManager']
