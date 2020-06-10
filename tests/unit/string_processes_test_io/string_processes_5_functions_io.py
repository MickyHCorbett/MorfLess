#
import libraries.constants as ct
import libraries.globals as gb

from collections import OrderedDict
#

test_values_1 = [\
{   'remark': 'Test Case 1:pcom_insert_default_additions_into_html - header content, add default=True, no additions',
    'additions': gb.DEFAULT_SETTINGS,
    'add_addition_placement': 'add_default_header_additions',
    'addition_placement': 'default_header_additions',
    'add_default': True,
    'default_additions': '',
    'content': """
<head>
  <!-- head additions -->
  <!-- end of head additions -->
  <!-- custom head additions -->
  <!-- end of custom head additions -->""",
    'placement': ct.PCOM_HEADER_PLACEMENT,
    'assertEqual': """
<head>
  <!-- head additions -->
  <!-- end of head additions -->
  <!-- custom head additions -->
  <!-- end of custom head additions -->"""
    },
{   'remark': 'Test Case 2:pcom_insert_default_additions_into_html - header content, add default=False, additions',
    'additions': gb.DEFAULT_SETTINGS,
    'add_addition_placement': 'add_default_header_additions',
    'addition_placement': 'default_header_additions',
    'add_default': False,
    'default_additions': 'Something',
    'content': """
<head>
  <!-- head additions -->
  <!-- end of head additions -->
  <!-- custom head additions -->
  <!-- end of custom head additions -->""",
    'placement': ct.PCOM_HEADER_PLACEMENT,
    'assertEqual': """
<head>
  <!-- head additions -->
  <!-- end of head additions -->
  <!-- custom head additions -->
  <!-- end of custom head additions -->"""
    },
{   'remark': 'Test Case 3:pcom_insert_default_additions_into_html - header content, add default=True, additions',
    'additions': gb.DEFAULT_SETTINGS,
    'add_addition_placement': 'add_default_header_additions',
    'addition_placement': 'default_header_additions',
    'add_default': True,
    'default_additions': 'Something\n',
    'content': """
<head>
  <!-- head additions -->
  <!-- end of head additions -->
  <!-- custom head additions -->
  <!-- end of custom head additions -->""",
    'placement': ct.PCOM_HEADER_PLACEMENT,
    'assertEqual': """
<head>
  <!-- head additions -->
  Something
  <!-- end of head additions -->
  <!-- custom head additions -->
  <!-- end of custom head additions -->"""
    },
{   'remark': 'Test Case 4:pcom_insert_default_additions_into_html - footer content, add default=False, additions',
    'additions': gb.DEFAULT_SETTINGS,
    'add_addition_placement': 'add_default_footer_additions',
    'addition_placement': 'default_footer_additions',
    'add_default': False,
    'default_additions': 'Something\n',
    'content': """
<footer>
<!-- footer additions -->
<!-- end of footer additions -->
<!-- custom footer additions -->
<!-- end of custom footer additions -->""",
    'placement': ct.PCOM_FOOTER_PLACEMENT,
    'assertEqual': """
<footer>
<!-- footer additions -->
<!-- end of footer additions -->
<!-- custom footer additions -->
<!-- end of custom footer additions -->"""
    },
{   'remark': 'Test Case 5:pcom_insert_default_additions_into_html - footer content, add default=True, additions',
    'additions': gb.DEFAULT_SETTINGS,
    'add_addition_placement': 'add_default_footer_additions',
    'addition_placement': 'default_footer_additions',
    'add_default': True,
    'default_additions': 'Something\n',
    'content': """
<footer>
<!-- footer additions -->
<!-- end of footer additions -->
<!-- custom footer additions -->
<!-- end of custom footer additions -->""",
    'placement': ct.PCOM_FOOTER_PLACEMENT,
    'assertEqual': """
<footer>
<!-- footer additions -->
Something
<!-- end of footer additions -->
<!-- custom footer additions -->
<!-- end of custom footer additions -->"""
    },
]

test_values_2 = [\
{   'remark': 'Test Case 1:pcom_insert_additions_into_html - header - no additions',
    'args':{\
        'html':  """
<head>
  <!-- head additions -->
  <!-- end of head additions -->
  <!-- custom head additions -->
  <!-- end of custom head additions -->
<footer>""",
        'settings': gb.DEFAULT_SETTINGS,
        'placement': ct.PCOM_HEADER_PLACEMENT,
        'js_name': 'js-name__list-1.js',
        'fileroot': 'test1',
        'pagination_name': '',
        'pagination': {},
        'is_template': False,
        'is_search': False
    },
    'postlist_present': False,
    'addition_placement': 'header_additions',
    'additions': [],
    'assertEqual':"""
<head>
  <!-- head additions -->
  <!-- end of head additions -->
  <!-- custom head additions -->
  <!-- end of custom head additions -->
<footer>"""
  },
{   'remark': 'Test Case 2:pcom_insert_additions_into_html - header - additions',
    'args':{\
        'html':  """
<head>
  <!-- head additions -->
  <!-- end of head additions -->
  <!-- custom head additions -->
  <!-- end of custom head additions -->
<footer>""",
        'settings': gb.DEFAULT_SETTINGS,
        'placement': ct.PCOM_HEADER_PLACEMENT,
        'js_name': 'js-name__list-1.js',
        'fileroot': 'test1',
        'pagination_name': '',
        'pagination': {},
        'is_template': False,
        'is_search': False
    },
    'postlist_present': False,
    'addition_placement': 'header_additions',
    'additions': ['  Something', 'else'],
    'assertEqual':"""
<head>
  <!-- head additions -->
  <!-- end of head additions -->
  <!-- custom head additions -->
    Something
  else
  <!-- end of custom head additions -->
<footer>"""
  },
{   'remark': 'Test Case 3:pcom_insert_additions_into_html - footer - no additions',
    'args':{\
        'html':  """
<footer>
<!-- footer additions -->
<!-- end of footer additions -->
<!-- custom footer additions -->
<!-- end of custom footer additions -->
</body>""",
        'settings': gb.DEFAULT_SETTINGS,
        'placement': ct.PCOM_FOOTER_PLACEMENT,
        'js_name': 'js-name__list-1.js',
        'fileroot': 'test1',
        'pagination_name': '',
        'pagination': {},
        'is_template': False,
        'is_search': False
    },
    'postlist_present': False,
    'addition_placement': 'footer_additions',
    'additions': [],
    'assertEqual':"""
<footer>
<!-- footer additions -->
<!-- end of footer additions -->
<!-- custom footer additions -->
<!-- end of custom footer additions -->
</body>"""
  },
{   'remark': 'Test Case 4:pcom_insert_additions_into_html - footer - additions',
    'args':{\
        'html':  """
<footer>
<!-- footer additions -->
<!-- end of footer additions -->
<!-- custom footer additions -->
<!-- end of custom footer additions -->
</body>""",
        'settings': gb.DEFAULT_SETTINGS,
        'placement': ct.PCOM_FOOTER_PLACEMENT,
        'js_name': 'js-name__list-1.js',
        'fileroot': 'test1',
        'pagination_name': '',
        'pagination': {},
        'is_template': False,
        'is_search': False
    },
    'postlist_present': False,
    'addition_placement': 'footer_additions',
    'additions': ['  Something', 'else'],
    'assertEqual':"""
<footer>
<!-- footer additions -->
<!-- end of footer additions -->
<!-- custom footer additions -->
  Something
else
<!-- end of custom footer additions -->
</body>"""
  },

{   'remark': 'Test Case 5:pcom_insert_additions_into_html - footer - additions, postlist present',
    'args':{\
        'html':  """
<footer>
<!-- footer additions -->
<!-- end of footer additions -->
<!-- custom footer additions -->
<!-- end of custom footer additions -->
</body>""",
        'settings': gb.DEFAULT_SETTINGS,
        'placement': ct.PCOM_FOOTER_PLACEMENT,
        'js_name': 'js-name__list-1.js',
        'fileroot': 'test1',
        'pagination_name': '',
        'pagination': {},
        'is_template': False,
        'is_search': False
    },
    'postlist_present': True,
    'addition_placement': 'footer_additions',
    'additions': ['  Something', 'else'],
    'assertEqual':"""
<footer>
<!-- footer additions -->
<!-- end of footer additions -->
<!-- custom footer additions -->
  Something
else
<script src="/js/js-lists/js-name__list-1.js" data-js-constant-name="_postlist_test1"></script>
<script src="/js/postlist-handler.js"></script>
<!-- end of custom footer additions -->
</body>"""
  },
{   'remark': 'Test Case 6:pcom_insert_additions_into_html - footer - additions, postlist present - different name',
    'args':{\
        'html':  """
<footer>
<!-- footer additions -->
<!-- end of footer additions -->
<!-- custom footer additions -->
<!-- end of custom footer additions -->
</body>""",
        'settings': gb.DEFAULT_SETTINGS,
        'placement': ct.PCOM_FOOTER_PLACEMENT,
        'js_name': 'js-name__list-2.js',
        'fileroot': 'test2',
        'pagination_name': '',
        'pagination': {},
        'is_template': False,
        'is_search': False
    },
    'postlist_present': True,
    'addition_placement': 'footer_additions',
    'additions': ['  Something', 'else'],
    'assertEqual':"""
<footer>
<!-- footer additions -->
<!-- end of footer additions -->
<!-- custom footer additions -->
  Something
else
<script src="/js/js-lists/js-name__list-2.js" data-js-constant-name="_postlist_test2"></script>
<script src="/js/postlist-handler.js"></script>
<!-- end of custom footer additions -->
</body>"""
  },

{   'remark': 'Test Case 7:pcom_insert_additions_into_html - footer - additions, pagination',
    'args':{\
        'html':  """
<footer>
<!-- footer additions -->
<!-- end of footer additions -->
<!-- custom footer additions -->
<!-- end of custom footer additions -->
</body>""",
        'settings': gb.DEFAULT_SETTINGS,
        'placement': ct.PCOM_FOOTER_PLACEMENT,
        'js_name': 'js-name__list-2.js',
        'fileroot': 'test2',
        'pagination_name': 'pagination__2.js',
        'pagination': {'something': 'here'},
        'is_template': False,
        'is_search': False
    },
    'postlist_present': False,
    'addition_placement': 'footer_additions',
    'additions': ['  Something', 'else'],
    'assertEqual':"""
<footer>
<!-- footer additions -->
<!-- end of footer additions -->
<!-- custom footer additions -->
  Something
else
<script src="/js/js-lists/pagination__2.js" data-pagination-constant-name="_pagination_test2"></script>
<script src="/js/pagination-handler.js"></script>
<!-- end of custom footer additions -->
</body>"""
  },

{   'remark': 'Test Case 8:pcom_insert_additions_into_html - footer - additions, pagination - different',
    'args':{\
        'html':  """
<footer>
<!-- footer additions -->
<!-- end of footer additions -->
<!-- custom footer additions -->
<!-- end of custom footer additions -->
</body>""",
        'settings': gb.DEFAULT_SETTINGS,
        'placement': ct.PCOM_FOOTER_PLACEMENT,
        'js_name': 'js-name__list-2.js',
        'fileroot': 'test3/something',
        'pagination_name': 'pagination__3.js',
        'pagination': {'something': 'here'},
        'is_template': False,
        'is_search': False
    },
    'postlist_present': False,
    'addition_placement': 'footer_additions',
    'additions': ['  Something', 'else'],
    'assertEqual':"""
<footer>
<!-- footer additions -->
<!-- end of footer additions -->
<!-- custom footer additions -->
  Something
else
<script src="/js/js-lists/pagination__3.js" data-pagination-constant-name="_pagination_test3_something"></script>
<script src="/js/pagination-handler.js"></script>
<!-- end of custom footer additions -->
</body>"""
  },

{   'remark': 'Test Case 9:pcom_insert_additions_into_html - footer - additions, template - fileroot not in list',
    'args':{\
        'html':  """
<footer>
<!-- footer additions -->
<!-- end of footer additions -->
<!-- custom footer additions -->
<!-- end of custom footer additions -->
</body>""",
        'settings': gb.DEFAULT_SETTINGS,
        'placement': ct.PCOM_FOOTER_PLACEMENT,
        'js_name': 'js-name__list-2.js',
        'fileroot': 'test3/something',
        'pagination_name': 'pagination__3.js',
        'pagination': {},
        'is_template': True,
        'is_search': False
    },
    'postlist_present': False,
    'addition_placement': 'footer_additions',
    'additions': ['  Something', 'else'],
    'assertEqual':"""
<footer>
<!-- footer additions -->
<!-- end of footer additions -->
<!-- custom footer additions -->
  Something
else
<script src="/js/js-lists/postlist--test3_something%%$TEMPLATE_JS_NAME$%%.js" data-template-constant-name="_postlist_test3_something%%$TEMPLATE_CONSTANT_NAME$%%"></script>
<script src="/js/postlist-template-handler.js"></script>
<!-- end of custom footer additions -->
</body>"""
  },

{   'remark': 'Test Case 9:pcom_insert_additions_into_html - footer - additions, template - fileroot in list',
    'args':{\
        'html':  """
<footer>
<!-- footer additions -->
<!-- end of footer additions -->
<!-- custom footer additions -->
<!-- end of custom footer additions -->
</body>""",
        'settings': gb.DEFAULT_SETTINGS,
        'placement': ct.PCOM_FOOTER_PLACEMENT,
        'js_name': 'js-name__list-2.js',
        'fileroot': 'categories',
        'pagination_name': 'pagination__3.js',
        'pagination': {},
        'is_template': True,
        'is_search': False
    },
    'postlist_present': False,
    'addition_placement': 'footer_additions',
    'additions': ['  Something', 'else'],
    'assertEqual':"""
<footer>
<!-- footer additions -->
<!-- end of footer additions -->
<!-- custom footer additions -->
  Something
else
<script src="/js/js-lists/postlist--categories%%$TEMPLATE_JS_NAME$%%.js" data-template-constant-name="_postlist_categories%%$TEMPLATE_CONSTANT_NAME$%%"></script>
<script src="/js/postlist-template-handler.js"></script>
<!-- end of custom footer additions -->
</body>"""
  },

{   'remark': 'Test Case 10:pcom_insert_additions_into_html - footer - additions, template, search - fileroot in list',
    'args':{\
        'html':  """
<footer>
<!-- footer additions -->
<!-- end of footer additions -->
<!-- custom footer additions -->
<!-- end of custom footer additions -->
</body>""",
        'settings': gb.DEFAULT_SETTINGS,
        'placement': ct.PCOM_FOOTER_PLACEMENT,
        'js_name': 'js-name__list-2.js',
        'fileroot': 'categories',
        'pagination_name': 'pagination__3.js',
        'pagination': {},
        'is_template': True,
        'is_search': True,
    },
    'postlist_present': False,
    'addition_placement': 'footer_additions',
    'additions': ['  Something', 'else'],
    'assertEqual':"""
<footer>
<!-- footer additions -->
<!-- end of footer additions -->
<!-- custom footer additions -->
  Something
else
<script src="/js/search-handler.js"></script>
<script src="/js/js-lists/search--config.js"></script>

<!-- end of custom footer additions -->
</body>"""
  },

]

test_values_3 = [\
{   'remark': 'Test Case 1:pcom_get_insert_info - empty content',
    'html_array': [],
    'assertEqual': []
    },
{   'remark': 'Test Case 2:pcom_get_insert_info - content but no insert',
    'html_array': ['Something', 'here', 'to read'],
    'assertEqual': []
    },
{   'remark': 'Test Case 3:pcom_get_insert_info - content and insert',
    'html_array': ['Something', 'INSERT=[MAIN:puppies.txt]:', 'to read'],
    'assertEqual': [\
        {'filename': 'puppies.txt',
        'placement': 'MAIN',
        'index': 1,
        'valid_entry': ct.PCOM_NOT_TRIED,
        'content': ''}
    ]
    },
{   'remark': 'Test Case 4:pcom_get_insert_info - content and 2 inserts',
    'html_array': ['Something', 'INSERT=[MAIN:puppies.txt]:',
    'to read', 'INSERT=[SIDEBAR:puppies2.txt]:'],
    'assertEqual': [\
        {'filename': 'puppies.txt',
        'placement': 'MAIN',
        'index': 1,
        'valid_entry': ct.PCOM_NOT_TRIED,
        'content': ''},
        {'filename': 'puppies2.txt',
        'placement': 'SIDEBAR',
        'index': 3,
        'valid_entry': ct.PCOM_NOT_TRIED,
        'content': ''}
    ]
    },
]


test_values_4 = [\
{   'remark': 'Test Case 1:pcom_get_postlists_info - empty content',
    'html_array': [],
    'fileroot': 'test2',
    'assertEqual': []
    },
{   'remark': 'Test Case 2:pcom_get_postlists_info - content but no insert',
    'html_array': ['Something', 'here', 'to read'],
    'fileroot': 'test2/things',
    'assertEqual': []
    },
{   'remark': 'Test Case 3:pcom_get_postlists_info - content and insert',
    'html_array': ['Something', 'POSTLIST=[test1.post,!!test3.post,test2.post,!!about.page:1:True]:', 'to read'],
    'fileroot': 'test2/things',
    'assertEqual': [\
        { 'index': 1,
          'fileroot': 'test2_things',
          'ppp': '1',
          'manual_sticky': 'True',
          'content': 'test1.post,!!test3.post,test2.post,!!about.page'}
    ]
    },
{   'remark': 'Test Case 4:pcom_get_postlists_info - content and 2 inserts',
    'html_array': ['Something', 'POSTLIST=[test1.post,!!test3.post,test2.post,!!about.page:1:True]:',
    'to read', 'POSTLIST=[test1.post,test3.post,test4.post:4:False]:'],
    'fileroot': 'test4',
    'assertEqual': [\
        { 'index': 1,
          'fileroot': 'test4',
          'ppp': '1',
          'manual_sticky': 'True',
          'content': 'test1.post,!!test3.post,test2.post,!!about.page'},
        { 'index': 3,
          'fileroot': 'test4',
          'ppp': '4',
          'manual_sticky': 'False',
          'content': 'test1.post,test3.post,test4.post'},
    ]
    },
]

test_values_5 = [\
{   'remark': 'Test Case 1:pcom_insert_postlist_wrapper - empty content',
    'html_array': [],
    'postlist_info': {},
    'outlog': 'Something',
    'assertEqual': {\
        'array': [],
        'log': 'Something'
        }
    },
{   'remark': 'Test Case 2:pcom_insert_postlist_wrapper - array and 1 info',
    'html_array': ['Something','POSTLIST','here'],
    'postlist_info': [\
        { 'index': 1 }
     ],
    'outlog': 'Something',
    'assertEqual': {\
        'array': ['Something','      <div class="pm-postlist-entries clearfix-small postlist-list-1">\n      </div><!-- end postlist entries data -->\n      <div class="pm-postlist-pagination clearfix-small" data-postlist-name="postlist-list-1">\n      </div><!-- end of .pm-postlist-pagination -->\n','here'],
        'log': 'Something'
        }
    },
{   'remark': 'Test Case 3:pcom_insert_postlist_wrapper - array and 2 infos',
    'html_array': ['Something','POSTLIST','here',''],
    'postlist_info': [\
        { 'index': 1 },
        { 'index': 3 }
     ],
    'outlog': 'Something here',
    'assertEqual': {\
        'array': ['Something',
        '      <div class="pm-postlist-entries clearfix-small postlist-list-1">\n      </div><!-- end postlist entries data -->\n      <div class="pm-postlist-pagination clearfix-small" data-postlist-name="postlist-list-1">\n      </div><!-- end of .pm-postlist-pagination -->\n',
        'here',
        '      <div class="pm-postlist-entries clearfix-small postlist-list-2">\n      </div><!-- end postlist entries data -->\n      <div class="pm-postlist-pagination clearfix-small" data-postlist-name="postlist-list-2">\n      </div><!-- end of .pm-postlist-pagination -->\n'
        ],
        'log': 'Something here'
        }
    },
]

test_values_6 = [\
{   'remark': 'Test Case 1:pcom_get_content_meta_info - empty array',
    'html_array': [],
    'assertEqual': []
    },
{   'remark': 'Test Case 2:pcom_get_content_meta_info - content but no meta',
    'html_array': ['Something', 'here', 'to read'],
    'assertEqual': []
    },
{   'remark': 'Test Case 3:pcom_get_insert_info - content and empty meta',
    'html_array': ['Something', 'CONTENT_META=[MAIN:]:', 'to read'],
    'assertEqual': [\
        {'index': 1,
        'placement': 'MAIN',
        'title': False,
        'category': False,
        'author': False,
        'date_created': False,
        'date_modified': False,
        'show_time': False}
        ]
    },
{   'remark': 'Test Case 4:pcom_get_insert_info - content and full meta',
    'html_array': ['Something', 'CONTENT_META=[MAIN:title,category,author,date_created,date_modified,show_time]:', 'to read'],
    'assertEqual': [\
        {'index': 1,
        'placement': 'MAIN',
        'title': True,
        'category': True,
        'author': True,
        'date_created': True,
        'date_modified': True,
        'show_time': True }
        ]
    },
]

test_values_7 = [\
{   'remark': 'Test Case 1:pcom_get_comma_list - empty',
    'list': '',
    'assertEqual': ['']
    },
{   'remark': 'Test Case 2:pcom_get_comma_list - one entry',
    'list': 'four',
    'assertEqual': ['four']
    },
{   'remark': 'Test Case 3:pcom_get_comma_list - multiple',
    'list': 'four,one,two',
    'assertEqual': ['four','one','two']
    },
]

test_values_8 = [\
{   'remark': 'Test Case 1:pcom_assign_content_meta - empty',
    'list': '',
    'assertEqual': {\
        'title': False,
        'category': False,
        'author': False,
        'date_created': False,
        'date_modified': False,
        'show_time': False
        }
    },
{   'remark': 'Test Case 2:pcom_assign_content_meta - one entry not in list',
    'list': 'four',
    'assertEqual': {\
        'title': False,
        'category': False,
        'author': False,
        'date_created': False,
        'date_modified': False,
        'show_time': False
        }
    },
{   'remark': 'Test Case 3:pcom_assign_content_meta - multiple but not in list',
    'list': 'four,one,two',
    'assertEqual': {\
        'title': False,
        'category': False,
        'author': False,
        'date_created': False,
        'date_modified': False,
        'show_time': False
        }
    },
{   'remark': 'Test Case 4:pcom_assign_content_meta - all options list',
    'list': 'title,category,author,date_created,date_modified,show_time',
    'assertEqual': {\
        'title': True,
        'category': True,
        'author': True,
        'date_created': True,
        'date_modified': True,
        'show_time': True
        }
    },
{   'remark': 'Test Case 5:pcom_assign_content_meta - all options list reversed',
    'list': 'show_time,date_modified,date_created,author,category,title',
    'assertEqual': {\
        'title': True,
        'category': True,
        'author': True,
        'date_created': True,
        'date_modified': True,
        'show_time': True
        }
    },
]

test_values_9 = [\
{   'remark': 'Test Case 1:pcom_strip_string - empty',
    'content': '',
    'assertEqual': ''
    },
{   'remark': 'Test Case 2:pcom_strip_string - numbers and letters',
    'content': '454huh454501910012345678',
    'assertEqual': '454huh454501910012345678'
    },
{   'remark': 'Test Case 3:pcom_strip_string - special characters included',
    'content': '78223=-{huh#$}',
    'assertEqual': '78223huh'
    },
]

test_values_10 = [\
{   'remark': 'Test Case 1:pcom_create_raw_content - empty content and meta keys',
    'content': '',
    'meta': {\
        'page_title': '',
        'page_description': '',
        'page_extract': ''
    },
    'assertEqual': 'NONE\n\n\n\n\n'
    },
{   'remark': 'Test Case 2:pcom_create_raw_content - content and empty meta keys',
    'content': """
<head>
Content head_start_end
</head>
<section id="main">
More here
</section>
<style>
<!-- things here to add {{}} -->
</style>
<script src="this script" />
<footer>
<div class="footer content">
    <div class="inner1"><h1>A title</h1></div>
    <div class="inner2"><p>Lots of data to talk about</p></div>
    <ul>
        <li>one</li>
        <li>Another here what!</li>
    </ul>
</div>
</footer>
    """,
    'meta': {\
        'page_title': '',
        'page_description': '',
        'page_extract': ''
    },
    'assertEqual': """
More hereA title
Lots of data to talk aboutone
Another here what!
    """
    },
{   'remark': 'Test Case 3:pcom_create_raw_content - content and meta keys',
    'content': """
<head>
Content head_start_end
</head>
<section id="main">
More here
</section>
<style>
<!-- things here to add {{}} -->
</style>
<script src="this script" />
<footer>
<div class="footer content">
    <div class="inner1"><h1>A title</h1></div>
    <div class="inner2"><p>Lots of data to talk about</p></div>
    <ul>
        <li>one</li>
        <li>Another here what!</li>
    </ul>
</div>
</footer>
    """,
    'meta': {\
        'page_title': 'A name',
        'page_description': 'A description',
        'page_extract': 'An extract'
    },
    'assertEqual': """
More hereA title
Lots of data to talk aboutone
Another here what!

A name
A description
An extract
    """
    },
]
