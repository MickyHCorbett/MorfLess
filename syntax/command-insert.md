<- [Back to Syntax Commands](syntax-commands.md)

# INSERT

The INSERT command will add content from another file.

For example: 

    ///HEADER:
    %%INSERT::
    ref={ <file.txt> }:
    
or

    ///MAIN:
    %%INSERT::
    ref={ <file1.txt> }:
    
## Subschematic Commands 

None

## Keywords

ref={ <the file you want to reference> }:

The file can have any extension but .post, .page, .json or .html.

