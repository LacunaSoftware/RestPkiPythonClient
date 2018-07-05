"""

Import all elements of the library to facilitate its importation from user.

"""
from .authentication import *
from .cades_signature_starter import *
from .cades_signature_finisher import *
from .detached_resource_xml_signature_starter import *
from .full_xml_signature_starter import *
from .namespace_manager import *
from .online_resource_xml_signature_starter import *
from .pades_signature_finisher import *
from .pades_signature_starter import *
from .pades_visual_positioning_presets import *
from .restpki_client import *
from .standard_security_contexts import *
from .standard_signature_policies import *
from .validation import *
from .xml_element_signature_starter import *
from .xml_id_resolution_table import *
from .xml_insertion_options import *
from .xml_signature_finisher import *
from .xml_signature_starter import *
from .version import *

__all__ = []
__all__ += authentication.__all__
__all__ += cades_signature_starter.__all__
__all__ += cades_signature_finisher.__all__
__all__ += detached_resource_xml_signature_starter.__all__
__all__ += full_xml_signature_starter.__all__
__all__ += namespace_manager.__all__
__all__ += online_resource_xml_signature_starter.__all__
__all__ += pades_signature_finisher.__all__
__all__ += pades_signature_starter.__all__
__all__ += pades_visual_positioning_presets.__all__
__all__ += restpki_client.__all__
__all__ += standard_security_contexts.__all__
__all__ += standard_signature_policies.__all__
__all__ += validation.__all__
__all__ += xml_element_signature_starter.__all__
__all__ += xml_id_resolution_table.__all__
__all__ += xml_insertion_options.__all__
__all__ += xml_signature_finisher.__all__
__all__ += xml_signature_starter.__all__
__all__ += version.__all__

