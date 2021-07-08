[Project homepage](https://peter88213.github.io/yw2odm)

------------------------------------------------------------------

The yw2odm Python script creates an ODM master document plus runs through all chapters and scenes of a yWriter 7 project and fills XTG templates.

## Instructions for use

It is recommended to create a link on the desktop.

You can either

- launch the program by dragging a yWriter project file and dropping it on the program/link icon, or
- launch the program on the command line passing the yWriter project file as an argument, or
- launch the program via a batch file.


usage: `yw2odm.pyw [--silent] Sourcefile`

#### positional arguments:

`Sourcefile` 

The path of the yWriter project file.

#### optional arguments:

`--silent`  suppress error messages and the request to confirm overwriting

