# test values of main.polimorf_add_main
import libraries.constants as ct
import libraries.globals as gb

# main and sidebar data are arrays of strings

test_values = [\
{   'remark': 'Test Case 1:polimorf_add_main - No sidebar, not template, not search, meta present, fileroot = myfile',
    'inputs': { 'main_data':    ['<div class="main-out"></div>'],
                'sidebar_data': [ct.PCOM_NO_ENTRY],
                'meta_present': True,
                'wrap':         False,
                'fileroot':     'myfile',
                'is_template':  False,
                'is_search':    False },
    'assertIn': ['<div class="main-out">'],
    'assertNotIn': ['main-outer', 'main-inner', 'with-sidebar'] },

{   'remark': 'Test Case 2:polimorf_add_main - No sidebar, not template, not search, NO meta present, fileroot = myfile',
    'inputs': { 'main_data':    ['<div class="main-out"></div>'],
                'sidebar_data': [ct.PCOM_NO_ENTRY],
                'meta_present': False,
                'wrap':         False,
                'fileroot':     'myfile',
                'is_template':  False,
                'is_search':    False },
    'assertIn': [ct.PCOM_NO_ENTRY],
    'assertNotIn': ['main-outer', 'main-inner', 'with-sidebar', '<div class="main-out">'] },

{   'remark': 'Test Case 3:polimorf_add_main - Sidebar data, not template, not search, meta present, fileroot = myfile',
    'inputs': { 'main_data':    ['<div class="main-out"></div>'],
                'sidebar_data': ['<div class="sidebar-out"></div>'],
                'meta_present': True,
                'wrap':         False,
                'fileroot':     'myfile',
                'is_template':  False,
                'is_search':    False },
    'assertIn': [\
                'main-outer',
                'main-inner',
                '<div class="main-out">',
                '<div class="sidebar-out">',
                'with-sidebar-main',
                'with-sidebar-sidebar'],
    'assertNotIn': [] },

{   'remark': 'Test Case 4:polimorf_add_main - Sidebar data, template, not search, meta present, fileroot = posts',
    'inputs': { 'main_data':    ['<div class="main-out"></div>'],
                'sidebar_data': ['<div class="sidebar-out"></div>'],
                'meta_present': True,
                'wrap':         False,
                'fileroot':     'posts',
                'is_template':  True,
                'is_search':    False },
    'assertIn': [\
                'data-postlist-name="postlist-template',
                'pm-postlist-entries',
                'pm-postlist-pagination',
                'pm-post-list-custom',
                'main-outer',
                'main-inner',
                '<div class="main-out">',
                '<div class="sidebar-out">',
                'with-sidebar-main',
                'with-sidebar-sidebar'],
    'assertNotIn': ['data-postlist-name="postlist-posts'] },

{   'remark': 'Test Case 5:polimorf_add_main - Sidebar data, template, search, meta present, fileroot = posts',
    'inputs': { 'main_data':    ['<div class="main-out"></div>'],
                'sidebar_data': ['<div class="sidebar-out"></div>'],
                'meta_present': True,
                'wrap':         False,
                'fileroot':     'posts',
                'is_template':  True,
                'is_search':    True },
    'assertIn': [\
                'class="pm-searchbar pm-search-page clearfix-small',
                'id="search-submit" class="pm-search-button"',
                'pm-post-list-custom',
                'main-outer',
                'main-inner',
                '<div class="main-out">',
                '<div class="sidebar-out">',
                'with-sidebar-main',
                'with-sidebar-sidebar'],
    'assertNotIn': [\
                'data-postlist-name="postlist-posts',
                'data-postlist-name="postlist-template',
                'pm-postlist-entries',
                'pm-postlist-pagination'] },

{   'remark': 'Test Case 6:polimorf_add_main - Sidebar data but not array,  not template, not search, meta present, fileroot = posts',
    'inputs': { 'main_data':    ['<div class="main-out"></div>'],
                'sidebar_data': 'ANO',
                'meta_present': True,
                'wrap':         False,
                'fileroot':     'posts',
                'is_template':  False,
                'is_search':    False },
    'assertIn': [\
                'A\n',
                'N\n',
                'O\n',
                'main-outer',
                'main-inner',
                '<div class="main-out">',
                'with-sidebar-main',
                'with-sidebar-sidebar'],
    'assertNotIn': ['ANO'] },

{   'remark': 'Test Case 7:polimorf_add_main - No sidebar, not template, not search, meta present, fileroot = myfile wrap= True',
    'inputs': { 'main_data':    ['<div class="main-out"></div>'],
                'sidebar_data': [ct.PCOM_NO_ENTRY],
                'meta_present': True,
                'wrap':         True,
                'fileroot':     'myfile',
                'is_template':  False,
                'is_search':    False },
    'assertIn': ['<div class="main-out">','section id="main'],
    'assertNotIn': ['main-outer', 'main-inner', 'with-sidebar'] },
]
