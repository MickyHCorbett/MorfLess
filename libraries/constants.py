# MorfLess v1.0
#
# Constants.py
#
# Global constants and settings used in MorfLess
#
NL = """\n"""
T1 = """  """ # 2 spaces
T2 = """    """
T3 = """      """
T4 = """        """
T5 = """          """ # 10 spaces
SITE_HOME = """/"""
IMAGES = """/images"""
PCOM_NO_ENTRY = 'NONE'
PCOM_JSON_LOAD_ERROR = 'JSON_FILE load error'
PCOM_NO_URL = 'NO_URL'
PCOM_NOT_USED = 'NOT_USED'
PCOM_NO_LOGO = 'NO_LOGO'
PCOM_SPACE = " "
PCOM_VALID_ENTRY = "VALID"
PCOM_NOT_VALID_ENTRY = "NOT_VALID"
PCOM_NOT_TRIED = "NOT_TRIED"

JS_ESCAPE = "\\"
JS_QUOTE_REPLACE = '&#34;'
JS_APOS_REPLACE = '&#39;'
#
PCOM_US_DATE_FORMAT = "US"
PCOM_UK_DATE_FORMAT = "UK"
#
PCOM_CUSTOM_CLASS_DECLARATION = '_CUSTOM:'
PCOM_SCHEMATIC_COMMAND_OPEN = """%%"""
PCOM_SCHEMATIC_COMMAND_CLOSE = '::'
PCOM_SUB_SCHEMATIC_CLOSE = ':'
PCOM_SUB_COMMAND_OPEN = '=['
PCOM_SUB_COMMAND_CLOSE = ']:'
PCOM_KEYWORD_OPEN = '={'
PCOM_KEYWORD_CLOSE = '}:'
PCOM_ATTRIBUTE_OPEN = '="'
PCOM_ATTRIBUTE_CLOSE = '"' # commas

PCOM_SECTION_NAME_OPEN = """{{"""
PCOM_SECTION_NAME_CLOSE = """}}"""
PCOM_SECTION_SCHEMATIC_COMMAND_OPEN = '[%'
PCOM_SECTION_SCHEMATIC_COMMAND_CLOSE = ':]'
PCOM_SECTION_SIDEBAR_TAB = '$$SIDEBAR_TAB%%'
#
PCOM_HEADER_PLACEMENT = 'HEADER'
PCOM_MAIN_PLACEMENT = 'MAIN'
# process main with a sidebar
PCOM_MAIN_WITH_SIDEBAR_PLACEMENT = 'MAIN_WITH_SIDEBAR'
# process sidebar
PCOM_SIDEBAR_PLACEMENT = 'WITH_SIDEBAR'
PCOM_FOOTER_PLACEMENT = 'FOOTER'
#
PCOM_BEFORE_TYPE = 'BEFORE_MAIN'
PCOM_AFTER_TYPE = 'AFTER_MAIN'
#
PCOM_SETTINGS_HEADER = 'SETTINGS_HEADER'
PCOM_SETTINGS_BEFORE = 'SETTINGS_BEFORE'
PCOM_SETTINGS_MAIN = 'SETTINGS_MAIN'
PCOM_SETTINGS_AFTER = 'SETTINGS_AFTER'
PCOM_SETTINGS_SIDEBAR = 'SETTINGS_SIDEBAR'
PCOM_SETTINGS_FOOTER = 'SETTINGS_FOOTER'

PCOM_SETTINGS_TYPE_POSTS = 'posts'
PCOM_SETTINGS_TYPE_CATEGORIES = 'categories'
PCOM_SETTINGS_TYPE_AUTHORS = 'authors'
PCOM_SETTINGS_TYPE_ARCHIVE = 'archive'
PCOM_SETTINGS_TYPE_SEARCH = 'search'

PCOM_SEARCHPAGE_SEARCHBAR_CLASS = 'pm-search-page'

PCOM_SEARCH_CONFIG_JS_NAME = 'search--config.js'

# Required json file names
PCOM_REQ_FILE_SETTINGS = 'settings.txt'
PCOM_REQ_FILE_POSTLIST = 'postlist.json'
PCOM_REQ_FILE_POSTLISTS_INFO = 'postlists_info.json'
PCOM_REQ_FILE_PAGINATION = 'pagination.json'
PCOM_REQ_FILE_CATEGORIES = 'categories.json'
PCOM_REQ_FILE_AUTHORS = 'authors.json'
PCOM_REQ_FILE_ARCHIVE = 'archive.json'
PCOM_REQ_FILE_DEPENDENCIES = 'dependencies.json'

PCOM_REQ_FILE_TEMPLATES = { PCOM_SETTINGS_TYPE_POSTS: 'posts.template',
PCOM_SETTINGS_TYPE_CATEGORIES: 'categories.template',
PCOM_SETTINGS_TYPE_AUTHORS: 'authors.template',
PCOM_SETTINGS_TYPE_ARCHIVE: 'archive.template' }

# dependency list tags
PCOM_DEPENDENCY_LIST_FILENAME = 'filename'
PCOM_DEPENDENCY_LIST_DEPS = 'dependencies'

PCOM_POSTLIST_CONSTANT_NAME_BASE = 'postlist--'

# SCHEMATIC SEPARATORS
PCOM_HEADER_SCHEMATIC_TAG = '///HEADER:'
PCOM_MAIN_SCHEMATIC_TAG = '///MAIN:'
PCOM_BEFORE_MAIN_SCHEMATIC_TAG = '///BEFORE:'
PCOM_AFTER_MAIN_SCHEMATIC_TAG = '///AFTER:'
PCOM_FOOTER_SCHEMATIC_TAG = '///FOOTER:'
PCOM_REMOTE_SCHEMATIC_TAG = '///REMOTE:'
PCOM_SIDEBAR_SCHEMATIC_TAG = '///SIDEBAR:'
#
# META tags
PCOM_META_VALID = 'META_VALID'
PCOM_META_NOT_VALID = 'META_NOT_VALID'
PCOM_META_TAG = '///META:'
PCOM_META_TITLE = 'title'
PCOM_META_CATEGORIES = 'categories'
PCOM_META_AUTHOR = 'author'
PCOM_META_DEFAULT_AUTHOR = 'default_author'
PCOM_META_DEFAULT_THUMB_LINK = 'default_thumbnail'
PCOM_META_DESCRIPTION = 'description'
PCOM_META_EXTRACT = 'extract'
PCOM_META_THUMBNAIL = 'thumbnail'
PCOM_META_STICKY = 'sticky'
PCOM_META_URL = 'url'
PCOM_META_UNLISTED = 'unlisted'
PCOM_META_TEMPLATE_TYPES = 'templates'
PCOM_META_POSTS_PER_PAGE = 'posts_per_page'
PCOM_META_POSTS_PER_PAGE_DEFAULT = 5
PCOM_META_DATE_FORMAT = 'date_format'
PCOM_META_SEARCH_API_URL = 'search_api_url'
PCOM_META_IGNORE_QUOTES = '!$!'

PCOM_META_TEMPLATE_MAIN_HEADER_TEXT = 'template_main_header_text'
PCOM_META_TEMPLATE_SUB_HEADER_TEXT = 'template_sub_header_text'
PCOM_META_TEMPLATE_SUB_HEADER_BACK_LINK_TEXT = 'template_sub_header_back_link_text'
PCOM_META_TEMPLATE_SEARCH_CONTENT = 'template_search_content'

# use system schematic settings
PCOM_DEFAULT_COMMAND = 'DEFAULT'
#
# NAV
PCOM_NAV_COMMAND = 'NAV'
# MENU - uses the same commands as NAV
PCOM_MENU_COMMAND = 'MENU'
#
PCOM_NAV_MENU_LINK_KEYWORD = 'mlk'
PCOM_NAV_LOGO_KEYWORD = 'logo'
PCOM_NAV_SEARCHBAR_KEYWORD = 'searchbar'
#
# BOXES
PCOM_BOX_COMMAND_ROOT = '_BOX'
PCOM_BOX_BOX = 'BOX'
PCOM_BOX_BOX_START = 'box-start'
PCOM_BOX_BOX_END = 'box-end'
PCOM_BOX_PLACEMENT = "N_BOX"
PCOM_MAX_NO_BOXES = 4

# min is hardcoded as 2
# used within boxes or content

PCOM_TEXT_COMMAND = 'TEXT'
#used as a filter in img, img_link and lnk
PCOM_TEXT_ATTRIBUTE = 'text'
PCOM_TEXT_IMG_KEYWORD = 'img'
PCOM_TEXT_IMG_LINK_KEYWORD = 'img_link'
PCOM_TEXT_LINK_KEYWORD = 'link'
#
#
# QUOTE
PCOM_QUOTE_COMMAND = 'QUOTE'
PCOM_QUOTE_BODY_KEYWORD = 'body'
PCOM_QUOTE_REF_KEYWORD = 'ref'
PCOM_QUOTE_LINK_KEYWORD = 'link'
PCOM_QUOTE_WRAP_CLASS = 'pm-quote-wrap'
#
PCOM_TITLE_COMMAND = 'TITLE' #
PCOM_TITLE_KEYWORD = 'title' #

# CONTENT
PCOM_CONTENT_COMMAND = 'CONTENT'
PCOM_CONTENT_TEXT_SUBCOMMAND = 'TEXT'

# CONTENT META
# title, author etc
PCOM_CONTENT_META_COMMAND = 'CONTENT_META'
PCOM_CONTENT_META_TITLE_KEYWORD = 'title'
PCOM_CONTENT_META_AUTHOR_KEYWORD = 'author'
PCOM_CONTENT_META_DATE_CREATED_KEYWORD = 'date_created'
PCOM_CONTENT_META_DATE_MODIFIED_KEYWORD = 'date_modified'
PCOM_CONTENT_META_CATEGORY_KEYWORD = 'category'
PCOM_CONTENT_META_SHOW_TIME_KEYWORD = 'show_time'

PCOM_CONTENT_META_POST_SETTINGS_DEFAULT = 'post_meta_default'
PCOM_CONTENT_META_PAGE_SETTINGS_DEFAULT = 'page_meta_default'

PCOM_CONTENT_META_TAG_OPEN = 'CONTENT_META=['
PCOM_CONTENT_META_TAG_CLOSE = ']:'

# POST LIST
PCOM_POST_LIST_COMMAND = 'POSTLIST'
PCOM_POST_LIST_ENTRY_LIST_KEYWORD = 'list'
PCOM_POST_LIST_TITLE_KEYWORD = 'title'
PCOM_POST_LIST_POSTS_PER_PAGE_KEYWORD = 'posts_per_page'
PCOM_POST_LIST_MANUAL_STICKY = 'manual_sticky'
PCOM_POST_LIST_ADD_ALL_POSTS = 'POSTS'
PCOM_POST_LIST_STICKY_INDICATOR = '!!'
PCOM_POSTLIST_TAG_OPEN = 'POSTLIST=['
PCOM_POSTLIST_TAG_CLOSE = ']:'

# RAW_CONTENT
PCOM_RAW_CONTENT_COMMAND = 'RAW'
PCOM_RAW_CONTENT_TEXT_SUBCOMMAND = 'TEXT'

#
# SECTION COMMAND
PCOM_SECTION_COMMAND = 'SECTION'
#
#
# Remote insert command
PCOM_INSERT_COMMAND = 'INSERT'
PCOM_INSERT_REF_KEYWORD = 'ref'
PCOM_INSERT_TAG_OPEN = 'INSERT=['
PCOM_INSERT_TAG_CLOSE = ']:'

#
# insert pagination
PCOM_INSERT_PAGINATION_COMMAND = 'PAGINATION'
PCOM_INSERT_PAGINATION_TAG_OPEN = 'PAGINATION=['
PCOM_INSERT_PAGINATION_TAG_CLOSE = ']:'
PCOM_INSERT_PAGINATION_PREV_KEYWORD = 'prev'
PCOM_INSERT_PAGINATION_NEXT_KEYWORD = 'next'
PCOM_PAGE_NUMBERS_CURRENT_CLASS = 'current'
PCOM_POSTLIST_PAGINATION_CLASS = 'pm-postlist-pagination'

# insert search bar
PCOM_INSERT_SEARCHBAR_COMMAND = 'SEARCHBAR'
#
# HEADER_CONTENT - scripts and stuff in the head
#
PCOM_HEADER_CONTENT_COMMAND = 'HEADER_ADDITIONS'
PCOM_HEADER_CONTENT_KEYWORD = 'content'

# FOOTER_CONTENT - scripts and stuff at end
PCOM_FOOTER_CONTENT_COMMAND = 'FOOTER_ADDITIONS'
PCOM_FOOTER_CONTENT_KEYWORD = 'content'
#
# POST to HTML conversions for TEXT=() commands
PCOM_POST_HTML_CONVERSIONS = {
  '[a_open]': '<a ',
  '[a_close]': '</a>',
  '[span_open]': '<span ',
  '[span_close]': '</span>',
  '[p]': '<p>',
  '[/p]': '</p>',
  '[i]': '<em>',
  '[/i]': '</em>',
  '[b]': '<strong>',
  '[/b]': '</strong>',
  '[strike]': '<span style="text-decoration: line-through;">',
  '[/strike]': '</span>',
  '[u]': '<span style="text-decoration: underline;">',
  '[/u]': '</span>',
  '[h1]': '<h1>',
  '[/h1]': '</h1>',
  '[h2]': '<h2>',
  '[/h2]': '</h2>',
  '[h3]': '<h3>',
  '[/h3]': '</h3>',
  '[h4]': '<h4>',
  '[/h4]': '</h4>',
  '[h5]': '<h5>',
  '[/h5]': '</h5>',
  '[ol]': '<ol>',
  '[/ol]': '</ol>',
  '[ul]': '<ul>',
  '[/ul]': '</ul>',
  '[li]': '<li>',
  '[/li]': '</li>',
  '[n]': '<br/>',
  '[2n]': '<br/><br/>',
  '[3n]': '<br/><br/><br/>',
  '[quote]': '<blockquote>',
  '[/quote]': '</blockquote>',
  '[code]': '<code>',
  '[/code]': '</code>',
  '[pre]': '<pre>',
  '[/pre]': '</pre>',
  '[samp]': '<samp>',
  '[/samp]': '</samp>',
  '[style]': '<style><!-- ',
  '[/style]': ' --></style>',
  '[caption]': '<div class="caption-pm"><p class="caption-text">',
  '[/caption]': '</p></div>',
  '[sch_cmd]': """%%""",
  '[/sch_cmd]': '::',
  '[sub_cmd]': '=[',
  '[/sub_cmd]': ']:',
  '[keyword]': '={',
  '[/keyword]': '}:',
  '[tag]': '<',
  '[/tag]': '>',
  '[fs]': '/',
  '[fa]': '<i ',
  '[/fa]': '></i>',
  '[pm-para]': '[p]',
  '[/pm-para]': '[/p]',
  '[UP-LOADS]': 'UPLOADS',
  '[SITE-HOME]': 'SITE_HOME',
  '[pm-tag]': '[',
  '[/pm-tag]': ']',
  '[script_open]': '<script ',
  '[/script]': '</script>',
  '[html_comment]': '<!--',
  '[/html_comment]': '-->'
}
#
#
# CUSTOMISED ATTRIBUTES
# ----------
# array is key: value
# key is the customised value that is used in a schematic
# value is the attribute that is processed
# e.g.
# 'charset': 'charset' can be changed to
# 'my_charset': 'charset'
#
# the value should remain the same but the key can be changed.
#
#
PCOM_CUSTOM_SITE_REPLACEMENTS = {
'SITE_HOME': 'SITE_HOME',
'IMAGES': 'IMAGES',
'UPLOADS': 'UPLOADS'
}
