# elements that output html
from libraries import globals as gb
from libraries import constants as ct
from libraries import schematics as sch
from libraries import string_processes as sp
from libraries import lists as ls

def pcom_command_selection(command,syntax,placement,type,settings):
    out = ct.PCOM_NO_ENTRY
    # process for custom tag in command
    proc_com = pcom_process_custom_command(command)

    if proc_com['command'] in gb.COMMAND_LIST:

        if proc_com['command'] == ct.PCOM_SECTION_COMMAND:
            out,settings = pcom_process_section_command(syntax,proc_com['custom_class'],placement,type,settings)
        else:
            function_call = gb.COMMAND_LIST[ proc_com['command'] ]
            args = "(syntax,proc_com['custom_class'],placement,type,settings)"
            out = eval(function_call + args)

        # if default command add settings file once to valid insert list
        # include default header and footer additions depending on placement
        if proc_com['command'] == ct.PCOM_DEFAULT_COMMAND:
            if ct.PCOM_REQ_FILE_SETTINGS not in settings['add_settings_to_dependencies']:
                settings['add_settings_to_dependencies'].append(ct.PCOM_REQ_FILE_SETTINGS)

            if placement == ct.PCOM_HEADER_PLACEMENT:
                settings['add_default_header_additions'] = True

            if placement == ct.PCOM_FOOTER_PLACEMENT:
                settings['add_default_footer_additions'] = True


        if proc_com['command'] == ct.PCOM_POST_LIST_COMMAND:
            settings['postlist_present'] = True

    # process for n_box
    n_box_test = sp.pcom_get_strings_syntax_separator(proc_com['command'],ct.PCOM_BOX_COMMAND_ROOT,True)
    if n_box_test['command_found'] == True:
      no_boxes = int(n_box_test['syntax_before'])
      out = pcom_process_n_box_command(syntax,proc_com['custom_class'],placement,settings,no_boxes)

    return out,settings


def pcom_addition_selection(command,syntax,placement,type, settings):
    # process for custom tag in command
    proc_com = pcom_process_custom_command(command)

    if proc_com['command'] in gb.ADDITIONS_LIST:
        function_call = gb.ADDITIONS_LIST[ proc_com['command'] ]

        args = "(syntax,proc_com['custom_class'],placement,type,settings)"
        # call function
        settings = eval(function_call + args)

    return settings

#
# Separates a custom class from a command
# Returns a dictionary with both

#
def pcom_process_custom_command(command):
    # parse command for custom keyword to pass onto class in html
    process_custom = sp.pcom_get_strings_syntax_separator(command,ct.PCOM_CUSTOM_CLASS_DECLARATION,True)

    return {'command': process_custom['syntax_before'], 'custom_class': process_custom['syntax_after']}


# ==========

# DEFAULT
def pcom_use_defaults(command,syntax,placement,type, settings):
    syntax = ''
    # defaults inside a schematic
    if placement == ct.PCOM_HEADER_PLACEMENT:
        syntax = settings['default_header']
    if placement == ct.PCOM_MAIN_PLACEMENT:
        if type == ct.PCOM_BEFORE_TYPE:
            syntax  = settings['default_before']
        elif type == ct.PCOM_AFTER_TYPE:
            syntax  = settings['default_after']
        else:
            syntax  = settings['default_main']
    if placement == ct.PCOM_SIDEBAR_PLACEMENT:
        syntax = settings['default_sidebar']
    if placement == ct.PCOM_FOOTER_PLACEMENT:
        syntax = settings['default_footer']

    return syntax

def pcom_use_settings_defaults(placement, settings):
    out_html = ''

    # from settings file - settings in will be the default
    if placement == ct.PCOM_SETTINGS_HEADER:
        out_html = settings['default_header']
    if placement == ct.PCOM_SETTINGS_BEFORE:
        out_html = settings['default_before']
    if placement == ct.PCOM_SETTINGS_MAIN:
        out_html = settings['default_main']
    if placement == ct.PCOM_SETTINGS_AFTER:
        out_html = settings['default_after']
    if placement == ct.PCOM_SETTINGS_SIDEBAR:
        out_html = settings['default_sidebar']
    if placement == ct.PCOM_SETTINGS_FOOTER:
        out_html = settings['default_footer']

    return out_html


# NAV
def pcom_process_nav_command(syntax, custom_class, placement, type, settings):

    # NAV is in header - no custom placement class
    out_html =''
    out_html += sp.pcom_open_custom_class_div(custom_class,sch.PM_NAV_OPEN) + ct.NL
    # process commands
    out_html += pcom_process_menu_command_syntax(syntax,custom_class,placement,ct.PCOM_NAV_COMMAND,settings)
    out_html += sch.PM_NAV_CLOSE

    return out_html

# MENU
def pcom_process_menu_command(syntax, custom_class, placement,type, settings):

    # NAV is in header - no custom placement class
    out_html = sp.pcom_open_placement_class(custom_class,placement)
    out_html += sp.pcom_open_custom_class_div(custom_class,sch.PM_NAV_OPEN) + ct.NL
    # process commands
    out_html += pcom_process_menu_command_syntax(syntax,custom_class,placement,ct.PCOM_MENU_COMMAND,settings)
    out_html += sch.PM_NAV_CLOSE
    out_html += sp.pcom_close_placement_class(placement)

    return out_html



# MENU NAV SYNTAX
#
# Function processes individual commands - NAV or MENU
# allowable keywords are:
# mlk for a link - this is mlk=}: - with url and name
# logo - logo=}: - for inserting a logo in the menu - url, src and name
# searchbar=}: (brackets empty) - for inserting a search bar
#
def pcom_process_menu_command_syntax(syntax,custom_class,placement,type,settings):
    out_html = ''
    # keywords all start with KEYWORD=
    # search for = in command
    first_menu_link = False
    insert_searchbar = False
    logo_present = False

    no_logo = ct.PCOM_NO_LOGO
    with_logo = sch.PM_NAV_MENU_OPEN
    logo_html_string = no_logo
    menu_html_string = ''
    title_string = ''
    menu_name = ''
    icon_string = ''
    logo_string = ''
    searchbar_string = ''

    args = {'open': ct.PCOM_KEYWORD_OPEN,'close': ct.PCOM_KEYWORD_CLOSE}

    # initialise open and close syntax
    commands = sp.pcom_build_dictionary(gb.DEFAULT_OPEN_CLOSE_SYNTAX_OUT_ARRAY)
    commands['command'] = ''

    #loop over keywords
    while commands['command'] != ct.PCOM_NO_ENTRY:

        commands = sp.pcom_process_command_open_close_syntax(syntax,args)

        # update elements present
        if commands['command'] == ct.PCOM_NAV_MENU_LINK_KEYWORD:
            # check to see if first menu link
            if (first_menu_link == False):
                menu_html_string = ct.NL + sp.pcom_process_menu_command_mlk_keyword(commands['command_syntax'])
                # latch first_menu_link
                first_menu_link = True
            else:
                menu_html_string += ct.NL  + sp.pcom_process_menu_command_mlk_keyword(commands['command_syntax'])

        if commands['command'] == ct.PCOM_NAV_LOGO_KEYWORD:
            logo_html_string = with_logo
            logo_html_string = sp.pcom_process_logo_for_nav(commands['command_syntax'],settings['site_title'])

        if commands['command'] == ct.PCOM_TITLE_KEYWORD:
            title_string = sp.pcom_add_title(commands['command_syntax'])

        if commands['command'] == ct.PCOM_NAV_SEARCHBAR_KEYWORD:
            insert_searchbar = True

        # update syntax
        syntax = commands['syntax_after']

    # check menu

    if first_menu_link == True:
        #add open and close html to menu
        if logo_html_string != no_logo:
            with_logo = sch.PM_NAV_MENU_OPEN_WITH_LOGO


    menu_html_string =  with_logo + menu_html_string + ct.NL + sch.PM_NAV_MENU_CLOSE + ct.NL


    # ----------
    # Select type of command - NAV or MENU

    if type == ct.PCOM_NAV_COMMAND:

        # NAV - only active in the header
        if placement == ct.PCOM_HEADER_PLACEMENT:
            icon_string = sch.PM_NAV_RESP_ICON_OPEN + ct.NL + sch.PM_ICON_HTML + ct.NL + sch.PM_NAV_RESP_ICON_CLOSE + ct.NL

        if logo_html_string != no_logo:
            logo_string = logo_html_string + ct.NL + sch.PM_NAV_MENU_SEARCH_WITH_LOGO_OPEN + ct.NL
        else:
            logo_string = sch.PM_NAV_MENU_SEARCH_OPEN + ct.NL

        if insert_searchbar:
            searchbar_string = pcom_insert_searchbar_command(syntax, custom_class, placement, type, settings)

        out_html = icon_string + logo_string + menu_html_string + searchbar_string + sch.PM_NAV_MENU_SEARCH_CLOSE + ct.NL


    # MENU - for general menus - default command

    if type == ct.PCOM_MENU_COMMAND:

        #  if menu is not in the header
        if placement != ct.PCOM_HEADER_PLACEMENT:
        #  add extra menu wrapper for after, main, before, or footer
        #  which is covered by main, main with sidebar and footer placement
            if placement == ct.PCOM_MAIN_PLACEMENT or placement == ct.PCOM_MAIN_WITH_SIDEBAR_PLACEMENT or placement == ct.PCOM_FOOTER_PLACEMENT:
                out_html = sp.pcom_open_custom_class_div(custom_class,sch.PM_GENERAL_MENU_OPEN) + ct.NL
            elif placement == ct.PCOM_SIDEBAR_PLACEMENT:
                # add sidebar div
                out_html = sp.pcom_open_custom_class_div(custom_class,sch.PM_SIDEBAR_CONTENT_OPEN) + ct.NL

            # add title string
            if (title_string):
                out_html += title_string + ct.NL

            # add menu string
            out_html += menu_html_string

            if placement == ct.PCOM_MAIN_PLACEMENT or placement == ct.PCOM_MAIN_WITH_SIDEBAR_PLACEMENT or placement == ct.PCOM_FOOTER_PLACEMENT:
                out_html += sch.PM_GENERAL_MENU_CLOSE + ct.NL
            elif placement == ct.PCOM_SIDEBAR_PLACEMENT:
                out_html += sch.PM_SIDEBAR_CONTENT_CLOSE + ct.NL

    return out_html


# ==========

# CONTENT
def pcom_add_content_command(syntax, custom_class, placement, type, settings):

    out_html = ''
    content = ''
    out_content = ''
    valid_content = False

    args = {'open': ct.PCOM_SUB_COMMAND_OPEN,'close': ct.PCOM_SUB_COMMAND_CLOSE}
    # initialise open and close syntax
    commands = sp.pcom_build_dictionary(gb.DEFAULT_OPEN_CLOSE_SYNTAX_OUT_ARRAY)
    commands['command'] = ''

    if syntax != ct.PCOM_NO_ENTRY:

        # trim
        syntax = syntax.rstrip().lstrip()

        while commands['command'] != ct.PCOM_NO_ENTRY:

            commands = sp.pcom_process_command_open_close_syntax(syntax,args) # default sub commands
            # filter out any custom classes - these should be applied to the top level
            command_custom = pcom_process_custom_command(commands['command'])

            if command_custom['command'] == ct.PCOM_CONTENT_TEXT_SUBCOMMAND:
                # replace substitions
                content = sp.pcom_replace_custom_attributes(commands['command_syntax'],ct.PCOM_POST_HTML_CONVERSIONS)
                # add tabs to lines
                content = sp.pcom_add_2tabs_to_content_line(content)

                out_content += content
                valid_content = True

            # update syntax
            syntax = commands['syntax_after']

        # show on main, main with sidebar and footer
        post_open = sch.PM_POST_OPEN
        post_close = sch.PM_POST_CLOSE
        if placement == ct.PCOM_FOOTER_PLACEMENT:
            post_open = sch.PM_POST_OPEN_FOOTER
            post_close = sch.PM_POST_CLOSE_FOOTER

        if valid_content:
            out_html = sp.pcom_open_placement_class(custom_class,placement)
            out_html += sp.pcom_open_custom_class_div(custom_class,post_open) + ct.NL
            out_html += out_content + ct.NL
            out_html += post_close + sp.pcom_close_placement_class(placement)

    return out_html


# SEARCHBAR
def pcom_insert_searchbar_command(syntax, custom_class, placement, type, settings):

    out_html = ''

    open_div = sch.PM_SEARCHBAR_OPEN
    close_div = sch.PM_SEARCHBAR_CLOSE

    if placement == ct.PCOM_HEADER_PLACEMENT:
        open_div = sch.PM_NAV_SEARCHBAR_OPEN
        close_div = sch.PM_NAV_SEARCHBAR_CLOSE

    if placement == ct.PCOM_MAIN_PLACEMENT:
        out_html += sp.pcom_open_placement_class(custom_class,placement) + ct.NL
        out_html += sch.PM_POST_OPEN_ONLY + ct.NL

    out_html += (ct.NL + open_div + ct.NL
            + sch.PM_SEARCH_BAR
            + close_div + ct.NL)

    if placement == ct.PCOM_MAIN_PLACEMENT:
        out_html += sch.PM_POST_CLOSE + ct.NL
        out_html += sp.pcom_close_placement_class(placement)

    return out_html

def pcom_insert_searchbar_for_search_page():

    placement = ct.PCOM_MAIN_PLACEMENT

    out_html = ''
    out_html += sp.pcom_open_placement_class(ct.PCOM_SEARCHPAGE_SEARCHBAR_CLASS,placement) + ct.NL
    out_html += sch.PM_POST_LIST_CUSTOM_OPEN_ONLY + ct.NL
    out_html += (ct.NL + sch.PM_SEARCHBAR_OPEN + ct.NL
            + sch.PM_SEARCH_BAR_SEARCH_PAGE
            + sch.PM_SEARCHBAR_CLOSE + ct.NL)
    out_html += ct.T2 + sch.PM_SEARCH_QUERY_TITLE + ct.NL
    out_html += ct.T2 + sch.PM_SEARCH_CONTENT + ct.NL
    out_html += ct.T2 + sch.PM_SEARCH_PAGINATION+ ct.NL
    out_html += sch.PM_POST_LIST_CLOSE + ct.NL
    out_html += sp.pcom_close_placement_class(placement)

    return out_html

# REMOTE INSERTS = other files in the folder
def pcom_process_insert_command(syntax, custom_class, placement, type, settings):

    out_string = ''
    args = {'open': ct.PCOM_KEYWORD_OPEN,'close': ct.PCOM_KEYWORD_CLOSE}

    keywords = sp.pcom_process_command_open_close_syntax(syntax,args)

    if keywords['command_syntax'] and keywords['command'] == ct.PCOM_INSERT_REF_KEYWORD:

        # do not process settings.txt as an insert
        if keywords['command_syntax'] != ct.PCOM_REQ_FILE_SETTINGS:
            out_string = ct.PCOM_INSERT_TAG_OPEN + placement + ":" +  keywords['command_syntax'] + ct.PCOM_INSERT_TAG_CLOSE

    return out_string

# REMOTE INSERTS = other files in the folder
def pcom_process_insert_additions_command(syntax, custom_class, placement, type, settings):

    out_string = ''
    args = {'open': ct.PCOM_KEYWORD_OPEN,'close': ct.PCOM_KEYWORD_CLOSE}
    defaults = {ct.PCOM_INSERT_REF_KEYWORD: '' }

    keywords = sp.pcom_process_command_open_close_syntax(syntax,args)

    if keywords['command_syntax'] and keywords['command'] == ct.PCOM_INSERT_REF_KEYWORD:

        # do not process settings.txt as an insert
        if keywords['command_syntax'] != ct.PCOM_REQ_FILE_SETTINGS:
            out_string = ct.PCOM_INSERT_TAG_OPEN + placement + ":" +  keywords['command_syntax'] + ct.PCOM_INSERT_TAG_CLOSE

    return out_string

def pcom_insert_pagination_command(syntax, custom_class, placement, type, settings):

    ref_insert = ''
    next_ref = ''
    prev_ref = ''
    # initialise open and close syntax
    args = {'open': ct.PCOM_KEYWORD_OPEN,'close': ct.PCOM_KEYWORD_CLOSE}
    commands = sp.pcom_build_dictionary(gb.DEFAULT_OPEN_CLOSE_SYNTAX_OUT_ARRAY)
    commands['command'] = ''

    if syntax:

        #process syntax for body and reference (ref)
        while commands['command'] != ct.PCOM_NO_ENTRY:

            commands = sp.pcom_process_command_open_close_syntax(syntax,args)
            # filter out any custom classes - these should be applied to the top level
            command_custom = pcom_process_custom_command(commands['command'])
            # process for next and prev
            if command_custom['command'] == ct.PCOM_INSERT_PAGINATION_NEXT_KEYWORD:
                next_ref = commands['command_syntax'].rstrip().lstrip()

            if command_custom['command'] == ct.PCOM_INSERT_PAGINATION_PREV_KEYWORD:
                prev_ref = commands['command_syntax'].rstrip().lstrip()

            #update syntax
            syntax = commands['syntax_after']

        ref_insert = next_ref + ',' + prev_ref

    out_html = (ct.PCOM_INSERT_PAGINATION_TAG_OPEN + placement + ':'
    + custom_class + ':' + ref_insert + ct.PCOM_INSERT_PAGINATION_TAG_CLOSE + ct.NL)

    return out_html


def pcom_create_pagination_link(links):

    pagination = False
    links_html = ''

    if links['next_url'] != ct.PCOM_NO_ENTRY and links['prev_url'] != ct.PCOM_NO_ENTRY:
        pagination = True
        next_link = ct.T4 + '<a href="' + links['next_url'] + '">' + links['next_title'] + '</a>'
        prev_link = ct.T4 + '<a href="' + links['prev_url'] + '">' + links['prev_title'] + '</a>'
        links_html = ("'" + ct.JS_ESCAPE + ct.NL
                + sch.PM_PAGINATION_NEXT_POST + ct.JS_ESCAPE + ct.NL
                + sch.PM_PAGINATION_FORMAT_NEXT_LINK + ct.JS_ESCAPE + ct.NL
                + next_link + ct.JS_ESCAPE + ct.NL
                + sch.PM_PAGINATION_CLOSE + ct.JS_ESCAPE + ct.NL
                + sch.PM_PAGINATION_PREV_POST + ct.JS_ESCAPE + ct.NL
                + sch.PM_PAGINATION_FORMAT_PREV_LINK + ct.JS_ESCAPE + ct.NL
                + prev_link + ct.JS_ESCAPE + ct.NL
                + sch.PM_PAGINATION_CLOSE + "'" + ct.NL)

    elif links['next_url'] == ct.PCOM_NO_ENTRY and links['prev_url'] != ct.PCOM_NO_ENTRY:
        pagination = True
        prev_link = ct.T4 + '<a href="' + links['prev_url'] + '">' + links['prev_title'] + '</a>'
        links_html = ("'" + ct.JS_ESCAPE + ct.NL
                + sch.PM_PAGINATION_SINGLE_POST + ct.JS_ESCAPE + ct.NL
                + sch.PM_PAGINATION_FORMAT_PREV_LINK + ct.JS_ESCAPE + ct.NL
                + prev_link + ct.JS_ESCAPE + ct.NL
                + sch.PM_PAGINATION_CLOSE + "'" + ct.NL)

    elif links['prev_url'] == ct.PCOM_NO_ENTRY and links['next_url'] != ct.PCOM_NO_ENTRY:
        pagination = True
        next_link = ct.T4 + '<a href="' + links['next_url'] + '">' + links['next_title'] + '</a>'
        links_html = ("'" + ct.JS_ESCAPE + ct.NL
                + sch.PM_PAGINATION_SINGLE_POST + ct.JS_ESCAPE + ct.NL
                + sch.PM_PAGINATION_FORMAT_NEXT_LINK + ct.JS_ESCAPE + ct.NL
                + next_link + ct.JS_ESCAPE + ct.NL
                + sch.PM_PAGINATION_CLOSE + "'" + ct.NL)

    return links_html,pagination

# N BOX COMMANDS
#
#
# Top level function to add box (or grid) elements
#
#

def pcom_process_n_box_command(syntax, custom_class, placement, settings, no_boxes):

    #limit box numbers
    box_max = ct.PCOM_MAX_NO_BOXES

    # limit no of boxes
    if no_boxes < 2:
        no_boxes = 2
    elif no_boxes > box_max:
        no_boxes = box_max

    #add starting wrap element and continue
    out_html =  sp.pcom_open_placement_class(custom_class,placement)
    out_html += sp.pcom_open_custom_class_div(custom_class,sch.PM_N_BOX_OPEN)

    out_html += ct.NL + pcom_parse_box_arguments(syntax,no_boxes,placement,settings['posts_per_page'])

    out_html += ct.NL + sch.PM_N_BOX_CLOSE
    out_html += sp.pcom_close_placement_class(placement)

    out_html = out_html.lstrip()

    return out_html

# ==============
# BOX PROCESSING
# ==============
#
def pcom_parse_box_arguments(syntax,no_boxes,placement,ppp):

    # only called if BOX commands exist
    sub_schem_end = ct.PCOM_SUB_SCHEMATIC_CLOSE
    markers_present = False
    marker_array = []

    # filter string for no of boxes
    # i.e. is someone has added BOX3 for a 2 box
    marker = ct.PCOM_BOX_BOX + str(no_boxes+1) + sub_schem_end
    split_strings_over = sp.pcom_get_strings_syntax_separator(syntax,marker,True)
    syntax = split_strings_over['syntax_before']

    # check for markers and set markers_present to found command
    for i in range(1,no_boxes+1):
        marker = ct.PCOM_BOX_BOX + str(i) + sub_schem_end
        marker_array.append(marker)

    for marker in marker_array:
        find_marker = sp.pcom_get_strings_syntax_separator(syntax,marker,True)
        markers_present = find_marker['command_found']

    # process marker commands

    i = 1
    out_html = ''

    if markers_present == True:

        while i <= no_boxes:
            # create box markers
            class1 = ct.PCOM_BOX_BOX + str(i)
            class2 = ct.PCOM_BOX_BOX + str(i+1)
            marker1 = ct.PCOM_BOX_BOX + str(i) + sub_schem_end
            marker2 = ct.PCOM_BOX_BOX + str(i+1) + sub_schem_end
            #
            split_strings1 = sp.pcom_get_strings_syntax_separator(syntax,marker1,True)

            if split_strings1['command_found'] == True:

                split_strings2 = sp.pcom_get_strings_syntax_separator(split_strings1['syntax_after'],marker2,True)

                # check i - if i is no_boxes then type is box box-end
                # default type is box
                # also add in box number

                if split_strings2['command_found'] == True:

                    if i == 1:
                        type = ct.PCOM_BOX_BOX +' ' + class1.lower() + ' ' + ct.PCOM_BOX_BOX_START
                    else:
                        type = ct.PCOM_BOX_BOX + ' ' + class1.lower()

                    #
                    out_html += \
                    pcom_add_box_for_n_box(split_strings2['syntax_before'],no_boxes,type,placement,ppp) + ct.NL

                else:

                    last_box = ct.PCOM_BOX_BOX + ' ' + class1.lower() + ' ' + ct.PCOM_BOX_BOX_END
                    out_html += pcom_add_box_for_n_box(split_strings1['syntax_after'],no_boxes,last_box,placement,ppp)

                #

            # increment i and set syntax for next pass
            i = i + 1

            syntax = marker2 + split_strings2['syntax_after']


    return out_html


#
# Processes box data and outputs to screen
#
#
def pcom_add_box_for_n_box(syntax,no_boxes,type,placement,ppp):


    # adds n box - depends on box type i.e. number
    args = {'open': ct.PCOM_SUB_COMMAND_OPEN,'close': ct.PCOM_SUB_COMMAND_CLOSE}

    # initialise open and close syntax
    commands = sp.pcom_build_dictionary(gb.DEFAULT_OPEN_CLOSE_SYNTAX_OUT_ARRAY)
    commands['command'] = ''

    out_html = ct.T3 + sch.PM_N_BOX_BOX_OPEN + str(no_boxes) + ' ' + type.lower() + sch.PM_CLOSE_DIV_WITH_COMMAS

    if syntax != '':

        while commands['command'] != ct.PCOM_NO_ENTRY:

            commands = sp.pcom_process_command_open_close_syntax(syntax,args) # default sub commands

            # filter out any custom classes - these should be applied to the top level
            command_custom = pcom_process_custom_command(commands['command'])
            #
            out_html += pcom_process_n_box_subcommands(
                                    command=command_custom['command'],
                                    syntax=commands['command_syntax'],
                                    ppp=ppp)
            # update syntax
            syntax = commands['syntax_after']


    out_html += ct.NL + ct.T3 + sch.PM_BOX_BOX_CLOSE


    return out_html
  #


# ---
#
#  Processes box subcommands
#

def pcom_process_n_box_subcommands(command,syntax,ppp):

    out_html = ''

    # process subcommands for n-box formats
    if syntax != "":
        #
        if command == ct.PCOM_MENU_COMMAND:
            out_html = pcom_process_n_box_menu_command(syntax)

        if command == ct.PCOM_TITLE_COMMAND:
            out_html = sp.pcom_add_title(syntax)

        if command == ct.PCOM_TEXT_COMMAND:
            out_html = pcom_process_n_box_text_command(syntax)

        if command == ct.PCOM_INSERT_SEARCHBAR_COMMAND:
            out_html = pcom_insert_searchbar_command(syntax,'',ct.PCOM_BOX_PLACEMENT,'',{})

        if command == ct.PCOM_QUOTE_COMMAND:
            out_html = pcom_insert_quote_box_command(syntax,'',ct.PCOM_BOX_PLACEMENT,'',{})

        if command == ct.PCOM_POST_LIST_COMMAND :
            settings = {'posts_per_page': ppp}
            out_html = pcom_add_post_list_command(syntax,'',ct.PCOM_BOX_PLACEMENT, '', settings)



    return out_html

# MENU command for N_BOX
def pcom_process_n_box_menu_command(syntax):

    # set settings to empty dictionary - not used in command
    settings = {}

    out_html = ct.NL+ ct.T1 + sp.pcom_open_custom_class_div('',sch.PM_NAV_OPEN) + ct.NL
    # process commands
    out_html += pcom_process_menu_command_syntax(syntax,'','n-box',ct.PCOM_MENU_COMMAND,settings)
    out_html += ct.T1 + sch.PM_NAV_CLOSE

    out_html = sp.pcom_add_2tabs_to_content_line(out_html)

    return out_html

# n-box TEXT content
def pcom_process_n_box_text_command(syntax):
    out_html = ''
    if syntax != ct.PCOM_NO_ENTRY:
        # replace substitions
        syntax = sp.pcom_replace_custom_attributes(syntax,ct.PCOM_POST_HTML_CONVERSIONS)
        # add tabs to lines
        syntax = sp.pcom_add_2tabs_to_content_line(syntax)
        syntax = sp.pcom_add_2tabs_to_content_line(syntax)
        syntax = sp.pcom_add_tab_to_content_line(syntax)

        out_html = ct.NL + ct.T2 + sch.PM_POST_OPEN_ONLY + ct.NL
        out_html += syntax + ct.NL
        out_html += ct.T2 + sch.PM_POST_CLOSE

    return out_html

# ========
# CONTENT_META
# ========

def pcom_add_content_meta_command(syntax, custom_class, placement, type, settings):

    out_html = ''
    if settings['current_file'].find('.post') > -1:
        meta_list = settings['default_content_post_meta']
    else:
        meta_list = settings['default_content_page_meta']

    out_html += ct.NL + ct.PCOM_CONTENT_META_TAG_OPEN + placement + ':'

    if syntax and syntax != ct.PCOM_NO_ENTRY:
        meta_list_keys = pcom_find_content_meta_keywords(syntax)
        meta_list = ls.pcom_create_comma_list_from_array(meta_list_keys)

    out_html += meta_list
    out_html += ct.PCOM_CONTENT_META_TAG_CLOSE

    return out_html


def pcom_find_content_meta_keywords(syntax):

    list=[]

    args = {'open': ct.PCOM_KEYWORD_OPEN, 'close': ct.PCOM_KEYWORD_CLOSE }

    # initialise open and close syntax
    commands = sp.pcom_build_dictionary(gb.DEFAULT_OPEN_CLOSE_SYNTAX_OUT_ARRAY)
    commands['command'] = ''

    if syntax:

        #process syntax for body and reference (ref)
        while commands['command'] != ct.PCOM_NO_ENTRY:

            commands = sp.pcom_process_command_open_close_syntax(syntax,args)
            # filter out any custom classes - these should be applied to the top level
            command_custom = pcom_process_custom_command(commands['command'])
            # process for text and reference
            if (command_custom['command'] == ct.PCOM_CONTENT_META_TITLE_KEYWORD or
            command_custom['command'] == ct.PCOM_CONTENT_META_AUTHOR_KEYWORD or
            command_custom['command'] == ct.PCOM_CONTENT_META_CATEGORY_KEYWORD or
            command_custom['command'] == ct.PCOM_CONTENT_META_DATE_CREATED_KEYWORD or
            command_custom['command'] == ct.PCOM_CONTENT_META_DATE_MODIFIED_KEYWORD or
            command_custom['command'] == ct.PCOM_CONTENT_META_SHOW_TIME_KEYWORD):

                list.append(command_custom['command'])

            #update syntax
            syntax = commands['syntax_after']

    return list

def pcom_insert_content_meta_data(html_array,content_meta_info,settings,list_meta,post,is_template):

    if content_meta_info:

        for ind,info in enumerate(content_meta_info):
            out_html = ''

            if post['postname'] != ct.PCOM_NO_ENTRY and not is_template:

                if info['placement'] == ct.PCOM_MAIN_PLACEMENT or info['placement'] == ct.PCOM_MAIN_WITH_SIDEBAR_PLACEMENT:

                    out_html += sp.pcom_open_placement_class('',info['placement']) + ct.NL
                    out_html += sp.pcom_open_custom_class_div('',sch.PM_META_OPEN) + ct.NL

                    if info['title']:
                      out_html += ct.T3 + '<h1>' + post['title'] + '</h1>' + ct.NL

                    # post,settings,list_meta_array,type,add_escape=False,no_js=False
                    if info['category']:
                        p_type = ct.PCOM_SETTINGS_TYPE_CATEGORIES
                        out_html += pcom_insert_author_category_in_post_list(
                                        post=post,
                                        settings=settings,
                                        list_meta_array=list_meta[p_type][p_type],
                                        type=p_type,
                                        add_escape=False,
                                        no_js=True)

                    if info['author']:
                        p_type = ct.PCOM_SETTINGS_TYPE_AUTHORS
                        out_html += pcom_insert_author_category_in_post_list(
                                        post=post,
                                        settings=settings,
                                        list_meta_array=list_meta[p_type][p_type],
                                        type=p_type,
                                        add_escape=False,
                                        no_js=True)

                    if info['date_created']:
                        out_html += pcom_insert_date_created(post,settings,info['show_time'])

                    if info['date_modified']:
                        out_html += pcom_insert_date_modified(post,settings,info['show_time'])

                    out_html += sch.PM_META_CLOSE + ct.NL
                    out_html += sp.pcom_close_placement_class(info['placement'])  + ct.NL


            html_array[info['index']] = out_html

    return html_array


def pcom_insert_date_created(post,settings,show_time):

    out_html = ''
    if post and post['postname']!= ct.PCOM_NO_ENTRY:

        date_info = ls.pcom_get_archive_date_info(post['creation_date'],settings)
        base_url = "/" + sp.pcom_create_template_fileroot(ct.PCOM_SETTINGS_TYPE_ARCHIVE,settings) + "/"
        url = base_url + date_info['date_url_name'] + "/"

        entry = post['creation_date']
        if show_time:
            entry += ' - ' + post['creation_time']

        out_html += sch.PM_POST_DATE_META_OPEN + ct.NL
        out_html += ct.T5 + sch.PM_DATE_CREATED_ICON + ct.NL
        out_html += (ct.T5 + '<a href="' + url + '" alt="' + date_info['date_url_name'] + '">'
                + entry + '</a>' +  ct.NL)

        out_html += sch.PM_POST_DATE_META_CLOSE + ct.NL

    return out_html


def pcom_insert_date_modified(post,settings,show_time):

    out_html = ''
    if post and post['postname']!= ct.PCOM_NO_ENTRY:


        #date_info = ls.pcom_get_archive_date_info(post['creation_date'],settings)

        #base_url = "/" + sp.pcom_create_template_fileroot(ct.PCOM_SETTINGS_TYPE_ARCHIVE,settings) + "/"
        #url = base_url + date_info['date_url_name'] + "/"

        entry = post['date_modified']
        if show_time:
            entry += ' - ' + post['time_modified']

        out_html += sch.PM_POST_DATE_META_OPEN + ct.NL
        out_html += ct.T5 + sch.PM_DATE_MODIFIED_ICON + ct.NL

        #out_html += (ct.T5 + '<a href="' + url + '" alt="' + date_info['date_url_name'] + '">'
        #        + entry + '</a>' +  ct.NL)

        out_html += ct.T5 + entry + ct.NL
        out_html += sch.PM_POST_DATE_META_CLOSE + ct.NL

    return out_html

# ========
# POST LIST
# ========

def pcom_add_post_list_command(syntax, custom_class, placement, type, settings):

    out_html = ''

    if syntax:

        keywords = pcom_process_postlist_keywords(syntax)
        #add starting wrap element and continue
        out_html =  sp.pcom_open_placement_class(custom_class,placement)
        out_html += sp.pcom_open_custom_class_div(custom_class,sch.PM_POST_LIST_CUSTOM_OPEN) + ct.NL

        if keywords[ct.PCOM_POST_LIST_TITLE_KEYWORD]:
            out_html += keywords[ct.PCOM_POST_LIST_TITLE_KEYWORD] + ct.NL

        if keywords[ct.PCOM_POST_LIST_POSTS_PER_PAGE_KEYWORD]:
            ppp =  keywords[ct.PCOM_POST_LIST_POSTS_PER_PAGE_KEYWORD]
        else:
            ppp = str(settings['posts_per_page'])

        #add postlist tag and list
        out_html += (ct.PCOM_POSTLIST_TAG_OPEN
            + keywords[ct.PCOM_POST_LIST_ENTRY_LIST_KEYWORD]
            + ":" + ppp
            + ":" + keywords[ct.PCOM_POST_LIST_MANUAL_STICKY])

        out_html += ct.PCOM_POSTLIST_TAG_CLOSE
        out_html += ct.NL + sch.PM_POST_LIST_CLOSE
        out_html += sp.pcom_close_placement_class(placement)

        out_html = out_html.lstrip()

    return out_html

# returns title and list
def pcom_process_postlist_keywords(syntax):

    args = {'open': ct.PCOM_KEYWORD_OPEN,'close': ct.PCOM_KEYWORD_CLOSE}
    keywords = { ct.PCOM_POST_LIST_TITLE_KEYWORD: '',
    ct.PCOM_POST_LIST_ENTRY_LIST_KEYWORD: '',
    ct.PCOM_POST_LIST_POSTS_PER_PAGE_KEYWORD: '',
    ct.PCOM_POST_LIST_MANUAL_STICKY: 'False' }

    # initialise open and close syntax
    commands = sp.pcom_build_dictionary(gb.DEFAULT_OPEN_CLOSE_SYNTAX_OUT_ARRAY)
    commands['command'] = ''

    #loop over keywords
    while ( commands['command'] != ct.PCOM_NO_ENTRY ):

        commands = sp.pcom_process_command_open_close_syntax(syntax,args)

        # update elements present
        if ( commands['command'] == ct.PCOM_POST_LIST_ENTRY_LIST_KEYWORD ):
            entry = commands['command_syntax'].rstrip().lstrip()
            entry = entry.replace('[','').replace(']','')

            # strip down and rejoin
            entries = entry.split(',')
            for ind,ent in enumerate(entries):
                entries[ind] = ent.strip()

            entry = ','.join(entries)

            keywords[ct.PCOM_POST_LIST_ENTRY_LIST_KEYWORD] = entry

        if ( commands['command'] == ct.PCOM_POST_LIST_TITLE_KEYWORD ):
            keywords[ct.PCOM_POST_LIST_TITLE_KEYWORD ] = sp.pcom_add_title(commands['command_syntax'])

        if ( commands['command'] == ct.PCOM_POST_LIST_POSTS_PER_PAGE_KEYWORD ):
            ppp = int(commands['command_syntax'])
            # limit to 1
            if ppp < 1:
                ppp = 1

            keywords[ct.PCOM_POST_LIST_POSTS_PER_PAGE_KEYWORD ] = str(ppp)

        if ( commands['command'] == ct.PCOM_POST_LIST_MANUAL_STICKY ):
            keywords[ct.PCOM_POST_LIST_MANUAL_STICKY ] = 'True'

        # update syntax
        syntax = commands['syntax_after']

    return keywords

# Create post entry using default image and post
# Outputs to screen
#
def pcom_create_post_list_entry(post,settings,list_meta,list_end,manual_sticky=False,ignore_meta=False,no_js=False):

    next_entry = "'"
    if not list_end:
        next_entry = "',"

    js_escape = ct.JS_ESCAPE
    if no_js:
        js_escape = ''

    extract = post['extract']
    extract = sp.pcom_replace_quotes(extract)

    out_html = "'" + js_escape + ct.NL
    out_html += sch.PM_POST_LIST_POST_CONTENT_OPEN + js_escape + ct.NL
    out_html += sch.PM_POST_LIST_POST_IMAGE_OPEN + js_escape + ct.NL

    if not post['thumbnail']:
        post['thumbnail'] = sch.PM_DEFAULT_THUMBNAIL_IMAGE_LINK

    out_html += ct.T4 + '<a href="' + post['url'] + '">' + js_escape + ct.NL
    out_html += ct.T5 + '<img src="' + post['thumbnail'] + '" alt="' + post['title'] + '"  />' + js_escape + ct.NL
    out_html += sch.PM_POST_LIST_POST_IMAGE_CLOSE + js_escape + ct.NL

    if manual_sticky:
        out_html += sch.PM_POST_LIST_BLOG_ENTRY_STICKY_OPEN + js_escape + ct.NL
    elif post['sticky'] == ct.PCOM_META_STICKY and not ignore_meta:
        out_html += sch.PM_POST_LIST_BLOG_ENTRY_STICKY_OPEN + js_escape + ct.NL
    else:
        out_html += sch.PM_POST_LIST_BLOG_ENTRY_OPEN + js_escape + ct.NL

    out_html += ct.T5 + '<h2><a href="' + post['url'] + '">' + post['title'] + '</a></h2>' + js_escape + ct.NL

    if post['type'] != 'page':
        p_type = ct.PCOM_SETTINGS_TYPE_CATEGORIES
        out_html += pcom_insert_author_category_in_post_list(
                        post=post,
                        settings=settings,
                        list_meta_array=list_meta[p_type][p_type],
                        type=p_type,
                        add_escape=True,
                        no_js=False)

    p_type = ct.PCOM_SETTINGS_TYPE_AUTHORS
    out_html += pcom_insert_author_category_in_post_list(
                        post=post,
                        settings=settings,
                        list_meta_array=list_meta[p_type][p_type],
                        type=p_type,
                        add_escape=True,
                        no_js=False)

    out_html += ct.T5 + '<p>' + extract.replace('\n','<br/>') + '</p>' + js_escape + ct.NL

    out_html += sch.PM_POST_LIST_BLOG_ENTRY_CLOSE + js_escape + ct.NL
    out_html += sch.PM_POST_LIST_POST_CONTENT_CLOSE + next_entry + ct.NL

    return out_html

def pcom_create_search_post_list_entry(post,settings,list_meta,ignore_meta=False):

    extract = post['extract']
    extract = sp.pcom_replace_quotes(extract)

    out_html = ''
    out_html += sch.PM_POST_LIST_POST_CONTENT_OPEN + ct.NL
    out_html += sch.PM_POST_LIST_POST_IMAGE_OPEN + ct.NL

    if not post['thumbnail']:
        post['thumbnail'] = sch.PM_DEFAULT_THUMBNAIL_IMAGE_LINK

    out_html += ct.T4 + '<a href="' + post['url'] + '">' + ct.NL
    out_html += ct.T5 + '<img src="' + post['thumbnail'] + '" alt="' + post['title'] + '"  />' + ct.NL
    out_html += sch.PM_POST_LIST_POST_IMAGE_CLOSE + ct.NL

    if not ignore_meta:
        out_html += sch.PM_POST_LIST_BLOG_ENTRY_STICKY_OPEN + ct.NL
    else:
        out_html += sch.PM_POST_LIST_BLOG_ENTRY_OPEN + ct.NL

    out_html += ct.T5 + '<h2><a href="' + post['url'] + '">' + post['title'] + '</a></h2>' + ct.NL

    if post['type'] != 'page':
        p_type = ct.PCOM_SETTINGS_TYPE_CATEGORIES
        out_html += pcom_insert_author_category_in_post_list(
                        post=post,
                        settings=settings,
                        list_meta_array=list_meta[p_type][p_type],
                        type=p_type,
                        add_escape=False,
                        no_js=True)

    p_type = ct.PCOM_SETTINGS_TYPE_AUTHORS
    out_html += pcom_insert_author_category_in_post_list(
                        post=post,
                        settings=settings,
                        list_meta_array=list_meta[p_type][p_type],
                        type=p_type,
                        add_escape=False,
                        no_js=True)

    out_html += ct.T5 + '<p>' + extract.replace('\n','<br/>') + '</p>' + ct.NL

    out_html += sch.PM_POST_LIST_BLOG_ENTRY_CLOSE + ct.NL
    out_html += sch.PM_POST_LIST_POST_CONTENT_CLOSE

    return out_html

# creates category, author etc  element for main info page list
def pcom_create_info_list_entry(entry,url,settings,list_end,no_js=False):

    next_entry = "'"
    if not list_end:
        next_entry = "',"

    js_escape = ct.JS_ESCAPE
    if no_js:
        js_escape = ''

    entry_name = sp.pcom_replace_quotes(entry['name'])
    entry_name_alt = entry['name'].replace("'","-").replace(" ","-")
    description = sp.pcom_replace_quotes(entry['description'])

    out_html = "'" + js_escape + ct.NL
    out_html += sch.PM_POST_LIST_POST_CONTENT_OPEN + js_escape + ct.NL
    out_html += sch.PM_POST_LIST_POST_IMAGE_OPEN + js_escape + ct.NL

    if not entry['thumbnail']:
        entry['thumbnail'] = sch.PM_DEFAULT_THUMBNAIL_IMAGE_LINK

    out_html += ct.T4 + '<a href="' + url + '">' + js_escape + ct.NL
    out_html += ct.T5 + '<img src="' + entry['thumbnail'] + '" alt="' + entry_name_alt + '"  />' + js_escape + ct.NL
    out_html += sch.PM_POST_LIST_POST_IMAGE_CLOSE + js_escape + ct.NL
    out_html += sch.PM_POST_LIST_BLOG_ENTRY_OPEN + js_escape + ct.NL
    out_html += ct.T5 + '<h2><a href="' + url + '">' + entry_name + '</a></h2>' + js_escape + ct.NL
    out_html += ct.T5 + '<p>' + description.replace('\n','<br/>') + '</p>' + js_escape + ct.NL
    out_html += sch.PM_POST_LIST_BLOG_ENTRY_CLOSE + js_escape + ct.NL
    out_html += sch.PM_POST_LIST_POST_CONTENT_CLOSE + next_entry + ct.NL

    return out_html

def pcom_create_template_search_list_entry(entry,url,settings):

    entry_name = sp.pcom_replace_quotes(entry['name'])
    entry_name_alt = entry['name'].replace("'","-").replace(" ","-")
    description = sp.pcom_replace_quotes(entry['description'])

    out_html = ''
    out_html += sch.PM_POST_LIST_POST_CONTENT_OPEN + ct.NL
    out_html += sch.PM_POST_LIST_POST_IMAGE_OPEN + ct.NL

    if not entry['thumbnail']:
        entry['thumbnail'] = sch.PM_DEFAULT_THUMBNAIL_IMAGE_LINK

    out_html += ct.T4 + '<a href="' + url + '">' + ct.NL
    out_html += ct.T5 + '<img src="' + entry['thumbnail'] + '" alt="' + entry_name_alt + '"  />' + ct.NL
    out_html += sch.PM_POST_LIST_POST_IMAGE_CLOSE + ct.NL
    out_html += sch.PM_POST_LIST_BLOG_ENTRY_OPEN + ct.NL
    out_html += ct.T5 + '<h2><a href="' + url + '">' + entry_name + '</a></h2>' + ct.NL
    out_html += ct.T5 + '<p>' + description.replace('\n','<br/>') + '</p>' + ct.NL
    out_html += sch.PM_POST_LIST_BLOG_ENTRY_CLOSE + ct.NL
    out_html += sch.PM_POST_LIST_POST_CONTENT_CLOSE

    return out_html

def pcom_create_archive_entry(entry,base_name,settings):

    out_html = sch.PM_TEMPLATE_ARCHIVE_MAIN_LINK_FORMAT
    out_html = out_html.replace(sch.PM_ARCHIVE_BASE,base_name)
    out_html = out_html.replace(sch.PM_ARCHIVE_BASE_SUB,entry['name'])

    out_html += ct.JS_ESCAPE + ct.NL

    return out_html

# creates category, author etc  element for main info page list
def pcom_insert_author_category_in_post_list(post,settings,list_meta_array,type,add_escape=False,no_js=False):

    out_html = ''
    delimiter = ',&nbsp;'
    next_meta = ''
    js_escape = ct.JS_ESCAPE
    if add_escape:
        next_meta = ct.JS_ESCAPE

    if no_js:
        js_escape = ''

    if post[type]:
        base_url = "/" + sp.pcom_create_template_fileroot(type,settings) + "/"
        out_html += sch.PM_POST_CATEGORY_META_OPEN + js_escape + ct.NL

        if type == ct.PCOM_SETTINGS_TYPE_CATEGORIES:
            out_html += ct.T5 + sch.PM_CATEGORY_ICON + js_escape + ct.NL
        if type == ct.PCOM_SETTINGS_TYPE_AUTHORS:
            out_html += ct.T5 + sch.PM_AUTHOR_ICON + js_escape + ct.NL

        for ind,entry in enumerate(post[type]):

            if ind == (len(post[type]) - 1):
                delimiter = ''

            if type == ct.PCOM_SETTINGS_TYPE_AUTHORS:
                entry = sp.pcom_find_author_full_name(entry,list_meta_array)
                entry_for_url = entry
                entry = sp.pcom_replace_quotes(entry)
                sub_url = entry_for_url.lower().replace("'","-").replace(' ','-')
            else:
                entry = sp.pcom_replace_quotes(entry)
                sub_url = entry.lower().replace("'","-").replace(' ','-')

            url = base_url + sub_url + "/"
            out_html += (ct.T5 + '<a href="' + url + '" alt="' + sub_url + '">'
                    + entry + '</a>' + delimiter + js_escape + ct.NL)

        out_html += sch.PM_POST_CATEGORY_META_CLOSE + next_meta + ct.NL


    return out_html


# ========
# QUOTE
# ========

def pcom_insert_quote_box_command(syntax,custom_class,placement,type,settings):

    body_text = ""
    ref_text = ""
    ref_link = ct.PCOM_NO_URL

    custom_class_wrap = ct.PCOM_QUOTE_WRAP_CLASS
    if custom_class != ct.PCOM_NO_ENTRY:
        custom_class_wrap = ct.PCOM_QUOTE_WRAP_CLASS + ' ' + custom_class

    args = {'open': ct.PCOM_KEYWORD_OPEN, 'close': ct.PCOM_KEYWORD_CLOSE }

    # set to keywords instead of commands
    body_command = ct.PCOM_QUOTE_BODY_KEYWORD
    ref_command = ct.PCOM_QUOTE_REF_KEYWORD
    ref_link_command = ct.PCOM_QUOTE_LINK_KEYWORD

    # initialise open and close syntax
    commands = sp.pcom_build_dictionary(gb.DEFAULT_OPEN_CLOSE_SYNTAX_OUT_ARRAY)
    commands['command'] = ''

    if syntax:

        #process syntax for body and reference (ref)
        while commands['command'] != ct.PCOM_NO_ENTRY:

            commands = sp.pcom_process_command_open_close_syntax(syntax,args)
            # filter out any custom classes - these should be applied to the top level
            command_custom = pcom_process_custom_command(commands['command'])
            # process for text and reference
            if command_custom['command'] == body_command:
                body_text = commands['command_syntax']

            if command_custom['command'] == ref_command:
                ref_text = commands['command_syntax']

            if command_custom['command'] == ref_link_command:
                # process link attributes
                ref_link = commands['command_syntax']

            #update syntax
            syntax = commands['syntax_after']

    # add tabs to body text
    body_text = sp.pcom_add_3tabs_to_content_line(body_text)
    body_text = sp.pcom_add_3tabs_to_content_line(body_text)

    # output quote
    out_html = (ct.NL + sp.pcom_open_placement_class(custom_class_wrap,placement) +
    sp.pcom_open_custom_class_div(custom_class,sch.PM_QUOTE_OPEN) )

    out_html += ct.NL + sch.PM_QUOTATION_MARKS + ct.NL
    out_html += body_text + ct.NL
    out_html += sch.PM_QUOTE_REF_OPEN
    # add in quote link if present
    if ref_link != ct.PCOM_NO_URL:
        out_html += ct.NL + ct.T5 + '<a href="' + ref_link + '">' + ref_text  + '</a>' + ct.NL
    else:
        out_html += ref_text + ct.NL

    out_html += sch.PM_QUOTE_REF_CLOSE + ct.NL
    out_html += sch.PM_QUOTE_CLOSE + ct.NL
    out_html += sp.pcom_close_placement_class(placement) + ct.NL

    return out_html


# ========
# HEADER CONTENT
# ========

def pcom_add_header_content_to_head(syntax,custom_class,placement,type,settings):

    args = {'open': ct.PCOM_KEYWORD_OPEN, 'close': ct.PCOM_KEYWORD_CLOSE }
    # initialise open and close syntax
    commands = sp.pcom_build_dictionary(gb.DEFAULT_OPEN_CLOSE_SYNTAX_OUT_ARRAY)
    commands['command'] = ''

    # only called in header
    if placement == ct.PCOM_HEADER_PLACEMENT:

        if syntax:

            #process syntax for body and reference (ref)
            while commands['command'] != ct.PCOM_NO_ENTRY:

                commands = sp.pcom_process_command_open_close_syntax(syntax,args)
                # filter out any custom classes - these should be applied to the top level
                command_custom = pcom_process_custom_command(commands['command'])
                # process for text and reference
                if command_custom['command'] == ct.PCOM_HEADER_CONTENT_KEYWORD:
                    settings['header_additions'].append(commands['command_syntax'])

                #update syntax
                syntax = commands['syntax_after']

    return settings

# ========
# FOOTER CONTENT
# ========

def pcom_add_footer_content_to_footer(syntax,custom_class,placement,type,settings):

    args = {'open': ct.PCOM_KEYWORD_OPEN, 'close': ct.PCOM_KEYWORD_CLOSE }
    # initialise open and close syntax
    commands = sp.pcom_build_dictionary(gb.DEFAULT_OPEN_CLOSE_SYNTAX_OUT_ARRAY)
    commands['command'] = ''

    # only called in footer
    if placement == ct.PCOM_FOOTER_PLACEMENT:

        if syntax:

            #process syntax for body and reference (ref)
            while commands['command'] != ct.PCOM_NO_ENTRY:

                commands = sp.pcom_process_command_open_close_syntax(syntax,args)
                # filter out any custom classes - these should be applied to the top level
                command_custom = pcom_process_custom_command(commands['command'])
                # process for text and reference
                if command_custom['command'] == ct.PCOM_FOOTER_CONTENT_KEYWORD:
                    settings['footer_additions'].append(commands['command_syntax'])

                #update syntax
                syntax = commands['syntax_after']

    return settings

# ========
# SECTION handling
# ========

def pcom_process_section_command(syntax,custom_class,placement,type,settings):

    name_args = { 'open': ct.PCOM_SECTION_NAME_OPEN, 'close': ct.PCOM_SECTION_NAME_CLOSE }
    command_args = { 'open': ct.PCOM_SECTION_SCHEMATIC_COMMAND_OPEN,
    'close': ct.PCOM_SECTION_SCHEMATIC_COMMAND_CLOSE }

    out = ''

    # condition custom_class
    if custom_class == ct.PCOM_NO_ENTRY:
        custom_class = ''
    else:
        custom_class = ' ' + custom_class

    # process schematic data for name
    section_data = sp.pcom_process_command_open_close_syntax(syntax,name_args)

    if section_data['command_found'] and section_data['command_syntax'] != ct.PCOM_NO_ENTRY:

        section_name = section_data['command_syntax']

        section_sub_tab = ''
        if placement == ct.PCOM_MAIN_PLACEMENT:
            section_sub_tab = ct.PCOM_SECTION_SIDEBAR_TAB

        # remove name and set as schematic, replace NONE strings

        schematic = section_data['command'] + section_data['syntax_after']
        schematic = schematic.replace(ct.PCOM_NO_ENTRY,'')

        if schematic == ct.PCOM_NO_ENTRY or not schematic:
            out = ct.PCOM_NO_ENTRY
        else:
            start_section = (section_sub_tab + '<div id="' + section_name + '"' +
            sch.PM_ADD_SECTION_CLASS + custom_class + '">' + ct.NL)

            out += start_section + ct.NL

            # set command data array
            schematic_commands = sp.pcom_build_dictionary(gb.DEFAULT_GET_FIRST_COMMAND_OUTPUTS)
            schematic_commands['next_command'] = ""

            # loop over schematic data
            while schematic_commands['next_command'] != ct.PCOM_NO_ENTRY:
                schematic_commands = sp.pcom_get_first_command(schematic,command_args)
                syntax,settings = pcom_command_selection(
                                        command=schematic_commands['command'],
                                        syntax=schematic_commands['command_syntax'],
                                        placement=placement,
                                        type=type,
                                        settings=settings)

                schematic = schematic_commands['next_command']
                # append to out data
                command = schematic_commands['command']
                syntax = sp.pcom_add_tab_to_content_line(syntax)
                out += syntax + ct.NL

            # close div
            out += section_sub_tab + '</div><!-- end of section -->' + ct.NL

    return out,settings

# ========
# RAW CONTENT - no filtering of content or adding any div wrappers
# ========

def pcom_add_raw_content_command(syntax,custom_class,placement,type,settings):

    args = {'open': ct.PCOM_SUB_COMMAND_OPEN, 'close': ct.PCOM_SUB_COMMAND_CLOSE }
    # initialise open and close syntax
    commands = sp.pcom_build_dictionary(gb.DEFAULT_OPEN_CLOSE_SYNTAX_OUT_ARRAY)
    commands['command'] = ''

    out_html = ''

    if syntax:

        #process syntax text subcommand
        while commands['command'] != ct.PCOM_NO_ENTRY:

            commands = sp.pcom_process_command_open_close_syntax(syntax,args)
            # filter out any custom classes - these should be applied to the top level
            command_custom = pcom_process_custom_command(commands['command'])
            # process for text and reference
            if command_custom['command'] == ct.PCOM_RAW_CONTENT_TEXT_SUBCOMMAND:
                out_html = commands['command_syntax']

            #update syntax
            syntax = commands['syntax_after']

    return out_html
