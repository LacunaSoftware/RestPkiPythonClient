import base64


class FileResult:
    _client = None
    _file = None

    def __init__(self, client, file_):
        self._client = client
        self._file = file_

    @property
    def content(self):
        if self._file:
            return base64.b64decode(self._file)
        return None

    @property
    def content_base64(self):
        if self._file:
            return self._file
        return None

    def write_to_file(self, path):
        with open(path, 'wb') as f:
            f.write(base64.b64decode(self._file))


__all__ = ['FileResult']
