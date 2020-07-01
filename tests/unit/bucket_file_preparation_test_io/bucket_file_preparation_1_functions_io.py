#
import libraries.constants as ct
import libraries.globals as gb
import libraries.schematics as sch

from unit.second_processes_test_io.second_processes_supplemental import LIST_META_1
from unit.second_processes_test_io.second_processes_supplemental import POSTLIST_2
from unit.lists_test_io.lists_supplemental import DEPENDENCIES_1

from collections import OrderedDict
#

test_values_1 = [\
{   'remark': 'Test Case 1:determine_bucket_and_key - test2.post',
    'content': '',
    'log': {\
        'inserts_processed': [],
        'search_content': [],
        'files_processed': 'N',
        'default_header_additions': [],
        'default_footer_additions': [],
        'file_header_additions': [],
        'file_footer_additions': []
    },
    'site_settings': gb.DEFAULT_SETTINGS,
    'list_meta': LIST_META_1,
    'filename': 'test2.post',
    'dependencies': DEPENDENCIES_1 ,
    'postlist': POSTLIST_2,
    'target': 'targetbucket',
    'list_bucket': 'listbucket',
    'meta': {\
        'unlisted': False,
        'url': 'this/url'
    },
    'assertEqual': {\
        'key': 'this/url/index.html',
        'bucket': 'targetbucket'
        }
    },

{   'remark': 'Test Case 2:determine_bucket_and_key - test3.post - url with front slash',
    'content': '',
    'log': {\
        'inserts_processed': [],
        'search_content': [],
        'files_processed': 'N',
        'default_header_additions': [],
        'default_footer_additions': [],
        'file_header_additions': [],
        'file_footer_additions': []
    },
    'site_settings': gb.DEFAULT_SETTINGS,
    'list_meta': LIST_META_1,
    'filename': 'test3.post',
    'dependencies': DEPENDENCIES_1 ,
    'postlist': POSTLIST_2,
    'target': 'targetbucket',
    'list_bucket': 'listbucket',
    'meta': {\
        'unlisted': False,
        'url': 'this/url2/'
    },
    'assertEqual': {\
        'key': 'this/url2/index.html',
        'bucket': 'targetbucket'
        }
    },

{   'remark': 'Test Case 3:determine_bucket_and_key - test3.template',
    'content': '',
    'log': {\
        'inserts_processed': [],
        'search_content': [],
        'files_processed': 'N',
        'default_header_additions': [],
        'default_footer_additions': [],
        'file_header_additions': [],
        'file_footer_additions': []
    },
    'site_settings': gb.DEFAULT_SETTINGS,
    'list_meta': LIST_META_1,
    'filename': 'test3.template',
    'dependencies': DEPENDENCIES_1 ,
    'postlist': POSTLIST_2,
    'target': 'targetbucket',
    'list_bucket': 'listbucket',
    'meta': {\
        'unlisted': False,
        'url': 'this/url3/'
    },
    'assertEqual': {\
        'key': 'this/url3/index.html',
        'bucket': 'targetbucket'
        }
    },

{   'remark': 'Test Case 4:determine_bucket_and_key - authors.page = is_template',
    'content': '',
    'log': {\
        'inserts_processed': [],
        'search_content': [],
        'files_processed': 'N',
        'default_header_additions': [],
        'default_footer_additions': [],
        'file_header_additions': [],
        'file_footer_additions': []
    },
    'site_settings': gb.DEFAULT_SETTINGS,
    'list_meta': LIST_META_1,
    'filename': 'authors.page',
    'dependencies': DEPENDENCIES_1 ,
    'postlist': POSTLIST_2,
    'target': 'targetbucket',
    'list_bucket': 'listbucket',
    'meta': {\
        'unlisted': False,
        'url': 'this/url3/'
    },
    'assertEqual': {\
        'key': 'authors.template',
        'bucket': 'listbucket'
        }
    },

{   'remark': 'Test Case 5:determine_bucket_and_key - index.page',
    'content': '',
    'log': {\
        'inserts_processed': [],
        'search_content': [],
        'files_processed': 'N',
        'default_header_additions': [],
        'default_footer_additions': [],
        'file_header_additions': [],
        'file_footer_additions': []
    },
    'site_settings': gb.DEFAULT_SETTINGS,
    'list_meta': LIST_META_1,
    'filename': 'index.page',
    'dependencies': DEPENDENCIES_1 ,
    'postlist': POSTLIST_2,
    'target': 'targetbucket',
    'list_bucket': 'listbucket',
    'meta': {\
        'unlisted': False,
        'url': 'this/url3/'
    },
    'assertEqual': {\
        'key': 'index.html',
        'bucket': 'targetbucket'
        }
    },

{   'remark': 'Test Case 6:determine_bucket_and_key - 404.page',
    'content': '',
    'log': {\
        'inserts_processed': [],
        'search_content': [],
        'files_processed': 'N',
        'default_header_additions': [],
        'default_footer_additions': [],
        'file_header_additions': [],
        'file_footer_additions': []
    },
    'site_settings': gb.DEFAULT_SETTINGS,
    'list_meta': LIST_META_1,
    'filename': '404.page',
    'dependencies': DEPENDENCIES_1 ,
    'postlist': POSTLIST_2,
    'target': 'targetbucket',
    'list_bucket': 'listbucket',
    'meta': {\
        'unlisted': False,
        'url': 'this/url3/'
    },
    'assertEqual': {\
        'key': '404.html',
        'bucket': 'targetbucket'
        }
    },

{   'remark': 'Test Case 7:determine_bucket_and_key - search.page',
    'content': '',
    'log': {\
        'inserts_processed': [],
        'search_content': [],
        'files_processed': 'N',
        'default_header_additions': [],
        'default_footer_additions': [],
        'file_header_additions': [],
        'file_footer_additions': []
    },
    'site_settings': gb.DEFAULT_SETTINGS,
    'list_meta': LIST_META_1,
    'filename': 'search.page',
    'dependencies': DEPENDENCIES_1 ,
    'postlist': POSTLIST_2,
    'target': 'targetbucket',
    'list_bucket': 'listbucket',
    'meta': {\
        'unlisted': False,
        'url': 'this/url3/'
    },
    'assertEqual': {\
        'key': 'search/index.html',
        'bucket': 'targetbucket'
        }
    },
]
