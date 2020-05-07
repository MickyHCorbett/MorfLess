<- [Back to Syntax Commands](syntax-commands.md)

# MENU

The MENU command will add a menu to any section.

For example: 

    ///MAIN:
    %%MENU::
    <syntax>
    
## Subschematic Commands 

None

## Keywords

There are 3 keywords for MENU:

- searchbar (no arguments)
- title (no arguments)
- mlk
  - required arguments: href, class
  - optional arguments: class
    
To add a nav menu link:

    mlk={ href="/path/" name="Text of link" }:
    
To add a title:

    title={ <text of title }:
    
To add the search bar:

    searchbar={}:
