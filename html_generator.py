"""
Generate html output from the metadata
"""
import os
from image_file import ImageFile

class htmlGenerator():
    """
    class to handle html generation
    """

    def __init__(self):
        """
        open the file handler to output the data
        """
        print("__init__")
        #self._file = open('generatedHtml.html', 'w')

    def __enter__(self):
        print("__enter__")
        self._file = open('generatedHtml.html', 'w')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__")
        self._file.close()

    def generate_heading(self):
        """
        Generate the first part of the html
        :return:
        """
        heading = '<!doctype html>' \
                  '<html>' \
                  '<head>' \
                  '<meta charset="utf-8">' \
                  '<title>Untitled Document</title>' \
                  '<style>' \
                  '.flex-container' \
                  '{display:flex;' \
                  'flex-direction:row;' \
                  'justify-content:space-around;' \
                  'flex-wrap:wrap;' \
                  'align-items:center;' \
                  'align-content:space-between;}' \
                  'figure:hover' \
                  '{box-shadow: 2px 2px 2px red;}' \
                  'figure:hover>.caption' \
                  '{visibility:visible;' \
                  '---display:inline-block;}' \
                  'figure>.caption' \
                  '{visibility:hidden;' \
                  '---display:none;}' \
                  '</style>' \
                  '</head>' \
                  '<body>' \
                  '<div class ="flex-container container">'

        self._file.write(heading)

    def generate_footer(self):
        """
        Generate the closing part of the html
        :return:
        """
        footer= '</div>' \
                '</body>' \
                '</html>'
        self._file.write(footer)

    def generate_figure_caption(self, image_file):
        """
        Generate a div for the figure for the specified image_file
        :param image_file:
        :return:
        """
        #print( image_file )
        #print(image_file._file)
        #print(image_file._title)
        #print(image_file._caption)

        div='<div style="align-content: space-around; margin: 50px 50px 50px 25px; background-color: lightblue; width: 350px;">' \
            '<figure style = "padding: 25px 25px 25px 0px">'
        div += f'<a href = "{image_file._file}">'
        div += f'<img src = "{image_file._file}" alt="{image_file._title}" height="200px">'
        div += '</a>' \
            '<figcaption style="text-align: center;">'
        div +=f'{image_file._title}'
        div +='</figcaption>' \
            '<p class="caption">'
        div +=f'{image_file._caption}'
        div +='</p>' \
            '</figure>' \
            '</div>'
        print(div)
        self._file.write(div)
