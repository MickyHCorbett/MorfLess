# globals
from libraries import constants as ct
from libraries import schematics as sch
from libraries import meta_defaults as md

# defines the output file
# change the value to suit language

DEFAULT_TEMPLATE_TYPES = { ct.PCOM_SETTINGS_TYPE_SEARCH: 'search',
ct.PCOM_SETTINGS_TYPE_CATEGORIES: 'categories',
ct.PCOM_SETTINGS_TYPE_AUTHORS: 'authors',
ct.PCOM_SETTINGS_TYPE_ARCHIVE: 'archive',
ct.PCOM_SETTINGS_TYPE_POSTS: 'posts'
}

DEFAULT_TEMPLATE_SEARCH_CONTENT = {\
    ct.PCOM_SETTINGS_TYPE_CATEGORIES: {
        'name': ct.PCOM_SETTINGS_TYPE_CATEGORIES.capitalize(),
        'thumbnail': '/images/Polimorf-shapes-background-orange.jpg',
        'description': 'Posts listed by category'
    },
    ct.PCOM_SETTINGS_TYPE_AUTHORS: {
        'name': ct.PCOM_SETTINGS_TYPE_AUTHORS.capitalize(),
        'thumbnail': '/images/Polimorf-shapes-background-yellow.jpg',
        'description': 'Posts and pages listed by author'
    },
    ct.PCOM_SETTINGS_TYPE_ARCHIVE: {
        'name': ct.PCOM_SETTINGS_TYPE_ARCHIVE.capitalize(),
        'thumbnail': '/images/Polimorf-shapes-background-black.jpg',
        'description': 'Monthly archives arranged by most recent to older'
    },
    ct.PCOM_SETTINGS_TYPE_POSTS: {
        'name': ct.PCOM_SETTINGS_TYPE_POSTS.capitalize(),
        'thumbnail': '/images/Polimorf-shapes-background-darkblue.jpg',
        'description': 'Posts by various authors and in various categories'
    },
    'index': {
        'name': 'Home',
        'thumbnail': sch.PM_DEFAULT_THUMBNAIL_IMAGE_LINK,
        'description': 'Welcome to the site! Feel free to browse around and follow the links to other pages and posts'
    },
    '404': {
        'name': 'Not Found',
        'thumbnail': sch.PM_DEFAULT_THUMBNAIL_IMAGE_LINK,
        'description': "When you can't find anything you end up here!"
    }
}

DEFAULT_TEMPLATE_MAIN_HEADER_TEXT={ ct.PCOM_SETTINGS_TYPE_SEARCH: "Results for: ",
ct.PCOM_SETTINGS_TYPE_CATEGORIES: "Categories",
ct.PCOM_SETTINGS_TYPE_AUTHORS: "Authors",
ct.PCOM_SETTINGS_TYPE_ARCHIVE: "Monthly Archives",
ct.PCOM_SETTINGS_TYPE_POSTS: "Posts"
}

DEFAULT_TEMPLATE_SUB_HEADER_TEXT = {
ct.PCOM_SETTINGS_TYPE_CATEGORIES: "Posts for Category: ",
ct.PCOM_SETTINGS_TYPE_AUTHORS: "Posts by author: ",
ct.PCOM_SETTINGS_TYPE_ARCHIVE: "Posts updated on: "
}

DEFAULT_TEMPLATE_SUB_HEADER_BACK_LINK_TEXT = {
ct.PCOM_SETTINGS_TYPE_CATEGORIES: "Back to Categories",
ct.PCOM_SETTINGS_TYPE_AUTHORS: "Back to Authors",
ct.PCOM_SETTINGS_TYPE_ARCHIVE: "Back to Archives"
}
DEFAULT_CONTENT_POST_META = ['title',
'category',
'author',
'date_created',
'date_modified',
'show_time']

DEFAULT_CONTENT_PAGE_META = {'title': True,
'author': True,
'date_created': True,
'date_modified': True}

DEFAULT_SETTINGS = {'site_title': md.DEFAULT_SITE_TITLE,
'site_description': md.DEFAULT_SITE_DESCRIPTION,
'page_description': md.DEFAULT_PAGE_DESCRIPTION,
'page_extract': ct.PCOM_NO_ENTRY,
'date_format': ct.PCOM_UK_DATE_FORMAT,
'posts_per_page': ct.PCOM_META_POSTS_PER_PAGE_DEFAULT,
'default_header': sch.PM_HEADER_SCHEMATIC,
'default_footer': sch.PM_FOOTER_SCHEMATIC,
'default_sidebar': '',
'default_before': '',
'default_after': '',
'default_main': '',
'default_header_additions': [],
'default_footer_additions': [],
'header_additions': [],
'footer_additions': [],
'add_settings_to_dependencies': [],
'current_file': ct.PCOM_NO_ENTRY,
'category_info': {},
'author_info': {},
'content_meta_info': {},
'sticky': '',
'search_api_url': '',
'private_link_api_url': '',
'template_types': DEFAULT_TEMPLATE_TYPES,
'template_main_header_text': DEFAULT_TEMPLATE_MAIN_HEADER_TEXT,
'template_sub_header_text': DEFAULT_TEMPLATE_SUB_HEADER_TEXT,
'template_sub_header_back_link_text': DEFAULT_TEMPLATE_SUB_HEADER_BACK_LINK_TEXT,
'default_content_post_meta': DEFAULT_CONTENT_POST_META,
'default_content_page_meta': DEFAULT_CONTENT_PAGE_META,
'template_search_content': DEFAULT_TEMPLATE_SEARCH_CONTENT,
'postlist_present': False
}

DEFAULT_SCHEMATICS = { 'meta': ct.PCOM_NO_ENTRY,
'header': ct.PCOM_NO_ENTRY,
'before': ct.PCOM_NO_ENTRY,
'main': ct.PCOM_NO_ENTRY,
'after': ct.PCOM_NO_ENTRY,
'sidebar': ct.PCOM_NO_ENTRY,
'footer': ct.PCOM_NO_ENTRY,
'sidebar_found': False,
'before_found': False,
'after_found': False}

DEFAULT_PAGE_META = {'page_title': md.DEFAULT_PAGE_TITLE,
'page_description': md.DEFAULT_PAGE_DESCRIPTION,
'authors': md.DEFAULT_AUTHOR,
'categories': md.DEFAULT_CATEGORY,
'thumb_link': sch.PM_DEFAULT_THUMBNAIL_IMAGE_LINK,
'page_extract': '',
'url': '',
'meta_valid': ct.PCOM_META_NOT_VALID,
'sticky': '',
'unlisted': False}

DEFAULT_CATEGORY = {'name': md.DEFAULT_CATEGORY,
'thumbnail': sch.PM_DEFAULT_THUMBNAIL_IMAGE_LINK,
'description': ''}

DEFAULT_AUTHOR = {'name': md.DEFAULT_AUTHOR,
'shortname': md.DEFAULT_AUTHOR,
'thumbnail': sch.PM_DEFAULT_THUMBNAIL_IMAGE_LINK,
'description': ''}

DEFAULT_STRING_SEPARATOR = {'command_found': False,
'syntax_before': ct.PCOM_NO_ENTRY,
'syntax_after': ct.PCOM_NO_ENTRY}

# header and footer custom classes
HEADER_CUSTOM_CLASS = 'header-class'
FOOTER_CUSTOM_CLASS = ''

DEFAULT_GET_FIRST_COMMAND_ARGS = { 'open': ct.PCOM_SCHEMATIC_COMMAND_OPEN,
'close': ct.PCOM_SCHEMATIC_COMMAND_CLOSE }

DEFAULT_GET_FIRST_COMMAND_OUTPUTS = {'command': ct.PCOM_NO_ENTRY,
'command_syntax': ct.PCOM_NO_ENTRY,
'next_command': ct.PCOM_NO_ENTRY}

DEFAULT_OPEN_CLOSE_SYNTAX_ARGS = { 'open': ct.PCOM_SUB_COMMAND_OPEN, 'close': ct.PCOM_SUB_COMMAND_CLOSE }

DEFAULT_OPEN_CLOSE_SYNTAX_OUT_ARRAY = { 'command_found': False,
'command': ct.PCOM_NO_ENTRY,
'command_syntax': ct.PCOM_NO_ENTRY,
'syntax_after': ct.PCOM_NO_ENTRY }

DEFAULT_MENU_COMMAND_MLK_KEYWORD_ATTRIBUTES = { 'href': ct.PCOM_NO_ENTRY,
'name': ct.PCOM_NO_ENTRY,
'src': ct.PCOM_NO_ENTRY,
'class': ct.PCOM_NO_ENTRY,
'fa': ct.PCOM_NO_ENTRY
}

DEFAULT_LOGO_ATTRIBUTES = {
'src': 'src'
}


# command functions list - global is predefined as empty in pcom_defaults
COMMAND_LIST = { ct.PCOM_DEFAULT_COMMAND: 'pcom_use_defaults',
ct.PCOM_NAV_COMMAND: 'pcom_process_nav_command',
ct.PCOM_MENU_COMMAND:'pcom_process_menu_command',
ct.PCOM_QUOTE_COMMAND:'pcom_insert_quote_box_command',
ct.PCOM_CONTENT_COMMAND:'pcom_add_content_command',
ct.PCOM_CONTENT_META_COMMAND:'pcom_add_content_meta_command',
ct.PCOM_POST_LIST_COMMAND:'pcom_add_post_list_command',
ct.PCOM_SECTION_COMMAND:'pcom_process_section_command',
ct.PCOM_INSERT_COMMAND:'pcom_process_insert_command',
ct.PCOM_INSERT_PAGINATION_COMMAND:'pcom_insert_pagination_command',
ct.PCOM_INSERT_SEARCHBAR_COMMAND:'pcom_insert_searchbar_command',
ct.PCOM_INSERT_STYLING_COMMAND:'pcom_insert_styling_command'}

# addition functions list - global is predefined as empty in pcom_defaults
ADDITIONS_LIST = { ct.PCOM_INSERT_STYLESHEET_REF_COMMAND:'pcom_insert_stylesheet_reference',
ct.PCOM_HEADER_CONTENT_COMMAND:'pcom_add_header_content_to_head',
ct.PCOM_FOOTER_CONTENT_COMMAND:'pcom_add_footer_content_to_footer',
ct.PCOM_INSERT_ADDITIONS_COMMAND:'pcom_process_insert_additions_command' }
