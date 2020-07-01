<- [Back to Syntax Commands](syntax-commands.md)

# CONTENT_META

The CONTENT_META command will add meta information about the post or page. This command is only applied in the MAIN placement.

It can be used multiple times. If no syntax is defined, the default meta will be used. The default meta can be set through Settings.txt

For example:

    ///MAIN:
    %%CONTENT_META::

or

    ///MAIN:
    %%CONTENT_META::
    title={}:
    category={}:
    author={}:
    date_created={}:
    date_modified={}:
    show_time={}:

Also

    ///MAIN:
    %%CONTENT_META::
    title={}:

    ... <other content> 

    %%CONTENT_META::
    category={}:
    author={}:
    date_created={}:
    date_modified={}:
    show_time={}:

## Subschematic Commands

None

## Keywords

There are 6 keywords for CONTENT_META:

- title - show the page title
- category - show the page category link. This will only work on post type pages
- author - show the page author link.
- date_created - show the date the page was created.
- date_modified- show the date the page was modified.
- show_time - show the time the page was created (if already present) and modified (if already present)
