"""
This module contains the main code for CreateFigureCaptionsFromImageMetaData
"""
from pathlib import Path
import fire
from image_file import ImageFile


class CreateFigureCaptionsFromImageMetaData:
    """
    The main class that drives things
    """

    def __init__(self):
        self._image_files = list()

    def read_filenames_from_directory(self, base_direcory='.', recursive=False,
                                      extensions=['*.png', '*.psd', '*.jpg']):
        """

        :param base_direcory:
        :param recursive:
        :param extensions:
        :return:
        """
        print(f'base_direcory:{base_direcory}')
        path = Path(base_direcory)
        for ext in extensions:
            print('searching for:' + ext)
            if True == recursive:
                for file in path.rglob(ext):
                    i = ImageFile(file)
                    self._image_files.extend([i])
            else:
                for file in path.glob(ext):
                    self._image_files.extend([ImageFile(file)])
        print(len(self._image_files))

    def print_image_files(self):
        """
        print all the image files
        """
        for file in self._image_files:
            if file.has_title():
                print(file)

    def do_all(self, directory='.'):
        """
        drive all the code for testing purposes
        :param directory:
        :return:
        """
        self.read_filenames_from_directory(directory, recursive=False)
        self.print_image_files()


if __name__ == '__main__':
    c = CreateFigureCaptionsFromImageMetaData()
    c.do_all('/mnt/h/LightRoomCatalogExperiments/DadPhotos/Pictures/DadsPhotos')
    # fire.Fire(CreateFigureCaptionsFromImageMetaData)

    from html_generator import htmlGenerator
    with htmlGenerator() as h:
        h.generate_heading()
        for file in c._image_files:
            h.generate_figure_caption( file )
        h.generate_footer()
