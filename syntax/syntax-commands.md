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
