# pylint: disable=too-few-public-methods
"""

This module contains the definition of the Apis enumeration.

"""
from .enum import Enum


class Apis(Enum):
    """

    This class represents the Apis enumeration. Each value represents a type
    of REST PKI operation. These operations is used to handle incompatibilities
    between REST PKI APIs.

    The available operation are:
     - START_CADES
     - COMPLETE_CADES
     - START_PADES
     - COMPLETE_PADES
     - MULTIPART_UPLOAD
     - ADD_PDF_MARKS

    """
    START_CADES = None
    COMPLETE_CADES = None
    START_PADES = None
    COMPLETE_PADES = None
    MULTIPART_UPLOAD = None
    ADD_PDF_MARKS = None


# The definition of the enumeration values.
#
# Note: This is made outside the class respecting the execution order, which
# makes the definition of the class be executed before the class itself.
Apis.START_CADES = Apis('StartCades')
Apis.COMPLETE_CADES = Apis('CompleteCades')
Apis.START_PADES = Apis('StartPades')
Apis.COMPLETE_PADES = Apis('CompletePades')
Apis.MULTIPART_UPLOAD = Apis('MultipartUpload')
Apis.ADD_PDF_MARKS = Apis('AddPdfMarks')


__all__ = ['Apis']
