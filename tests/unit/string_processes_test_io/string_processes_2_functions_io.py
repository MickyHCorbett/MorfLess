#
import libraries.constants as ct
import libraries.globals as gb

from collections import OrderedDict
#

test_values_1 = [\
{   'remark': 'Test Case 1:pcom_create_template_fileroot - fileroot empty',
    'fileroot': '',
    'template_types': {\
        'post': 'entries',
        'tags': 'markers'
    },
    'assertEqual': ''
    },

{   'remark': 'Test Case 2:pcom_create_template_fileroot - fileroot not a template',
    'fileroot': 'this',
    'template_types': {\
        'post': 'entries',
        'tags': 'markers'
    },
    'assertEqual': 'this'
    },

{   'remark': 'Test Case 3:pcom_create_template_fileroot - fileroot template - post',
    'fileroot': 'post',
    'template_types': {\
        'post': 'entries',
        'tags': 'markers'
    },
    'assertEqual': 'entries'
    },

{   'remark': 'Test Case 4:pcom_create_template_fileroot - fileroot template - tags',
    'fileroot': 'tags',
    'template_types': {\
        'post': 'entries',
        'tags': 'markers'
    },
    'assertEqual': 'markers'
    },

]

test_values_2 = [\
{   'remark': 'Test Case 1:pcom_get_template_key - fileroot empty',
    'fileroot': '',
    'template_types': {\
        'post': 'entries',
        'tags': 'markers'
    },
    'assertEqual': ''
    },

{   'remark': 'Test Case 2:pcom_get_template_key - fileroot not a template',
    'fileroot': 'this',
    'template_types': {\
        'post': 'entries',
        'tags': 'markers'
    },
    'assertEqual': 'this'
    },

{   'remark': 'Test Case 3:pcom_get_template_key - fileroot template - key = post',
    'fileroot': 'post',
    'template_types': {\
        'post': 'entries',
        'tags': 'markers'
    },
    'assertEqual': 'post'
    },

{   'remark': 'Test Case 4:pcom_get_template_key - fileroot template - value of post',
    'fileroot': 'entries',
    'template_types': {\
        'post': 'entries',
        'tags': 'markers'
    },
    'assertEqual': 'post'
    },

{   'remark': 'Test Case 5:pcom_get_template_key- fileroot template - tags/entry',
    'fileroot': 'tags/entry',
    'template_types': {\
        'tags_entry': 'entries-of-tags',
        'tags': 'markers'
    },
    'assertEqual': 'tags_entry'
    },

{   'remark': 'Test Case 6:pcom_get_template_key- fileroot template - value of tags/entry',
    'fileroot': 'entries-of-tags',
    'template_types': {\
        'tags_entry': 'entries-of-tags',
        'tags': 'markers'
    },
    'assertEqual': 'tags_entry'
    },
]

test_values_3 = [\
{   'remark': 'Test Case 1:pcom_replace_quotes - empty',
    'text': '',
    'assertEqual': ''
    },
{   'remark': 'Test Case 2:pcom_replace_quotes - quotes',
    'text': '"Some text"',
    'assertEqual': '&#34;Some text&#34;'
    },
{   'remark': 'Test Case 3:pcom_replace_quotes - apostrophe',
    'text': "'Some text'",
    'assertEqual': '&#39;Some text&#39;'
    },
{   'remark': 'Test Case 4:pcom_replace_quotes - ignore',
    'text': ct.PCOM_META_IGNORE_QUOTES + "'Some text'",
    'assertEqual': "'Some text'"
    },
]

test_values_4 = [\
{   'remark': 'Test Case 1:pcom_find_author_full_name - empty - name in authors',
    'name': '',
    'authors': {'name': 'NONE'},
    'assertEqual': ''
    },
{   'remark': 'Test Case 2:pcom_find_author_full_name - non empty - name in authors',
    'name': 'terry',
    'authors': {'name': 'NONE'},
    'assertEqual': 'terry'
    },
{   'remark': 'Test Case 3:pcom_find_author_full_name - non empty - not in authors',
    'name': 'terry',
    'authors': [\
        { 'name': 'Bill Jones', 'shortname': 'Billy' },
        { 'name': 'Knut Manford', 'shortname': 'KM' }
    ],
    'assertEqual': 'terry'
    },
{   'remark': 'Test Case 4:pcom_find_author_full_name - non empty name',
    'name': 'Bill Jones',
    'authors': [\
        { 'name': 'Bill Jones', 'shortname': 'Billy' },
        { 'name': 'Knut Manford', 'shortname': 'KM' }
    ],
    'assertEqual': 'Bill Jones'
    },
{   'remark': 'Test Case 5:pcom_find_author_full_name - non empty shortname',
    'name': 'KM',
    'authors': [\
        { 'name': 'Bill Jones', 'shortname': 'Billy' },
        { 'name': 'Knut Manford', 'shortname': 'KM' }
    ],
    'assertEqual': 'Knut Manford'
    },
]
