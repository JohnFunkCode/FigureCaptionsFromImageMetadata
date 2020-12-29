"""
object to hold the metadata about the image files
"""
import pyexiv2


class ImageFile():
    """
    Provides a class to represent an image file and the metadata that we care about
    """

    def __init__(self, file):
        self._file = file
        self._title = ''
        self._caption = ''
        self.read_metadata()

    def __repr__(self):
        return f'{self._file},{self._title},{self._caption}'

    def __str__(self):
        return f'\033[37;1m{self._file}\n\33[0m\033[34m{self._title}\n\033[94m{self._caption}\33[0m'

    def read_metadata(self):
        """
        method to read the metadata from the image file
        :return:
        """
        filename = self._file.as_posix()
        metadata = pyexiv2.ImageMetadata(filename)
        metadata.read()
        try:
            tag = 'Xmp.dc.title'
            dictionary = metadata[tag].value
            value = dictionary['x-default']
            # print(f'  \033[34;1m{tag}\33[0m:\033[31m{type(value)}\33[0m: \033[32m{value}\33[0m')
            self._title = value
        except Exception as ex:
            pass
            # print(f'{filename}:{ex}')

        try:
            tag = 'Xmp.dc.description'
            dictionary = metadata[tag].value
            value = dictionary['x-default']
            self._caption = value
        except Exception as ex:
            pass
            # print(f'{filename}:{ex}')

    def has_title(self):
        """
        does the imagefile have a title?
        :return:
        """
        return '' != self._title

    def has_caption(self):
        """
        does the imagefile have a caption
        :return:
        """
        return '' != self._title
