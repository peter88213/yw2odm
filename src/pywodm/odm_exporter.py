"""Provide an ODM/ODT exporter class for yWriter.

Copyright (c) 2022 Peter Triesberger
For further information see https://github.com/peter88213/yw2odm
Published under the MIT License (https://opensource.org/licenses/mit-license.php)
"""
from pywriter.converter.yw_cnv_ff import YwCnvFf
from pywriter.yw.yw7_file import Yw7File
from pywodm.odm_chapters import OdmChapters


class OdmExporter(YwCnvFf):
    """A converter class for ODM/ODT export."
    Extend the Super class. 
    Show 'Open' button after conversion from yw.
    """
    EXPORT_SOURCE_CLASSES = [Yw7File]
    EXPORT_TARGET_CLASSES = [OdmChapters]

    def export_from_yw(self, source, target):
        """Extend the super class method, showing an 'open' button after conversion."""
        super().export_from_yw(source, target)

        try:
            if self.newFile:
                self.ui._show_open_button(self._open_newFile)

        except AttributeError:
            pass



