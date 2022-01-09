[Project homepage](https://peter88213.github.io/yw2odm)

------------------------------------------------------------------

The yw2odm Python script creates an ODM master document plus one ODT sub document per chapter.

## Instructions for use

### Intended usage

The included installation script prompts you to create a shortcut on the desktop. You can launch the program by dragging a yWriter project file and dropping it on the shortcut icon. 

### Command line usage

Alternatively, you can

- launch the program on the command line passing the yWriter project file as an argument, or
- launch the program via a batch file.

usage: `yw2odm.pyw [--silent] Sourcefile`

#### positional arguments:

`Sourcefile` 

The path of the yWriter project file.

#### optional arguments:

`--silent`  suppress error messages and the request to confirm overwriting


## General

-   All generated documents are placed in the same folder as the yWriter project.
-   The **master document's filename**: `<yW project name>.odm`.
-   The **sub document's filenames**: `<Chapter ID>.odt`.
-   Text markup: Bold and italics are supported. Other highlighting such
    as underline and strikethrough are lost.
-   Only "normal" chapters and scenes are exported. Chapters and
    scenes marked "unused", "todo" or "notes" are not exported.
-   Only scenes that are intended for RTF export in yWriter will be
    exported.
-   Comments in the text bracketed with slashes and asterisks (like
    `/* this is a comment */`) are converted to author's comments.
-   Interspersed HTML, TEX, or RTF commands are taken over unchanged.
-   Gobal variables and project variables are not resolved.
-   Chapter titles appear as first level heading if the chapter is
    marked as beginning of a new section in yWriter. Such headings are
    considered as "part" headings.
-   Chapter titles appear as second level heading if the chapter is not
    marked as beginning of a new section. Such headings are considered
    as "chapter" headings.
-   Scene titles appear as navigable comments pinned to the beginning of
    the scene.
-   Usually, scenes are separated by three asterisks. The first line is not
    indented.
-   Starting from the second paragraph, paragraphs begin with
    indentation of the first line.
-   Scenes marked "attach to previous scene" in yWriter appear like
    continuous paragraphs.
-   Chapter titles and chapter descriptions can be found in the sub document's
    file properties.

## Installation path

The setup script installs *yw2odm.pyw* in the user profile. This is the installation path on Windows: 

`c:\Users\<user name>\.pywriter\yw2odm`
    