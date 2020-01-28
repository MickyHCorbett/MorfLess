#
import libraries.constants as ct
import libraries.globals as gb

from collections import OrderedDict
#

test_values_1 = [\
{   'remark': 'Test Case 1:pcom_process_json - JSON compliant data',
    'input': """
                {
                    "variable1": [
                        "variable2"
                    ],
                    "variable3": {
                        "variable4" : "this",
                        "variable5" : "that"
                    }
                }
            """,
    'assertEqual': (OrderedDict([('variable1', ['variable2']), ('variable3', OrderedDict([('variable4', 'this'), ('variable5', 'that')]))]), ''),
    'assertNotEqual': { 'variable1': ['variable2'],
    'variable3': { 'variable4': 'this', 'variable5': 'that'} }
    },


{   'remark': 'Test Case 2:pcom_process_json - non-compliant data',
    'input': """
                {
                    "variable1" [
                        'variable2'
                    ]
                    "variable3": {
                        "variable4" : "this"
                        "variable5" : "that"
                    }
                }

                """,
    'assertEqual': ('NONE', 'JSON_FILE load error'),
    'assertNotEqual': (OrderedDict([('variable1', ['variable2']), ('variable3', OrderedDict([('variable4', 'this'), ('variable5', 'that')]))]), '')
    },

{   'remark': 'Test Case 3:pcom_process_json - no data',
    'input': '',
    'assertEqual': ('NONE', 'JSON_FILE load error'),
    'assertNotEqual': (OrderedDict([('variable1', ['variable2']), ('variable3', OrderedDict([('variable4', 'this'), ('variable5', 'that')]))]), '')
    },

{   'remark': 'Test Case 4:pcom_process_json - data = NONE',
    'input': ct.PCOM_NO_ENTRY,
    'assertEqual': ('NONE', ''),
    'assertNotEqual': (OrderedDict([('variable1', ['variable2']), ('variable3', OrderedDict([('variable4', 'this'), ('variable5', 'that')]))]), '')
    },

{   'remark': 'Test Case 5:pcom_process_json - JSON compliant data',
    'input': """
                {
                    "variable1": [
                        "variable2"
                    ],
                    "variable3": "that",
                    "variable4": "that again",
                    "variable5": "something"
                }
            """,
    'assertEqual': (OrderedDict([('variable1', ['variable2']), ('variable3', 'that'),('variable4', 'that again'),('variable5', 'something') ]),''),
    'assertNotEqual': { 'variable1': ['variable2'],
    'variable3': { 'variable4': 'this', 'variable5': 'that'} }
    }
]

test_values_2 = [\
{   'remark': 'Test Case 1:pcom_write_json - JSON compliant data',
    'input' :  { 'variable1': ['variable2'],
        'variable3': { 'variable4': 'this', 'variable5': 'that'} },
    'assertEqual': """

{
    "variable1": [
        "variable2"
    ],
    "variable3": {
        "variable4": "this",
        "variable5": "that"
    }
}

""" },

{   'remark': 'Test Case 3:pcom_write_json - no data',
    'input' : '',
    'assertEqual': '""'
    },

{   'remark': 'Test Case 3:pcom_write_json - strings',
    'input' : 'string',
    'assertEqual': '"string"'
    }
]

test_values_3 = [\
{   'remark': 'Test Case 1:pcom_create_url - post1.post, meta: url, empty',
    'inputs' :  {\
            'name': 'post1.post',
            'meta_url': ''
            },
    'assertEqual': {\
            'outkey': '/post1/',
            'type' : 'post'}
            },

{   'remark': 'Test Case 2:pcom_create_url - page1.page, meta: url, empty',
    'inputs' :  {\
            'name': 'page1.page',
            'meta_url': ''
            },
    'assertEqual': {\
            'outkey': '/page1/',
            'type' : 'page'}
            },

{   'remark': 'Test Case 3:pcom_create_url - index.page, meta: url, empty',
    'inputs' :  {\
            'name': 'index.page',
            'meta_url': ''
            },
    'assertEqual': {\
            'outkey': '/',
            'type' : 'page'}
            },

{   'remark': 'Test Case 4:pcom_create_url - index.page, meta: url = /this_url/',
    'inputs' :  {\
            'name': 'index.page',
            'meta_url': '/this_url/'
            },
    'assertEqual': {\
            'outkey': '/',
            'type' : 'page'}
            },

{   'remark': 'Test Case 5:pcom_create_url - 404.page, meta: url, empty',
    'inputs' :  {\
            'name': '404.page',
            'meta_url': ''
            },
    'assertEqual': {\
            'outkey': '404.html',
            'type' : 'page'}
            },

{   'remark': 'Test Case 6:pcom_create_url - 404.page, meta: url = /this_url/',
    'inputs' :  {\
            'name': '404.page',
            'meta_url': '/this_url/'
            },
    'assertEqual': {\
            'outkey': '404.html',
            'type' : 'page'}
            },

{   'remark': 'Test Case 7:pcom_create_url - post1.post, meta: url = /this_post/',
    'inputs' :  {\
            'name': 'post1.post',
            'meta_url': '/this_post/'
            },
    'assertEqual': {\
            'outkey': '/this_post/',
            'type' : 'post'}
            },

{   'remark': 'Test Case 8:pcom_create_url - page-of-all-things.page, meta: url = /this_page/here/',
    'inputs' :  {\
            'name': 'page-of-all-things.page',
            'meta_url': '/this_page/here/'
            },
    'assertEqual': {\
            'outkey': '/this_page/here/',
            'type' : 'page'}
            }

]


test_values_4 = [\
{   'remark': 'Test Case 1:pcom_filter_template - posts, template not search',
    'input' : 'posts',
    'assertEqual': {\
            'is_template': True,
            'is_search' : False}
            },
{   'remark': 'Test Case 2:pcom_filter_template - authors, template not search',
    'input' : 'authors',
    'assertEqual': {\
            'is_template': True,
            'is_search' : False}
            },
{   'remark': 'Test Case 3:pcom_filter_template - categories, template not search',
    'input' : 'categories',
    'assertEqual': {\
            'is_template': True,
            'is_search' : False}
            },
{   'remark': 'Test Case 4:pcom_filter_template - archive, template not search',
    'input' : 'archive',
    'assertEqual': {\
            'is_template': True,
            'is_search' : False}
            },
{   'remark': 'Test Case 5:pcom_filter_template - search, template and search',
    'input' : 'search',
    'assertEqual': {\
            'is_template': True,
            'is_search' : True}
            },
{   'remark': 'Test Case 6:pcom_filter_template - post1, not template not search',
    'input' : 'post1',
    'assertEqual': {\
            'is_template': False,
            'is_search' : False}
            }
]
