# elements that output html
from libraries import globals as gb
from libraries import constants as ct
from libraries import schematics as sch
from libraries import meta_defaults as md
from libraries import string_processes as sp

#
import json

json_simple = 'no_array'
json_nested = 'nested'
#
def pcom_process_meta_syntax(syntax):

    out_html = ct.PCOM_NO_ENTRY

    # keywords all start with KEYWORD={
    # search for ={ in meta
    meta = sp.pcom_build_dictionary(gb.DEFAULT_PAGE_META)

    title_string = md.DEFAULT_PAGE_TITLE
    description_string = md.DEFAULT_PAGE_DESCRIPTION
    author_string = md.DEFAULT_AUTHOR
    categories_string = md.DEFAULT_CATEGORY
    thumb_link = sch.PM_DEFAULT_THUMBNAIL_IMAGE_LINK
    extract_string = ''
    url_string = ''
    unlisted = False
    sticky_set = ct.PCOM_NO_ENTRY

    args = {'open': ct.PCOM_KEYWORD_OPEN,'close': ct.PCOM_KEYWORD_CLOSE}

    # initialise open and close syntax
    commands = sp.pcom_build_dictionary(gb.DEFAULT_OPEN_CLOSE_SYNTAX_OUT_ARRAY)
    commands['command'] = ''

    #loop over keywords
    while commands['command'] != ct.PCOM_NO_ENTRY:

        commands = sp.pcom_process_command_open_close_syntax(syntax,args)

        # if title is present - update settings
        if commands['command'] == ct.PCOM_META_TITLE:
            title_string = commands['command_syntax'].rstrip().lstrip()

        if commands['command'] == ct.PCOM_META_CATEGORIES:
            categories_string = commands['command_syntax'].rstrip().lstrip()

        if commands['command'] == ct.PCOM_META_AUTHOR:
            author_string = commands['command_syntax'].rstrip().lstrip()

        if commands['command'] == ct.PCOM_META_DESCRIPTION:
            description_string = commands['command_syntax'].rstrip().lstrip()

        if commands['command'] == ct.PCOM_META_EXTRACT:
            extract_string = commands['command_syntax'].rstrip().lstrip()

        if commands['command'] == ct.PCOM_META_THUMBNAIL:
            thumb_link = commands['command_syntax'].rstrip().lstrip()

        if commands['command'] == ct.PCOM_META_URL:
            url_string = commands['command_syntax'].rstrip().lstrip()

        if commands['command'] == ct.PCOM_META_UNLISTED:
            unlisted = True

        if commands['command'] == ct.PCOM_META_STICKY:
            sticky_set = ct.PCOM_META_STICKY

        # update syntax
        syntax = commands['syntax_after']

    # check strings
    #
    if title_string != ct.PCOM_NO_ENTRY and url_string != ct.PCOM_NO_ENTRY:
        meta['page_title'] = title_string

        if categories_string != md.DEFAULT_CATEGORY:
            meta['categories'] = categories_string

        if author_string != md.DEFAULT_AUTHOR:
            meta['authors'] = author_string

        if description_string != ct.PCOM_NO_ENTRY:
            meta['page_description'] = description_string

        if extract_string:
            meta['page_extract'] = extract_string

        if url_string:
            meta['url'] = url_string

        if thumb_link != ct.PCOM_NO_ENTRY:
            meta['thumb_link'] = thumb_link

        if sticky_set != ct.PCOM_NO_ENTRY:
            meta['sticky'] = sticky_set

        if unlisted != ct.PCOM_NO_ENTRY:
            meta['unlisted'] = unlisted

        meta['meta_valid'] = ct.PCOM_META_VALID

    return meta


def pcom_process_settings_meta_syntax(syntax,settings):

    args = {'open': ct.PCOM_KEYWORD_OPEN,'close': ct.PCOM_KEYWORD_CLOSE}

    # initialise open and close syntax
    commands = sp.pcom_build_dictionary(gb.DEFAULT_OPEN_CLOSE_SYNTAX_OUT_ARRAY)
    commands['command'] = ''

    #loop over keywords
    while commands['command'] != ct.PCOM_NO_ENTRY:

        commands = sp.pcom_process_command_open_close_syntax(syntax,args)

        # if posts_per_page is present - update settings
        if commands['command'] == ct.PCOM_META_POSTS_PER_PAGE:
            posts_per_page = commands['command_syntax'].rstrip().lstrip()
            # convert to integer and limit to 1
            posts_per_page = int(posts_per_page)
            if posts_per_page < 1:
                posts_per_page = 1

            settings['posts_per_page'] = posts_per_page

        if commands['command'] == ct.PCOM_META_DATE_FORMAT:
            settings['date_format'] = commands['command_syntax'].rstrip().lstrip()

        if commands['command'] == ct.PCOM_META_TITLE:
            if commands['command_syntax'] != '':
                settings['site_title'] = commands['command_syntax'].rstrip().lstrip()

        if commands['command'] == ct.PCOM_META_DESCRIPTION:
            if commands['command_syntax'] != '':
                settings['site_description'] = commands['command_syntax'].rstrip().lstrip()

        if commands['command'] == ct.PCOM_META_CATEGORIES:
            updates,error = sp.pcom_process_json(commands['command_syntax'].rstrip().lstrip())
            if error != ct.PCOM_JSON_LOAD_ERROR:
                settings['category_info'] = updates
            else:
                settings['category_info'] = { 'name': ct.PCOM_JSON_LOAD_ERROR }

        if commands['command'] == ct.PCOM_META_AUTHOR:
            updates,error = sp.pcom_process_json(commands['command_syntax'].rstrip().lstrip())
            if error != ct.PCOM_JSON_LOAD_ERROR:
                settings['author_info'] = updates
            else:
                settings['author_info'] = { 'name': ct.PCOM_JSON_LOAD_ERROR }

        if commands['command'] == ct.PCOM_META_TEMPLATE_TYPES:
            updates,error = sp.pcom_process_json(commands['command_syntax'].rstrip().lstrip())
            if error != ct.PCOM_JSON_LOAD_ERROR:
                settings['template_types'] = \
                pcom_update_json_based_settings(settings['template_types'],updates,json_simple)

        if commands['command'] == ct.PCOM_META_TEMPLATE_MAIN_HEADER_TEXT:
            updates,error = sp.pcom_process_json(commands['command_syntax'].rstrip().lstrip())
            if error != ct.PCOM_JSON_LOAD_ERROR:
                settings['template_main_header_text'] = \
                pcom_update_json_based_settings(settings['template_main_header_text'],updates,json_simple)

        if commands['command'] == ct.PCOM_META_TEMPLATE_SUB_HEADER_TEXT:
            updates,error = sp.pcom_process_json(commands['command_syntax'].rstrip().lstrip())
            if error != ct.PCOM_JSON_LOAD_ERROR:
                settings['template_sub_header_text'] = \
                pcom_update_json_based_settings(settings['template_sub_header_text'],updates,json_simple)

        if commands['command'] == ct.PCOM_META_TEMPLATE_SUB_HEADER_BACK_LINK_TEXT:
            updates,error = sp.pcom_process_json(commands['command_syntax'].rstrip().lstrip())
            if error != ct.PCOM_JSON_LOAD_ERROR:
                settings['template_sub_header_back_link_text'] = \
                pcom_update_json_based_settings(settings['template_sub_header_back_link_text'],updates,json_simple)

        if commands['command'] == ct.PCOM_META_TEMPLATE_SEARCH_CONTENT:
            updates,error = sp.pcom_process_json(commands['command_syntax'].rstrip().lstrip())
            if error != ct.PCOM_JSON_LOAD_ERROR:
                settings['template_search_content'] = \
                pcom_update_json_based_settings(settings['template_search_content'],updates,json_nested)

        if commands['command'] == ct.PCOM_META_DEFAULT_AUTHOR:
            updates,error = sp.pcom_process_json(commands['command_syntax'].rstrip().lstrip())
            if error != ct.PCOM_JSON_LOAD_ERROR:
                settings['default_author'] = \
                pcom_update_json_based_settings(settings['default_author'],updates,json_simple)

        if commands['command'] == ct.PCOM_CONTENT_META_POST_SETTINGS_DEFAULT:
            settings['default_content_post_meta'] = commands['command_syntax'].rstrip().lstrip()

        if commands['command'] == ct.PCOM_CONTENT_META_PAGE_SETTINGS_DEFAULT:
            settings['default_content_page_meta'] = commands['command_syntax'].rstrip().lstrip()

        if commands['command'] == ct.PCOM_META_SEARCH_API_URL:
            settings['search_api_url'] = commands['command_syntax'].rstrip().lstrip()

        if commands['command'] == ct.PCOM_META_DEFAULT_THUMB_LINK:
            if commands['command_syntax'] != ct.PCOM_NO_ENTRY:
                settings['default_thumb_link'] = commands['command_syntax'].rstrip().lstrip()

        # update syntax
        syntax = commands['syntax_after']

    return settings


def pcom_update_json_based_settings(settings_element,updates,json_type):

    if updates:

        if json_type == json_simple:
            for k,v in settings_element.items():
                if k in updates:
                    settings_element[k] = updates[k]

        if json_type == json_nested:
            # used for template search
            for k,v in settings_element.items():
                if k in updates:
                    for kk,vv in settings_element[k].items():
                        if kk in updates[k]:
                            settings_element[k][kk] = updates[k][kk]

    return settings_element
