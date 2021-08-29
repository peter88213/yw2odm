"""Provide an ODM/ODT exporter class for yWriter.

Copyright (c) 2021 Peter Triesberger
For further information see https://github.com/peter88213/yw2odm
Published under the MIT License (https://opensource.org/licenses/mit-license.php)
"""
from pywriter.converter.yw_cnv_ui import YwCnvUi
from pywriter.yw.yw7_file import Yw7File
from pywodm.odm_chapters import OdmChapters


class OdmExporter(YwCnvUi):
    """A converter class for ODM/ODT export."
    Extend the Super class. 
    Show 'Open' button after conversion from yw.
    """
    EXPORT_SOURCE_CLASSES = [Yw7File]
    EXPORT_TARGET_CLASSES = [OdmChapters]

    def export_from_yw(self, sourceFile, targetFile):
        """Extend the super class method, showing an 'open' button after conversion."""
        YwCnvUi.export_from_yw(self, sourceFile, targetFile)

        try:
            if self.newFile:
                self.ui.show_open_button(self.open_newFile)

        except AttributeError:
            pass
