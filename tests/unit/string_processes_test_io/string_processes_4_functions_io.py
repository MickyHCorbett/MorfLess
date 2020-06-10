#
import libraries.constants as ct
import libraries.globals as gb

from collections import OrderedDict
#

test_values_1 = [\
{   'remark': 'Test Case 1:pcom_process_menu_command_mlk_keyword - empty',
    'command_string': '',
    'assertEqual': ''
    },
{   'remark': 'Test Case 2:pcom_process_menu_command_mlk_keyword - no identifiers',
    'command_string': 'This command',
    'assertEqual': ''
    },
{   'remark': 'Test Case 3:pcom_process_menu_command_mlk_keyword - href only',
    'command_string': 'href="this"',
    'assertEqual': ''
    },
{   'remark': 'Test Case 4:pcom_process_menu_command_mlk_keyword - name only',
    'command_string': 'name="this"',
    'assertEqual': ''
    },
{   'remark': 'Test Case 5:pcom_process_menu_command_mlk_keyword - href and name',
    'command_string': 'href="that" name="this"',
    'assertEqual': '      <li><a href="that" name="this">this</a></li>'
    },
{   'remark': 'Test Case 6:pcom_process_menu_command_mlk_keyword - href and name 2',
    'command_string': 'href="SITE_HOME" name="this2"',
    'assertEqual': '      <li><a href="'+ ct.SITE_HOME + '" name="this2">this2</a></li>'
    },
{   'remark': 'Test Case 7:pcom_process_menu_command_mlk_keyword - href and name 2 and src',
    'command_string': 'href="SITE_HOME" name="this2" src="IMAGES"',
    'assertEqual': '      <li><a href="'+ ct.SITE_HOME + '" name="this2"><img src="/images" alt="this2" /></a></li>'
    },
{   'remark': 'Test Case 8:pcom_process_menu_command_mlk_keyword - href and name 2 and fa',
    'command_string': 'href="SITE_HOME" name="this2" fa="ThisFA"',
    'assertEqual': '      <li><a href="'+ ct.SITE_HOME + '" name="this2"><i class="ThisFA" aria-hidden="true"></i></a></li>'
    },
{   'remark': 'Test Case 9:pcom_process_menu_command_mlk_keyword - href and name 2, fa and src',
    'command_string': 'href="SITE_HOME" name="this2" fa="ThisFA" src="this-link"',
    'assertEqual': '      <li><a href="'+ ct.SITE_HOME + '" name="this2"><i class="ThisFA" aria-hidden="true"></i></a></li>'
    },
]


test_values_2 = [\
{   'remark': 'Test Case 1:pcom_process_logo_for_nav - empty syntax',
    'syntax': '',
    'site_title': '',
    'assertEqual': """
    <div class="pm-nav-logo">
      <a href="/" name=""><img src="src" alt="" /></a>
    </div><!-- end of logo -->
    """
    },
{   'remark': 'Test Case 2:pcom_process_logo_for_nav - syntax no entry',
    'syntax': ct.PCOM_NO_ENTRY,
    'site_title': '',
    'assertEqual': ''
    },
{   'remark': 'Test Case 3:pcom_process_logo_for_nav - data but no keyword',
    'syntax': 'This string of data',
    'site_title': '',
    'assertEqual': """
    <div class="pm-nav-logo">
      <a href="/" name=""><img src="src" alt="" /></a>
    </div><!-- end of logo -->
    """
    },
{   'remark': 'Test Case 4:pcom_process_logo_for_nav - src data but no title',
    'syntax': 'src="This string of data"',
    'site_title': '',
    'assertEqual': """
    <div class="pm-nav-logo">
      <a href="/" name=""><img src="This string of data" alt="" /></a>
    </div><!-- end of logo -->
    """
    },
{   'remark': 'Test Case 5:pcom_process_logo_for_nav - src data and title',
    'syntax': 'src="This string of data"',
    'site_title': 'This site',
    'assertEqual': """
    <div class="pm-nav-logo">
      <a href="/" name="This site"><img src="This string of data" alt="This site" /></a>
    </div><!-- end of logo -->
    """
    },
]

test_values_3 = [\
{   'remark': 'Test Case 1:pcom_add_title - empty syntax',
    'syntax': '',
    'assertEqual': '<div class="pm-title-nav"></div><!-- end of .pm-title-nav -->'
    },
{   'remark': 'Test Case 2:pcom_add_title - non empty syntax with spaces',
    'syntax': '   Title of page    ',
    'assertEqual': '<div class="pm-title-nav">Title of page</div><!-- end of .pm-title-nav -->'
    },
]

test_values_4 = [\
{   'remark': 'Test Case 1:pcom_replace_custom_attributes - empty syntax and keys',
    'syntax': '',
    'custom_keys': {},
    'assertEqual': ''
    },
{   'remark': 'Test Case 2:pcom_replace_custom_attributes - syntax but empty keys',
    'syntax': 'Something to REPLACE here. Next 667 things',
    'custom_keys': {},
    'assertEqual': 'Something to REPLACE here. Next 667 things'
    },
{   'remark': 'Test Case 3:pcom_replace_custom_attributes - syntax and keys',
    'syntax': 'Something to REPLACE here. Next 667 things',
    'custom_keys': {'REPLACE': 'I know', '667': '[]'},
    'assertEqual': 'Something to I know here. Next [] things'
    },
{   'remark': 'Test Case 4:pcom_replace_custom_attributes - different syntax and keys',
    'syntax': 'Another line to here. Next plate of things',
    'custom_keys': {'line': 'Bucket', 'things': '999'},
    'assertEqual': 'Another Bucket to here. Next plate of 999'
    },
]

test_values_5 = [\
{   'remark': 'Test Case 1:pcom_open_custom_class_div - custom class empty',
    'custom_class': '',
    'html': '<div class="opening',
    'assertEqual': '<div class="opening">'
    },
{   'remark': 'Test Case 2:pcom_open_custom_class_div - custom class not empty',
    'custom_class': 'class',
    'html': '<div class="opening',
    'assertEqual': '<div class="opening class">'
    },
{   'remark': 'Test Case 3:pcom_open_custom_class_div - custom class not empty',
    'custom_class': 'class2',
    'html': '<div class="opening',
    'assertEqual': '<div class="opening class2">'
    },
{   'remark': 'Test Case 4:pcom_open_custom_class_div - custom class no entry',
    'custom_class': ct.PCOM_NO_ENTRY,
    'html': '<div class="opening',
    'assertEqual': '<div class="opening">'
    },
]

test_values_6 = [\
{   'remark': 'Test Case 1:pcom_open_placement_class - custom class and placement empty',
    'custom_class': '',
    'placement': '',
    'assertEqual': ''
    },
]

test_values_7 = [\
{   'remark': 'Test Case 1:pcom_close_placement_class - placement empty',
    'placement': '',
    'assertEqual': ''
    },
{   'remark': 'Test Case 2:pcom_close_placement_class - placement MAIN',
    'placement': ct.PCOM_MAIN_PLACEMENT,
    'assertEqual': '</div><!-- end of .main-inner -->\n</div><!-- end of .main-outer -->'
    },
]

test_values_8 = [\
{   'remark': 'Test Case 1:pcom_close_placement_class - command string empty, no keywords',
    'command_string': '',
    'defaults': {},
    'assertEqual': {}
    },
{   'remark': 'Test Case 2:pcom_close_placement_class - command string empty, keywords',
    'command_string': '',
    'defaults': {'one': '', 'two': ''},
    'assertEqual': {'one': '', 'two': ''}
    },
{   'remark': 'Test Case 3:pcom_close_placement_class - command string no entry, keywords',
    'command_string': ct.PCOM_NO_ENTRY,
    'defaults': {'one': '', 'two': ''},
    'assertEqual': {'one': '', 'two': ''}
    },
{   'remark': 'Test Case 4:pcom_close_placement_class - command string with other keywords, keywords',
    'command_string': ' one="four" two="ten" three="five"  ',
    'defaults': {'one': '', 'two': ''},
    'assertEqual': {'one': 'four', 'two': 'ten'}
    },
{   'remark': 'Test Case 5:pcom_close_placement_class - command string with other keywords, keywords',
    'command_string': ' seven="four" two="eleven" three="five"  ',
    'defaults': {'two': '', 'three': ''},
    'assertEqual': {'two': 'eleven', 'three': 'five'}
    },
]

test_values_9 = [\
{   'remark': 'Test Case 1:pcom_site_constants_replacement - string',
    'content': 'I need to go SITE_HOME with a bunch of IMAGES',
    'assertEqual': 'I need to go / with a bunch of /images'
    },
]
