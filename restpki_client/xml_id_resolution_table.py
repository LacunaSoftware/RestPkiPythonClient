class XmlIdResolutionTable:
    _include_xml_id_attribute = None
    _element_id_attributes = None
    _global_id_attributes = None

    def __init__(self, include_xml_id_attribute=True):
        self._include_xml_id_attribute = include_xml_id_attribute
        self._element_id_attributes = []
        self._global_id_attributes = []

    def add_global_id_attribute(self,
                                id_attribute_local_name,
                                id_attribute_namespace=None):
        self._global_id_attributes.append({
            'localName': id_attribute_local_name,
            'namespace': id_attribute_namespace
        })

    def set_element_id_attribute(self,
                                 element_local_name,
                                 element_namespace,
                                 id_attribute_local_name,
                                 id_attribute_namespace=None):
        self._element_id_attributes.append({
            'element': {
                'localName': element_local_name,
                'namespace': element_namespace
            },
            'attribute': {
                'localName': id_attribute_local_name,
                'namespace': id_attribute_namespace
            }
        })

    def to_model(self):
        return {
            'includeXmlIdAttribute': self._include_xml_id_attribute,
            'elementIdAttributes': self._element_id_attributes,
            'globalIdAttributes': self._global_id_attributes
        }


__all__ = ['XmlIdResolutionTable']
