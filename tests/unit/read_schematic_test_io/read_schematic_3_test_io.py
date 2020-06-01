#
import libraries.constants as ct
import libraries.globals as gb
import libraries.meta_defaults as md
import libraries.schematics as sch

#
test_values_1 = [\
{   'remark': 'Test Case 1:polimorf_process_settings_schematic - schematic empty, Settings HEADER PLACEMENT',
    'test_val': 'default_header_additions',
    'inputs': {\
        'schematic': '',
        'args': gb.DEFAULT_GET_FIRST_COMMAND_ARGS,
        'placement': ct.PCOM_SETTINGS_HEADER,
        'type': 'post',
        'settings': gb.DEFAULT_SETTINGS
    },
    'assertEqual': {
        'out': [ct.PCOM_NO_ENTRY],
        'default_header_additions': ''
        }
    },
{   'remark': 'Test Case 2:polimorf_process_settings_schematic - schematic NONE, Settings HEADER PLACEMENT',
    'test_val': 'default_header_additions',
    'inputs': {\
        'schematic': ct.PCOM_NO_ENTRY,
        'args': gb.DEFAULT_GET_FIRST_COMMAND_ARGS,
        'placement': ct.PCOM_SETTINGS_HEADER,
        'type': 'post',
        'settings': gb.DEFAULT_SETTINGS
    },
    'assertEqual': {
        'out': [ct.PCOM_NO_ENTRY],
        'default_header_additions': ''
        }
    },
{   'remark': 'Test Case 3:polimorf_process_settings_schematic - schematic, Settings HEADER PLACEMENT',
    'test_val': 'default_header_additions',
    'inputs': {\
        'schematic': '\
        %%CONTENT:: TEXT=[ <p>This is a test paragraph</p> ]:',
        'args': gb.DEFAULT_GET_FIRST_COMMAND_ARGS,
        'placement': ct.PCOM_SETTINGS_HEADER,
        'type': 'post',
        'settings': gb.DEFAULT_SETTINGS
    },
    'assertEqual': {
        'out': ['    <div class="post">\n    <p>This is a test paragraph</p>\n    </div><!-- end of .post -->'],
        'default_header_additions': ''
        }
    },
{   'remark': 'Test Case 4:polimorf_process_settings_schematic - schematic 2, Settings HEADER PLACEMENT',
    'test_val': 'default_header_additions',
    'inputs': {\
        'schematic': '\
        %%CONTENT:: TEXT=[ <p>This is a test paragraph</p> ]:\n\
        %%CONTENT:: TEXT=[ <p>This is another test paragraph</p> ]:',
        'args': gb.DEFAULT_GET_FIRST_COMMAND_ARGS,
        'placement': ct.PCOM_SETTINGS_HEADER,
        'type': 'post',
        'settings': gb.DEFAULT_SETTINGS
    },
    'assertEqual': {
        'out': ['    <div class="post">\n    <p>This is a test paragraph</p>\n    </div><!-- end of .post -->',
        '    <div class="post">\n    <p>This is another test paragraph</p>\n    </div><!-- end of .post -->'],
        'default_header_additions': ''
        }
    },
{   'remark': 'Test Case 5:polimorf_process_settings_schematic - header additions - schematic 2, Settings HEADER PLACEMENT',
    'test_val': 'default_header_additions',
    'inputs': {\
        'schematic': '\
        %%CONTENT:: TEXT=[ <p>This is a test paragraph</p> ]:\n\
        %%CONTENT:: TEXT=[ <p>This is another test paragraph</p> ]:\n\
        %%HEADER_ADDITIONS:: content={ <!-- something to comment --> }:',
        'args': gb.DEFAULT_GET_FIRST_COMMAND_ARGS,
        'placement': ct.PCOM_SETTINGS_HEADER,
        'type': 'post',
        'settings': gb.DEFAULT_SETTINGS
    },
    'assertEqual': {
        'out': ['    <div class="post">\n    <p>This is a test paragraph</p>\n    </div><!-- end of .post -->',
        '    <div class="post">\n    <p>This is another test paragraph</p>\n    </div><!-- end of .post -->', 'NONE'],
        'default_header_additions': ''
        }
    },
{   'remark': 'Test Case 6:polimorf_process_settings_schematic - footer additions - schematic 2, Settings FOOTER PLACEMENT',
    'test_val': 'default_footer_additions',
    'inputs': {\
        'schematic': '\
        %%CONTENT:: TEXT=[ <p>This is a test paragraph</p> ]:\n\
        %%CONTENT:: TEXT=[ <p>This is another test paragraph</p> ]:\n\
        %%FOOTER_ADDITIONS:: content={ <!-- something to comment --> }:',
        'args': gb.DEFAULT_GET_FIRST_COMMAND_ARGS,
        'placement': ct.PCOM_SETTINGS_FOOTER,
        'type': 'post',
        'settings': gb.DEFAULT_SETTINGS
    },
    'assertEqual': {
        'out': ['  <div class="post">\n    <p>This is a test paragraph</p>\n  </div><!-- end of .post -->', '  <div class="post">\n    <p>This is another test paragraph</p>\n  </div><!-- end of .post -->', 'NONE'],
        'default_footer_additions': ''
        }
    },
]

test_values_2 = [\
{   'remark': 'Test Case 1:polimorf_process_additions_schematic - schematic empty, Settings HEADER PLACEMENT',
    'test_val': 'header_additions',
    'inputs': {\
        'schematic': '',
        'args': gb.DEFAULT_GET_FIRST_COMMAND_ARGS,
        'placement': ct.PCOM_SETTINGS_HEADER,
        'type': 'post'
    },
    'assertEqual': {
        'out': [],
        }
    },
{   'remark': 'Test Case 2:polimorf_process_additions_schematic - schematic NONE, Settings HEADER PLACEMENT',
    'test_val': 'header_additions',
    'inputs': {\
        'schematic': ct.PCOM_NO_ENTRY,
        'args': gb.DEFAULT_GET_FIRST_COMMAND_ARGS,
        'placement': ct.PCOM_SETTINGS_HEADER,
        'type': 'post'
    },
    'assertEqual': {
        'out': ct.PCOM_NO_ENTRY,
        }
    },
{   'remark': 'Test Case 3:polimorf_process_additions_schematic - schematic, Settings HEADER PLACEMENT',
    'test_val': 'header_additions',
    'inputs': {\
        'schematic': '\
        %%CONTENT:: TEXT=[ <p>This is a test paragraph</p> ]:',
        'args': gb.DEFAULT_GET_FIRST_COMMAND_ARGS,
        'placement': ct.PCOM_SETTINGS_HEADER,
        'type': 'post'
    },
    'assertEqual': {
        'out': []
        }
    },
{   'remark': 'Test Case 4:polimorf_process_additions_schematic - schematic 2, Settings HEADER PLACEMENT',
    'test_val': 'header_additions',
    'inputs': {\
        'schematic': '\
        %%CONTENT:: TEXT=[ <p>This is a test paragraph</p> ]:\n\
        %%CONTENT:: TEXT=[ <p>This is another test paragraph</p> ]:',
        'args': gb.DEFAULT_GET_FIRST_COMMAND_ARGS,
        'placement': ct.PCOM_SETTINGS_HEADER,
        'type': 'post'
    },
    'assertEqual': {
        'out': []
        }
    },
{   'remark': 'Test Case 5:polimorf_process_additions_schematic - header additions - schematic 2, Settings HEADER PLACEMENT',
    'test_val': 'header_additions',
    'inputs': {\
        'schematic': '\
        %%CONTENT:: TEXT=[ <p>This is a test paragraph</p> ]:\n\
        %%CONTENT:: TEXT=[ <p>This is another test paragraph</p> ]:\n\
        %%HEADER_ADDITIONS:: content={ <!-- something to comment --> }:',
        'args': gb.DEFAULT_GET_FIRST_COMMAND_ARGS,
        'placement': ct.PCOM_SETTINGS_HEADER,
        'type': 'post'
    },
    'assertEqual': {
        'out': ['<!-- something to comment -->'],
        }
    },
{   'remark': 'Test Case 6:polimorf_process_additions_schematic - footer additions - schematic 2, Settings FOOTER PLACEMENT',
    'test_val': 'footer_additions',
    'inputs': {\
        'schematic': '\
        %%CONTENT:: TEXT=[ <p>This is a test paragraph</p> ]:\n\
        %%CONTENT:: TEXT=[ <p>This is another test paragraph</p> ]:\n\
        %%FOOTER_ADDITIONS:: content={ <!-- something else to comment --> }:',
        'args': gb.DEFAULT_GET_FIRST_COMMAND_ARGS,
        'placement': ct.PCOM_SETTINGS_FOOTER,
        'type': 'post'
    },
    'assertEqual': {
        'out': ['<!-- something else to comment -->'],
        }
    },
]

test_values_3 = [\
{   'remark': 'Test Case 1:polimorf_determine_schematic_reference - empty content',
    'inputs': {\
        'content': '',
        'settings': gb.DEFAULT_SETTINGS
    },
    'assertEqual': {
        'processed': {'meta': 'NONE'},
        'schematic_content': {\
            'meta': 'NONE',
            'header': 'NONE',
            'before': 'NONE',
            'main': 'NONE',
            'after': 'NONE',
            'sidebar': 'NONE',
            'footer': 'NONE',
            'sidebar_found': False,
            'before_found': False,
            'after_found': False
            },
        'processed_settings': gb.DEFAULT_SETTINGS
        }
    },
{   'remark': 'Test Case 2:polimorf_determine_schematic_reference - schematic content 1',
    'inputs': {\
        'content': """

        ///META:
        url={ this/url}:
        title={ this page }:
        ///HEADER:
        %%CONTENT:: TEXT=[ Something ]:
        ///MAIN:
        This
        ///FOOTER:
        That

        """,
        'settings': gb.DEFAULT_SETTINGS
    },
    'assertEqual': {
        'processed': {\
            'meta': {\
                'page_title': 'this page',
                'page_description': 'Another page to view. Please read on',
                'authors': 'anon',
                'categories': 'none',
                'thumb_link': '/images/Polimorf-shapes-background.jpg',
                'page_extract': '',
                'url': 'this/url',
                'meta_valid': ct.PCOM_META_VALID,
                'sticky': '',
                'unlisted': False
                },
            'header': ['    <div class="post">\n    Something\n    </div><!-- end of .post -->'],
            'before': ['NONE'],
            'after': ['NONE'],
            'main': ['NONE'],
            'sidebar': ['NONE'],
            'footer': ['NONE']},
        'schematic_content': {\
            'meta': '\n        url={ this/url}:\n        title={ this page }:\n        ',
            'header': '\n        %%CONTENT:: TEXT=[ Something ]:\n        ',
            'before': 'NONE',
            'main': '\n        This\n        ',
            'after': 'NONE',
            'sidebar': 'NONE',
            'footer': '\n        That\n\n        ',
            'sidebar_found': False,
            'before_found': False,
            'after_found': False
            },
        'processed_settings': gb.DEFAULT_SETTINGS
        }
    },
{   'remark': 'Test Case 3:polimorf_determine_schematic_reference - schematic content 2',
    'inputs': {\
        'content': """

        ///META:
        url={ this/url}:
        title={ this page }:
        ///HEADER:
        %%CONTENT:: TEXT=[ Something ]:
        ///MAIN:
        %%CONTENT:: TEXT=[ Something else ]:
        ///FOOTER:
        That

        """,
        'settings': gb.DEFAULT_SETTINGS
    },
    'assertEqual': {
        'processed': {\
            'meta': {\
                'page_title': 'this page',
                'page_description': 'Another page to view. Please read on',
                'authors': 'anon',
                'categories': 'none',
                'thumb_link': '/images/Polimorf-shapes-background.jpg',
                'page_extract': '',
                'url': 'this/url',
                'meta_valid': ct.PCOM_META_VALID,
                'sticky': '',
                'unlisted': False
                },
            'header': ['    <div class="post">\n    Something\n    </div><!-- end of .post -->'],
            'before': ['NONE'],
            'after': ['NONE'],
            'main': ['\n<div class="main-outer clearfix-small">\n  <div class="main-inner clearfix-small">\n    <div class="post">\n    Something else\n    </div><!-- end of .post -->\n  </div><!-- end of .main-inner -->\n</div><!-- end of .main-outer -->'],
            'sidebar': ['NONE'],
            'footer': ['NONE']},
        'schematic_content': {\
            'meta': '\n        url={ this/url}:\n        title={ this page }:\n        ',
            'header': '\n        %%CONTENT:: TEXT=[ Something ]:\n        ',
            'before': 'NONE',
            'main': '\n        %%CONTENT:: TEXT=[ Something else ]:\n        ',
            'after': 'NONE',
            'sidebar': 'NONE',
            'footer': '\n        That\n\n        ',
            'sidebar_found': False,
            'before_found': False,
            'after_found': False
            },
        'processed_settings': gb.DEFAULT_SETTINGS
        }
    },
{   'remark': 'Test Case 4:polimorf_determine_schematic_reference - schematic content with sidebar',
    'inputs': {\
        'content': """

        ///META:
        url={ this/url}:
        title={ this page }:
        ///HEADER:
        %%CONTENT:: TEXT=[ Something ]:
        ///MAIN:
        %%CONTENT:: TEXT=[ Something else ]:
        ///SIDEBAR:
        %%CONTENT:: TEXT=[ Something sidebar ]:
        ///FOOTER:
        That

        """,
        'settings': gb.DEFAULT_SETTINGS
    },
    'assertEqual': {
        'processed': {\
            'meta': {\
                'page_title': 'this page',
                'page_description': 'Another page to view. Please read on',
                'authors': 'anon',
                'categories': 'none',
                'thumb_link': '/images/Polimorf-shapes-background.jpg',
                'page_extract': '',
                'url': 'this/url',
                'meta_valid': ct.PCOM_META_VALID,
                'sticky': '',
                'unlisted': False
                },
            'header': ['    <div class="post">\n    Something\n    </div><!-- end of .post -->'],
            'before': ['NONE'],
            'after': ['NONE'],
            'main': ['    <div class="post">\n    Something else\n    </div><!-- end of .post -->'],
            'sidebar': ['    <div class="post">\n    Something sidebar\n    </div><!-- end of .post -->'],
            'footer': ['NONE']},
        'schematic_content': {\
            'meta': '\n        url={ this/url}:\n        title={ this page }:\n        ',
            'header': '\n        %%CONTENT:: TEXT=[ Something ]:\n        ',
            'before': 'NONE',
            'main': '%%CONTENT:: TEXT=[ Something else ]:',
            'after': 'NONE',
            'sidebar': '%%CONTENT:: TEXT=[ Something sidebar ]:',
            'footer': '\n        That\n\n        ',
            'sidebar_found': True,
            'before_found': False,
            'after_found': False
            },
        'processed_settings': gb.DEFAULT_SETTINGS
        }
    },
]

test_values_4 = [\
{   'remark': 'Test Case 1:get_settings - empty content',
    'inputs': {\
        'content': \
        """

        """
    },
    'assertEqual': {
        'site_title': md.DEFAULT_SITE_TITLE,
        'site_description': md.DEFAULT_SITE_DESCRIPTION,
        'page_description': md.DEFAULT_PAGE_DESCRIPTION,
        'page_extract': ct.PCOM_NO_ENTRY,
        'date_format': ct.PCOM_UK_DATE_FORMAT,
        'posts_per_page': ct.PCOM_META_POSTS_PER_PAGE_DEFAULT,
        'default_header': '',
        'default_footer': '',
        'default_sidebar': '',
        'default_before': '',
        'default_after': '',
        'default_main': '',
        'default_header_additions': '',
        'default_footer_additions': '',
        'add_default_header_additions': False,
        'add_default_footer_additions': False,
        'header_additions': [],
        'footer_additions': [],
        'add_settings_to_dependencies': [],
        'current_file': ct.PCOM_NO_ENTRY,
        'category_info': {},
        'author_info': {},
        'default_author': gb.DEFAULT_AUTHOR,
        'default_thumb_link': sch.PM_DEFAULT_THUMBNAIL_IMAGE_LINK,
        'content_meta_info': {},
        'sticky': '',
        'search_api_url': '',
        'private_link_api_url': '',
        'template_types': gb.DEFAULT_TEMPLATE_TYPES,
        'template_main_header_text': gb.DEFAULT_TEMPLATE_MAIN_HEADER_TEXT,
        'template_sub_header_text': gb.DEFAULT_TEMPLATE_SUB_HEADER_TEXT,
        'template_sub_header_back_link_text': gb.DEFAULT_TEMPLATE_SUB_HEADER_BACK_LINK_TEXT,
        'default_content_post_meta': gb.DEFAULT_CONTENT_POST_META,
        'default_content_page_meta': gb.DEFAULT_CONTENT_PAGE_META,
        'template_search_content': gb.DEFAULT_TEMPLATE_SEARCH_CONTENT,
        'postlist_present': False
        }
    },
{   'remark': 'Test Case 3:get_settings - footer additions only',
    'inputs': {\
        'content': \
        """
        ///META:

        ///HEADER:

        ///MAIN:

        ///FOOTER:
        %%FOOTER_ADDITIONS::
        content={ Something to add in footer }:
        """
    },
    'assertEqual': {
        'site_title': md.DEFAULT_SITE_TITLE,
        'site_description': md.DEFAULT_SITE_DESCRIPTION,
        'page_description': md.DEFAULT_PAGE_DESCRIPTION,
        'page_extract': ct.PCOM_NO_ENTRY,
        'date_format': ct.PCOM_UK_DATE_FORMAT,
        'posts_per_page': ct.PCOM_META_POSTS_PER_PAGE_DEFAULT,
        'default_header': '',
        'default_footer': '',
        'default_sidebar': '',
        'default_before': '',
        'default_after': '',
        'default_main': '',
        'default_header_additions': '',
        'default_footer_additions': 'Something to add in footer\n',
        'add_default_header_additions': False,
        'add_default_footer_additions': False,
        'header_additions': [],
        'footer_additions': [],
        'add_settings_to_dependencies': [],
        'current_file': ct.PCOM_NO_ENTRY,
        'category_info': {},
        'author_info': {},
        'default_author': gb.DEFAULT_AUTHOR,
        'default_thumb_link': sch.PM_DEFAULT_THUMBNAIL_IMAGE_LINK,
        'content_meta_info': {},
        'sticky': '',
        'search_api_url': '',
        'private_link_api_url': '',
        'template_types': gb.DEFAULT_TEMPLATE_TYPES,
        'template_main_header_text': gb.DEFAULT_TEMPLATE_MAIN_HEADER_TEXT,
        'template_sub_header_text': gb.DEFAULT_TEMPLATE_SUB_HEADER_TEXT,
        'template_sub_header_back_link_text': gb.DEFAULT_TEMPLATE_SUB_HEADER_BACK_LINK_TEXT,
        'default_content_post_meta': gb.DEFAULT_CONTENT_POST_META,
        'default_content_page_meta': gb.DEFAULT_CONTENT_PAGE_META,
        'template_search_content': gb.DEFAULT_TEMPLATE_SEARCH_CONTENT,
        'postlist_present': False
        }
    },
]

test_values_5 = [\
{   'remark': 'Test Case 1:polimorf_process_schematic_sections - meta no entry empty entries',
    'inputs': {\
        'data': {\
            'meta': ct.PCOM_NO_ENTRY,
            'header': '',
            'before': '',
            'main': '',
            'after': '',
            'sidebar': '',
            'footer': ''
        },
        'settings': gb.DEFAULT_SETTINGS,
        'filename': '',
        'fileroot': ''
    },
    'assertEqual': ct.PCOM_NO_ENTRY
    },
{   'remark': 'Test Case 2:polimorf_process_schematic_sections - meta only ',
    'inputs': {\
        'data': {\
            'meta': {\
                'page_title': 'this page',
                'page_description': 'Another page to view. Please read on',
                'authors': 'anon',
                'categories': 'none',
                'thumb_link': '/images/Polimorf-shapes-background.jpg',
                'page_extract': '',
                'url': 'this/url',
                'meta_valid': ct.PCOM_META_VALID,
                'sticky': '',
                'unlisted': False
                },
            'header': [ct.PCOM_NO_ENTRY],
            'before': [ct.PCOM_NO_ENTRY],
            'main': [ct.PCOM_NO_ENTRY],
            'after': [ct.PCOM_NO_ENTRY],
            'sidebar': [ct.PCOM_NO_ENTRY],
            'footer': [ct.PCOM_NO_ENTRY]
        },
        'settings': gb.DEFAULT_SETTINGS,
        'filename': '',
        'fileroot': ''
    },
    'assertEqual': """

<!doctype html>
<html class="" lang="en">
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <title>this page</title>
  <link rel="shortcut icon" type"image/x-icon" href="/images/favicon.ico" />
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="A Morfless Site - a serverless site">
  <link rel="stylesheet" href="/extras/font-awesome-4.7.0/css/font-awesome.min.css" type="text/css" media="screen">
  <link rel="stylesheet" href="/fonts/Faustina-FontFace.css" type="text/css" media="screen">
  <link rel="stylesheet" href="/css/normalize.css" type="text/css" media="screen">
  <link rel="stylesheet" href="/css/style-core.css" type="text/css" media="screen">
  <link rel="stylesheet" href="/css/style-responsive.css" type="text/css" media="screen">
    <!-- head additions -->
    <!-- end of head additions -->
    <!-- custom head additions -->
    <!-- end of custom head additions -->
</head>
<body>
<section id="main-wrap">
</section><!-- end of main-wrap -->

<!-- standard scripts-->
<script src="/js/vendor/jquery-3.1.0.js"></script>
<script src="/js/nav-menu-drop-down.js"></script>
<script src="/js/width-change-zoom-fix.js"></script>
<!-- end of standard scripts-->
<!-- footer additions -->
<!-- end of footer additions -->
<!-- custom footer additions -->
<!-- end of custom footer additions -->
</body>
</html>

    """
    },
{   'remark': 'Test Case 3:polimorf_process_schematic_sections - header, before, footer ',
    'inputs': {\
        'data': {\
            'meta': {\
                'page_title': 'this page',
                'page_description': 'Another page to view. Please read on',
                'authors': 'anon',
                'categories': 'none',
                'thumb_link': '/images/Polimorf-shapes-background.jpg',
                'page_extract': '',
                'url': 'this/url',
                'meta_valid': ct.PCOM_META_VALID,
                'sticky': '',
                'unlisted': False
                },
            'header': ['<div class="more header"></div>'],
            'before': ['<div class="more before"></div>'],
            'main': [ct.PCOM_NO_ENTRY],
            'after': [ct.PCOM_NO_ENTRY],
            'sidebar': [ct.PCOM_NO_ENTRY],
            'footer': ['<div class="more footer"></div>']
        },
        'settings': gb.DEFAULT_SETTINGS,
        'filename': '',
        'fileroot': ''
    },
    'assertEqual': """

<!doctype html>
<html class="" lang="en">
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <title>this page</title>
  <link rel="shortcut icon" type"image/x-icon" href="/images/favicon.ico" />
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="A Morfless Site - a serverless site">
  <link rel="stylesheet" href="/extras/font-awesome-4.7.0/css/font-awesome.min.css" type="text/css" media="screen">
  <link rel="stylesheet" href="/fonts/Faustina-FontFace.css" type="text/css" media="screen">
  <link rel="stylesheet" href="/css/normalize.css" type="text/css" media="screen">
  <link rel="stylesheet" href="/css/style-core.css" type="text/css" media="screen">
  <link rel="stylesheet" href="/css/style-responsive.css" type="text/css" media="screen">
    <!-- head additions -->
    <!-- end of head additions -->
    <!-- custom head additions -->
    <!-- end of custom head additions -->
</head>
<body>
<header id="header-fixed">
<div class="header-outer">
  <div class="header-inner">
<div class="more header"></div>
  </div><!-- end of .header-inner -->
</div><!-- end of .header-outer -->
</header><!-- end of #header-fixed -->
<section id="main-wrap">
<div class="more before"></div></section><!-- end of main-wrap -->
<footer id="footer-wrap">
<div class="footer-outer clearfix-small">
  <div class="footer-inner clearfix-small">
<div class="more footer"></div>
  </div><!-- end of .footer-inner -->
</div><!-- end of .footer-outer -->
</footer><!-- end of footer-wrap -->
<!-- standard scripts-->
<script src="/js/vendor/jquery-3.1.0.js"></script>
<script src="/js/nav-menu-drop-down.js"></script>
<script src="/js/width-change-zoom-fix.js"></script>
<!-- end of standard scripts-->
<!-- footer additions -->
<!-- end of footer additions -->
<!-- custom footer additions -->
<!-- end of custom footer additions -->
</body>
</html>

    """
    },
{   'remark': 'Test Case 4:polimorf_process_schematic_sections - header, before, main, footer ',
    'inputs': {\
        'data': {\
            'meta': {\
                'page_title': 'this page',
                'page_description': 'Another page to view. Please read on',
                'authors': 'anon',
                'categories': 'none',
                'thumb_link': '/images/Polimorf-shapes-background.jpg',
                'page_extract': '',
                'url': 'this/url',
                'meta_valid': ct.PCOM_META_VALID,
                'sticky': '',
                'unlisted': False
                },
            'header': ['<div class="more header"></div>'],
            'before': ['<div class="more before"></div>'],
            'main': ['<div class="more main"></div>'],
            'after': [ct.PCOM_NO_ENTRY],
            'sidebar': [ct.PCOM_NO_ENTRY],
            'footer': ['<div class="more footer"></div>']
        },
        'settings': gb.DEFAULT_SETTINGS,
        'filename': '',
        'fileroot': ''
    },
    'assertEqual': """

<!doctype html>
<html class="" lang="en">
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <title>this page</title>
  <link rel="shortcut icon" type"image/x-icon" href="/images/favicon.ico" />
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="A Morfless Site - a serverless site">
  <link rel="stylesheet" href="/extras/font-awesome-4.7.0/css/font-awesome.min.css" type="text/css" media="screen">
  <link rel="stylesheet" href="/fonts/Faustina-FontFace.css" type="text/css" media="screen">
  <link rel="stylesheet" href="/css/normalize.css" type="text/css" media="screen">
  <link rel="stylesheet" href="/css/style-core.css" type="text/css" media="screen">
  <link rel="stylesheet" href="/css/style-responsive.css" type="text/css" media="screen">
    <!-- head additions -->
    <!-- end of head additions -->
    <!-- custom head additions -->
    <!-- end of custom head additions -->
</head>
<body>
<header id="header-fixed">
<div class="header-outer">
  <div class="header-inner">
<div class="more header"></div>
  </div><!-- end of .header-inner -->
</div><!-- end of .header-outer -->
</header><!-- end of #header-fixed -->
<section id="main-wrap">
<div class="more before"></div><div class="more main"></div>
</section><!-- end of main-wrap -->
<footer id="footer-wrap">
<div class="footer-outer clearfix-small">
  <div class="footer-inner clearfix-small">
<div class="more footer"></div>
  </div><!-- end of .footer-inner -->
</div><!-- end of .footer-outer -->
</footer><!-- end of footer-wrap -->
<!-- standard scripts-->
<script src="/js/vendor/jquery-3.1.0.js"></script>
<script src="/js/nav-menu-drop-down.js"></script>
<script src="/js/width-change-zoom-fix.js"></script>
<!-- end of standard scripts-->
<!-- footer additions -->
<!-- end of footer additions -->
<!-- custom footer additions -->
<!-- end of custom footer additions -->
</body>
</html>

    """
    },
{   'remark': 'Test Case 5:polimorf_process_schematic_sections - header, before, main, sidebar, footer ',
    'inputs': {\
        'data': {\
            'meta': {\
                'page_title': 'this page',
                'page_description': 'Another page to view. Please read on',
                'authors': 'anon',
                'categories': 'none',
                'thumb_link': '/images/Polimorf-shapes-background.jpg',
                'page_extract': '',
                'url': 'this/url',
                'meta_valid': ct.PCOM_META_VALID,
                'sticky': '',
                'unlisted': False
                },
            'header': ['<div class="more header"></div>'],
            'before': ['<div class="more before"></div>'],
            'main': ['<div class="more main"></div>'],
            'after': [ct.PCOM_NO_ENTRY],
            'sidebar': ['<div class="more sidebar"></div>'],
            'footer': ['<div class="more footer"></div>']
        },
        'settings': gb.DEFAULT_SETTINGS,
        'filename': '',
        'fileroot': ''
    },
    'assertEqual': """

<!doctype html>
<html class="" lang="en">
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <title>this page</title>
  <link rel="shortcut icon" type"image/x-icon" href="/images/favicon.ico" />
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="A Morfless Site - a serverless site">
  <link rel="stylesheet" href="/extras/font-awesome-4.7.0/css/font-awesome.min.css" type="text/css" media="screen">
  <link rel="stylesheet" href="/fonts/Faustina-FontFace.css" type="text/css" media="screen">
  <link rel="stylesheet" href="/css/normalize.css" type="text/css" media="screen">
  <link rel="stylesheet" href="/css/style-core.css" type="text/css" media="screen">
  <link rel="stylesheet" href="/css/style-responsive.css" type="text/css" media="screen">
    <!-- head additions -->
    <!-- end of head additions -->
    <!-- custom head additions -->
    <!-- end of custom head additions -->
</head>
<body>
<header id="header-fixed">
<div class="header-outer">
  <div class="header-inner">
<div class="more header"></div>
  </div><!-- end of .header-inner -->
</div><!-- end of .header-outer -->
</header><!-- end of #header-fixed -->
<section id="main-wrap">
<div class="more before"></div>
<div class="main-outer clearfix-small">
  <div class="main-inner clearfix-small">
  <div class="pm-main-with-sidebar-main clearfix-small">
<div class="more main"></div>
  </div><!-- end of .pm-main-with-sidebar-main" -->
  <div class="pm-main-with-sidebar-sidebar clearfix-small">
<div class="more sidebar"></div>
  </div><!-- end of .pm-main-with-sidebar-sidebar" -->
  </div><!-- end of .main-inner -->
</div><!-- end of .main-outer -->
</section><!-- end of main-wrap -->
<footer id="footer-wrap">
<div class="footer-outer clearfix-small">
  <div class="footer-inner clearfix-small">
<div class="more footer"></div>
  </div><!-- end of .footer-inner -->
</div><!-- end of .footer-outer -->
</footer><!-- end of footer-wrap -->
<!-- standard scripts-->
<script src="/js/vendor/jquery-3.1.0.js"></script>
<script src="/js/nav-menu-drop-down.js"></script>
<script src="/js/width-change-zoom-fix.js"></script>
<!-- end of standard scripts-->
<!-- footer additions -->
<!-- end of footer additions -->
<!-- custom footer additions -->
<!-- end of custom footer additions -->
</body>
</html>

    """
    },
{   'remark': 'Test Case 5:polimorf_process_schematic_sections - header, main, after, footer ',
    'inputs': {\
        'data': {\
            'meta': {\
                'page_title': 'this page',
                'page_description': 'Another page to view. Please read on',
                'authors': 'anon',
                'categories': 'none',
                'thumb_link': '/images/Polimorf-shapes-background.jpg',
                'page_extract': '',
                'url': 'this/url',
                'meta_valid': ct.PCOM_META_VALID,
                'sticky': '',
                'unlisted': False
                },
            'header': ['<div class="more header"></div>'],
            'before': [ct.PCOM_NO_ENTRY],
            'main': ['<div class="more main"></div>'],
            'after': ['<div class="more after"></div>'],
            'sidebar': [ct.PCOM_NO_ENTRY],
            'footer': ['<div class="more footer"></div>']
        },
        'settings': gb.DEFAULT_SETTINGS,
        'filename': '',
        'fileroot': ''
    },
    'assertEqual': """

<!doctype html>
<html class="" lang="en">
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <title>this page</title>
  <link rel="shortcut icon" type"image/x-icon" href="/images/favicon.ico" />
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="A Morfless Site - a serverless site">
  <link rel="stylesheet" href="/extras/font-awesome-4.7.0/css/font-awesome.min.css" type="text/css" media="screen">
  <link rel="stylesheet" href="/fonts/Faustina-FontFace.css" type="text/css" media="screen">
  <link rel="stylesheet" href="/css/normalize.css" type="text/css" media="screen">
  <link rel="stylesheet" href="/css/style-core.css" type="text/css" media="screen">
  <link rel="stylesheet" href="/css/style-responsive.css" type="text/css" media="screen">
    <!-- head additions -->
    <!-- end of head additions -->
    <!-- custom head additions -->
    <!-- end of custom head additions -->
</head>
<body>
<header id="header-fixed">
<div class="header-outer">
  <div class="header-inner">
<div class="more header"></div>
  </div><!-- end of .header-inner -->
</div><!-- end of .header-outer -->
</header><!-- end of #header-fixed -->
<section id="main-wrap"><div class="more main"></div>
<div class="more after"></div>
</section><!-- end of main-wrap -->
<footer id="footer-wrap">
<div class="footer-outer clearfix-small">
  <div class="footer-inner clearfix-small">
<div class="more footer"></div>
  </div><!-- end of .footer-inner -->
</div><!-- end of .footer-outer -->
</footer><!-- end of footer-wrap -->
<!-- standard scripts-->
<script src="/js/vendor/jquery-3.1.0.js"></script>
<script src="/js/nav-menu-drop-down.js"></script>
<script src="/js/width-change-zoom-fix.js"></script>
<!-- end of standard scripts-->
<!-- footer additions -->
<!-- end of footer additions -->
<!-- custom footer additions -->
<!-- end of custom footer additions -->
</body>
</html>



    """
    },
]
