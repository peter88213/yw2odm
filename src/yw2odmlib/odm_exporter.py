"""Provide an ODM/ODT exporter class for yWriter.

Copyright (c) 2022 Peter Triesberger
For further information see https://github.com/peter88213/yw2odm
Published under the MIT License (https://opensource.org/licenses/mit-license.php)
"""
from pywriter.converter.yw_cnv_ff import YwCnvFf
from pywriter.yw.yw7_file import Yw7File
from yw2odmlib.odm_chapters import OdmChapters


class OdmExporter(YwCnvFf):
    """A converter class for ODM/ODT export."

    Public methods:
        export_from_yw(sourceFile, targetFile) -- Convert from yWriter project to other file format.

    Class constants:
        EXPORT_SOURCE_CLASSES -- List of YwFile subclasses from which can be exported.
        EXPORT_TARGET_CLASSES -- List of FileExport subclasses to which export is possible.

    Shows the 'Open' button after conversion from yw.
    """
    EXPORT_SOURCE_CLASSES = [Yw7File]
    EXPORT_TARGET_CLASSES = [OdmChapters]

    def export_from_yw(self, source, target):
        """Convert from yWriter project to ODM/ODT file format.

        Positional arguments:
            source -- YwFile subclass instance.
            target -- OdmFile instance.
        
        Extends the super class method, showing an 'open' button after conversion.
        """
        super().export_from_yw(source, target)
        try:
            if self.newFile:
                self.ui.show_open_button(self._open_newFile)
        except AttributeError:
            pass



