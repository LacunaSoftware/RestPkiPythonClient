import base64

from six import BytesIO

from .utils import _base64_decode
from .utils import _base64_encode_string
from .utils import _copy_stream
from .utils import _get_raw_stream


class FileResult(object):

    def __init__(self, client, file_model):
        self.__client = client
        self.__file = file_model

    @property
    def client(self):
        return self.__client

    @client.setter
    def client(self, value):
        self.__client = value

    def open(self, buff_size=4096):
        content_base64 = self.__file.get('content')
        content_raw = _base64_decode(content_base64)
        if content_raw is not None:
            stream = _get_raw_stream(content_raw)
        else:
            stream = BytesIO()
            for chunk in self.__client.get_raw(self.__file.get('url'))\
                    .iter_content(buff_size):
                stream.write(chunk)
            stream.seek(0, 0)
        return stream

    def write_to(self, f_out, offset=0, from_where=0, buff_size=4096):
        content_base64 = self.__file.get('content')
        content_raw = _base64_decode(content_base64)
        if content_raw is not None:
            f_in = self.open()
            _copy_stream(f_in, f_out, offset, from_where, buff_size)
            f_in.close()
        else:
            f_out.seek(offset, from_where)
            for chunk in self.__client.get_raw(self.__file.get('url'))\
                    .iter_content(buff_size):
                f_out.write(chunk)

    def write_to_file(self, path, offset=0, from_where=0, buff_size=4096):
        content_base64 = self.__file.get('content')
        content_raw = _base64_decode(content_base64)
        with open(path, 'wb') as f_out:
            if content_raw is not None:
                f_in = self.open()
                _copy_stream(f_in, f_out, offset, from_where, buff_size)
                f_in.close()
            else:
                for chunk in self.__client.get_raw(self.__file.get('url'))\
                        .iter_content(buff_size):
                    f_out.write(chunk)

    # region "content" accessors

    @property
    def content(self):
        return self.__get_content()

    def __get_content(self):
        buffer = BytesIO()
        self.write_to(buffer)
        buffer.seek(0, 0)
        return buffer.read()

    @content.setter
    def content(self, value):
        self.__set_content(value)

    def __set_content(self, value):
        if value is None:
            raise Exception('The provided "content" is not valid')
        if self.__file is None:
            self.__file = {
                'content': None,
                'mimeType': None,
                'blobToken': None,
                'url': None
            }
        self.__file['content'] = base64.b64encode(value)

    # endregion

    # region "content_base64" accessors

    @property
    def content_base64(self):
        return self.__get_content_base64()

    def __get_content_base64(self):
        buffer = BytesIO()
        self.write_to(buffer)
        buffer.seek(0, 0)
        return _base64_encode_string(buffer.read())

    @content_base64.setter
    def content_base64(self, value):
        self.__set_content_base64(value)

    def __set_content_base64(self, value):
        if value is None:
            raise Exception('The provided "content_base64" is not valid')
        if self.__file is None:
            self.__file = {
                'content': None,
                'mimeType': None,
                'blobToken': None,
                'url': None
            }
        self.__file['content'] = value

    # endregion


__all__ = ['FileResult']
