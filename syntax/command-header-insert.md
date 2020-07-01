<- [Back to Syntax Commands](syntax-commands.md)

# HEADER_INSERT

The HEADER_INSERT command will add content from another file to the html head section. It can only be called in the header.

For example:

    ///HEADER:
    %%HEADER_INSERT::
    ref={ <file.txt> }:


## Subschematic Commands

None

## Keywords

ref={ <the file you want to reference> }:

The file can have any extension but .post, .page, .json or .html.
