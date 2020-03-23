<- [Back to Syntax](https://github.com/MickyHCorbett/MorfLess/blob/master/syntax/syntax-commands.md)

# Default

The DEFAULT command will add the default schematic settings as defined in **settings.txt**

For example: 

    ///HEADER:
    %%DEFAULT::
    
Will add whatever the settings for the ///HEADER: tag where in Settings. 

If this command is used in the Settings, the default ///HEADER: content as defined in [libraries/schematics.py](https://github.com/MickyHCorbett/MorfLess/blob/master/libraries/morflessLibs/schematics.py) will be used.

For the case of Header this is:

    PM_HEADER_SCHEMATIC = """%%NAV::
    mlk={href="SITE_HOME" name="Home" src="IMAGES/home_icon.png"}:
    searchbar={}:"""
