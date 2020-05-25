#
import libraries.constants as ct
import libraries.globals as gb
import libraries.schematics as sch

from collections import OrderedDict

from unit.lists_test_io.lists_supplemental import POST_LISTS_INFO_1
from unit.lists_test_io.lists_supplemental import POST_LISTS_INFO_2
from unit.lists_test_io.lists_supplemental import POST_LISTS_INFO_3
from unit.lists_test_io.lists_supplemental import POST_LISTS_INFO_4
from unit.lists_test_io.lists_supplemental import POST_LISTS_INFO_5
from unit.lists_test_io.lists_supplemental import POST_LISTS_INFO_6
from unit.lists_test_io.lists_supplemental import POST_LISTS_INFO_7
from unit.lists_test_io.lists_supplemental import POST_LISTS_INFO_8

from unit.lists_test_io.lists_supplemental import PAGINATION_1
from unit.lists_test_io.lists_supplemental import PAGINATION_2
from unit.lists_test_io.lists_supplemental import PAGINATION_3
from unit.lists_test_io.lists_supplemental import PAGINATION_4
from unit.lists_test_io.lists_supplemental import PAGINATION_5
from unit.lists_test_io.lists_supplemental import PAGINATION_6
from unit.lists_test_io.lists_supplemental import PAGINATION_7

from unit.lists_test_io.lists_supplemental import ARCHIVE_POSTLIST_1
from unit.lists_test_io.lists_supplemental import ARCHIVE_POSTLIST_2

from unit.lists_test_io.lists_supplemental import ARCHIVE_1
from unit.lists_test_io.lists_supplemental import ARCHIVE_2
from unit.lists_test_io.lists_supplemental import ARCHIVE_3
from unit.lists_test_io.lists_supplemental import ARCHIVE_4
from unit.lists_test_io.lists_supplemental import ARCHIVE_5

#

test_values_1 = [\
{   'remark': 'Test 1: test_pcom_update_postlists_info - no postlist_info or local_info',
    'inputs': {\
        'postlist_info': [],
        'local_info': [],
        'js_name': 'postlist__post1.js',
        'fileroot': 'test1',
        'is_template': False,
        'is_search': False
    },
    'assertEqual': []
    },
{   'remark': 'Test 2: test_pcom_update_postlists_info - postlist_info but no local_info',
    'inputs': {\
        'postlist_info': POST_LISTS_INFO_1,
        'local_info': [],
        'js_name': 'postlist__post1.js',
        'fileroot': 'test1',
        'is_template': False,
        'is_search': False
    },
    'assertEqual': POST_LISTS_INFO_1
    },
{   'remark': 'Test 3: test_pcom_update_postlists_info - postlist_info, local_info but different js_name',
    'inputs': {\
        'postlist_info': POST_LISTS_INFO_2,
        'local_info': ["this"],
        'js_name': 'postlist__post1.js',
        'fileroot': 'test1',
        'is_template': False,
        'is_search': False
    },
    'assertEqual': POST_LISTS_INFO_3
    },
{   'remark': 'Test 4: test_pcom_update_postlists_info - postlist_info, local_info update',
    'inputs': {\
        'postlist_info': POST_LISTS_INFO_4,
        'local_info': [{\
            "index": 76,
            "fileroot": "test1",
            "ppp": "3",
            "content": "test1.post, test2.post"
            }],
        'js_name': 'postlist--test1.js',
        'fileroot': 'test1',
        'is_template': False,
        'is_search': False
    },
    'assertEqual': POST_LISTS_INFO_5
    },
{   'remark': 'Test 5: test_pcom_update_postlists_info - no postlist_info, local_info',
    'inputs': {\
        'postlist_info': [],
        'local_info': ["this"],
        'js_name': 'postlist__post1.js',
        'fileroot': 'test1',
        'is_template': False,
        'is_search': False
    },
    'assertEqual': POST_LISTS_INFO_6
    },
{   'remark': 'Test 6: test_pcom_update_postlists_info - postlist_info, local_info but is template',
    'inputs': {\
        'postlist_info': POST_LISTS_INFO_5,
        'local_info': ["this"],
        'js_name': 'postlist__post6.js',
        'fileroot': 'test1',
        'is_template': True,
        'is_search': False
    },
    'assertEqual': POST_LISTS_INFO_5
    },
{   'remark': 'Test 7: test_pcom_update_postlists_info - postlist_info, local_info - no match to js name - is search true',
    'inputs': {\
        'postlist_info': POST_LISTS_INFO_5,
        'local_info': ["this"],
        'js_name': 'postlist__post1.js',
        'fileroot': 'test1',
        'is_template': False,
        'is_search': True
    },
    'assertEqual': POST_LISTS_INFO_7
    },
{   'remark': 'Test 8: test_pcom_update_postlists_info - postlist_info, local_info empty - js name match - delete entry',
    'inputs': {\
        'postlist_info': POST_LISTS_INFO_8,
        'local_info': [],
        'js_name': 'postlist--test2.js',
        'fileroot': 'test1',
        'is_template': False,
        'is_search': False
    },
    'assertEqual': []
    },
]

test_values_2 = [\
{   'remark': 'Test 1: test_pcom_update_pagination_info - no pagination or local_info',
    'inputs': {\
        'pagination_info': [],
        'local_info': [],
        'pagination_name': 'pagination__post1.js',
        'fileroot': 'test1'
    },
    'assertEqual': []
    },
{   'remark': 'Test 2: test_pcom_update_pagination_info  - pagination_info but no local_info',
    'inputs': {\
        'pagination_info': PAGINATION_1,
        'local_info': [],
        'pagination_name': 'pagination__post1.js',
        'fileroot': 'test1'
    },
    'assertEqual': PAGINATION_1
    },
{   'remark': 'Test 3: test_pcom_update_pagination_info - pagination_info, local_info but different pagination_name',
    'inputs': {\
        'pagination_info': PAGINATION_2,
        'local_info': ["this"],
        'pagination_name': 'pagination__post1.js',
        'fileroot': 'test1'
    },
    'assertEqual': PAGINATION_3
    },
{   'remark': 'Test 4: test_pcom_update_pagination_info - pagination_info, local_info update',
    'inputs': {\
        'pagination_info': PAGINATION_4,
        'local_info': {\
            'index': 1,
            'fileroot': 'test1-here',
            'next_ref': 'this.ref',
            'prev_ref': 'that.ref',
            'postname': 'test1-here.post',
            'type': False
            },
        'pagination_name': 'pagination--test1.js',
        'fileroot': 'test1'
    },
    'assertEqual': PAGINATION_5
    },
{   'remark': 'Test 5: test_pcom_update_pagination_info - no pagination_info, local_info',
    'inputs': {\
        'pagination_info': [],
        'local_info': ["this"],
        'pagination_name': 'pagination__post1.js',
        'fileroot': 'test1'
    },
    'assertEqual': PAGINATION_6
    },
{   'remark': 'Test 6: test_pcom_update_pagination_info - pagination_info, local_info empty - js name match - delete entry',
    'inputs': {\
        'pagination_info': PAGINATION_7,
        'local_info': [],
        'pagination_name': 'pagination--test2.js',
        'fileroot': 'test1'
    },
    'assertEqual': []
    },
]


test_values_3 = [\
{   'remark': 'Test 1: test_pcom_update_archive - no archive or postlist',
    'inputs': {\
        'archive': [],
        'postlist': {'posts':[]},
        'settings': gb.DEFAULT_SETTINGS
    },
    'assertEqual': []
    },
{   'remark': 'Test 2: test_pcom_update_archive - postlist but not entries in archive',
    'inputs': {\
        'archive': {'created':[], 'modified': []},
        'postlist': ARCHIVE_POSTLIST_1,
        'settings': gb.DEFAULT_SETTINGS
    },
    'assertEqual': ARCHIVE_1
    },
{   'remark': 'Test 3: test_pcom_update_archive - postlist with entries, new entries in archive',
    'inputs': {\
        'archive': ARCHIVE_2,
        'postlist': ARCHIVE_POSTLIST_1,
        'settings': gb.DEFAULT_SETTINGS
    },
    'assertEqual': ARCHIVE_3
    },
{   'remark': 'Test 4: test_pcom_update_archive - postlist with entries, new post entries existing archive',
    'inputs': {\
        'archive': ARCHIVE_4,
        'postlist': ARCHIVE_POSTLIST_2,
        'settings': gb.DEFAULT_SETTINGS
    },
    'assertEqual': ARCHIVE_5
    }
]
