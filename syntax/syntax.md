# Syntax

MorfLess uses a template syntax that is a simplified version of the PoliMorf syntax. 

Schematic files (templates) are used to create the html page on the site. Syntax contained in other files can be referenced and will be imported into the file. 

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
 
 The BEFORE, AFTER and SIDEBAR tags are optional. 
 
 MorfLess has the capability to display a page with either a full-width style or two-column style (main and sidebar). 
 
 <p align="center">
 <img src="MorfLessWebPageLayout.png" width=50% />
 </p>
 
