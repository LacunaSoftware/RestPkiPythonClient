import base64

from six import BytesIO


def _base64_encode_string(value):
    """

    This method is just a wrapper that handle the incompatibility between the
    standard_b64encode() method on versions 2 and 3 of Python. On Python 2, a
    string is returned, but on Python 3, a bytes-class instance is returned.

    """
    value_base64 = base64.standard_b64encode(value)
    if type(value_base64) is str:
        return value_base64
    elif type(value_base64) is bytes or type(value_base64) is bytearray:
        return value_base64.decode('ascii')
    return None


def _base64_url_safe_encode_string(value):
    """

    This method is just a wrapper that handle the incompatibility between the
    standard_b64encode() method on versions 2 and 3 of Python. On Python 2, a
    string is returned, but on Python 3, a bytes-class instance is returned.

    """
    value_base64 = base64.urlsafe_b64encode(value)
    if type(value_base64) is str:
        return value_base64
    elif type(value_base64) is bytes or type(value_base64) is bytearray:
        return value_base64.decode('ascii')
    return None


def _base64_decode(base64_value):
    if base64_value is None:
        return None
    return base64.standard_b64decode(base64_value)


def _copy_stream(src, dst, offset=0, from_where=0, buff_size=4096):
    # Position source ont he required position.
    dst.seek(offset, from_where)
    while True:
        buff = src.read(buff_size)
        if not buff:
            break
        dst.write(buff)


def _get_raw_stream(content):
    stream = BytesIO(content)
    stream.seek(0, 0)
    return stream
