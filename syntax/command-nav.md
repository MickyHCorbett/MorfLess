<- [Back to Syntax Commands](syntax-commands.md)

# NAV

The NAV command will add a navigation bar to the Header section. It only works when called in the Header tag.

For example: 

    ///HEADER:
    %%NAV::
    <syntax>
    
## Subschematic Commands 

None

## Keywords

There are 3 keywords for NAV:

- searchbar (no arguments)
- logo
  - required arguments: src
- mlk
  - required arguments: href, class
  - optional arguments: class
    
To add a nav menu link:

    mlk={ href="/path/" name="Text of link" }:
    
To add a logo:

    logo={ src="/path/" }:
    
To add the search bar:

    searchbar={}:
