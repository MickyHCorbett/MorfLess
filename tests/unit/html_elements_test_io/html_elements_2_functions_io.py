#
import libraries.constants as ct
import libraries.globals as gb
import libraries.schematics as sch

from collections import OrderedDict
#

test_values_1 = [\
{   'remark': 'Test Case 1:pcom_add_content_command -  empty syntax',
    'syntax': '',
    'custom_class': '',
    'placement': '',
    'type': '',
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': ''
    },

{   'remark': 'Test Case 2:pcom_add_content_command -  syntax NONE',
    'syntax': ct.PCOM_NO_ENTRY,
    'custom_class': '',
    'placement': '',
    'type': 'that',
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': ''
    },

{   'remark': 'Test Case 4:pcom_add_content_command -  syntax but no TEXT command',
    'syntax': 'FONT=[ Something here ]:',
    'custom_class': '',
    'placement': '',
    'type': 'this',
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': ''
    },

{   'remark': 'Test Case 5:pcom_add_content_command -  syntax TEXT command',
    'syntax': 'TEXT=[ Something here ]:',
    'custom_class': '',
    'placement': '',
    'type': 'this',
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': """

    <div class="post">
    Something here
    </div><!-- end of .post -->

    """
    },

{   'remark': 'Test Case 6:pcom_add_content_command -  MAIN placement - syntax TEXT command',
    'syntax': 'TEXT=[ Something here ]:',
    'custom_class': '',
    'placement': ct.PCOM_MAIN_PLACEMENT,
    'type': 'this',
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': """

<div class="main-outer clearfix-small">
  <div class="main-inner clearfix-small">
    <div class="post">
    Something here
    </div><!-- end of .post -->
  </div><!-- end of .main-inner -->
</div><!-- end of .main-outer -->

    """
    },

{   'remark': 'Test Case 7:pcom_add_content_command -  MAIN placement - syntax TEXT command - custom class',
    'syntax': 'TEXT=[ Something here ]:',
    'custom_class': 'my-class',
    'placement': ct.PCOM_MAIN_PLACEMENT,
    'type': 'this',
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': """

<div class="main-outer clearfix-small my-class">
  <div class="main-inner clearfix-small my-class">
    <div class="post my-class">
    Something here
    </div><!-- end of .post -->
  </div><!-- end of .main-inner -->
</div><!-- end of .main-outer -->

    """
    },

{   'remark': 'Test Case 8:pcom_add_content_command -  MAIN placement - syntax TEXT command - custom class - replacements',
    'syntax': 'TEXT=[ [p][b]Something here[/b][/p] ]:',
    'custom_class': 'my-class',
    'placement': ct.PCOM_MAIN_PLACEMENT,
    'type': 'this',
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': """

<div class="main-outer clearfix-small my-class">
  <div class="main-inner clearfix-small my-class">
    <div class="post my-class">
    <p><strong>Something here</strong></p>
    </div><!-- end of .post -->
  </div><!-- end of .main-inner -->
</div><!-- end of .main-outer -->

    """
    },

{   'remark': 'Test Case 9:pcom_add_content_command -  HEADER placement - syntax TEXT command - custom class - replacements',
    'syntax': 'TEXT=[ [p][b]Something here[/b][/p] ]:',
    'custom_class': 'my-class',
    'placement': ct.PCOM_HEADER_PLACEMENT,
    'type': 'this',
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': """

    <div class="post my-class">
    <p><strong>Something here</strong></p>
    </div><!-- end of .post -->

    """
    },

{   'remark': 'Test Case 10:pcom_add_cosntent_command -  FOOTER placement - syntax TEXT command - custom class - replacements',
    'syntax': 'TEXT=[ [p][b]Something here[/b][/p] ]:',
    'custom_class': 'my-class',
    'placement': ct.PCOM_FOOTER_PLACEMENT,
    'type': 'this',
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': """

  <div class="post my-class">
    <p><strong>Something here</strong></p>
  </div><!-- end of .post -->

    """
    },
]

test_values_2 = [\
{   'remark': 'Test Case 1:pcom_insert_searchbar_command - no placement',
    'syntax': 'TEXT=[ [p][b]Something here[/b][/p] ]:',
    'custom_class': 'my-class',
    'placement': '',
    'type': 'this',
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': """

    <div id="pm-searchbar-general" class="clearfix-small">

    <div class="pm-searchbar clearfix-small">
      <form action="/$$SEARCH$$/" autocomplete="on">
      <input id="search" type="text" name="s" />
      </form>
      <span id="search-submit" class="pm-search-button" name="search-submit"></span>
    </div><!-- end of #pm-searchbar -->
    </div><!-- end of #pm-searchbar-general -->

    """
    },

{   'remark': 'Test Case 2:pcom_insert_searchbar_command - header placement',
    'syntax': 'TEXT=[ [p][b]Something here[/b][/p] ]:',
    'custom_class': 'my-class',
    'placement': ct.PCOM_HEADER_PLACEMENT,
    'type': 'this',
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': """

    <div id="pm-nav-searchbar" class="clearfix-small">

    <div class="pm-searchbar clearfix-small">
      <form action="/$$SEARCH$$/" autocomplete="on">
      <input id="search" type="text" name="s" />
      </form>
      <span id="search-submit" class="pm-search-button" name="search-submit"></span>
    </div><!-- end of #pm-searchbar -->
    </div><!-- end of #pm-nav-searchbar-->

    """
    },

{   'remark': 'Test Case 3:pcom_insert_searchbar_command - main placement',
    'syntax': 'TEXT=[ [p][b]Something here[/b][/p] ]:',
    'custom_class': 'my-class',
    'placement': ct.PCOM_MAIN_PLACEMENT,
    'type': 'this',
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': """

<div class="main-outer clearfix-small my-class">
  <div class="main-inner clearfix-small my-class">

    <div class="post">

    <div id="pm-searchbar-general" class="clearfix-small">

    <div class="pm-searchbar clearfix-small">
      <form action="/$$SEARCH$$/" autocomplete="on">
      <input id="search" type="text" name="s" />
      </form>
      <span id="search-submit" class="pm-search-button" name="search-submit"></span>
    </div><!-- end of #pm-searchbar -->
    </div><!-- end of #pm-searchbar-general -->
    </div><!-- end of .post -->

  </div><!-- end of .main-inner -->
</div><!-- end of .main-outer -->

    """
    },
]

test_values_3 = [\
{   'remark': 'Test Case 1:pcom_process_insert_command - main placement syntax not with ref keyword',
    'syntax': 'TEXT=[ [p][b]Something here[/b][/p] ]:',
    'custom_class': 'my-class',
    'placement': ct.PCOM_MAIN_PLACEMENT,
    'type': 'this',
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': """

    """
    },

{   'remark': 'Test Case 2:pcom_process_insert_command - main placement syntax with subschematic command and ref keyword',
    'syntax': 'TEXT=[ some name ]: ref={ this_insert.txt }:',
    'custom_class': 'my-class',
    'placement': ct.PCOM_MAIN_PLACEMENT,
    'type': 'this',
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': """

    """
    },

{   'remark': 'Test Case 3:pcom_process_insert_command - main placement syntax with ref keyword',
    'syntax': 'ref={ this_insert.txt }:',
    'custom_class': 'my-class',
    'placement': ct.PCOM_MAIN_PLACEMENT,
    'type': 'this',
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': 'INSERT=[MAIN:this_insert.txt]:'
    },

{   'remark': 'Test Case 4:pcom_process_insert_command - header placement syntax with ref keyword',
    'syntax': 'ref={ this_insert2.txt }:',
    'custom_class': 'my-class',
    'placement': ct.PCOM_HEADER_PLACEMENT,
    'type': 'this',
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': 'INSERT=[HEADER:this_insert2.txt]:'
    },
]

# test_values_4 = [\
# {   'remark': 'Test Case 1:pcom_process_insert_addiitons_command - main placement syntax not with ref keyword',
#     'syntax': 'TEXT=[ [p][b]Something here[/b][/p] ]:',
#     'custom_class': 'my-class',
#     'placement': ct.PCOM_MAIN_PLACEMENT,
#     'type': 'this',
#     'settings': gb.DEFAULT_SETTINGS,
#     'assertEqual': """
#
#     """
#     },
#
# {   'remark': 'Test Case 2:pcom_process_insert_addiitons_command - main placement syntax with subschematic command and ref keyword',
#     'syntax': 'TEXT=[ some name ]: ref={ this_insert.txt }:',
#     'custom_class': 'my-class',
#     'placement': ct.PCOM_MAIN_PLACEMENT,
#     'type': 'this',
#     'settings': gb.DEFAULT_SETTINGS,
#     'assertEqual': """
#
#     """
#     },
#
# {   'remark': 'Test Case 3:pcom_process_insert_addiitons_command - main placement syntax with ref keyword',
#     'syntax': 'ref={ this_insert.txt }:',
#     'custom_class': 'my-class',
#     'placement': ct.PCOM_MAIN_PLACEMENT,
#     'type': 'this',
#     'settings': gb.DEFAULT_SETTINGS,
#     'assertEqual': 'INSERT=[MAIN:this_insert.txt]:'
#     },
#
# {   'remark': 'Test Case 4:pcom_process_insert_addiitons_command - header placement syntax with ref keyword',
#     'syntax': 'ref={ this_insert2.txt }:',
#     'custom_class': 'my-class',
#     'placement': ct.PCOM_HEADER_PLACEMENT,
#     'type': 'this',
#     'settings': gb.DEFAULT_SETTINGS,
#     'assertEqual': 'INSERT=[HEADER:this_insert2.txt]:'
#     },
# ]

test_values_5 = [\
{   'remark': 'Test Case 1:pcom_insert_pagination_command - main placement syntax with subschematic command and ref keyword',
    'syntax': 'TEXT=[ some name ]: ref={ this_insert.txt }:',
    'custom_class': '',
    'placement': ct.PCOM_MAIN_PLACEMENT,
    'type': 'this',
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': 'PAGINATION=[MAIN::,]:'
    },

{   'remark': 'Test Case 2:pcom_insert_pagination_command - main placement syntax with subschematic command and ref keyword, class',
    'syntax': '',
    'custom_class': 'my-class',
    'placement': ct.PCOM_HEADER_PLACEMENT,
    'type': 'this',
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': 'PAGINATION=[HEADER:my-class:]:'
    },

{   'remark': 'Test Case 3:pcom_insert_pagination_command - header placement next link',
    'syntax': 'next={ this-link.page }:',
    'custom_class': 'my-class',
    'placement': ct.PCOM_HEADER_PLACEMENT,
    'type': 'this',
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': 'PAGINATION=[HEADER:my-class:this-link.page,]:'
    },

{   'remark': 'Test Case 4:pcom_insert_pagination_command - header placement next and prev link',
    'syntax': 'prev={ that-page.post }: next={ this-link.page }: ',
    'custom_class': 'my-class',
    'placement': ct.PCOM_HEADER_PLACEMENT,
    'type': 'this',
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': 'PAGINATION=[HEADER:my-class:this-link.page,that-page.post]:'
    },
]

test_values_6 = [\
{   'remark': 'Test Case 1:pcom_create_pagination_link - empty link data',
    'links': {\
        'next_url': '',
        'prev_url': '',
        'next_title': '',
        'prev_title': ''
    },
    'assertEqual': {
        'pagination': True
        },
    'assertIn': [\
        '<div id="pm-next-post-link">',
        '<span class="pm-post-link-text"><i class="fa fa-arrow-right" aria-hidden="true"></i>',
        '<a href=""></a>',
        '</span></div><!-- post link -->',
        '<div id="pm-prev-post-link">',
        '<span class="pm-post-link-text"><i class="fa fa-arrow-left" aria-hidden="true"></i>',
        '<a href=""></a>',
        '</span></div><!-- post link -->'
        ]
    },

{   'remark': 'Test Case 2:pcom_create_pagination_link - link data NONE',
    'links': {\
        'next_url': ct.PCOM_NO_ENTRY,
        'prev_url': ct.PCOM_NO_ENTRY,
        'next_title': ct.PCOM_NO_ENTRY,
        'prev_title': ct.PCOM_NO_ENTRY
    },
    'assertEqual': {
        'pagination': False
        },
    'assertIn': [\
        ''
        ]
    },
]
