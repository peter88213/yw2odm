"""Provide a class for ODM master document export with chapters as subdocuments.

Copyright (c) 2022 Peter Triesberger
For further information see https://github.com/peter88213/yw2odm
Published under the MIT License (https://opensource.org/licenses/mit-license.php)
"""
import os

from yw2odmlib.odm_file import OdmFile
from pywriter.odt.odt_export import OdtExport


class OdmChapters(OdmFile):
    """OpenDocument master document representation."""

    _chapterTemplate = '''<text:section text:style-name="Sect1" text:name="${Title}" text:protected="true">
<text:section-source xlink:href="../ChID_${ID}.odt"/>
</text:section>
'''

    def _get_chapters(self):
        """Process the chapters and nested scenes.
        
        Create a subdocument for each chapter, containing the scenes.
        Return a list of strings for the master document.
        Extends the superclass method.
        """
        projectDir = os.path.dirname(self._originalPath)
        if not projectDir:
            projectDir = '.'
        for chId in self.srtChapters:
            subDocument = OdtExport(f'{projectDir}/ChID_{chId}.odt')
            subDocument.title = f'{self.title} - ChID: {chId}'
            subDocument.desc = self.chapters[chId].title
            if self.chapters[chId].desc:
                subDocument.desc += (f'\n{self.chapters[chId].desc}')
            subDocument.authorName = self.authorName
            subDocument._fileHeader = self._CONTENT_XML_HEADER
            subDocument.chapters[chId] = self.chapters[chId]
            subDocument.srtChapters = [chId]
            subDocument.locations = self.locations
            subDocument.characters = self.characters
            subDocument.items = self.items
            for scId in self.chapters[chId].srtScenes:
                subDocument.scenes[scId] = self.scenes[scId]
            subDocument.write()
        return super()._get_chapters()
