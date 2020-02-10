# string parsing and processing functions
from libraries import globals as gb
from libraries import constants as ct
from libraries import schematics as sch

from collections import OrderedDict
import json, re

def pcom_process_json(json_data):

    out_data = ct.PCOM_NO_ENTRY
    error = ''

    if json_data != ct.PCOM_NO_ENTRY:
        try:
            out_data = json.loads(json_data,encoding='utf-8',object_pairs_hook=OrderedDict)
        except:
            error = ct.PCOM_JSON_LOAD_ERROR

    return out_data, error

def pcom_write_json(json_data):

    out = json.dumps(json_data,indent=4)

    return out

def pcom_create_url(file,meta):

    type = 'post'
    # check for index or 404 pages and return NONE
    if file == "index.page":
        outkey = '/'
        type = 'page'
    elif file == "404.page":
        outkey = '404.html'
        type = 'page'
    else:
        if meta['url']:
            outkey = meta['url']
            if file.find('.page') > -1:
                type = 'page'
        else:
            outkey = '/' + file.lower().replace(".post","").replace(".page","") + '/'
            if file.find('.page') > -1:
                type = 'page'

    return outkey,type

def pcom_create_template_search_content_url(file,settings):

    url = "/"
    fileroot = ''
    if file.lower().find('.page') > -1:
        fileroot = file.replace('.page','')

    if fileroot:
        if fileroot == "index":
            url = '/'
        elif fileroot == "404":
            url = '404.html'
        elif fileroot in settings['template_search_content']:
            url = '/' + pcom_create_template_fileroot(fileroot,settings) + '/'

    return url

def pcom_filter_template(fileroot,settings):

    is_template = False
    is_search = False
    for k,v in settings['template_types'].items():
        if fileroot == k or fileroot == v:
            is_template = True
            if k == ct.PCOM_SETTINGS_TYPE_SEARCH:
                is_search = True
            break

    return is_template,is_search

def pcom_check_root(fileroot):

    is_root= False

    if fileroot == 'index' or fileroot == '404':
        is_root = True

    return is_root

def pcom_create_template_fileroot(fileroot,settings):
    fileroot_out = fileroot
    for k,v in settings['template_types'].items():
        if fileroot == k:
            fileroot_out = v.lower()

    return fileroot_out

def pcom_get_template_key(fileroot,settings):
    key = fileroot.replace("/","_")
    for k,v in settings['template_types'].items():
        if fileroot == k or fileroot == v:
            key = k.lower()
            break

    return key

def pcom_replace_quotes(text):

    if text.find(ct.PCOM_META_IGNORE_QUOTES) > -1:
        text = text.replace(ct.PCOM_META_IGNORE_QUOTES,'')
    else:
        text = text.replace("'",ct.JS_APOS_REPLACE)
        text = text.replace('"',ct.JS_QUOTE_REPLACE)

    return text

def pcom_find_author_full_name(name,authors):
    # if 'name' is in the array it means there is an error
    if 'name' not in authors:
        for author in authors:
            if name.lower() == author['name'].lower() or name.lower() == author['shortname'].lower():
                name = author['name']

    return name
#
# Separates a string at separator. Strings can be raw or trimmed
# Returns an array with both strings and a boolean
# If none found it returns the string and sets the syntax after to
# no entry
#
#

def pcom_get_strings_syntax_separator(syntax,separator,trim):
    # returns commands before separator and after
    # set out_array to default - command_found = false
    out_array = pcom_build_dictionary(gb.DEFAULT_STRING_SEPARATOR)
    # find position of separator
    if syntax.find(separator) > -1:
        out_array['command_found'] = True
        # get data
        split_array = syntax.split(separator,1) # splits into before and after
        # create trimmed values for checks
        before = split_array[0].rstrip().lstrip()
        after = split_array[1].rstrip().lstrip()
        # set out array
        if trim == True:
            # remove leading and trailing whitespace
            split_array[0] = before
            split_array[1] = after

        # check for no data
        if not before:
            out_array['syntax_before'] = ct.PCOM_NO_ENTRY
        else:
            out_array['syntax_before'] = split_array[0]

        if not after:
            out_array['syntax_after'] = ct.PCOM_NO_ENTRY
        else:
            out_array['syntax_after'] = split_array[1]

    else:
        out_array['command_found'] = False
        out_array['syntax_before'] = syntax
        out_array['syntax_after'] = ct.PCOM_NO_ENTRY

    return out_array

# ----- -----
#
# Function gets first command -
# returns array of command command syntax
#
def pcom_get_first_command(format,args):
    # check args - default is schematic commands
    # can be used for inserts as well
    out_array = pcom_build_dictionary(gb.DEFAULT_GET_FIRST_COMMAND_OUTPUTS)
    out_array['next_command'] = ct.PCOM_NO_ENTRY

    # only execute for non empty format
    if format:
        # search for command end
        command_close = pcom_get_strings_syntax_separator(format,args['close'],True)

        if command_close['command_found']:
            #search for command open
            string_start = command_close['syntax_before']
            string_remain = command_close['syntax_after']
            command_open = pcom_get_strings_syntax_separator(string_start,args['open'],True)

            if command_open['command_found']:
                out_array['command'] = command_open['syntax_after']
                #retrieve syntax - search for next command open
                get_syntax = pcom_get_strings_syntax_separator(string_remain,args['open'],True)
                out_array['command_syntax'] = get_syntax['syntax_before']
                string_remain = get_syntax['syntax_after']

                # if next command found - add open schematic to syntax after
                # so it will be recognised on the next call of the function
                if get_syntax['command_found']:
                    out_array['next_command'] = args['open'] + string_remain

    return out_array

#
# Separates command and syntax using the format
# COMMAND <open identifier>SYNTAX<close identifier> SYNTAX AFTER
# Default is open and close identifiers for subcommands


def pcom_process_command_open_close_syntax(syntax,args):
    # used with a series of commands
    #
    # define args
    # default are SUB_COMMAND
    args_used = pcom_build_dictionary(gb.DEFAULT_OPEN_CLOSE_SYNTAX_ARGS)
    # initialise array - command found, command, command syntax, syntax after
    out_array = pcom_build_dictionary(gb.DEFAULT_OPEN_CLOSE_SYNTAX_OUT_ARRAY)

    # condition input
    if not (args):
         args = args_used
    #
    args_used['open'] = args['open']
    args_used['close'] = args['close']

    if (syntax != ct.PCOM_NO_ENTRY):
        # find command start
        commands = pcom_get_strings_syntax_separator(syntax,args_used['close'],True)
        # if command end found
        if commands['command_found']:
            # set output string as remaining keyword commands
            temp_after = commands['syntax_after']
            # process syntax before command end
            commands = pcom_get_strings_syntax_separator(commands['syntax_before'],args_used['open'],True)
            if commands['command_found']:
                out_array['command_found'] = True
                out_array['command'] = commands['syntax_before']
                out_array['command_syntax'] = commands['syntax_after']
                out_array['syntax_after'] = temp_after

    else:
        out_array['command'] = ct.PCOM_NO_ENTRY

    return out_array


# creates text lines from array elements

def pcom_create_html_from_array(array):
    out_html = ''
    for insert in array:
        if insert != ct.PCOM_NO_ENTRY:
            out_html += insert + ct.NL

    return out_html

def pcom_remove_empty_lines(content):
    line_array = content.splitlines(True)
    out_html = ''
    for insert in line_array:
        #remove tabs
        insert_stripped = insert.replace(ct.T1,'')
        if insert_stripped != ct.NL:
            out_html += insert

    return out_html

def pcom_build_dictionary(data_in):
    # copies a dictionary
    out_dict = {}
    for key, val in data_in.items():
        dict2 = {key: val}
        out_dict.update(dict2)

    return out_dict

def pcom_add_tab_to_content_line(content):
    out_content_array = content.splitlines(True)
    out_content = ''

    for line in out_content_array:
        out_content += ct.T1 + line

    return out_content

def pcom_add_2tabs_to_content_line(content):
    out_content_array = content.splitlines(True)
    out_content = ''

    for line in out_content_array:
        out_content += ct.T2 + line

    return out_content

def pcom_add_3tabs_to_content_line(content):
    out_content_array = content.splitlines(True)
    out_content = ''

    for line in out_content_array:
        out_content += ct.T3 + line

    return out_content
#
# Creates a menu list entry for a menu
# In the nav bar or anywhere else
#
#
def pcom_process_menu_command_mlk_keyword(command_string):

    # menu link must have href and name otherwise return empty string
    no_entry = ct.PCOM_NO_ENTRY
    allowed_args = {}
    default_args = pcom_build_dictionary(gb.DEFAULT_MENU_COMMAND_MLK_KEYWORD_ATTRIBUTES)
    html_string = ""
    src_found = False
    list_open_with_class = ct.T3 + """<li>"""
    list_class = ''
    html_string_start = ''
    html_string_end = ''
    out_html = ''

    # replace custom attributes
    allowed_args = pcom_process_keyword_args(command_string,default_args)
    #
    if ( ( allowed_args['href'] != no_entry ) and ( allowed_args['name'] != no_entry ) ):
        # process constants
        href = pcom_site_constants_replacement(allowed_args['href'])
        name = allowed_args['name']
        # if src found - link is an image
        if ( allowed_args['src'] != no_entry ):
            src = pcom_site_constants_replacement(allowed_args['src'])
            src_found = True

        # additional class
        if ( allowed_args['class'] != no_entry ):
            list_class = allowed_args['class']
            list_open_with_class = ct.T3 + '<li class="' + list_class + ' clearfix-small">'

        # Font Awesome icon - adds to or replaces image src
        if ( allowed_args['fa'] != no_entry ):
            fa = allowed_args['fa']
            # set image src true - icon may be only image
            src_found = True
            # create icon - append to src
            src = src + sch.PM_FA_ICON_OPEN + fa + sch.PM_FA_ICON_CLOSE

        #
        html_string_start = list_open_with_class + sch.PM_NAV_MENU_LINK_HTML_1
        html_string_start += href + sch.PM_NAV_MENU_LINK_HTML_2 + name + sch.PM_NAV_MENU_LINK_HTML_3
        # add img or text
        if ( src_found == True ):
            html_string_end = sch.PM_NAV_MENU_IMG_LINK_HTML_1 + src + sch.PM_NAV_MENU_IMG_LINK_HTML_2
            html_string_end += name + sch.PM_NAV_MENU_IMG_LINK_HTML_3 + sch.PM_NAV_MENU_LINK_HTML_4
        else:
            html_string_end = name + sch.PM_NAV_MENU_LINK_HTML_4

    out_html = html_string_start + html_string_end

    return out_html

#
# Add logo to nav
# Accommodates for custom attributes
#
#
def pcom_process_logo_for_nav(syntax, site_title):
    #
    out_html = ''
    img_attributes = pcom_build_dictionary(gb.DEFAULT_LOGO_ATTRIBUTES)
    #
    if syntax != ct.PCOM_NO_ENTRY:
        img_attributes = pcom_process_keyword_args(syntax,img_attributes);
        # process for remote attributes - if not present process shortcuts
        src = img_attributes['src']
        # create logo html
        if src != ct.PCOM_NO_ENTRY:
            out_html = (ct.T2 + sch.PM_NAV_LOGO_DIV_OPEN + ct.NL +
            ct.T3 + '<a href="/" name="' + site_title + '">' + '<img src="' + src + '" alt="'  + site_title +  '" /></a>' + ct.NL
            + ct.T2 + sch.PM_NAV_LOGO_DIV_CLOSE)

    return out_html

def pcom_add_title(syntax):
    # no attribute - text itself - trim for spaces and esc
    syntax = syntax.rstrip().lstrip()
    title_string = (ct.T2 + sch.PM_TITLE_NAV_DIV_OPEN + syntax + sch.PM_TITLE_NAV_DIV_CLOSE)

    return title_string

#
# Replaces custom attributes with actual attributes
# Allows source attributes to be written in any fashion or language
# yet be processed as allowed html attributes or command attributes
#
#
def pcom_replace_custom_attributes(syntax,custom_keys):
    # replace custom attributes with mandated ones
    for key, val in custom_keys.items():
        syntax = syntax.replace(key, val)

    return syntax

#
# Adds custom class to opening div for html element
# and returns this as a string

def pcom_open_custom_class_div(custom_class,opening_html):
    # uses the opening html to add in a custom class call if needed
    # requires the opening html have the class variable last
    out_html = ''
    if ((custom_class != ct.PCOM_NO_ENTRY) and (custom_class != '')):
        # insert custom class into div - sanitize class
        out_html = opening_html + ' ' + custom_class + sch.PM_CLOSE_DIV_WITH_COMMAS
    else:
        # no custom class
        out_html = opening_html + sch.PM_CLOSE_DIV_WITH_COMMAS

    return out_html

# creates opening outer and inner divs for full width
def pcom_open_placement_class(custom_class,placement):

    out_html = ''

    if (placement == ct.PCOM_MAIN_PLACEMENT):
        out_html = ct.NL + pcom_open_custom_class_div(custom_class,sch.PM_MAIN_OUTER_OPEN) + ct.NL
        out_html += pcom_open_custom_class_div(custom_class,sch.PM_MAIN_INNER_OPEN) + ct.NL

    return out_html

# creates opening outer and inner divs for full width
def pcom_close_placement_class(placement):

    out_html = ''

    if (placement == ct.PCOM_MAIN_PLACEMENT):
        out_html = ct.NL + sch.PM_MAIN_INNER_CLOSE + ct.NL + sch.PM_MAIN_OUTER_CLOSE

    return out_html

#
# Separates command and syntax using the format
# COMMAND <open identifier>SYNTAX<close identifier> SYNTAX AFTER
# Default is open and close identifiers for subcommands
#
#
def pcom_process_keyword_args(command_string,defaults):
    # goes through keyword syntax matching against arguments
    # returns an array of argument tags with content
    # search for first argument
    #
    keyword_args = defaults
    #
    arg_start = ct.PCOM_ATTRIBUTE_OPEN
    arg_end = ct.PCOM_ATTRIBUTE_CLOSE

    found_args = pcom_build_dictionary(gb.DEFAULT_STRING_SEPARATOR)
    found_args['syntax_after'] = ''

    if (command_string != ct.PCOM_NO_ENTRY):
        while ( found_args['syntax_after'] != ct.PCOM_NO_ENTRY ):
            found_args = pcom_get_strings_syntax_separator(command_string,arg_start,True)
            # set argument keyword
            arg_keyword = found_args['syntax_before']
            command_string = found_args['syntax_after']
            # find argument end
            end_args = pcom_get_strings_syntax_separator(command_string,arg_end,True)
            arg_detail = end_args['syntax_before']
            command_string = end_args['syntax_after']
            #
            # check if in list of allowed_args
            if arg_keyword in keyword_args:
                keyword_args[arg_keyword] = arg_detail

    return keyword_args



#
# Replaces constants with explicit links
#
#
def pcom_site_constants_replacement(content):
    # replaces SITE_HOME with blog url
    # replaces IMAGES with template_url & /images
    # used for link commands in both text and html link
    content_update = content
    site_ref_constants = { 'SITE_HOME': ct.SITE_HOME, 'IMAGES': ct.IMAGES}
    # check for customised keys
    for key, val in ct.PCOM_CUSTOM_SITE_REPLACEMENTS.items():
        content_update = content_update.replace(key, val)
    # replace with paths
    for key, val in site_ref_constants.items():
        content_update = content_update.replace(key, val)
    #
    return content_update

# add text for additions
def pcom_insert_additions_into_html(args):

    content = args['html']
    additions = args['settings']
    placement = args['placement']
    js_constant_name = args['js_name']
    fileroot = args['fileroot']
    pagination_name = args['pagination_name']
    pagination = args['pagination']
    is_template = args['is_template']
    is_search = args['is_search']

    fileroot = fileroot.replace("/","_")

    # additions are added to header or footer
    if placement == ct.PCOM_HEADER_PLACEMENT:
        start_tag = sch.HEADER_ADDITIONS_START
        end_tag = sch.HEADER_ADDITIONS_END
        list = additions['header_additions']
        tab = ct.T1

    if placement == ct.PCOM_FOOTER_PLACEMENT:
        start_tag = sch.SCRIPT_ADDITION_TAG_START
        end_tag = sch.SCRIPT_ADDITION_TAG_END
        list = additions['footer_additions']
        tab = ''

        if additions['postlist_present']:
            postlist_insert = sch.POSTLIST_SCRIPTS.replace(sch.PM_POSTLIST_PLACEHOLDER,js_constant_name)
            postlist_insert = postlist_insert.replace(sch.PM_POSTLIST_CONSTANT_PLACEHOLDER,fileroot)
            list.append(postlist_insert)

        if pagination:
            pagination_insert = sch.PAGINATION_SCRIPTS.replace(sch.PM_PAGINATION_NAME,pagination_name)
            pagination_insert = pagination_insert.replace(sch.PM_PAGINATION_CONSTANT_NAME,fileroot)
            list.append(pagination_insert)

        if is_template and not is_search:
            root = pcom_get_template_key(fileroot,additions)
            js_replacement = root + sch.PM_TEMPLATE_JS_NAME
            constant_replacement = root + sch.PM_TEMPLATE_CONSTANT_NAME
            postlist_template_insert = sch.POSTLIST_TEMPLATE_SCRIPTS.replace(sch.PM_TEMPLATE_JS_NAME,js_replacement)
            postlist_template_insert = postlist_template_insert.replace(sch.PM_TEMPLATE_CONSTANT_NAME,constant_replacement)
            list.append(postlist_template_insert)

        if is_search:
            #search_template_insert = sch.PM_SEARCHBAR_JS_INSERT.replace(sch.PM_SEARCH_API_URL,additions['search_api_url'])
            list.append(sch.PM_SEARCHBAR_JS_INSERT)

    # replace search url
    search_root = pcom_create_template_fileroot(ct.PCOM_SETTINGS_TYPE_SEARCH,additions)
    content = content.replace(sch.PM_SEARCH_NAME,search_root)

    # tags are present by design
    # find tags
    split_strings = pcom_get_strings_syntax_separator(content,start_tag,True)
    content_before = split_strings['syntax_before'].replace(start_tag,'') + ct.NL + tab + start_tag + ct.NL

    split_strings = pcom_get_strings_syntax_separator(content,end_tag,True)
    content_after = tab + end_tag + ct.NL + split_strings['syntax_after']

    # add data
    additions = pcom_create_html_from_array(list)
    if placement == ct.PCOM_HEADER_PLACEMENT:
        additions = pcom_add_tab_to_content_line(additions)

    content = content_before + additions + content_after

    return content

def pcom_get_insert_info(html_array):
    info = []

    # check for inserts
    tag_open = ct.PCOM_INSERT_TAG_OPEN
    tag_close = ct.PCOM_INSERT_TAG_CLOSE

    # scan through html array
    for ind,line in enumerate(html_array):

        found_data = pcom_get_strings_syntax_separator(line,tag_open,True)
        if found_data['command_found'] == True:
            before_insert = found_data['syntax_before']
            found_data2 = pcom_get_strings_syntax_separator(found_data['syntax_after'],tag_close,True)
            if found_data2['command_found'] == True:
                # insert syntax should include placement key as this is added programmatically
                #- if not the insert information will be ignored in processing anyway
                found_data3 = pcom_get_strings_syntax_separator(found_data2['syntax_before'],':',True)
                placement = found_data3['syntax_before']
                key_ref = found_data3['syntax_after']

                # update insert info array
                info_entry = {'filename': key_ref,
                'placement': placement,
                'index': ind,
                'valid_entry': ct.PCOM_NOT_TRIED,
                'content': ''}

                info.append(info_entry)

    return info

def pcom_get_postlists_info(html_array,fileroot):
    info = []

    # check for postlist list
    tag_open = ct.PCOM_POSTLIST_TAG_OPEN
    tag_close = ct.PCOM_POSTLIST_TAG_CLOSE

    # scan through html array
    for ind,line in enumerate(html_array):

        found_data = pcom_get_strings_syntax_separator(line,tag_open,True)
        if found_data['command_found'] == True:
            found_data2 = pcom_get_strings_syntax_separator(found_data['syntax_after'],tag_close,True)
            if found_data2['command_found'] == True:
                # split at :
                all_content = found_data2['syntax_before'].rstrip().lstrip()
                found_data3 = all_content.split(':')

                if found_data3[0] == ct.PCOM_POST_LIST_ADD_ALL_POSTS:
                    content = ct.PCOM_SETTINGS_TYPE_POSTS
                else:
                    content = found_data3[0]

                # update insert info array
                info_entry = {'index': ind,
                'fileroot': fileroot.replace("/","_"),
                'ppp': found_data3[1],
                'manual_sticky': found_data3[2],
                'content': content}

                info.append(info_entry)

    return info


def pcom_insert_postlist_wrapper(html_array,postlist_info,outlog):

    if postlist_info:
        postlist_constant = ''
        entry_end = '},'

        for ind,info in enumerate(postlist_info):

            # add entry div with postlist index
            postlist_identifier = sch.PM_POST_LIST_IDENTIFIER + str(ind+1)
            out_html = (pcom_open_custom_class_div(postlist_identifier,sch.PM_POST_LIST_DATA_OPEN)
                + ct.NL + sch.PM_POST_LIST_DATA_CLOSE
                + ct.NL + sch.PM_POSTLIST_PAGINATION_OPEN.replace(sch.PM_POSTLIST_PAGINATION_IDENT,postlist_identifier)
                + ct.NL + sch.PM_POSTLIST_PAGINATION_CLOSE
                + ct.NL)

            html_array[info['index']] = out_html

    return html_array,outlog

# content meta

def pcom_get_content_meta_info(html_array):
    info = []

    # check for postlist list
    tag_open = ct.PCOM_CONTENT_META_TAG_OPEN
    tag_close = ct.PCOM_CONTENT_META_TAG_CLOSE

    # scan through html array
    for ind,line in enumerate(html_array):

        found_data = pcom_get_strings_syntax_separator(line,tag_open,True)
        if found_data['command_found'] == True:
            found_data2 = pcom_get_strings_syntax_separator(found_data['syntax_after'],tag_close,True)
            if found_data2['command_found'] == True:
                # split at :
                content_data = found_data2['syntax_before'].rstrip().lstrip()
                content_data = content_data.split(':')

                content_meta = pcom_assign_content_meta(content_data[1])
                placement = content_data[0].rstrip().lstrip()

                # update insert info array
                info_entry = {'index': ind,
                'placement': placement,
                'title': content_meta['title'],
                'category': content_meta['category'],
                'author': content_meta['author'],
                'date_created': content_meta['date_created'],
                'date_modified': content_meta['date_modified'],
                'show_time': content_meta['show_time']}

                info.append(info_entry)

    return info

# ----

def pcom_get_comma_list(list):

    comma_list = []
    # split list at commas
    split_strings = list.split(",")
    for string in split_strings:
        comma_list.append(string.rstrip().lstrip())

    return comma_list

def pcom_assign_content_meta(content_meta_list):

    content_meta = {'title': False,
    'category': False,
    'author': False,
    'date_created': False,
    'date_modified': False,
    'show_time': False}

    # convert to array
    content_meta_list = pcom_get_comma_list(content_meta_list)

    if ct.PCOM_CONTENT_META_TITLE_KEYWORD in content_meta_list:
        content_meta['title'] = True

    if ct.PCOM_CONTENT_META_CATEGORY_KEYWORD in content_meta_list:
        content_meta['category'] = True

    if ct.PCOM_CONTENT_META_AUTHOR_KEYWORD in content_meta_list:
        content_meta['author'] = True

    if ct.PCOM_CONTENT_META_DATE_CREATED_KEYWORD in content_meta_list:
        content_meta['date_created'] = True

    if ct.PCOM_CONTENT_META_DATE_MODIFIED_KEYWORD in content_meta_list:
        content_meta['date_modified'] = True

    if ct.PCOM_CONTENT_META_SHOW_TIME_KEYWORD in content_meta_list:
        content_meta['show_time'] = True

    return content_meta

# Strip string - leaves only spaces

def pcom_strip_string(content):

    sub_for_space = '8SP8'
    sub_for_dots = 'D9D9'
    sub_for_new_line = '34NL43'
    # replace spaces
    content = content.replace(' ',sub_for_space)
    content = content.replace('.',sub_for_dots)
    content = content.replace('\n',sub_for_new_line)
    # strip
    content = ''.join(e for e in content if e.isalnum())
    # re sub spaces, dots and new line
    content = content.replace(sub_for_space,' ')
    content = content.replace(sub_for_dots,'.')
    content = content.replace(sub_for_new_line,'\n')

    return content

# =======
# RAW CONTENT - removes head and style remarks
# =======

def pcom_create_raw_content(content,meta):

    # remove head, style from html content
    head_start_end = pcom_get_strings_syntax_separator(content,"</head>",True)
    content = head_start_end['syntax_after']

    start_found = pcom_build_dictionary(gb.DEFAULT_STRING_SEPARATOR)
    start_found['syntax_after'] = ''

    while start_found['syntax_after'] != ct.PCOM_NO_ENTRY:
        start_found = pcom_get_strings_syntax_separator(content,"<style>",True)
        if start_found['command_found']:
            tags_start_end = pcom_get_strings_syntax_separator(content,"</style>",True)
            if tags_start_end['command_found']:
                # remove style content
                content = start_found['syntax_before'] + tags_start_end['syntax_after']



    # remove script content
    start_found = pcom_build_dictionary(gb.DEFAULT_STRING_SEPARATOR)
    start_found['syntax_after'] = ''
    #
    while start_found['syntax_after'] != ct.PCOM_NO_ENTRY:
        start_found = pcom_get_strings_syntax_separator(content,"<script>",True)
        if start_found['command_found']:
            tags_start_end = pcom_get_strings_syntax_separator(start_found['syntax_after'],"</script>",True)
            if tags_start_end['command_found']:
                # remove style content
                content = start_found['syntax_before'] + tags_start_end['syntax_after']


    clean_section = re.compile('<.*?>')
    raw_content = re.sub(clean_section, '', content).rstrip().lstrip()
    # remove tabs, double new lines and double spaces
    raw_content = raw_content.replace("\t","").replace("  ","").replace("\n\n","")
    # add meta
    raw_content += """\n\n""" + meta['page_title'] + """\n"""
    raw_content += meta['page_description'] + """\n"""
    raw_content += meta['page_extract'] + """\n"""

    return raw_content
