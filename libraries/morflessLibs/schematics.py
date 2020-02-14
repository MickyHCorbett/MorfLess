# MorfLess v1.0
#
# default schematics for header, main (post) and footer
# also includes basic html calls
#
from libraries import constants as ct

PM_HTML_OPEN_DECLARATION = ("""<!doctype html>""" + ct.NL
+ """<html class="" lang="en">""" + ct.NL
+ """<head>""" + ct.NL
+ ct.T1 + """<meta charset="utf-8">""" + ct.NL
+ ct.T1 + """<meta http-equiv="X-UA-Compatible" content="IE=edge">"""  + ct.NL)

PM_HEADER_SCHEMATIC = """%%NAV::
mlk={href="SITE_HOME" name="Home" src="IMAGES/home_icon.png"}:
searchbar={}:"""

PM_FOOTER_SCHEMATIC = """%%MENU::
mlk={href="SITE_HOME" name="Home" src="IMAGES/home_icon.png" class="home-ref"}:
mlk={href="/about/" name="about" }:
%%SEARCHBAR::"""
#
PM_AWS_ERROR_START = """%%CONTENT:: TEXT=[ [p]"""
PM_AWS_ERROR_END = """[/p] ]:"""
#
PM_DEFAULT_THUMBNAIL_IMAGE_LINK = """/images/Polimorf-shapes-background.jpg"""
PM_SEARCH_ICON_LINK = """/images/search-icon-small.png"""

# FONT AWESOME icons


PM_PAGINATION_NEXT_ICON = """<i class="fa fa-arrow-right" aria-hidden="true"></i>"""
PM_PAGINATION_PREV_ICON = """<i class="fa fa-arrow-left" aria-hidden="true"></i>"""
PM_QUOTE_ICON = """<i class="fa fa-quote-left fa-3x fa-pull-left" aria-hidden="true"></i>"""
PM_ICON_HTML = ct.T3 + """<i class="fa fa-bars fa-x" aria-hidden="true"></i>"""
PM_FA_ICON_OPEN = '<i class="'
PM_FA_ICON_CLOSE = """" aria-hidden="true"></i>"""
PM_CATEGORY_ICON = """<span class="pm-meta-icon"><i class="fa fa-list" aria-hidden="true"></i></span>"""
PM_AUTHOR_ICON = """<span class="pm-meta-icon"><i class="fa fa-user" aria-hidden="true"></i></span>"""
PM_DATE_CREATED_ICON = """<span class="pm-meta-icon"><i class="fa fa-calendar-plus-o" aria-hidden="true"></i></span>"""
PM_DATE_MODIFIED_ICON = """<span class="pm-meta-icon"><i class="fa fa-refresh" aria-hidden="true"></i></span>"""

# CLASS IDENTIFIERS
# -------------
PM_MAIN_POST_LIST_OPEN = """MAIN_POST_LIST_OPEN"""
PM_MAIN_POST_LIST_INDEX_OPEN = """MAIN_POST_LIST_INDEX_OPEN"""
PM_MAIN_POST_LIST_CLOSE = """MAIN_POST_LIST_CLOSE"""
PM_FOOTER_DIVS_OPEN = """FOOTER_DIVS_OPEN"""
PM_FOOTER_DIVS_BODY_HTML_CLOSE = """FOOTER_DIVS_BODY_HTML_CLOSE"""

# HTML
# -------------
PM_DEFAULT_MENU_LINK_COLOR = "#000000"
PM_EXCERPT_LENGTH = 30
PM_ALL_CLEAR = """<div class="aclear clearfix"></div>"""
PM_ALL_CLEAR_SPAN = """<span class="aclear"></span>"""
PM_10PX_SPACER = """<div class="pm-10px-spacer clearfix"></div>"""
PM_20PX_SPACER = """<div class="pm-20px-spacer clearfix"></div>"""
PM_50PX_SPACER = """<div class="pm-50px-spacer clearfix"></div>"""
PM_NAV_SPACER = """<div id="pm-nav-spacer">&nbsp</div>"""

PM_HEADER_WRAP_OPEN = """<header id="header-fixed">"""
PM_HEADER_WRAP_CLOSE = """</header><!-- end of #header-fixed -->"""
PM_HEADER_OUTER_OPEN = """<div class="header-outer">"""
PM_HEADER_OUTER_CLOSE = """</div><!-- end of .header-outer -->"""
PM_HEADER_INNER_OPEN = ct.T1 + """<div class="header-inner">"""
PM_HEADER_INNER_CLOSE = ct.T1 + """</div><!-- end of .header-inner -->"""

PM_MAIN_WRAP_OPEN = """<section id="main-wrap">"""
PM_MAIN_WRAP_CLOSE = """</section><!-- end of main-wrap -->"""
PM_MAIN_OUTER_OPEN = """<div class="main-outer clearfix-small"""
PM_MAIN_OUTER_CLOSE = """</div><!-- end of .main-outer -->"""
PM_MAIN_INNER_OPEN = ct.T1 + """<div class="main-inner clearfix-small"""
PM_MAIN_INNER_CLOSE = ct.T1 + """</div><!-- end of .main-inner -->"""

PM_FOOTER_WRAP_OPEN = """<footer id="footer-wrap">"""
PM_FOOTER_WRAP_CLOSE = """</footer><!-- end of footer-wrap -->"""
PM_FOOTER_OUTER_OPEN = """<div class="footer-outer clearfix-small">"""
PM_FOOTER_OUTER_CLOSE = """</div><!-- end of .footer-outer -->"""
PM_FOOTER_INNER_OPEN = ct.T1 + """<div class="footer-inner clearfix-small">"""
PM_FOOTER_INNER_CLOSE = ct.T1 + """</div><!-- end of .footer-inner -->"""

PM_MAIN_WITH_SIDEBAR_MAIN_OPEN = ct.T1 + """<div class="pm-main-with-sidebar-main clearfix-small">"""
PM_MAIN_WITH_SIDEBAR_MAIN_CLOSE = ct.T1 + """</div><!-- end of .pm-main-with-sidebar-main" -->"""
PM_MAIN_WITH_SIDEBAR_SIDEBAR_OPEN = ct.T1 + """<div class="pm-main-with-sidebar-sidebar clearfix-small">"""
PM_MAIN_WITH_SIDEBAR_SIDEBAR_CLOSE = ct.T1 + """</div><!-- end of .pm-main-with-sidebar-sidebar" -->"""

# =======
PM_POST_LIST_OPEN = ct.T2 + """<div class="pm-post-list clearfix-small">"""
PM_POST_LIST_CUSTOM_OPEN = ct.T2 + """<div class="pm-post-list-custom clearfix-small"""
PM_POST_LIST_CUSTOM_OPEN_ONLY = ct.T2 + """<div class="pm-post-list-custom clearfix-small">"""
PM_POST_LIST_CLOSE = ct.T2 + """</div><!-- end of .pm-post-list -->"""
PM_POST_LIST_POST_CONTENT_OPEN = ct.T3 + """<div class="pm-post-content clearfix-small">"""
PM_POST_LIST_POST_CONTENT_CLOSE = ct.T3 + """</div><!-- end of .pm-post-content -->"""
PM_POST_LIST_POST_IMAGE_OPEN = ct.T4 + """<div class="pm-post-image">"""
PM_POST_LIST_POST_IMAGE_CLOSE = ct.T4 + """</a></div><!-- end of .pm-post-image -->"""
PM_POST_LIST_BLOG_ENTRY_OPEN = ct.T4 + """<div class="pm-blog-entry">"""
PM_POST_LIST_BLOG_ENTRY_STICKY_OPEN = ct.T4 + """<div class="pm-blog-entry sticky">"""
PM_POST_LIST_BLOG_ENTRY_CLOSE = ct.T4 + """</div><!-- end of .pm-blog_entry -->"""
PM_POST_LIST_DATA_OPEN = ct.T3 + """<div class="pm-postlist-entries clearfix-small"""
PM_POST_LIST_DATA_CLOSE = ct.T3 + """</div><!-- end postlist entries data -->"""
PM_POST_LIST_IDENTIFIER = """postlist-list-"""
PM_POST_LIST_TEMPLATE_IDENTIFIER = """postlist-template"""

# =============

PM_META_OPEN = ct.T2 + """<div class="pm-post-meta clearfix-small"""
PM_META_CLOSE = ct.T2 + """</div><!-- end of .pm-post-meta -->"""
PM_POST_TITLE_OPEN = """<div class="pm-post-title">"""
PM_POST_TITLE_CLOSE = """</div><!-- end of .pm-post-title -->"""
PM_POST_DATE_META_OPEN = ct.T4 + """<div class="pm-date-meta">"""
PM_POST_DATE_META_CLOSE = ct.T4 + """</div><!-- end of .pm-date-meta -->"""
PM_POST_CATEGORY_META_OPEN = ct.T4 + """<div class="pm-author-category-meta">"""
PM_POST_CATEGORY_META_CLOSE = ct.T4 + """</div><!-- end of .pm-author-category-meta -->"""
PM_POST_TAG_META_OPEN = """<div class="pm-tag-meta">"""
PM_POST_TAG_META_CLOSE = """</div><!-- end of .pm-tag-meta -->"""

PM_POST_PAGINATION_OPEN = ct.T2 + """<div class="pm-post-pagination"""
PM_POST_PAGINATION_CLOSE = ct.T2 + """</div><!-- end of .pm-post-pagination -->"""
PM_PAGE_NAV_OPEN = ct.T2 + """<div class="page-nav">"""
PM_PAGE_NAV_CLOSE = ct.T2 + """</div><!-- end of .page-nav-->"""

PM_NEXTPAGE_NAV_OPEN = """<div class="page-nav nextpage">"""
PM_NEXTPAGE_NAV_CLOSE = """</div><!-- end of .page-nav .nextpage -->"""

PM_POST_NAV_OPEN = ct.T2 + """<div id="pm-post-nav">"""
PM_POST_NAV_CLOSE = ct.T2 + """</div><!-- end of #pm-post-nav -->"""

PM_PAGINATION_SINGLE_POST = ct.T3 + """<div id="pm-single-post-link">"""
PM_PAGINATION_NEXT_POST = ct.T3 + """<div id="pm-next-post-link">"""
PM_PAGINATION_PREV_POST = ct.T3 + """<div id="pm-prev-post-link">"""
PM_PAGINATION_CLOSE = ct.T3 + """</span></div><!-- post link -->"""
PM_PAGINATION_FORMAT_NEXT_LINK = ct.T4 + '<span class="pm-post-link-text">' + PM_PAGINATION_NEXT_ICON
PM_PAGINATION_FORMAT_PREV_LINK = ct.T4 + '<span class="pm-post-link-text">' + PM_PAGINATION_PREV_ICON

PM_POST_OPEN = ct.T2 + """<div class="post"""
PM_POST_OPEN_FOOTER = ct.T1 + """<div class="post"""
PM_POST_OPEN_ONLY = ct.T2 + """<div class="post">"""
PM_POST_CLOSE = ct.T2 + """</div><!-- end of .post -->"""
PM_POST_CLOSE_FOOTER = ct.T1 + """</div><!-- end of .post -->"""

PM_QUOTE_OPEN = ct.T3 + """<div class="post pm-quote clearfix-small"""
PM_QUOTE_CLOSE = ct.T3 + """</div><!-- end of .pm-quote -->"""
PM_QUOTATION_MARKS = ct.T4 + """<span class="pm-quotation-marks">""" + PM_QUOTE_ICON + """</span>"""
PM_QUOTE_REF_OPEN = ct.T4 + """<span class="pm-quote-ref">"""
PM_QUOTE_REF_CLOSE = ct.T4 + """</span><!-- end of .pm-quote-ref -->"""

PM_GENERAL_CONTENT_WRAP_OPEN = """<div class="post pm-general-content clearfix-small"""
PM_GENERAL_CONTENT_WRAP_CLOSE = """</div><!-- end of .pm-general-content -->"""

PM_SIDEBAR_CONTENT_OPEN = """<div class="pm-sidebar-content clearfix-small"""
PM_SIDEBAR_CONTENT_CLOSE = """</div><!-- end of .pm-sidebar-content -->"""

PM_AFTER_POST_OPEN = """<div class="post clearfix">"""
PM_AFTER_POST_CLOSE = """</div><!-- end of .post with clearfix -->"""

PM_COMMENT_INFO_OPEN = """<div class="pm-comment-info clearfix-small">"""
PM_COMMENT_INFO_CLOSE = """</div><!-- end of .pm-comment-info -->"""

PM_CLOSE_DIV_WITH_COMMAS = '">'
#for adding classes to first div

PM_CLOSE_BODY_TAG = """</body>""" + ct.NL
PM_CLOSE_HTML_TAG = """</html>"""
PM_LINE_BR = """<br/>"""

# -------------
# NAV MENU html defaults
# -------------
PM_NAV_OPEN = ct.T1 + """<div class="pm-nav clearfix-small"""
PM_NAV_CLOSE = ct.T1 + """</div><!-- end of .pm-nav -->"""
PM_GENERAL_MENU_OPEN = ct.T1 + """<div class="pm-general-menu clearfix-small"""
PM_GENERAL_MENU_CLOSE = ct.T1 + """</div><!-- end of .pm-general-menu -->"""
#
PM_NAV_MENU_OPEN = ct.T2 + """<div class="pm-nav-menu clearfix-small">""" + ct.NL + ct.T3 + """<ul>"""
PM_NAV_MENU_OPEN_WITH_LOGO = ct.T2 + """<div class="pm-nav-menu nav-with-logo clearfix-small">""" +  ct.NL + ct.T3 + """<ul>"""
PM_NAV_MENU_CLOSE = ct.T3 + """</ul>""" + ct.NL + ct.T2 + """</div><!-- end of NAV menu -->"""
PM_NAV_RESP_ICON_OPEN = ct.T2 + """<div class="pm-responsive-icon">""" + ct.NL + ct.T3 + """<div class="pm-resp-icon">"""
PM_NAV_RESP_ICON_CLOSE = ct.T3 + """</div>""" + ct.NL + ct.T2 + """</div>"""
PM_NAV_MENU_SEARCH_OPEN = ct.T2 + """<div class="pm-nav-menu-search clearfix-small">"""
PM_NAV_MENU_SEARCH_WITH_LOGO_OPEN = ct.T2 + """<div class="pm-nav-menu-search with-logo clearfix-small">"""
PM_NAV_MENU_SEARCH_CLOSE = ct.T2 + """</div><!-- end of .pm-nav-menu-search -->"""

PM_NAV_SEARCHBAR_OPEN = ct.T2 + """<div id="pm-nav-searchbar" class="clearfix-small">"""
PM_NAV_SEARCHBAR_CLOSE = ct.T2 + """</div><!-- end of #pm-nav-searchbar-->"""
PM_SEARCHBAR_OPEN = ct.T2 + """<div id="pm-searchbar-general" class="clearfix-small">"""
PM_SEARCHBAR_CLOSE = ct.T2 + """</div><!-- end of #pm-searchbar-general -->"""

PM_NAV_MENU_LINK_HTML_1 = '<a href="'
PM_NAV_MENU_LINK_HTML_2 = '" name="'
PM_NAV_MENU_LINK_HTML_3 = '">'
PM_NAV_MENU_LINK_HTML_4 = """</a></li>"""
PM_NAV_MENU_IMG_LINK_HTML_1 = '<img src="'
PM_NAV_MENU_IMG_LINK_HTML_2 = '" alt="'
PM_NAV_MENU_IMG_LINK_HTML_3 = '" />'
PM_NAV_LOGO_DIV_OPEN = """<div class="pm-nav-logo">"""
PM_NAV_LOGO_DIV_CLOSE = """</div><!-- end of logo -->"""

# N BOX (TWO, THREE, FOUR) html defaults
# ---------------
PM_N_BOX_OPEN = ct.T2 + """<div class="pm-n-box clearfix-small"""
PM_N_BOX_CLOSE = ct.T2+ """</div><!-- end of .pm-n-box -->"""
PM_N_BOX_BOX_OPEN = """<div class="clearfix-small pm-n-box-box pm-box-"""
PM_BOX_BOX_CLOSE =  """</div><!-- end of .pm-n-box-box -->"""

# TITLE
# -----
PM_TITLE_NAV_DIV_OPEN = """<div class="pm-title-nav">"""
PM_TITLE_NAV_DIV_CLOSE = """</div><!-- end of .pm-title-nav -->"""

PM_TITLE_LIST_DIV_OPEN = """<div class="pm-title-list">\n"""
PM_TITLE_LIST_DIV_CLOSE = """</div><!-- end of .pm-title-list -->\n"""

# SECTION add class
PM_ADD_SECTION_CLASS = """ class="pm-section"""
#
# DEFAULT FOOTER SCRIPTS
SCRIPT_ADDITION_TAG_START = '<!-- custom footer additions -->'
SCRIPT_ADDITION_TAG_END = '<!-- end of custom footer additions -->'
HEADER_ADDITIONS_START = '<!-- custom head additions -->'
HEADER_ADDITIONS_END = '<!-- end of custom head additions -->'
DEFAULT_FOOTER_SCRIPTS =  (ct.NL + '<!-- standard scripts-->' + ct.NL
+ '<script src="/js/vendor/jquery-3.1.0.js"></script>' + ct.NL
+ '<script src="/js/nav-menu-drop-down.js"></script>' + ct.NL
+ '<script src="/js/width-change-zoom-fix.js"></script>'+ ct.NL
+ '<!-- end of standard scripts-->' + ct.NL
+ SCRIPT_ADDITION_TAG_START + ct.NL
+ SCRIPT_ADDITION_TAG_END + ct.NL)

# postlist calls
PM_TEMPLATE_TITLE_REPLACEMENT = "%%#TITLE#%%"
PM_TEMPLATE_DESCRIPTION_REPLACEMENT = "%%#DESCRIPTION#%%"
PM_POSTLIST_PLACEHOLDER = "%%#POSTLIST_NAME#%%"
PM_POSTLIST_CONSTANT_PLACEHOLDER = "%%#POSTLIST_CONSTANT_STUB#%%"
PM_TEMPLATE_JS_NAME = '%%$TEMPLATE_JS_NAME$%%'
PM_TEMPLATE_CONSTANT_NAME = '%%$TEMPLATE_CONSTANT_NAME$%%'
PM_TEMPLATE_CLASS = '%%$TEMPLATE_CLASS$%%'
PM_PAGINATION_NAME = '%%$PAGINATION$%%'
PM_PAGINATION_CONSTANT_NAME = '%%$_PAGINATION_$%%'
PM_POSTLIST_PAGINATION_NUMBER = '%%$_NUMBER_$%%'
PM_POSTLIST_PAGINATION_IDENT = '%%$_NUMBERIDENT_$%%'
PM_POSTLIST_PAGINATION_SELECTOR_IDENT = '-pm-page-numbers'
PM_POSTLIST_TEMPLATE_BACKLINK = '%%$BACKLINK$%%'
PM_POSTLIST_TEMPLATE_BACKLINK_NAME = '%%$_BACKLINK_$%%'
PM_ARCHIVE_BASE = '$$ARCHIVE$$'
PM_ARCHIVE_BASE_SUB = '$$_ARCHIVE_$$'
PM_SEARCH_NAME = '$$SEARCH$$'
PM_SEARCH_API_URL = '$$_SEARCH_API_$$'

POSTLIST_TEMPLATE_SCRIPTS = ('<script src="/js/js-lists/' + ct.PCOM_POSTLIST_CONSTANT_NAME_BASE
+ PM_TEMPLATE_JS_NAME + '.js" data-template-constant-name="_postlist_'
+ PM_TEMPLATE_CONSTANT_NAME + '"></script>' + ct.NL + '<script src="/js/postlist-template-handler.js"></script>')

POSTLIST_SCRIPTS = ('<script src="/js/js-lists/' + PM_POSTLIST_PLACEHOLDER + '" data-js-constant-name="_postlist_'
+ PM_POSTLIST_CONSTANT_PLACEHOLDER + '"></script>' + ct.NL + '<script src="/js/postlist-handler.js"></script>')

PAGINATION_SCRIPTS = ('<script src="/js/js-lists/' + PM_PAGINATION_NAME + '" data-pagination-constant-name="_pagination_'
+ PM_PAGINATION_CONSTANT_NAME + '"></script>' + ct.NL + '<script src="/js/pagination-handler.js"></script>')

POSTLIST_PAGINATION = (ct.T4 + '<span class="pm-page-numbers ' + PM_POSTLIST_PAGINATION_IDENT+ '">' + PM_POSTLIST_PAGINATION_NUMBER + '</span>')

PM_POSTLIST_PAGINATION_OPEN = (ct.T3 + '<div class="pm-postlist-pagination clearfix-small" data-postlist-name="'
+ PM_POSTLIST_PAGINATION_IDENT + '">')
PM_POSTLIST_PAGINATION_CLOSE = ct.T3 + """</div><!-- end of .pm-postlist-pagination -->"""

PM_TEMPLATE_POSTLIST_INSERT = (PM_POST_LIST_CUSTOM_OPEN_ONLY + ct.NL
    + ct.T3 + '<div class="pm-postlist-entries clearfix-small postlist-template">' + ct.NL
    + PM_POST_LIST_DATA_CLOSE + ct.NL
    + ct.T3 + '<div class="pm-postlist-pagination clearfix-small" data-postlist-name="postlist-template">' + ct.NL
    + PM_POSTLIST_PAGINATION_CLOSE + ct.NL
    + PM_POST_LIST_CLOSE + ct.NL)

PM_TEMPLATE_HEADER_FORMAT = ct.T3 + '<h1 class="pm-template-header"></h1>'
PM_SUB_TEMPLATE_BACK_LINK = (ct.T3 + '<div class="pm-pagination-header-backlink pm-post-link-text">' + ct.JS_ESCAPE + ct.NL
+ ct.T4 + PM_PAGINATION_PREV_ICON + ct.JS_ESCAPE + ct.NL
+ ct.T4 +'<a href="' + PM_POSTLIST_TEMPLATE_BACKLINK + '">' + PM_POSTLIST_TEMPLATE_BACKLINK_NAME + '</a>' + ct.JS_ESCAPE + ct.NL
+ ct.T3 + '</div><!-- end of .pm-pagination-header-backlink -->')

PM_TEMPLATE_ARCHIVE_MAIN_LINK_FORMAT = (ct.T3 + '<p class="pm-archive-links"><a href="/' + PM_ARCHIVE_BASE + '/'
        + PM_ARCHIVE_BASE_SUB + '">' + PM_ARCHIVE_BASE_SUB + '</a></p>')

PM_TEMPLATE_BODY_NAME = "$$TEMPLATE_BODYNAME$$"
PM_TEMPLATE_BODY_CLASS = '<body class="body-' + PM_TEMPLATE_BODY_NAME + PM_TEMPLATE_JS_NAME + '">'
# ======
# SEARCHBAR TYPES
# =====
PM_SEARCH_BAR = (ct.NL + ct.T2 + '<div class="pm-searchbar clearfix-small">' + ct.NL
+ ct.T3 + '<form action="/' + PM_SEARCH_NAME + '/" autocomplete="on">' + ct.NL
+ ct.T3 + '<input id="search" type="text" name="s" />' + ct.NL
+ ct.T3 + '</form>' + ct.NL
+ ct.T3 + '<span id="search-submit" class="pm-search-button" name="search-submit"></span>' + ct.NL
+ ct.T2 + '</div><!-- end of #pm-searchbar -->' + ct.NL)

PM_SEARCH_BAR_SEARCH_PAGE = (ct.NL + ct.T2 + '<div class="pm-searchbar pm-search-page clearfix-small">' + ct.NL
+ ct.T3 + '<form action="/' + PM_SEARCH_NAME + '/" autocomplete="on">' + ct.NL
+ ct.T3 + '<input id="search" type="text" name="s" />' + ct.NL
+ ct.T3 + '</form>' + ct.NL
+ ct.T3 + '<span id="search-submit" class="pm-search-button" name="search-submit"></span>' + ct.NL
+ ct.T2 + '</div><!-- end of #pm-searchbar -->' + ct.NL)

PM_SEARCH_QUERY_IDENTIFIER = 'pm-search-query'
PM_SEARCH_CONTENT_IDENTIFIER = 'pm-search-content'
PM_SEARCH_PAGINATION_IDENTIFIER = 'pm-search-pagination'
PM_SEARCH_QUERY_TITLE = '<h1 class="' + PM_SEARCH_QUERY_IDENTIFIER + '"></h1>'
PM_SEARCH_CONTENT = '<div class="' + PM_SEARCH_CONTENT_IDENTIFIER + ' clearfix-small"></div>'
PM_SEARCH_PAGINATION = '<div class="' + PM_SEARCH_PAGINATION_IDENTIFIER +' clearfix-small"></div>'

PM_SEARCHBAR_JS_INSERT = ('<script src="/js/search-handler.js"></script>' + ct.NL
+ '<script src="/js/js-lists/' + ct.PCOM_SEARCH_CONFIG_JS_NAME + '"></script>' + ct.NL)

# =====
# EFFECTS
# -----
PM_SCROLL_REVEAL_SOURCE_INCLUDE = """<script src="https:unpkg.com/scrollreveal/dist/scrollreveal.min.js"></script>\n"""

# HIDE AND DISPLAY IMAGES
PM_HIDE_IMAGES = """<style>body img { visibility: hidden }</style>\n"""
PM_DISPLAY_IMAGES = """<style>body img { visibility: visible }</style>\n"""

# ===============
