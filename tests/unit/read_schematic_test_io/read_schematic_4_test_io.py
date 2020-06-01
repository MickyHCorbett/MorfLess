#
import libraries.constants as ct
import libraries.globals as gb
import libraries.meta_defaults as md
import libraries.schematics as sch

from collections import OrderedDict

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

test_values_6 = [\
{   'remark': 'Test Case 1:pcom_process_inserts - no insert info',
    'inputs': {\
        'html_array': ['Something here'],
        'insert_info': [],
        'log': {'inserts_processed': []},
        'settings': gb.DEFAULT_SETTINGS,
        'add_settings_to_dependencies': ['THIS'],
        'filename': 'test1.post',
        'dependencies': [
                {
                    "filename": "404.page",
                    "dependencies": [
                        "extra2.txt"
                    ]
                }
            ]
    },
    'assertEqual': {
        'html_array': ['Something here'],
        'outlog': {'inserts_processed': []},
        'site_settings': gb.DEFAULT_SETTINGS,
        'add_settings_to_dependencies': ['THIS'],
        'dependencies' : [
                {
                    "filename": "404.page",
                    "dependencies": [
                        "extra2.txt"
                    ]
                }
            ]
        }
    },

{   'remark': 'Test Case 2:pcom_process_inserts - insert info no content',
    'inputs': {\
        'html_array': ['Something here','INSERT=[]','Something else'],
        'insert_info': [
            {'filename': 'insert1.txt',
            'placement': ct.PCOM_MAIN_PLACEMENT,
            'index': 1,
            'valid_entry': ct.PCOM_VALID_ENTRY,
            'content': ''}
        ],
        'log': {'inserts_processed': []},
        'settings': gb.DEFAULT_SETTINGS,
        'add_settings_to_dependencies': ['THIS'],
        'filename': 'test1.post',
        'dependencies': [
                {
                    "filename": "404.page",
                    "dependencies": [
                        "extra2.txt"
                    ]
                }
            ]
    },
    'assertEqual': {
        'html_array': ['Something here','','Something else'],
        'outlog': {'inserts_processed': ['test1.post--insert1.txt-PLACEMENT=MAIN']},
        'site_settings': gb.DEFAULT_SETTINGS,
        'add_settings_to_dependencies': ['THIS'],
        'dependencies' : [
                {
                    "filename": "404.page",
                    "dependencies": [
                        "extra2.txt"
                    ]
                },
                OrderedDict([('filename', 'test1.post'), ('dependencies', ['insert1.txt'])])
            ]
        }
    },

{   'remark': 'Test Case 3:pcom_process_inserts - insert info content',
    'inputs': {\
        'html_array': ['Something here','INSERT=[]','Something else'],
        'insert_info': [
            {'filename': 'insert1.txt',
            'placement': ct.PCOM_MAIN_PLACEMENT,
            'index': 1,
            'valid_entry': ct.PCOM_VALID_ENTRY,
            'content': '%%CONTENT:: TEXT=[ Something here]:'}
        ],
        'log': {'inserts_processed': []},
        'settings': gb.DEFAULT_SETTINGS,
        'add_settings_to_dependencies': ['THIS'],
        'filename': 'test1.post',
        'dependencies': [
                {
                    "filename": "404.page",
                    "dependencies": [
                        "extra2.txt"
                    ]
                }
            ]
    },
    'assertEqual': {
        'html_array': ['Something here', '\n<div class="main-outer clearfix-small">\n  <div class="main-inner clearfix-small">\n    <div class="post">\n    Something here\n    </div><!-- end of .post -->\n  </div><!-- end of .main-inner -->\n</div><!-- end of .main-outer -->\n', 'Something else'],
        'outlog': {'inserts_processed': ['test1.post--insert1.txt-PLACEMENT=MAIN']},
        'site_settings': gb.DEFAULT_SETTINGS,
        'add_settings_to_dependencies': ['THIS'],
        'dependencies' : [
                {
                    "filename": "404.page",
                    "dependencies": [
                        "extra2.txt"
                    ]
                },
                OrderedDict([('filename', 'test1.post'), ('dependencies', ['insert1.txt'])])
            ]
        }
    },

{   'remark': 'Test Case 4:pcom_process_inserts - insert info not valid content',
    'inputs': {\
        'html_array': ['Something here','INSERT=[]','Something else'],
        'insert_info': [
            {'filename': 'insert1.txt',
            'placement': ct.PCOM_MAIN_PLACEMENT,
            'index': 1,
            'valid_entry': ct.PCOM_NO_ENTRY,
            'content': '%%CONTENT:: TEXT=[ Something here]:'}
        ],
        'log': {'inserts_processed': []},
        'settings': gb.DEFAULT_SETTINGS,
        'add_settings_to_dependencies': ['THIS'],
        'filename': 'test1.post',
        'dependencies': [
                {
                    "filename": "404.page",
                    "dependencies": [
                        "extra2.txt"
                    ]
                }
            ]
    },
    'assertEqual': {
        'html_array': ['Something here','','Something else'],
        'outlog': {'inserts_processed': ['test1.post--insert1.txt:No such file-PLACEMENT=MAIN']},
        'site_settings': gb.DEFAULT_SETTINGS,
        'add_settings_to_dependencies': ['THIS'],
        'dependencies' : [
                {
                    "filename": "404.page",
                    "dependencies": [
                        "extra2.txt"
                    ]
                }
            ]
        }
    },

{   'remark': 'Test Case 5:pcom_process_inserts - insert info not valid content - settings file',
    'inputs': {\
        'html_array': ['Something here','INSERT=[]','Something else'],
        'insert_info': [
            {'filename': 'insert1.txt',
            'placement': ct.PCOM_MAIN_PLACEMENT,
            'index': 1,
            'valid_entry': ct.PCOM_NO_ENTRY,
            'content': '%%CONTENT:: TEXT=[ Something here]:'}
        ],
        'log': {'inserts_processed': []},
        'settings': gb.DEFAULT_SETTINGS,
        'add_settings_to_dependencies': ['THIS', ct.PCOM_REQ_FILE_SETTINGS],
        'filename': 'test1.post',
        'dependencies': [
                {
                    "filename": "404.page",
                    "dependencies": [
                        "extra2.txt"
                    ]
                }
            ]
    },
    'assertEqual': {
        'html_array': ['Something here','','Something else'],
        'outlog': {'inserts_processed': ['test1.post--insert1.txt:No such file-PLACEMENT=MAIN']},
        'site_settings': gb.DEFAULT_SETTINGS,
        'add_settings_to_dependencies': ['THIS',ct.PCOM_REQ_FILE_SETTINGS],
        'dependencies' : [
                {
                    "filename": "404.page",
                    "dependencies": [
                        "extra2.txt"
                    ]
                },
                OrderedDict([('filename', 'test1.post'), ('dependencies', ['settings.txt'])])
            ]
        }
    },
]
