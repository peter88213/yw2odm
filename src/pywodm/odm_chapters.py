"""Provide a class for ODM master document export
with chapters as subdocuments.

Copyright (c) 2021 Peter Triesberger
For further information see https://github.com/peter88213/yw2odm
Published under the MIT License (https://opensource.org/licenses/mit-license.php)
"""
import os

from pywodm.odm_file import OdmFile
from pywriter.odt.odt_export import OdtExport


class OdmChapters(OdmFile):
    """OpenDocument master document representation."""

    chapterTemplate = '''<text:section text:style-name="Sect1" text:name="${Title}" text:protected="true">
<text:section-source xlink:href="../ChID_${ID}.odt"/>
</text:section>
'''

    def get_chapters(self):
        """Process the chapters and nested scenes.
        Return a list of strings.
        Extend the superclass method by generating subdocuments.
        """
        projectDir = os.path.dirname(self.originalPath)

        if projectDir == '':
            projectDir = '.'

        for chId in self.srtChapters:
            subDocument = OdtExport(projectDir + '/ChID_' + chId + '.odt')

            subDocument.title = self.title + ' - ChID: ' + chId

            subDocument.desc = self.chapters[chId].title

            if self.chapters[chId].desc:
                subDocument.desc += ('\n' + self.chapters[chId].desc)

            subDocument.author = self.author
            subDocument.fileHeader = self.CONTENT_XML_HEADER

            subDocument.chapters[chId] = self.chapters[chId]
            subDocument.srtChapters = [chId]

            subDocument.locations = self.locations
            subDocument.characters = self.characters
            subDocument.items = self.items

            for scId in self.chapters[chId].srtScenes:
                subDocument.scenes[scId] = self.scenes[scId]

            print(subDocument.write())

        return OdmFile.get_chapters(self)
