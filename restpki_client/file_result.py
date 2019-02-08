import base64


class FileResult:

    def __init__(self, client, file_base64):
        self._client = client
        self._file = file_base64

    @property
    def client(self):
        return self._client

    @client.setter
    def client(self, value):
        self._client = value

    @property
    def content(self):
        if self._file:
            return base64.b64decode(self._file)
        return None

    @property
    def content_base64(self):
        return self._file

    @content_base64.setter
    def content_base64(self, value):
        self._file = value

    def write_to_file(self, path):
        with open(path, 'wb') as f:
            f.write(base64.b64decode(self._file))


__all__ = ['FileResult']
