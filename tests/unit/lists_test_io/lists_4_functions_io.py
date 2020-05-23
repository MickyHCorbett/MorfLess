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

test_values_4 = [\
{   'remark': 'Test 1: pcom_find_post_pagination - no postlist',
    'inputs': {\
        'postlist': [],
        'postname': 'test1.post',
        'type': True
    },
    'assertEqual': {\
        "found": False,
        "out": {\
            'next_url': ct.PCOM_NO_ENTRY,
            'prev_url': ct.PCOM_NO_ENTRY,
            'next_title': ct.PCOM_NO_ENTRY,
            'prev_title': ct.PCOM_NO_ENTRY
            }
        }
    },
{   'remark': 'Test 2: pcom_find_post_pagination - test3.post - prev (more recent) links only',
    'inputs': {\
        'postlist': POSTLIST_1,
        'postname': 'test3.post',
        'type': True
    },
    'assertEqual': {\
        "found": True,
        "out": {\
            'next_url': ct.PCOM_NO_ENTRY,
            'prev_url': "/test2/",
            'next_title': ct.PCOM_NO_ENTRY,
            'prev_title': "A new post - second coming - redux"
            }
        }
    },
{   'remark': 'Test 3: pcom_find_post_pagination - test2.post - next and prev',
    'inputs': {\
        'postlist': POSTLIST_1,
        'postname': 'test2.post',
        'type': True
    },
    'assertEqual': {\
        "found": True,
        "out": {\
            'next_url': "/test3-post-something-new/",
            'prev_url': "/test1-the-first-post/",
            'next_title': "A new post",
            'prev_title': "A new post"
            }
        }
    },
{   'remark': 'Test 4: pcom_find_post_pagination - about-this.post - next (older) only',
    'inputs': {\
        'postlist': POSTLIST_1,
        'postname': 'about-this.post',
        'type': True
    },
    'assertEqual': {\
        "found": True,
        "out": {\
            'next_url': "/test1-the-first-post/",
            'prev_url': ct.PCOM_NO_ENTRY,
            'next_title': "A new post",
            'prev_title': ct.PCOM_NO_ENTRY
            }
        }
    },
{   'remark': 'Test 5: pcom_find_post_pagination - about.page ',
    'inputs': {\
        'postlist': POSTLIST_1,
        'postname': 'about.page',
        'type': False
    },
    'assertEqual': {\
        "found": True,
        "out": {\
            'next_url': "/contact/",
            'prev_url': ct.PCOM_NO_ENTRY,
            'next_title': "Contact",
            'prev_title': ct.PCOM_NO_ENTRY
            }
        }
    },
{   'remark': 'Test 6: pcom_find_post_pagination - about.page but type = post',
    'inputs': {\
        'postlist': POSTLIST_1,
        'postname': 'about.page',
        'type': True
    },
    'assertEqual': {\
        "found": False,
        "out": {\
            'next_url': ct.PCOM_NO_ENTRY,
            'prev_url': ct.PCOM_NO_ENTRY,
            'next_title': ct.PCOM_NO_ENTRY,
            'prev_title': ct.PCOM_NO_ENTRY
            }
        }
    },

]

test_values_5 = [\
{   'remark': 'Test 1: pcom_find_manual_pagination - no next prev',
    'inputs': {\
        'postlist': POSTLIST_1,
        'next': '',
        'prev': ''
    },
    'assertEqual': {\
        "found": False,
        "out": {\
            'next_url': ct.PCOM_NO_ENTRY,
            'prev_url': ct.PCOM_NO_ENTRY,
            'next_title': ct.PCOM_NO_ENTRY,
            'prev_title': ct.PCOM_NO_ENTRY
            }
        }
    },
{   'remark': 'Test 2: pcom_find_manual_pagination - prev - no next',
    'inputs': {\
        'postlist': POSTLIST_1,
        'next': '',
        'prev': 'about.page'
    },
    'assertEqual': {\
        "found": True,
        "out": {\
            'next_url': ct.PCOM_NO_ENTRY,
            'prev_url': "/about/",
            'next_title': ct.PCOM_NO_ENTRY,
            'prev_title': "About Morfless"
            }
        }
    },
{   'remark': 'Test 3: pcom_find_manual_pagination - next - no prev',
    'inputs': {\
        'postlist': POSTLIST_1,
        'next': '',
        'prev': 'test2.post'
    },
    'assertEqual': {\
        "found": True,
        "out": {\
            'next_url': ct.PCOM_NO_ENTRY,
            'prev_url': "/test2/",
            'next_title': ct.PCOM_NO_ENTRY,
            'prev_title': "A new post - second coming - redux"
            }
        }
    },
{   'remark': 'Test 4: pcom_find_manual_pagination - both',
    'inputs': {\
        'postlist': POSTLIST_1,
        'next': 'test3.post',
        'prev': 'test1.post'
    },
    'assertEqual': {\
        "found": True,
        "out": {\
            'next_url': "/test3-post-something-new/",
            'prev_url': "/test1-the-first-post/",
            'next_title': "A new post",
            'prev_title': "A new post"
            }
        }
    }
]

test_values_6 = [\
{   'remark': 'Test 1: pcom_get_pagination_info - no list data',
    'inputs': {\
        'html': '',
        'postlist': POSTLIST_1,
        'postname': 'this.post',
        'fileroot': 'this'
    },
    'assertEqual': {\
        "array": [],
        "info": {}
        }
    },
{   'remark': 'Test 2: pcom_get_pagination_info - array but no tags',
    'inputs': {\
        'html': '<div class="something">\nMARKER\n</div>',
        'postlist': POSTLIST_1,
        'postname': 'this.post',
        'fileroot': 'this'
    },
    'assertEqual': {\
        "array": ['<div class="something">\n','MARKER\n','</div>'],
        "info": {}
        }
    },
{   'remark': 'Test 3: pcom_get_pagination_info - tags no manual - ref not in list - no pagination',
    'inputs': {\
        'html': ('<div class="something">\n'
                + ct.PCOM_INSERT_PAGINATION_TAG_OPEN + 'MAIN:'
                + '' + ':' + '' + ct.PCOM_INSERT_PAGINATION_TAG_CLOSE + ct.NL
                + '</div>'),
        'postlist': POSTLIST_1,
        'postname': 'this.post',
        'fileroot': 'this'
    },
    'assertEqual': {\
        "array": ['<div class="something">\n', '', '</div>'],
        "info": {\
            'index': 1,
            'fileroot': 'this',
            'next_ref': '',
            'prev_ref': '',
            'postname': 'this.post',
            'type': False
            }
        }
    },
{   'remark': 'Test 4: pcom_get_pagination_info - tags no manual - ref in list',
    'inputs': {\
        'html': ('<div class="something">\n'
                + ct.PCOM_INSERT_PAGINATION_TAG_OPEN + 'MAIN:'
                + '' + ':' + '' + ct.PCOM_INSERT_PAGINATION_TAG_CLOSE + ct.NL
                + '</div>'),
        'postlist': POSTLIST_1,
        'postname': 'test1.post',
        'fileroot': 'test1'
    },
    'assertEqual': {\
        "array": [\
        '<div class="something">\n',
        '\n<div class="main-outer clearfix-small">\n  <div class="main-inner clearfix-small">\n    <div class="pm-post-pagination">\n    </div><!-- end of .pm-post-pagination -->\n\n  </div><!-- end of .main-inner -->\n</div><!-- end of .main-outer -->',
        '</div>'],
        "info": {\
            'index': 1,
            'fileroot': 'test1',
            'next_ref': '',
            'prev_ref': '',
            'postname': 'test1.post',
            'type': True
            }
        }
    },
{   'remark': 'Test 5: pcom_get_pagination_info - tags no manual - ref in list - custom class',
    'inputs': {\
        'html': ('<div class="something">\n'
                + ct.PCOM_INSERT_PAGINATION_TAG_OPEN + 'MAIN:'
                + 'custom-1' + ':' + '' + ct.PCOM_INSERT_PAGINATION_TAG_CLOSE + ct.NL
                + '</div>'),
        'postlist': POSTLIST_1,
        'postname': 'test1.post',
        'fileroot': 'test1'
    },
    'assertEqual': {\
        "array": [\
        '<div class="something">\n',
        '\n<div class="main-outer clearfix-small custom-1">\n  <div class="main-inner clearfix-small custom-1">\n    <div class="pm-post-pagination custom-1">\n    </div><!-- end of .pm-post-pagination -->\n\n  </div><!-- end of .main-inner -->\n</div><!-- end of .main-outer -->',
        '</div>'],
        "info": {\
            'index': 1,
            'fileroot': 'test1',
            'next_ref': '',
            'prev_ref': '',
            'postname': 'test1.post',
            'type': True
            }
        }
    },
{   'remark': 'Test 6: pcom_get_pagination_info - tags manual - next ref in list',
    'inputs': {\
        'html': ('<div class="something">\n'
                + ct.PCOM_INSERT_PAGINATION_TAG_OPEN + 'MAIN:'
                + '' + ':' + 'this.ref,' + ct.PCOM_INSERT_PAGINATION_TAG_CLOSE + ct.NL
                + '</div>'),
        'postlist': POSTLIST_1,
        'postname': 'test1.post',
        'fileroot': 'test1'
    },
    'assertEqual': {\
        "array": [\
        '<div class="something">\n',
        '\n<div class="main-outer clearfix-small">\n  <div class="main-inner clearfix-small">\n    <div class="pm-post-pagination">\n    </div><!-- end of .pm-post-pagination -->\n\n  </div><!-- end of .main-inner -->\n</div><!-- end of .main-outer -->',
        '</div>'],
        "info": {\
            'index': 1,
            'fileroot': 'test1',
            'next_ref': 'this.ref',
            'prev_ref': '',
            'postname': 'test1.post',
            'type': True
            }
        }
    },
{   'remark': 'Test 7: pcom_get_pagination_info - tags manual - prev ref in list',
    'inputs': {\
        'html': ('<div class="something">\n'
                + ct.PCOM_INSERT_PAGINATION_TAG_OPEN + 'MAIN:'
                + '' + ':' + ',this.ref' + ct.PCOM_INSERT_PAGINATION_TAG_CLOSE + ct.NL
                + '</div>'),
        'postlist': POSTLIST_1,
        'postname': 'test1.post',
        'fileroot': 'test1'
    },
    'assertEqual': {\
        "array": [\
        '<div class="something">\n',
        '\n<div class="main-outer clearfix-small">\n  <div class="main-inner clearfix-small">\n    <div class="pm-post-pagination">\n    </div><!-- end of .pm-post-pagination -->\n\n  </div><!-- end of .main-inner -->\n</div><!-- end of .main-outer -->',
        '</div>'],
        "info": {\
            'index': 1,
            'fileroot': 'test1',
            'next_ref': '',
            'prev_ref': 'this.ref',
            'postname': 'test1.post',
            'type': True
            }
        }
    },
]
