#
import libraries.constants as ct
import libraries.globals as gb
import libraries.schematics as sch

from unit.second_processes_test_io.second_processes_supplemental import LIST_META_1
from unit.second_processes_test_io.second_processes_supplemental import LIST_META_BLANK_1
from unit.second_processes_test_io.second_processes_supplemental import LIST_META_BLANK_2

from unit.second_processes_test_io.second_processes_supplemental import POSTLIST_2
from unit.second_processes_test_io.second_processes_supplemental import POSTLIST_SINGLE
from unit.second_processes_test_io.second_processes_supplemental import POSTLIST_BLANK

from unit.second_processes_test_io.second_processes_supplemental import ARCHIVE_1
from unit.lists_test_io.lists_supplemental import DEPENDENCIES_1

from collections import OrderedDict
#

test_values_1 = [\
{   'remark': 'Test Case 1:HtmlOut:init - empty init parameters',
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
    'list_meta': {},
    'filename': '',
    'dependencies': [],
    'postlist': {},
    'assertEqual': {\
        'postlist_constant_name': 'postlist--.js',
        'pagination_name': 'pagination--.js',
        'is_template': False,
        'is_root': False,
        'is_search': False,
        'fileroot': ''
        }
    },

{   'remark': 'Test Case 2:HtmlOut:init - empty init parameters except filename',
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
    'list_meta': {},
    'filename': 'this-post.page',
    'dependencies': [],
    'postlist': {},
    'assertEqual': {\
        'postlist_constant_name': 'postlist--this-post.js',
        'pagination_name': 'pagination--this-post.js',
        'is_template': False,
        'is_root': False,
        'is_search': False,
        'fileroot': 'this-post'
        }
    },

{   'remark': 'Test Case 3:HtmlOut:init - empty init parameters except filename = search.page',
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
    'list_meta': {},
    'filename': 'search.page',
    'dependencies': [],
    'postlist': {},
    'assertEqual': {\
        'postlist_constant_name': 'postlist--search.js',
        'pagination_name': 'pagination--search.js',
        'is_template': True,
        'is_root': False,
        'is_search': True,
        'fileroot': 'search'
        }
    },
{   'remark': 'Test Case 4:HtmlOut:init - empty init parameters except filename = index.page',
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
    'list_meta': {},
    'filename': 'index.page',
    'dependencies': [],
    'postlist': {},
    'assertEqual': {\
        'postlist_constant_name': 'postlist--index.js',
        'pagination_name': 'pagination--index.js',
        'is_template': False,
        'is_root': True,
        'is_search': False,
        'fileroot': 'index'
        }
    },

{   'remark': 'Test Case 5:HtmlOut:init - empty init parameters except filename = categories.page',
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
    'list_meta': {},
    'filename': 'categories.page',
    'dependencies': [],
    'postlist': {},
    'assertEqual': {\
        'postlist_constant_name': 'postlist--categories.js',
        'pagination_name': 'pagination--categories.js',
        'is_template': True,
        'is_root': False,
        'is_search': False,
        'fileroot': 'categories'
        }
    },
]

test_values_2 = [\
{   'remark': 'Test Case 1:HtmlOut:process_pagination - filename test2.post - empty html array',
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
    'meta': {\
        'unlisted': False
    },
    'html_array': [''],
    'assertEqual': {\

        }
    },

{   'remark': 'Test Case 2:HtmlOut:process_pagination - filename test2.post - pagination in html array',
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
    'meta': {\
        'unlisted': False
    },
    'html_array': ['Something', 'PAGINATION=[HEADER:my-class:]:', 'This thing'],
    'assertEqual': {\
          'fileroot': 'test2',
          'index': 1,
          'next_ref': '',
          'postname': 'test2.post',
          'prev_ref': '',
          'type': True
        }
    },

{   'remark': 'Test Case 3:HtmlOut:process_pagination - filename test2.post - pagination in html array - unlisted',
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
    'meta': {\
        'unlisted': True
    },
    'html_array': ['Something', 'PAGINATION=[HEADER:my-class:]:', 'This thing'],
    'assertEqual': {\

        }
    },

{   'remark': 'Test Case 4:HtmlOut:process_pagination - filename index.page - pagination in html array',
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
    'meta': {\
        'unlisted': False
    },
    'html_array': ['Something', 'PAGINATION=[HEADER:my-class:]:', 'This thing'],
    'assertEqual': {\

        }
    },

{   'remark': 'Test Case 5:HtmlOut:process_pagination - filename authors.page - pagination in html array',
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
    'meta': {\
        'unlisted': False
    },
    'html_array': ['Something', 'PAGINATION=[HEADER:my-class:]:', 'This thing'],
    'assertEqual': {\

        }
    },
]

test_values_3 = [\
{   'remark': 'Test Case 1:HtmlOut:insert_additions_into_html - header additions',
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
    'meta': {\
        'unlisted': False
    },
    'placement': ct.PCOM_HEADER_PLACEMENT,
    'add_default_header_additions': True,
    'add_default_footer_additions': False,
    'default_header_additions': 'Something in the header',
    'default_footer_additions': 'Something in the footer',
    'assertEqual': {\
        'header_additions': ['Something in the header'],
        'footer_additions': [],
        }
    },

{   'remark': 'Test Case 1:HtmlOut:insert_additions_into_html - footer additions',
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
    'meta': {\
        'unlisted': False
    },
    'placement': ct.PCOM_FOOTER_PLACEMENT,
    'add_default_header_additions': False,
    'add_default_footer_additions': True,
    'default_header_additions': 'Something in the header',
    'default_footer_additions': 'Something in the footer',
    'assertEqual': {\
        'header_additions': [],
        'footer_additions': ['Something in the footer'],
        }
    },
]

test_values_4 = [\
{   'remark': 'Test Case 1:HtmlOut:get_raw_content - not search or unlisted',
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
    'html_content': """
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
        'unlisted': False,
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

{   'remark': 'Test Case 2:HtmlOut:get_raw_content - search or unlisted',
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
    'html_content': """
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
        'unlisted': False,
        'page_title': 'A name',
        'page_description': 'A description',
        'page_extract': 'An extract'
    },
    'assertEqual': """

    """
    },

{   'remark': 'Test Case 3:HtmlOut:get_raw_content - not search but unlisted',
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
    'filename': 'search-this.page',
    'dependencies': DEPENDENCIES_1 ,
    'postlist': POSTLIST_2,
    'html_content': """
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
        'unlisted': True,
        'page_title': 'A name',
        'page_description': 'A description',
        'page_extract': 'An extract'
    },
    'assertEqual': """

    """
    },
]

test_values_5 = [\
{   'remark': 'Test Case 1:HtmlOut:update_postlist - new post',
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
    'filename': 'test-update1.post',
    'dependencies': DEPENDENCIES_1 ,
    'postlist': POSTLIST_2,
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
        'unlisted': False
        },
    'assertEqual': 'test-update1.post'
    },

{   'remark': 'Test Case 2:HtmlOut:update_postlist - new post meta = no entry',
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
    'filename': 'test-update1.post',
    'dependencies': DEPENDENCIES_1 ,
    'postlist': POSTLIST_BLANK,
    'meta': ct.PCOM_NO_ENTRY,
    'assertEqual': ct.PCOM_NO_ENTRY
    },

{   'remark': 'Test Case 3:HtmlOut:update_postlist - unlisted',
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
    'filename': 'test-update1.post',
    'dependencies': DEPENDENCIES_1 ,
    'postlist': POSTLIST_BLANK,
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
        'unlisted': True
        },
    'assertEqual': ct.PCOM_NO_ENTRY
    },

{   'remark': 'Test Case 4:HtmlOut:update_postlist - template = authors.page',
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
    'postlist': POSTLIST_BLANK,
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
        'unlisted': False
        },
    'assertEqual': ct.PCOM_NO_ENTRY
    },

{   'remark': 'Test Case 5:HtmlOut:update_postlist - root = 404.page',
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
    'postlist': POSTLIST_BLANK,
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
        'unlisted': False
        },
    'assertEqual': ct.PCOM_NO_ENTRY
    },

]


test_values_6 = [\
{   'remark': 'Test Case 1:HtmlOut:update_categories - update category',
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
    'list_meta': LIST_META_BLANK_1,
    'filename': 'contact.post',
    'dependencies': DEPENDENCIES_1 ,
    'postlist': POSTLIST_SINGLE,
    'meta': {\
        'unlisted': False
        },
    'assertEqual': {\
            "no_of_category_pages": 1,
            "categories": [
                OrderedDict([('name', 'stuff'),
                ('thumbnail', '/images/Polimorf-shapes-background.jpg'),
                ('description', '')])
                ]
            },
    },

{   'remark': 'Test Case 2:HtmlOut:update_categories - unlisted',
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
    'list_meta': LIST_META_BLANK_2,
    'filename': 'contact.post',
    'dependencies': DEPENDENCIES_1 ,
    'postlist': POSTLIST_SINGLE,
    'meta': {\
        'unlisted': True
        },
    'assertEqual': {\
            "no_of_category_pages": 1,
            "categories": []
            },
    },
{   'remark': 'Test Case 3:HtmlOut:update_categories - template',
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
    'list_meta': LIST_META_BLANK_2,
    'filename': 'categories.page',
    'dependencies': DEPENDENCIES_1 ,
    'postlist': POSTLIST_SINGLE,
    'meta': {\
        'unlisted': False
        },
    'assertEqual': {\
            "no_of_category_pages": 1,
            "categories": []
            },
    },

{   'remark': 'Test Case 4:HtmlOut:update_categories - root = index ',
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
    'list_meta': LIST_META_BLANK_2,
    'filename': 'index.page',
    'dependencies': DEPENDENCIES_1 ,
    'postlist': POSTLIST_SINGLE,
    'meta': {\
        'unlisted': False
        },
    'assertEqual': {\
            "no_of_category_pages": 1,
            "categories": []
            },
    },
]

test_values_7 = [\
{   'remark': 'Test Case 1:HtmlOut:update_authors - update category',
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
    'list_meta': LIST_META_BLANK_1,
    'filename': 'contact.post',
    'dependencies': DEPENDENCIES_1 ,
    'postlist': POSTLIST_SINGLE,
    'meta': {\
        'unlisted': False
        },
    'assertEqual': {\
            "no_of_author_pages": 1,
            "authors": [
                OrderedDict([('name', 'Clive'), ('shortname', 'Clive'),
                ('thumbnail', '/images/Polimorf-shapes-background.jpg'),
                ('description', '')])
                ]
            },
    },

{   'remark': 'Test Case 2:HtmlOut:update_authors - unlisted',
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
    'list_meta': LIST_META_BLANK_2,
    'filename': 'contact.post',
    'dependencies': DEPENDENCIES_1 ,
    'postlist': POSTLIST_SINGLE,
    'meta': {\
        'unlisted': True
        },
    'assertEqual': {\
            "no_of_author_pages": 1,
            "authors": []
            },
    },
{   'remark': 'Test Case 3:HtmlOut:update_authors - template',
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
    'list_meta': LIST_META_BLANK_2,
    'filename': 'categories.page',
    'dependencies': DEPENDENCIES_1 ,
    'postlist': POSTLIST_SINGLE,
    'meta': {\
        'unlisted': False
        },
    'assertEqual': {\
            "no_of_author_pages": 1,
            "authors": []
            },
    },

{   'remark': 'Test Case 4:HtmlOut:update_authors - root = index ',
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
    'list_meta': LIST_META_BLANK_2,
    'filename': 'index.page',
    'dependencies': DEPENDENCIES_1 ,
    'postlist': POSTLIST_SINGLE,
    'meta': {\
        'unlisted': False
        },
    'assertEqual': {\
            "no_of_author_pages": 1,
            "authors": []
            },
    },
]
