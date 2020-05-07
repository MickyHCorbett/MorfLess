<- [Back to Syntax Commands](syntax-commands.md)

# Default

The DEFAULT command will add the default schematic settings as defined in **settings.txt**

For example: 

    ///HEADER:
    %%DEFAULT::
    
will add whatever the settings for the ///HEADER: tag are in Settings. 

If this command is used in the Settings, the default ///HEADER: content as defined in [libraries/schematics.py](../libraries/schematics.py) will be used.

For the case of Header this is:

    PM_HEADER_SCHEMATIC = """%%NAV::
    mlk={href="SITE_HOME" name="Home" src="IMAGES/home_icon.png"}:
    searchbar={}:"""
    
If you want to change the underlying default value as above, change the schematics.py file.
