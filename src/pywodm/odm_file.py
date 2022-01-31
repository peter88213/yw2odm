"""Provide a class for ODM master document export.

Copyright (c) 2022 Peter Triesberger
For further information see https://github.com/peter88213/yw2odm
Published under the MIT License (https://opensource.org/licenses/mit-license.php)
"""
from pywriter.odt.odt_file import OdtFile


class OdmFile(OdtFile):
    """OpenDocument master document representation."""

    EXTENSION = '.odm'
    # overwrites Novel.EXTENSION

    _MIMETYPE = 'application/vnd.oasis.opendocument.text-master'

    _MANIFEST_XML = OdtFile._MANIFEST_XML.replace(
        'opendocument.text', 'opendocument.text-master')

    fileHeader = f'''{OdtFile.CONTENT_XML_HEADER}<text:p text:style-name="Title">$Title</text:p>
<text:p text:style-name="Subtitle">$AuthorName</text:p>
'''
