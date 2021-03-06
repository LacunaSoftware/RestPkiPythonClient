from six import BytesIO
from six import text_type

from .utils import _base64_decode
from .utils import _base64_encode_string


class FileReference(object):

    def __init__(self):
        self.__path = None
        self.__blob_token = None
        self.__content_base64 = None
        self.__content_raw = None
        self.__file_desc = None

    @staticmethod
    def _get_file_size(file_desc):
        file_desc.seek(0, 2)
        size = file_desc.tell()
        file_desc.seek(0, 0)
        return size

    @staticmethod
    def from_file(file_desc):
        reference = FileReference()
        reference.file_desc = file_desc
        return reference

    @staticmethod
    def from_path(path):
        reference = FileReference()
        reference.path = path
        return reference

    @staticmethod
    def from_content_raw(content_raw):
        reference = FileReference()
        reference.content_raw = content_raw
        return reference

    @staticmethod
    def from_content_base64(content_base64):
        reference = FileReference()
        reference.content_base64 = content_base64
        return reference

    @staticmethod
    def from_blob(blob):
        reference = FileReference()
        reference.blob_token = blob.token
        return reference

    @staticmethod
    def from_result(result):
        if result.file.blob_token is not None:
            reference = FileReference()
            reference.blob_token = result.file.blob_token
            return reference
        return FileReference.from_content_raw(result.file.content)

    # region "path" accessors

    @property
    def path(self):
        return self.__get_path()

    def __get_path(self):
        return self.__path

    @path.setter
    def path(self, value):
        self.__set_path(value)

    def __set_path(self, value):
        if value is None:
            raise Exception('The provided "path" is not valid')
        self.__path = value

    # endregion

    # region "content_base64" accessors

    @property
    def content_base64(self):
        return self.__get_content_base64()

    def __get_content_base64(self):
        if self.__content_base64 is not None:
            return self.__content_base64
        if self.__content_raw is not None:
            return _base64_encode_string(self.__content_raw)
        content_raw = self.__open_or_use_existing_stream(lambda s: s.read())
        return _base64_encode_string(content_raw)

    @content_base64.setter
    def content_base64(self, value):
        self.__set_content_base64(value)

    def __set_content_base64(self, value):
        if value is None:
            raise Exception('The provided "content_base64" is not valid')
        self.__content_base64 = value

    # endregion

    # region "content_raw" accessors

    @property
    def content_raw(self):
        return self.__get_content_raw()

    def __get_content_raw(self):
        if self.__content_raw is not None:
            return self.__content_raw
        if self.__content_base64 is not None:
            return _base64_encode_string(self.__content_base64)
        return self.__open_or_use_existing_stream(lambda s: s.read())

    @content_raw.setter
    def content_raw(self, value):
        self.__set_content_raw(value)

    def __set_content_raw(self, value):
        if value is None:
            raise Exception('The provided "content_raw" is not valid')
        self.__content_raw = value

    # endregion

    # region "blob_token" accessors

    @property
    def blob_token(self):
        return self.__get_blob_token()

    def __get_blob_token(self):
        return self.__blob_token

    @blob_token.setter
    def blob_token(self, value):
        self.__set_blob_token(value)

    def __set_blob_token(self, value):
        if value is None:
            raise Exception('The provided "blob_token" is not valid')
        self.__blob_token = value

    # endregion

    # region "file_desc" accessors

    @property
    def file_desc(self):
        return self.__get_file_desc()

    def __get_file_desc(self):
        return self.__file_desc

    @file_desc.setter
    def file_desc(self, value):
        self.__set_file_desc(value)

    def __set_file_desc(self, value):
        if value is None:
            raise Exception('The provided "file_desc" is not valid')
        self.__file_desc = value

    # endregion

    def upload_or_reference(self, client):
        file = {
            'mimeType': None,
            'content': None,
            'blobToken': None,
            'url': None
        }
        if self.__blob_token is not None:
            file['blobToken'] = self.__blob_token
        elif self.__content_base64 is not None and \
                len(_base64_decode(self.__content_base64)) < \
                client.multipart_upload_threshold:
            file['content'] = self.__content_base64
        elif self.__content_raw is not None and \
                len(self.__content_raw) < client.multipart_upload_threshold:
            file['content'] = _base64_encode_string(self.__content_raw)
        else:
            stream = self.__open_or_use_existing_stream()
            file_size = FileReference._get_file_size(stream)
            if file_size < client.multipart_upload_threshold:
                file['content'] = _base64_encode_string(stream.read())
            else:
                upload_result = client.upload_or_read(stream)
                if type(upload_result) == text_type:
                    self.__blob_token = upload_result
                    file['blobToken'] = self.__blob_token
                else:
                    file['content'] = _base64_encode_string(upload_result)
        return file

    def compute_data_hashes(self, algorithms):
        data_hashes = []
        stream = self.__open_or_use_existing_stream()
        for digest_alg in algorithms:
            stream.seek(0, 0)
            hash_func = digest_alg.get_hash_func()
            hash_func.update(stream.read())
            digest = hash_func.digest()
            data_hashes.append({
                'algorithm': digest_alg.api_model.value,
                'value': _base64_encode_string(digest),
                'hexValue': None
            })

        return data_hashes

    def __open_or_use_existing_stream(self, action=None):
        if self.__file_desc is not None:
            stream = self.__file_desc
        elif self.__path is not None:
            file_desc = open(self.__path, 'rb')
            stream = file_desc
        elif self.__content_base64 is not None:
            content_raw = _base64_decode(self.__content_base64)
            stream = BytesIO()
            stream.write(content_raw)
            stream.seek(0, 0)
        elif self.__content_raw is not None:
            stream = BytesIO()
            stream.write(self.__content_raw)
            stream.seek(0, 0)
        else:
            raise Exception('Invalid operation.')

        if action is not None:
            return action(stream)
        return stream


__all__ = ['FileReference']
