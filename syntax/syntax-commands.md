# Syntax - Commands

MorfLess uses the following schematic commands in relation to their placement. They result in html elements being rendered on the page:

| Command | Use  | Placement |
| :-------| :----| :-------- |
| DEFAULT | Use the default for the placement tag as defined in settings.txt | All placements |
| NAV | Insert the nav bar | HEADER only |
| MENU | Insert a menu | All placements |
| QUOTE | Add a quote | All placements |
| CONTENT | Add content i.e. text/html | All placements |
| CONTENT_META |  Add the title, author, category, date modified and date created information to a post/page| MAIN only |
| POSTLIST | Add a list of posts or pages | All placements except HEADER |
| SECTION | Adds a general div element that wraps other commands creating a section | All placements except HEADER |
| INSERT | Add in schematic commands from another file | All placements |
| HEADER_INSERT | Add in schematic commands from another file | HEADER only |
| PAGINATION | Add next and previous links for pages and posts | MAIN only |
| SEARCHBAR| Add the search bar | All placements |
| STYLING | Add manual style remarks | All placements |

As as a reminder the placements are as follows (* means mandatory): 
- HEADER*
- BEFORE (Before main section)
- MAIN*
- AFTER
- SIDEBAR
- FOOTER*

There are also Addition commands:

| Command | Use  | Placement |
| :-------| :----| :-------- |
| HEADER_ADDITIONS | Adds text and scripts to the head | HEADER only |
| FOOTER_ADDITIONS | Adds text and scripts just before close body tag | FOOTER only |

## Schematic Tags

Each page or post (saved as a .post or .page) needs a minimum of information to be processed. The following schematic is that absolute basic that will allow html content to be created:

    ///META:
    title={ <something> }:
    url={ /<link>/<to>/<something>/ }:
    
    ///HEADER:
    %%DEFAULT::
    
    ///MAIN:
    %%DEFAULT::
    
    ///FOOTER:
    %%DEFAULT::
    
The tags "///xxxxx:" are **Schematic Tags** in that they represent the different sections of a html document, with the META section representing backend information that can be organised and indexed separately. 

In the example about there is one **Schematic Command** in the form "%%xxxxx::". MorfLess will parse this text by Schematic Tag then by Schematic Command. If the Schematic Command syntax is incorrect the command and all its subcommands or keywords will be ignored.
    


