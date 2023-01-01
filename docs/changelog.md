[Project home page](index) > Changelog

------------------------------------------------------------------------

## Changelog

### v01.0.11

- Make it run with old Windows versions.

Based on PyWriter v7.14.3

### v1.0.10

- Modify "shebang" line to make the script run with Python 3.11 under Windows.

Based on PyWriter v7.14.2

### v1.0.9

- Update the PyWriter library for future Python versions.
- Count words like in LibreOffice. See: https://help.libreoffice.org/latest/en-GB/text/swriter/guide/words_count.html.
- Use language markup for text passages when converting ODF and HTML.
- When exporting to ODT, paragraphs that start with "> " are formatted as "Quotations".
- Write non-system language and country codes when converting to ODF.

Based on PyWriter v7.14.2

### v1.0.8 Optional release

- Code refactoring and library update.

Based on PyWriter v7.2.1

### v1.0.7 Update setup script

- Change the working dir to the script dir on startup in order to avoid "file not found" error.

Based on PyWriter v5.18.0

### v1.0.6 Improved setup

- Catch exceptions in the setup script.

Based on PyWriter v5.18.0

### v1.0.5 Improved word counting

- Fix word counting considering ellipses.

Based on PyWriter v5.12.4

### v1.0.4 Improved word counting

- Fix word counting considering comments, hyphens, and dashes.

Based on PyWriter v5.12.3

### v1.0.3 Optional update

PyWriter library update.

Based on PyWriter v5.12.2

### v1.0.2 Optional update

- Clean up ODF templates to make the code and generated documents more compact.

Based on PyWriter v5.0.3

### v1.0.1 Optional update

- Improve code and documentation quality.

Based on PyWriter v5.0.2

### v1.0.0

- Fix a bug where "To do" chapters cause an exception.
- Rework the user interface. 
- Refactor the code.

Based on PyWriter v5.0.0

### v0.2.9 Update text formatting

When creating odt files, make paragraphs after blank lines "Text body" without indent.

Based on PyWriter v3.32.2

### v0.2.8 Make the installation OS independent.

- Add a shebang to the script.
- Use a Python installation script instead of a batch file.
- Make the installed script executable under Linux.

Based on PyWriter v3.28.1

### v0.2.7 Support non-Windows OS

- Move installation to another location (see instructions for use).

Based on PyWriter v3.28.1

### v0.2.6 Bugfix release

Avoid an exception in case the source file doesn't exist.

Based on PyWriter v3.18.0

### v0.2.5 Bugfix release

This release is strongly recommended.
Fix a regression from PyWriter v3.12.5. causing a crash if a scene has an 
hour, but no minute set.

Based on PyWriter v3.16.4

### v0.2.4 No automatic shortcut creation

- Due to sporadic security warnings, the automatic shortcut creation during installation is removed. The user is now guided to create the application shortcut manually.  

Based on PyWriter v3.16.0

### v0.2.2 Include installation script

**install.bat** installs the script for the local user and creates a 
shortcut on the desktop.

Based on PyWriter v3.12.7

### v0.2.1 Bugfix release

- Catch the "AttibuteError" exception for silent mode.

Based on PyWriter v3.12.7

### v0.2.0 Beta test release

Based on PyWriter v3.12.7
