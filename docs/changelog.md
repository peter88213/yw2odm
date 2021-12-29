[Project home page](index) > Changelog

------------------------------------------------------------------------

## Changelog

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
