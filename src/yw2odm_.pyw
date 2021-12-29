#!/usr/bin/env python3
"""Convert yWriter project to odm/odt. 

Version @release

Copyright (c) 2021 Peter Triesberger
For further information see https://github.com/peter88213/yw2odm
Published under the MIT License (https://opensource.org/licenses/mit-license.php)
"""
import argparse

from pywriter.ui.ui_tk import UiTk
from pywriter.ui.ui import Ui
from pywodm.odm_exporter import OdmExporter


def run(sourcePath, silentMode=True):
    suffix = ''
    converter = OdmExporter()

    if silentMode:
        converter.ui = Ui('')

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
    run(args.sourcePath, args.silent)