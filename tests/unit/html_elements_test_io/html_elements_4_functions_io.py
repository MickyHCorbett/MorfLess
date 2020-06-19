#
import libraries.constants as ct
import libraries.globals as gb
import libraries.schematics as sch

from collections import OrderedDict
#

test_values_1 = [\
{   'remark': 'Test Case 1:pcom_add_content_meta_command -  empty syntax, post',
    'syntax': '',
    'custom_class': '',
    'current_file': 'test1.post',
    'placement': '',
    'type': '',
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': 'CONTENT_META=[:title,category,author,date_created,date_modified,show_time]:'
    },

{   'remark': 'Test Case 2:pcom_add_content_meta_command -  empty syntax, not post',
    'syntax': '',
    'custom_class': '',
    'current_file': 'NONE',
    'placement': ct.PCOM_HEADER_PLACEMENT,
    'type': '',
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': 'CONTENT_META=[HEADER:title,author,date_created,date_modified]:'
    },

{   'remark': 'Test Case 3:pcom_add_content_meta_command -  syntax not including keywords, not post',
    'syntax': 'build,things',
    'custom_class': '',
    'current_file': 'NONE',
    'placement': ct.PCOM_MAIN_PLACEMENT,
    'type': '',
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': 'CONTENT_META=[MAIN:]:'
    },

{   'remark': 'Test Case 4:pcom_add_content_meta_command -  syntax with keywords, not post',
    'syntax': 'author={}: date_created={}:',
    'custom_class': '',
    'current_file': 'NONE',
    'placement': ct.PCOM_MAIN_PLACEMENT,
    'type': '',
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': 'CONTENT_META=[MAIN:author,date_created]:'
    },
]

test_values_2 = [\
{   'remark': 'Test Case 1:pcom_find_content_meta_keywords -  syntax with keywords and non keywords',
    'syntax': 'author={}: date_created={}: something={}:',
    'assertEqual': ['author','date_created']
    },

{   'remark': 'Test Case 2:pcom_find_content_meta_keywords -  syntax with non keywords',
    'syntax': 'thishere={}: something={}:',
    'assertEqual': []
    },

{   'remark': 'Test Case 3:pcom_find_content_meta_keywords -  syntax with all keywords and some non keywords',
    'syntax': """
    thishere={}: something={}:
    title={}:
    category={}:
    author={}:
    date_created={}:
    date_modified={}:
    show_time={}:


    """,
    'assertEqual': ['title','category','author','date_created','date_modified','show_time']
    },
]

test_values_3 = [\
{   'remark': 'Test Case 1:pcom_insert_content_meta_data -  empty content meta info',
    'array': [''],
    'meta_info': [],
    'settings': gb.DEFAULT_SETTINGS,
    'list_meta': {},
    'post': {\
        "index": 1,
        "type": "post",
        "url": "/contact/",
        "title": "Contact",
        "postname": "contact.post",
        "description": "Morfless Contact page",
        "categories": [
            "things"
        ],
        "authors": [
            "anon"
        ],
        "extract": "Contact Morfless",
        "thumbnail": "/images/Polimorf-shapes-background-2.jpg",
        "creation_date": "12/09/2018",
        "creation_time": "12:18:10",
        "date_modified": "17/06/2020",
        "time_modified": "12:22:06",
        "sticky": ""
    },
    'is_template': False,
    'assertEqual': ['']
    },

{   'remark': 'Test Case 2:pcom_insert_content_meta_data -  meta info, postname = NONE',
    'array': ['', 'Something', ''],
    'meta_info': [\
        {'index': 1,
        'placement': 'MAIN',
        'title': False,
        'category': False,
        'author': False,
        'date_created': False,
        'date_modified': False,
        'show_time': False}
    ],
    'settings': gb.DEFAULT_SETTINGS,
    'list_meta': {},
    'post': {\
        "index": 1,
        "type": "post",
        "url": "/contact/",
        "title": "Contact",
        "postname": ct.PCOM_NO_ENTRY,
        "description": "Morfless Contact page",
        "categories": [
            "things"
        ],
        "authors": [
            "anon"
        ],
        "extract": "Contact Morfless",
        "thumbnail": "/images/Polimorf-shapes-background-2.jpg",
        "creation_date": "12/09/2018",
        "creation_time": "12:18:10",
        "date_modified": "17/06/2020",
        "time_modified": "12:22:06",
        "sticky": ""
    },
    'is_template': False,
    'assertEqual': ['', '', '']
    },

{   'remark': 'Test Case 3:pcom_insert_content_meta_data -  meta info, is_template',
    'array': ['', 'Something', ''],
    'meta_info': [\
        {'index': 1,
        'placement': 'MAIN',
        'title': False,
        'category': False,
        'author': False,
        'date_created': False,
        'date_modified': False,
        'show_time': False}
    ],
    'settings': gb.DEFAULT_SETTINGS,
    'list_meta': {},
    'post': {\
        "index": 1,
        "type": "post",
        "url": "/contact/",
        "title": "Contact",
        "postname": 'contact.post',
        "description": "Morfless Contact page",
        "categories": [
            "things"
        ],
        "authors": [
            "anon"
        ],
        "extract": "Contact Morfless",
        "thumbnail": "/images/Polimorf-shapes-background-2.jpg",
        "creation_date": "12/09/2018",
        "creation_time": "12:18:10",
        "date_modified": "17/06/2020",
        "time_modified": "12:22:06",
        "sticky": ""
    },
    'is_template': True,
    'assertEqual': ['', '', '']
    },

{   'remark': 'Test Case 4:pcom_insert_content_meta_data -  meta info, but all false',
    'array': ['', 'Something', ''],
    'meta_info': [\
        {'index': 1,
        'placement': 'MAIN',
        'title': False,
        'category': False,
        'author': False,
        'date_created': False,
        'date_modified': False,
        'show_time': False}
    ],
    'settings': gb.DEFAULT_SETTINGS,
    'list_meta': {},
    'post': {\
        "index": 1,
        "type": "post",
        "url": "/contact/",
        "title": "Contact",
        "postname": 'contact.post',
        "description": "Morfless Contact page",
        "categories": [
            "things"
        ],
        "authors": [
            "anon"
        ],
        "extract": "Contact Morfless",
        "thumbnail": "/images/Polimorf-shapes-background-2.jpg",
        "creation_date": "12/09/2018",
        "creation_time": "12:18:10",
        "date_modified": "17/06/2020",
        "time_modified": "12:22:06",
        "sticky": ""
    },
    'is_template': False,
    'assertEqual': ['','\
\n<div class="main-outer clearfix-small">\
\n  <div class="main-inner clearfix-small">\n\
\n    <div class="pm-post-meta clearfix-small">\
\n    </div><!-- end of .pm-post-meta -->\n\
\n  </div><!-- end of .main-inner -->\
\n</div><!-- end of .main-outer -->\n',
    '']
    },

{   'remark': 'Test Case 5:pcom_insert_content_meta_data -  meta info, date created, modified and show time',
    'array': ['', 'Something', ''],
    'meta_info': [\
        {'index': 1,
        'placement': 'MAIN',
        'title': False,
        'category': False,
        'author': False,
        'date_created': True,
        'date_modified': True,
        'show_time': True}
    ],
    'settings': gb.DEFAULT_SETTINGS,
    'list_meta': {},
    'post': {\
        "index": 1,
        "type": "post",
        "url": "/contact/",
        "title": "Contact",
        "postname": 'contact.post',
        "description": "Morfless Contact page",
        "categories": [
            "things"
        ],
        "authors": [
            "anon"
        ],
        "extract": "Contact Morfless",
        "thumbnail": "/images/Polimorf-shapes-background-2.jpg",
        "creation_date": "12/09/2018",
        "creation_time": "12:18:10",
        "date_modified": "17/06/2020",
        "time_modified": "12:22:06",
        "sticky": ""
    },
    'is_template': False,
    'assertEqual': ['', '\
\n<div class="main-outer clearfix-small">\
\n  <div class="main-inner clearfix-small">\n\
\n    <div class="pm-post-meta clearfix-small">\
\n        <div class="pm-date-meta">\
\n          <span class="pm-meta-icon"><i class="fa fa-calendar-plus-o" aria-hidden="true"></i></span>\
\n          <a href="/archive/09-2018/" alt="09-2018">12/09/2018 - 12:18:10</a>\
\n        </div><!-- end of .pm-date-meta -->\
\n        <div class="pm-date-meta">\
\n          <span class="pm-meta-icon"><i class="fa fa-refresh" aria-hidden="true"></i></span>\
\n          17/06/2020 - 12:22:06\
\n        </div><!-- end of .pm-date-meta -->\
\n    </div><!-- end of .pm-post-meta -->\n\
\n  </div><!-- end of .main-inner -->\
\n</div><!-- end of .main-outer -->\n',
    '']

    },

{   'remark': 'Test Case 6:pcom_insert_content_meta_data -  meta info, title',
    'array': ['', 'Something', ''],
    'meta_info': [\
        {'index': 1,
        'placement': 'MAIN',
        'title': True,
        'category': False,
        'author': False,
        'date_created': False,
        'date_modified': False,
        'show_time': False}
    ],
    'settings': gb.DEFAULT_SETTINGS,
    'list_meta': {},
    'post': {\
        "index": 1,
        "type": "post",
        "url": "/contact/",
        "title": "Contact",
        "postname": 'contact.post',
        "description": "Morfless Contact page",
        "categories": [
            "things"
        ],
        "authors": [
            "anon"
        ],
        "extract": "Contact Morfless",
        "thumbnail": "/images/Polimorf-shapes-background-2.jpg",
        "creation_date": "12/09/2018",
        "creation_time": "12:18:10",
        "date_modified": "17/06/2020",
        "time_modified": "12:22:06",
        "sticky": ""
    },
    'is_template': False,
    'assertEqual': ['', '\
\n<div class="main-outer clearfix-small">\
\n  <div class="main-inner clearfix-small">\n\
\n    <div class="pm-post-meta clearfix-small">\
\n      <h1>Contact</h1>\
\n    </div><!-- end of .pm-post-meta -->\n\
\n  </div><!-- end of .main-inner -->\
\n</div><!-- end of .main-outer -->\n',
    '']
    },

{   'remark': 'Test Case 7:pcom_insert_content_meta_data -  meta info, category',
    'array': ['', 'Something', ''],
    'meta_info': [\
        {'index': 1,
        'placement': 'MAIN',
        'title': False,
        'category': True,
        'author': False,
        'date_created': False,
        'date_modified': False,
        'show_time': False}
    ],
    'settings': gb.DEFAULT_SETTINGS,
    'list_meta': {\
          "authors": {
            "authors":
                [
                    {
                        "name": "anon",
                        "shortname": "anon",
                        "thumbnail": "/images/Polimorf-shapes-background.jpg",
                        "description": ""
                    }
                ]
           },
          "categories": {
            "categories":
                [
                    {
                        "name": "things",
                        "thumbnail": "/images/Polimorf-shapes-background.jpg",
                        "description": ""
                    }
                ]
            }
    },
    'post': {\
        "index": 1,
        "type": "post",
        "url": "/contact/",
        "title": "Contact",
        "postname": 'contact.post',
        "description": "Morfless Contact page",
        "categories": [
            "things"
        ],
        "authors": [
            "anon"
        ],
        "extract": "Contact Morfless",
        "thumbnail": "/images/Polimorf-shapes-background-2.jpg",
        "creation_date": "12/09/2018",
        "creation_time": "12:18:10",
        "date_modified": "17/06/2020",
        "time_modified": "12:22:06",
        "sticky": ""
    },
    'is_template': False,
    'assertEqual': ['', '\
\n<div class="main-outer clearfix-small">\
\n  <div class="main-inner clearfix-small">\n\
\n    <div class="pm-post-meta clearfix-small">\
\n        <div class="pm-author-category-meta">\
\n          <span class="pm-meta-icon"><i class="fa fa-list" aria-hidden="true"></i></span>\
\n          <a href="/categories/things/" alt="things">things</a>\
\n        </div><!-- end of .pm-author-category-meta -->\
\n    </div><!-- end of .pm-post-meta -->\n\
\n  </div><!-- end of .main-inner -->\
\n</div><!-- end of .main-outer -->\n',
    '']
    },

{   'remark': 'Test Case 8:pcom_insert_content_meta_data -  meta info, author',
    'array': ['', 'Something', ''],
    'meta_info': [\
        {'index': 1,
        'placement': 'MAIN',
        'title': False,
        'category': False,
        'author': True,
        'date_created': False,
        'date_modified': False,
        'show_time': False}
    ],
    'settings': gb.DEFAULT_SETTINGS,
    'list_meta': {\
          "authors": {
            "authors":
                [
                    {
                        "name": "anon",
                        "shortname": "anon",
                        "thumbnail": "/images/Polimorf-shapes-background.jpg",
                        "description": ""
                    }
                ]
           },
          "categories": {
            "categories":
                [
                    {
                        "name": "things",
                        "thumbnail": "/images/Polimorf-shapes-background.jpg",
                        "description": ""
                    }
                ]
            }
    },
    'post': {\
        "index": 1,
        "type": "post",
        "url": "/contact/",
        "title": "Contact",
        "postname": 'contact.post',
        "description": "Morfless Contact page",
        "categories": [
            "things"
        ],
        "authors": [
            "anon"
        ],
        "extract": "Contact Morfless",
        "thumbnail": "/images/Polimorf-shapes-background-2.jpg",
        "creation_date": "12/09/2018",
        "creation_time": "12:18:10",
        "date_modified": "17/06/2020",
        "time_modified": "12:22:06",
        "sticky": ""
    },
    'is_template': False,
    'assertEqual': ['', '\
\n<div class="main-outer clearfix-small">\
\n  <div class="main-inner clearfix-small">\n\
\n    <div class="pm-post-meta clearfix-small">\
\n        <div class="pm-author-category-meta">\
\n          <span class="pm-meta-icon"><i class="fa fa-user" aria-hidden="true"></i></span>\
\n          <a href="/authors/anon/" alt="anon">anon</a>\
\n        </div><!-- end of .pm-author-category-meta -->\
\n    </div><!-- end of .pm-post-meta -->\n\
\n  </div><!-- end of .main-inner -->\
\n</div><!-- end of .main-outer -->\n',
    '']
    },
]

test_values_4 = [\
{   'remark': 'Test Case 1:pcom_insert_date_created -  show_time false',
    'settings': gb.DEFAULT_SETTINGS,
    'post': {\
        "index": 1,
        "type": "post",
        "url": "/contact/",
        "title": "Contact",
        "postname": 'contact.post',
        "description": "Morfless Contact page",
        "categories": [
            "things"
        ],
        "authors": [
            "anon"
        ],
        "extract": "Contact Morfless",
        "thumbnail": "/images/Polimorf-shapes-background-2.jpg",
        "creation_date": "12/09/2018",
        "creation_time": "12:18:10",
        "date_modified": "17/06/2020",
        "time_modified": "12:22:06",
        "sticky": ""
    },
    'show_time': False,
    'assertEqual': """

        <div class="pm-date-meta">
          <span class="pm-meta-icon"><i class="fa fa-calendar-plus-o" aria-hidden="true"></i></span>
          <a href="/archive/09-2018/" alt="09-2018">12/09/2018</a>
        </div><!-- end of .pm-date-meta -->

    """
    },

{   'remark': 'Test Case 2:pcom_insert_date_created -  show_time false',
    'settings': gb.DEFAULT_SETTINGS,
    'post': {\
        "index": 1,
        "type": "post",
        "url": "/contact/",
        "title": "Contact",
        "postname": 'contact.post',
        "description": "Morfless Contact page",
        "categories": [
            "things"
        ],
        "authors": [
            "anon"
        ],
        "extract": "Contact Morfless",
        "thumbnail": "/images/Polimorf-shapes-background-2.jpg",
        "creation_date": "12/09/2018",
        "creation_time": "12:18:10",
        "date_modified": "17/06/2020",
        "time_modified": "12:22:06",
        "sticky": ""
    },
    'show_time': True,
    'assertEqual': """

        <div class="pm-date-meta">
          <span class="pm-meta-icon"><i class="fa fa-calendar-plus-o" aria-hidden="true"></i></span>
          <a href="/archive/09-2018/" alt="09-2018">12/09/2018 - 12:18:10</a>
        </div><!-- end of .pm-date-meta -->

    """
    },
]

test_values_5 = [\
{   'remark': 'Test Case 1:pcom_insert_date_modified -  show_time false',
    'settings': gb.DEFAULT_SETTINGS,
    'post': {\
        "index": 1,
        "type": "post",
        "url": "/contact/",
        "title": "Contact",
        "postname": 'contact.post',
        "description": "Morfless Contact page",
        "categories": [
            "things"
        ],
        "authors": [
            "anon"
        ],
        "extract": "Contact Morfless",
        "thumbnail": "/images/Polimorf-shapes-background-2.jpg",
        "creation_date": "12/09/2018",
        "creation_time": "12:18:10",
        "date_modified": "17/06/2020",
        "time_modified": "12:22:06",
        "sticky": ""
    },
    'show_time': False,
    'assertEqual': """

        <div class="pm-date-meta">
          <span class="pm-meta-icon"><i class="fa fa-refresh" aria-hidden="true"></i></span>
          17/06/2020
        </div><!-- end of .pm-date-meta -->

    """
    },

{   'remark': 'Test Case 2:pcom_insert_date_modified -  show_time false',
    'settings': gb.DEFAULT_SETTINGS,
    'post': {\
        "index": 1,
        "type": "post",
        "url": "/contact/",
        "title": "Contact",
        "postname": 'contact.post',
        "description": "Morfless Contact page",
        "categories": [
            "things"
        ],
        "authors": [
            "anon"
        ],
        "extract": "Contact Morfless",
        "thumbnail": "/images/Polimorf-shapes-background-2.jpg",
        "creation_date": "12/09/2018",
        "creation_time": "12:18:10",
        "date_modified": "17/06/2020",
        "time_modified": "12:22:06",
        "sticky": ""
    },
    'show_time': True,
    'assertEqual': """

        <div class="pm-date-meta">
          <span class="pm-meta-icon"><i class="fa fa-refresh" aria-hidden="true"></i></span>
          17/06/2020 - 12:22:06
        </div><!-- end of .pm-date-meta -->

    """
    },
]
