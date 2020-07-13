# Syntax

MorfLess uses a template syntax that is a simplified version of the PoliMorf syntax. 

Schematic files (templates) are used to create the html page on the site. Syntax contained in other files can be referenced and will be imported into the file. 

[Go here for syntax command details](syntax-commands.md)

[Go here for details on the settings file and schematics](../user-guide/building-the-site.md)

## Schematic Requirements

The schematics are simple text files with the following tags:

    ///META:
    title={ A title }:
    url={ /path-to-page/ }:
    
    ///HEADER:
    <various commands>
    
    ///BEFORE:
    <various commands>
    
    ///MAIN:
    <various commands>
    
    ///AFTER:
    <various commands>
    
    ///SIDEBAR:
    <various commands>
    
    ///FOOTER:
    <various commands>
    
 For the schematic to be processed the following elements are needed:
 
 - META tag with title and url keyword
 - The HEADER, MAIN and FOOTER tag
 
 The BEFORE, AFTER and SIDEBAR tags are optional. Other meta tags are also optional.
 
 MorfLess has the capability to display a page with either a full-width style or two-column style (main and sidebar). Note that if there is no Sidebar defined, Main is full-width
 
 <p align="center">
 <img src="MorfLessWebPageLayout.png" width=50% />
 </p>
 
 ### File extensions
 
 Though MorfLess will trigger on any file upload, RenderHtml will perform processing in the following cases:
 
 - A file ending in ".post" or ".page" is uploaded. 
 - A file that isn't HTML or JSON is uploaded
 
 If a non post/page file is uploaded, RenderHtml will check it is included in the dependencies.json file stored in the List Bucket. 

If it is, a list of files that are dependent on the uploaded file will be created and processed. If not the single file is processed. Dependent files can be settings.txt (if the DEFAULT command is used) or any inserted files (if the INSERT command is used)

When a file is deleted, it is removed from the master list of posts and pages (postlist.json) as well as the website bucket. The file, dependencies.json, will be amended only when the dependent file is updated. This is trivial for the deleted file as content for that file will not be visible.

## Identifiers

The syntax is organised using 3 types of identifiers:

- Schematic commands idenfied by %%<command>::
- Sub commands identified by <sub_command>=[ <syntax> ]:
- Keyword identified by <keyword>={ <syntax> }:

The exception is for table elements called Boxes:

For example, a 3-elements box (3BOX) is called as follows:

        %%3_BOX::
        BOX1:
        <sub_command>=[ ]:
        
        BOX2:
        <sub_command>=[ ]:
        
        BOX3:
        <sub_command>=[ ]:
        
If the BOXn elements are not present the nBOX will not be processed. Currently there is support for 2, 3 and 4 Boxes.

For sub-commands and keywords the opening syntax ***must be written without spaces*** from the sub-command or keyword. Spaces can be used in the syntax and after the closing identifier syntax.

## Sections

Elements can be grouped into a general Section element (different than an HTML5 section tag). This is done so things like a common background can be added. To add a Section, the command structure is slightly altered. Using the 3BOX example, the command identifiers are altered to start and end with a square bracket, and a Section id needs to be present:

        %%SECTION::
        {{ <section-id> }}
        [%3_BOX:]
        BOX1:
        <sub_command>=[ ]:
        
        BOX2:
        <sub_command>=[ ]:
        
        BOX3:
        <sub_command>=[ ]:
        
 If you create html elements using React or Vue, add the section id at the very start just after the SECTION command. That way it will be processed as expected and not mistaken for a parameter. The section id can be placed anywhere within the syntax and for standard html there is expected to be only one.
        
 ## Custom classes
 
 Custom classes can be added to commands by using a CUSTOM tag as follows:
 
        %%SECTION_CUSTOM: custom-class ::
        {{ <section-id> }}
        [%3_BOX:]
        BOX1:
        <sub_command>=[ ]:
        
        BOX2:
        <sub_command>=[ ]:
        
        BOX3:
        <sub_command>=[ ]:
        
 ## Meta
 
 The mandatory meta is title and url. If you don't add any other meta the defaults will be applied. These can be the ones within meta_defaults.py and also globals.py. But there is also the ability to change meta like default thumbnail, default author, author descriptions and category descriptions within settings.txt.
 
 For pages and posts the full meta is as follows:
 
        ///META:
        title={ <title> }:
        url={ /path/to/page/ }:
        author={ author1, <author list> }:
        categories={ category1, <category list> }:
        description={ <Short description for head of page> }:
        extract={ <More detailed description for when post/page is listed > }:
        thumbnail={ /link/to/thumbnail.png }:
        sticky={}: 
        unlisted={}:
        
Author meta (author) is singular as you tend to have one author, but you can have more. Categories tend to be plural hence the meta keyword is "categories".

Sticky (sticky={}: - no syntax ) is for posts and indicates you want this post to be at the top of the full posts list or in an author or category page. 
Unlisted (unlisted={}: - no syntax) indicates that you don't want the post to appear in searches or listings. 
