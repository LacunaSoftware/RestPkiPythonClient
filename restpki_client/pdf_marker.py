from restpki_client.rest_pki_client import _get_api_version
from .apis import Apis
from .file_reference import FileReference
from .file_result import FileResult
from .pades_measurement_units import PadesMeasurementUnits


class PdfMarker(object):

    def __init__(self, client):
        self.__client = client
        self.__file = None
        self.__measurement_units = PadesMeasurementUnits.CENTIMETERS
        self.__page_optimization = None
        self.__abort_if_signed = None
        self.__marks = []
        self.__force_blob_result = None

    # region "client" accessors

    @property
    def client(self):
        return self.__get_client()

    def __get_client(self):
        return self.__client

    @client.setter
    def client(self, value):
        self.__set_client(value)

    def __set_client(self, value):
        if value is None:
            raise Exception('The provided "client" is not valid')
        self.__client = value

    # endregion

    # region "file" accessors

    @property
    def file(self):
        return self.__get_file()

    def __get_file(self):
        return self.__file.file_desc

    @file.setter
    def file(self, value):
        self.__set_file(value)

    def __set_file(self, value):
        if value is None:
            raise Exception('The provided "file" is not valid')
        self.__file = FileReference.from_file(value)

    # endregion

    # region "file_path" accessors

    @property
    def file_path(self):
        return self.__get_file_path()

    def __get_file_path(self):
        return self.__file.path

    @file_path.setter
    def file_path(self, value):
        self.__set_file_path(value)

    def __set_file_path(self, value):
        if value is None:
            raise Exception('The provided "file_path" is not valid')
        self.__file = FileReference.from_path(value)

    # endregion

    # region "file_content" accessors

    @property
    def file_content(self):
        return self.__get_file_content()

    def __get_file_content(self):
        return self.__file.content_raw

    @file_content.setter
    def file_content(self, value):
        self.__set_file_content(value)

    def __set_file_content(self, value):
        if value is None:
            raise Exception('The provided "file_content" is not valid')
        self.__file = FileReference.from_content_raw(value)

    # endregion

    # region "file_base64" accessors

    @property
    def file_base64(self):
        return self.__get_file_base64()

    def __get_file_base64(self):
        return self.__file.content_base64

    @file_base64.setter
    def file_base64(self, value):
        self.__set_file_base64(value)

    def __set_file_base64(self, value):
        if value is None:
            raise Exception('The provided "file_base64" is not valid')
        self.__file = FileReference.from_content_raw(value)

    # endregion

    # region "file_blob_token" accessors

    @property
    def file_blob_token(self):
        return self.__get_file_blob_token()

    def __get_file_blob_token(self):
        return self.__file.blob_token

    @file_blob_token.setter
    def file_blob_token(self, value):
        self.__set_file_blob_token(value)

    def __set_file_blob_token(self, value):
        if value is None:
            raise Exception('The provided "file_blob_token" is not valid')
        self.__file = FileReference.from_blob(value)

    # endregion

    # region "file_result" accessors

    @property
    def file_result(self):
        return self.__get_file_result()

    def __get_file_result(self):
        result = FileResult(self.__client, self.__file.content_base64)
        return result

    @file_result.setter
    def file_result(self, value):
        self.__set_file_result(value)

    def __set_file_result(self, value):
        if value is None:
            raise Exception('The provided "file_result" is not valid')
        self.__file = FileReference.from_result(value)

    # endregion

    # region "measurements_units" accessors

    @property
    def measurements_units(self):
        return self.__get_measurements_units()

    def __get_measurements_units(self):
        return self.__measurements_units

    @measurements_units.setter
    def measurements_units(self, value):
        self.__set_measurements_units(value)

    def __set_measurements_units(self, value):
        if value is None:
            raise Exception('The provided "measurements_units" is not valid')
        self.__measurements_units = value

    # endregion

    # region "page_optimization" accessors

    @property
    def page_optimization(self):
        return self.__get_page_optimization()

    def __get_page_optimization(self):
        return self.__page_optimization

    @page_optimization.setter
    def page_optimization(self, value):
        self.__set_page_optimization(value)

    def __set_page_optimization(self, value):
        if value is None:
            raise Exception('The provided "page_optimization" is not valid')
        self.__page_optimization = value

    # endregion

    # region "abort_if_signed" accessors

    @property
    def abort_if_signed(self):
        return self.__get_abort_if_signed()

    def __get_abort_if_signed(self):
        return self.__abort_if_signed

    @abort_if_signed.setter
    def abort_if_signed(self, value):
        self.__set_abort_if_signed(value)

    def __set_abort_if_signed(self, value):
        if value is None:
            raise Exception('The provided "abort_if_signed" is not valid')
        self.__abort_if_signed = value

    # endregion

    # region "marks" accessors

    @property
    def marks(self):
        return self.__get_marks()

    def __get_marks(self):
        return self.__marks

    @marks.setter
    def marks(self, value):
        self.__set_marks(value)

    def __set_marks(self, value):
        if value is None:
            raise Exception('The provided "marks" is not valid')
        self.__marks = value

    # endregion

    def append_mark(self, mark):
        if self.__marks is None:
            self.__marks = []
        self.__marks.append(mark)

    # region "force_blob_result" accessors

    @property
    def force_blob_result(self):
        return self.__get_force_blob_result()

    def __get_force_blob_result(self):
        return self.__force_blob_result

    @force_blob_result.setter
    def force_blob_result(self, value):
        self.__set_force_blob_result(value)

    def __set_force_blob_result(self, value):
        if value is None:
            raise Exception('The provided "force_blob_result" is not valid')
        self.__force_blob_result = value

    # endregion

    def apply(self):

        api_version = _get_api_version(self.__client, Apis.ADD_PDF_MARKS)
        if api_version < 1:
            raise Exception('The PdfMarker class can only be used with '
                            'REST PKI 1.13 or later. Please contact technical '
                            'support to update your REST PKI.')
        request = {
            'marks': [mark.to_model() for mark in self.__marks],
            'measurementUnits': self.__measurement_units,
            'forceBlobResult': self.__force_blob_result,
            'abortIfSigned': self.__abort_if_signed,
            'file': self.__file.upload_or_reference(self.__client),
            'pageOptimization': self.__page_optimization.to_model()
                                if self.__page_optimization is not None
                                else None
        }
        response = self.__client.post('Api/Pdf/AddMarks', request)
        return FileResult(self.__client, response.get('file', None))


__all__ = ['PdfMarker']
