#
import libraries.constants as ct
import libraries.globals as gb
import libraries.schematics as sch

from collections import OrderedDict
#

test_values_1 = [\
{   'remark': 'Test Case 1:pcom_process_n_box_command -  empty syntax',
    'syntax': '',
    'custom_class': '',
    'placement': '',
    'no_boxes': 2,
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': """

<div class="pm-n-box clearfix-small">

    </div><!-- end of .pm-n-box -->

    """
    },

{   'remark': 'Test Case 2:pcom_process_n_box_command -  empty syntax - custom class',
    'syntax': '',
    'custom_class': 'the-box-class',
    'placement': '',
    'no_boxes': 2,
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': """

<div class="pm-n-box clearfix-small the-box-class">

    </div><!-- end of .pm-n-box -->

    """
    },

{   'remark': 'Test Case 3:pcom_process_n_box_command -  3 Boxes but no syntax - custom class - no-boxes = 2',
    'syntax': """
BOX1:


BOX2:


BOX3:


    """,
    'custom_class': 'the-box-class',
    'placement': '',
    'no_boxes': 2,
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': """

<div class="pm-n-box clearfix-small the-box-class">
      <div class="clearfix-small pm-n-box-box pm-box-2 box box1 box-start">
      </div><!-- end of .pm-n-box-box -->
      <div class="clearfix-small pm-n-box-box pm-box-2 box box2 box-end">
      </div><!-- end of .pm-n-box-box -->
    </div><!-- end of .pm-n-box -->

    """
    },

{   'remark': 'Test Case 3:pcom_process_n_box_command -  3 Boxes with syntax - custom class - no-boxes = 2',
    'syntax': """
BOX1:
TEXT=[ Box 1 text ]:

BOX2:
TEXT=[ Box 2 text ]:

BOX3:
TEXT=[ Box 3 text ]:

    """,
    'custom_class': 'the-box-class',
    'placement': '',
    'no_boxes': 2,
    'ppp': 3,
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': """

<div class="pm-n-box clearfix-small the-box-class">
      <div class="clearfix-small pm-n-box-box pm-box-2 box box1 box-start">
        <div class="post">
          Box 1 text
        </div><!-- end of .post -->
      </div><!-- end of .pm-n-box-box -->
      <div class="clearfix-small pm-n-box-box pm-box-2 box box2 box-end">
        <div class="post">
          Box 2 text
        </div><!-- end of .post -->
      </div><!-- end of .pm-n-box-box -->
    </div><!-- end of .pm-n-box -->

    """
    },

{   'remark': 'Test Case 3:pcom_process_n_box_command -  3 Boxes with syntax - custom class - no-boxes = 3, placement = MAIN',
    'syntax': """
BOX1:
TEXT=[ Box 1 text ]:

BOX2:
TEXT=[ Box 2 text ]:

BOX3:
TEXT=[ Box 3 text ]:

    """,
    'custom_class': 'the-box-class',
    'placement': ct.PCOM_MAIN_PLACEMENT,
    'no_boxes': 3,
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': """

<div class="main-outer clearfix-small the-box-class">
  <div class="main-inner clearfix-small the-box-class">
    <div class="pm-n-box clearfix-small the-box-class">
      <div class="clearfix-small pm-n-box-box pm-box-3 box box1 box-start">
        <div class="post">
          Box 1 text
        </div><!-- end of .post -->
      </div><!-- end of .pm-n-box-box -->
      <div class="clearfix-small pm-n-box-box pm-box-3 box box2">
        <div class="post">
          Box 2 text
        </div><!-- end of .post -->
      </div><!-- end of .pm-n-box-box -->
      <div class="clearfix-small pm-n-box-box pm-box-3 box box3 box-end">
        <div class="post">
          Box 3 text
        </div><!-- end of .post -->
      </div><!-- end of .pm-n-box-box -->
    </div><!-- end of .pm-n-box -->
  </div><!-- end of .main-inner -->
</div><!-- end of .main-outer -->

    """
    },
]

test_values_2 = [\
{   'remark': 'Test Case 1:pcom_parse_box_arguments - empty syntax - no-boxes = 3, placement = MAIN',
    'syntax': """

    """,
    'placement': ct.PCOM_MAIN_PLACEMENT,
    'no_boxes': 3,
    'ppp': 3,
    'assertEqual': """


    """
    },

{   'remark': 'Test Case 2:pcom_parse_box_arguments - two box syntax - no-boxes = 3, placement = MAIN',
    'syntax': """
    BOX1:
    Something

    BOX2:
    Something else

    """,
    'placement': ct.PCOM_MAIN_PLACEMENT,
    'no_boxes': 3,
    'ppp': 3,
    'assertEqual': """


    """
    },

{   'remark': 'Test Case 3:pcom_parse_box_arguments - 3 box syntax - no-boxes = 3, placement = MAIN',
    'syntax': """
    BOX1:
    Something

    BOX2:
    Something else

    BOX3:
    This again

    """,
    'placement': ct.PCOM_MAIN_PLACEMENT,
    'no_boxes': 3,
    'ppp': 3,
    'assertEqual': """

      <div class="clearfix-small pm-n-box-box pm-box-3 box box1 box-start">
      </div><!-- end of .pm-n-box-box -->
      <div class="clearfix-small pm-n-box-box pm-box-3 box box2">
      </div><!-- end of .pm-n-box-box -->
      <div class="clearfix-small pm-n-box-box pm-box-3 box box3 box-end">
      </div><!-- end of .pm-n-box-box -->

    """
    },

{   'remark': 'Test Case 4:pcom_parse_box_arguments - 1 box syntax - no-boxes = 2, placement = MAIN',
    'syntax': """
    BOX1:
    Something


    """,
    'placement': ct.PCOM_MAIN_PLACEMENT,
    'no_boxes': 2,
    'ppp': 3,
    'assertEqual': """

    """
    },

{   'remark': 'Test Case 5:pcom_parse_box_arguments - 2 box syntax - no-boxes = 2, placement = MAIN',
    'syntax': """

    BOX1:
    Something

    BOX2:
    Something else

    """,
    'placement': ct.PCOM_MAIN_PLACEMENT,
    'no_boxes': 2,
    'ppp': 3,
    'assertEqual': """

      <div class="clearfix-small pm-n-box-box pm-box-2 box box1 box-start">
      </div><!-- end of .pm-n-box-box -->
      <div class="clearfix-small pm-n-box-box pm-box-2 box box2 box-end">
      </div><!-- end of .pm-n-box-box -->

    """
    },

{   'remark': 'Test Case 6:pcom_parse_box_arguments - 5 box syntax - no-boxes = 4, placement = MAIN',
    'syntax': """
    BOX1:
    Something

    BOX2:
    Something else

    BOX3:
    This again

    BOX4:
    This again 2

    BOX5:
    This again 3

    """,
    'placement': ct.PCOM_MAIN_PLACEMENT,
    'no_boxes': 4,
    'ppp': 3,
    'assertEqual': """

      <div class="clearfix-small pm-n-box-box pm-box-4 box box1 box-start">
      </div><!-- end of .pm-n-box-box -->
      <div class="clearfix-small pm-n-box-box pm-box-4 box box2">
      </div><!-- end of .pm-n-box-box -->
      <div class="clearfix-small pm-n-box-box pm-box-4 box box3">
      </div><!-- end of .pm-n-box-box -->
      <div class="clearfix-small pm-n-box-box pm-box-4 box box4 box-end">
      </div><!-- end of .pm-n-box-box -->

    """
    },
]

test_values_3 = [\
{   'remark': 'Test Case 1:pcom_add_box_for_n_box - empty syntax - no-boxes = 3, placement = MAIN',
    'syntax': """

    """,
    'type': 'this-box',
    'placement': ct.PCOM_MAIN_PLACEMENT,
    'no_boxes': 3,
    'ppp': 3,
    'assertEqual': """

      <div class="clearfix-small pm-n-box-box pm-box-3 this-box">
      </div><!-- end of .pm-n-box-box -->

    """
    },

{   'remark': 'Test Case 2:pcom_add_box_for_n_box - text syntax - no-boxes = 2, placement = MAIN',
    'syntax': """

    TEXT=[ Something here ]:

    """,
    'type': 'this-box-here',
    'placement': ct.PCOM_MAIN_PLACEMENT,
    'no_boxes': 2,
    'ppp': 3,
    'assertEqual': """

      <div class="clearfix-small pm-n-box-box pm-box-2 this-box-here">
        <div class="post">
          Something here
        </div><!-- end of .post -->
      </div><!-- end of .pm-n-box-box -->

    """
    },

{   'remark': 'Test Case 3:pcom_add_box_for_n_box - text syntax - no-boxes = 2, placement = FOOTER',
    'syntax': """

    TEXT=[ Something here again ]:

    """,
    'type': 'this-box-here',
    'placement': ct.PCOM_FOOTER_PLACEMENT,
    'no_boxes': 2,
    'ppp': 3,
    'assertEqual': """

      <div class="clearfix-small pm-n-box-box pm-box-2 this-box-here">
        <div class="post">
          Something here again
        </div><!-- end of .post -->
      </div><!-- end of .pm-n-box-box -->

    """
    },
]

test_values_4 = [\
{   'remark': 'Test Case 1:pcom_parse_box_arguments - empty syntax, empty command',
    'command': '',
    'syntax': """

    """,
    'ppp': 3,
    'assertEqual': """


    """
    },

{   'remark': 'Test Case 2:pcom_parse_box_arguments - empty syntax, TEXT command',
    'command': 'TEXT',
    'syntax': '',
    'ppp': 3,
    'assertEqual': """


    """
    },
{   'remark': 'Test Case 3:pcom_parse_box_arguments - syntax, TEXT command',
    'command': 'TEXT',
    'syntax': 'Something there',
    'ppp': 3,
    'assertEqual': """

        <div class="post">
          Something there
        </div><!-- end of .post -->

    """
    },

{   'remark': 'Test Case 4:pcom_parse_box_arguments - syntax, MENU command',
    'command': 'MENU',
    'syntax': 'Something there',
    'ppp': 3,
    'assertEqual': """

        <div class="pm-nav clearfix-small">
        <div class="pm-nav-menu clearfix-small">
          <ul>
          </ul>
        </div><!-- end of NAV menu -->
        </div><!-- end of .pm-nav -->

    """
    },

{   'remark': 'Test Case 5:pcom_parse_box_arguments - syntax, TITLE command',
    'command': 'TITLE',
    'syntax': 'Something there',
    'ppp': 3,
    'assertEqual': """

    <div class="pm-title-nav">Something there</div><!-- end of .pm-title-nav -->

    """
    },

{   'remark': 'Test Case 5:pcom_parse_box_arguments - syntax, SEARCHBAR command',
    'command': 'SEARCHBAR',
    'syntax': 'Something there',
    'ppp': 3,
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

{   'remark': 'Test Case 6:pcom_parse_box_arguments - syntax, QUOTE command',
    'command': 'QUOTE',
    'syntax': 'Something there',
    'ppp': 3,
    'assertEqual': """

      <div class="post pm-quote clearfix-small">
        <span class="pm-quotation-marks"><i class="fa fa-quote-left fa-3x fa-pull-left" aria-hidden="true"></i></span>

        <span class="pm-quote-ref">
        </span><!-- end of .pm-quote-ref -->
      </div><!-- end of .pm-quote -->

    """
    },

{   'remark': 'Test Case 7:pcom_parse_box_arguments - syntax, POSTLIST command',
    'command': 'POSTLIST',
    'syntax': 'Something there',
    'ppp': 3,
    'assertEqual': """

<div class="pm-post-list-custom clearfix-small">
POSTLIST=[:3:False]:
    </div><!-- end of .pm-post-list -->

    """
    },
]

test_values_5 = [\
{   'remark': 'Test Case 1:pcom_process_n_box_menu_command - empty syntax',
    'syntax': """

    """,
    'assertEqual': """

        <div class="pm-nav clearfix-small">
        <div class="pm-nav-menu clearfix-small">
          <ul>
          </ul>
        </div><!-- end of NAV menu -->
        </div><!-- end of .pm-nav -->

    """
    },

{   'remark': 'Test Case 2:pcom_process_n_box_menu_command - syntax title',
    'syntax': """
    title={ This title }:
    """,
    'assertEqual': """

        <div class="pm-nav clearfix-small">
        <div class="pm-title-nav">This title</div><!-- end of .pm-title-nav -->
        <div class="pm-nav-menu clearfix-small">
          <ul>
          </ul>
        </div><!-- end of NAV menu -->
        </div><!-- end of .pm-nav -->

    """
    },
]

test_values_6 = [\
{   'remark': 'Test Case 1:pcom_process_n_box_text_command - syntax NONE',
    'syntax': ct.PCOM_NO_ENTRY,
    'assertIn': []
    },

{   'remark': 'Test Case 1:pcom_process_n_box_text_command - syntax',
    'syntax': """
    A whole load of Text
    And other stuff
    """,
    'assertIn': [\
        '        <div class="post">',
        '              A whole load of Text',
        '              And other stuff',
        '        </div><!-- end of .post -->'
        ]
    },
]
