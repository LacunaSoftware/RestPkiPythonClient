from .pades_size import PadesSize
from .page_orientations import PageOrientations
from .paper_sizes import PaperSizes


class PadesPageOptimization(object):

    def __init__(self, paper_size=None, custom_paper_size=None):
        if custom_paper_size is not None:
            self.__paper_size = paper_size
        else:
            self.__paper_size = PaperSizes.CUSTOM
            self.__custom_paper_size = custom_paper_size
        self.__page_orientation = PageOrientations.AUTO

    # region "paper_size" accessors

    @property
    def paper_size(self):
        return self.__get_paper_size()

    def __get_paper_size(self):
        return self.__paper_size

    @paper_size.setter
    def paper_size(self, value):
        self.__set_paper_size(value)

    def __set_paper_size(self, value):
        if value is None:
            raise Exception('The provided "paper_size" is not valid')
        self.__paper_size = value

    # endregion

    # region "custom_paper_size" accessors

    @property
    def custom_paper_size(self):
        return self.__get_custom_paper_size()

    def __get_custom_paper_size(self):
        return self.__custom_paper_size

    @custom_paper_size.setter
    def custom_paper_size(self, value):
        self.__set_custom_paper_size(value)

    def __set_custom_paper_size(self, value):
        if value is None:
            raise Exception('The provided "custom_paper_size" is not valid')
        self.__custom_paper_size = value

    # endregion

    # region "page_orientation" accessors

    @property
    def page_orientation(self):
        return self.__get_page_orientation()

    def __get_page_orientation(self):
        return self.__page_orientation

    @page_orientation.setter
    def page_orientation(self, value):
        self.__set_page_orientation(value)

    def __set_page_orientation(self, value):
        if value is None:
            raise Exception('The provided "page_orientation" is not valid')
        self.__page_orientation = value

    # endregion

    def to_model(self):
        return {
            'paperSize': self.__paper_size,
            'customPaperSize': self.__custom_paper_size.to_model()
                               if self.__custom_paper_size is not None
                               else None,
            'pageOrientation': self.__page_orientation
        }

    @staticmethod
    def create_from_model(model):
        entity = PadesPageOptimization()
        entity.paper_size = model.get('paperSize', None)
        custom_paper_size = model.get('customPaperSize', None)
        if custom_paper_size is not None:
            entity.custom_paper_size = \
                PadesSize.create_from_model(custom_paper_size)
        page_orientation = model.get('pageOrientation', None)
        entity.page_orientation = page_orientation or PageOrientations.AUTO
        return entity


__all__ = ['PadesPageOptimization']
