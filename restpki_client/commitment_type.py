class CommitmentType:
    def __init__(self, data=None):
        self._oid = None
        self._name = None

        _oid = data.get('oid', None)
        if _oid is not None:
            self._oid = _oid

        _name = data.get('name', None)
        if _name is not None:
            self._name = _name

    @property
    def oid(self):
        return self._oid

    @oid.setter
    def oid(self, value):
        self._oid = value if value is not None else None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value if value is not None else None

__all__ = ['CommitmentType']