<- [Back to Syntax Commands](syntax-commands.md)

# PAGINATION

The PAGINATION command will add links to the next and previous post, if the page is a post type. It will add the next and previous pages links if the page is a page type. Manual links can also be used. This command is only applied in the MAIN placement.

For example:

    ///MAIN:
    %%PAGINATION::

or

    ///MAIN:
    %%PAGINATION::
    prev={ link1.page }:
    next={ link2.post }:

## Subschematic Commands

None

## Keywords

There are 2 keywords for PAGINATION:

- next - the name of the next page you wish to link to (not the url)
- prev - the name of the previous page you wish to link to (not the url)
