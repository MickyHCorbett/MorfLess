#
import libraries.constants as ct
import libraries.globals as gb
import libraries.schematics as sch

from collections import OrderedDict

from unit.lists_test_io.lists_supplemental import POSTLIST_1, POST_ENTRY_1
#

test_values_1 = [\
{   'remark': 'Test 1: pcom_update_postlist - empty list',
    'inputs': {\
        'postlist': [],
        'postname': 'something',
        'url': 'this/url',
        'meta': {},
        'date_format': ct.PCOM_UK_DATE_FORMAT,
        'type': 'post',
        'settings': gb.DEFAULT_SETTINGS
    },
    'assertEqual': [],
    'assertNotEqual': []
    }
]

test_values_2 = [\
{   'remark': 'Test 2 pcom_update_postlist - update test1.post',
    'inputs': {\
        'postlist': POSTLIST_1,
        'postname': 'test1.post',
        'url': 'this/url',
        'meta': {\
            'page_title': 'Something',
            'page_description': 'A short description',
            'authors': 'Charles',
            'categories': 'stuff',
            'thumb_link': 'default/image/link.png',
            'page_extract': 'An extract',
            'url': 'this/link',
            'meta_valid': ct.PCOM_META_VALID,
            'sticky': '',
            'unlisted': False}
        ,
        'date_format': ct.PCOM_UK_DATE_FORMAT,
        'type': 'post',
        'settings': gb.DEFAULT_SETTINGS
    },
    'post_index': POSTLIST_1['post_index'],
    'no_posts': POSTLIST_1['no_posts'],
    'entry': 'test1.post',
    'assertEqual': {\
        "index": 5,
        "type": "post",
        "url": "this/link",
        "title": "Something",
        "postname": "test1.post",
        "description": "A short description",
        "extract": "An extract",
        "categories": ['stuff'],
        "authors": ['Charles'],
        "thumbnail": "default/image/link.png",
        "sticky": ""
    },
    'assertNotEqual': []
    },

{   'remark': 'Test 3: pcom_update_postlist - create new_new.post',
    'inputs': {\
        'postlist': POSTLIST_1,
        'postname': 'new_new.post',
        'url': 'this/url',
        'meta': {\
            'page_title': 'Something',
            'page_description': 'A short description',
            'authors': 'Charles',
            'categories': 'stuff',
            'thumb_link': 'default/image/link.png',
            'page_extract': 'An extract',
            'url': 'this/link',
            'meta_valid': ct.PCOM_META_VALID,
            'sticky': '',
            'unlisted': False}
        ,
        'date_format': ct.PCOM_UK_DATE_FORMAT,
        'type': 'post',
        'settings': gb.DEFAULT_SETTINGS
    },
    'post_index': POSTLIST_1['post_index']+1,
    'no_posts': POSTLIST_1['no_posts']+1,
    'entry': 'new_new.post',
    'assertEqual': {\
        "index": 7,
        "type": "post",
        "url": "this/url",
        "title": "Something",
        "postname": "new_new.post",
        "description": "A short description",
        "extract": "An extract",
        "categories": ['stuff'],
        "authors": ['Charles'],
        "thumbnail": "default/image/link.png",
        "sticky": ""
    },
    'assertNotEqual': []
    }

]

test_values_3 = [\
{   'remark': 'Test 1: pcom_update_postlist_entry - current post',
    'inputs': {\
        'index': 5,
        'post': POST_ENTRY_1,
        'postname': 'test5.post',
        'url': 'this/url',
        'meta': {\
            'page_title': 'Something',
            'page_description': 'A short description',
            'authors': 'Micky,Mark,Luke',
            'categories': 'stuff-to-look-at,another thing',
            'thumb_link': 'default/image/link.png',
            'page_extract': 'An extract to read',
            'url': 'this/link/here',
            'meta_valid': ct.PCOM_META_VALID,
            'sticky': 'sticky',
            'unlisted': False}
        ,
        'date': '56/78/90',
        'time': '12:34:23',
        'type': 'post',
        'settings': gb.DEFAULT_SETTINGS,
        'new': False
    },
    'entry': 'test5.post',
    'assertEqual': {\
        "index": POST_ENTRY_1['index'],
        "type": "post",
        "url": "this/link/here",
        "title": "Something",
        'date_modified': '56/78/90',
        'creation_date': POST_ENTRY_1['creation_date'],
        'time_modified': '12:34:23',
        'creation_time': POST_ENTRY_1['creation_time'],
        "postname": "test5.post",
        "description": "A short description",
        "extract": "An extract to read",
        "categories": ['stuff-to-look-at', 'another thing'],
        "authors": ['Micky','Mark','Luke'],
        "thumbnail": "default/image/link.png",
        "sticky": "sticky"
    },
    'assertNotEqual': []
    },
{   'remark': 'Test 2: pcom_update_postlist_entry - new post',
    'inputs': {\
        'index': 5,
        'post': POST_ENTRY_1,
        'postname': 'test6.post',
        'url': 'this/url',
        'meta': {\
            'page_title': 'Something',
            'page_description': 'A short description',
            'authors': 'Micky,Mark,Luke',
            'categories': 'stuff-to-look-at,another thing',
            'thumb_link': 'default/image/link.png',
            'page_extract': 'An extract to read',
            'url': 'this/link/here',
            'meta_valid': ct.PCOM_META_VALID,
            'sticky': 'sticky',
            'unlisted': False}
        ,
        'date': '56/78/90',
        'time': '12:34:23',
        'type': 'post',
        'settings': gb.DEFAULT_SETTINGS,
        'new': True
    },
    'entry': 'test5.post',
    'assertEqual': {\
        "index": 5,
        "type": "post",
        "url": "this/url",
        "title": "Something",
        'date_modified': '56/78/90',
        'creation_date': '56/78/90',
        'time_modified': '12:34:23',
        'creation_time': '12:34:23',
        "postname": "test6.post",
        "description": "A short description",
        "extract": "An extract to read",
        "categories": ['stuff-to-look-at', 'another thing'],
        "authors": ['Micky','Mark','Luke'],
        "thumbnail": "default/image/link.png",
        "sticky": "sticky"
    },
    'assertNotEqual': []
    }
]
