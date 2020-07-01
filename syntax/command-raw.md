<- [Back to Syntax Commands](syntax-commands.md)

# RAW

The RAW command will add content as is - text, html etc, to any section. It bypasses any outer and inner divs so can be used to add your own html markup. In effect the RAW command allows you to take current html from other sites and transplant it to MorfLess

For example:

    ///HEADER:
    %%RAW::
    TEXT=[ <text, html etc> ]:

or

    ///SIDEBAR:
    %%RAW::
    TEXT=[ <text, html etc> ]:

## Subschematic Commands

- TEXT (no arguments)

The syntax within the "=[ ]:" can be any text or html.

## Keywords

None
