"""Convert yWriter project to odm/odt. 

Version @release

Copyright (c) 2021 Peter Triesberger
For further information see https://github.com/peter88213/yw2odm
Published under the MIT License (https://opensource.org/licenses/mit-license.php)
"""
import os
import argparse

from pywriter.converter.yw_cnv_ui import YwCnvUi
from pywriter.ui.ui_tk import UiTk
from pywriter.ui.ui import Ui
from pywriter.yw.yw7_file import Yw7File
from pywodm.odm_chapters import OdmChapters


class Exporter(YwCnvUi):
    """A converter class for XPress tagged file export."
    Extend the Super class. 
    Show 'Open' button after conversion from yw.
    """
    EXPORT_SOURCE_CLASSES = [Yw7File]
    EXPORT_TARGET_CLASSES = [OdmChapters]

    def export_from_yw(self, sourceFile, targetFile):
        """Extend the super class method, showing an 'open' button after conversion."""
        YwCnvUi.export_from_yw(self, sourceFile, targetFile)

        if self.newFile:
            self.ui.show_open_button(self.open_newFile)


def run(sourcePath, silentMode=True):
    suffix = ''
    converter = Exporter()

    if silentMode:
        converter.ui = Ui('yWriter export to odm/odt documents @release')

    else:
        converter.ui = UiTk('yWriter export to odm/odt documents @release')

    kwargs = {'suffix': suffix}
    converter.run(sourcePath, **kwargs)
    converter.ui.start()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='yWriter export to odm/odt documents',
        epilog='')
    parser.add_argument('sourcePath', metavar='Sourcefile',
                        help='The path of the yWriter project file.')

    parser.add_argument('--silent',
                        action="store_true",
                        help='suppress error messages and the request to confirm overwriting')
    args = parser.parse_args()

    if args.silent:
        silentMode = True

    else:
        silentMode = False

    if os.path.isfile(args.sourcePath):
        sourcePath = args.sourcePath

    else:
        sourcePath = None

    run(sourcePath, silentMode)
