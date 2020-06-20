#
import libraries.constants as ct
import libraries.globals as gb
import libraries.schematics as sch

from collections import OrderedDict
#

test_values_1 = [\
{   'remark': 'Test Case 1:pcom_insert_quote_box_command -  HEADER placement, empty syntax',
    'syntax': '',
    'custom_class': '',
    'placement': ct.PCOM_HEADER_PLACEMENT,
    'type': '',
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': """

      <div class="post pm-quote clearfix-small">
        <span class="pm-quotation-marks"><i class="fa fa-quote-left fa-3x fa-pull-left" aria-hidden="true"></i></span>

        <span class="pm-quote-ref">
        </span><!-- end of .pm-quote-ref -->
      </div><!-- end of .pm-quote -->

    """
    },

{   'remark': 'Test Case 2:pcom_insert_quote_box_command -  MAIN placement, body only and custom class',
    'syntax': 'body={ This is the body of the quote with various things in it }:',
    'custom_class': 'my-class',
    'placement': ct.PCOM_MAIN_PLACEMENT,
    'type': '',
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': """

<div class="main-outer clearfix-small pm-quote-wrap my-class">
  <div class="main-inner clearfix-small pm-quote-wrap my-class">
      <div class="post pm-quote clearfix-small my-class">
        <span class="pm-quotation-marks"><i class="fa fa-quote-left fa-3x fa-pull-left" aria-hidden="true"></i></span>
            This is the body of the quote with various things in it
        <span class="pm-quote-ref">
        </span><!-- end of .pm-quote-ref -->
      </div><!-- end of .pm-quote -->

  </div><!-- end of .main-inner -->
</div><!-- end of .main-outer -->

    """
    },

{   'remark': 'Test Case 3:pcom_insert_quote_box_command -  MAIN placement, body and ref, custom class',
    'syntax': """

    body={ This is the body of the quote with various things in it }:
    ref={ John of Old }:

    """,
    'custom_class': 'my-class',
    'placement': ct.PCOM_MAIN_PLACEMENT,
    'type': '',
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': """

<div class="main-outer clearfix-small pm-quote-wrap my-class">
  <div class="main-inner clearfix-small pm-quote-wrap my-class">
      <div class="post pm-quote clearfix-small my-class">
        <span class="pm-quotation-marks"><i class="fa fa-quote-left fa-3x fa-pull-left" aria-hidden="true"></i></span>
            This is the body of the quote with various things in it
        <span class="pm-quote-ref">John of Old
        </span><!-- end of .pm-quote-ref -->
      </div><!-- end of .pm-quote -->

  </div><!-- end of .main-inner -->
</div><!-- end of .main-outer -->

    """
    },

{   'remark': 'Test Case 4:pcom_insert_quote_box_command -  FOOTER placement, body, ref, url custom class',
    'syntax': """

    body={ This is the body of the quote with various things in it }:
    ref={ John of Old }:
    link={ http://something/to/linkto/ }:

    """,
    'custom_class': 'my-class',
    'placement': ct.PCOM_FOOTER_PLACEMENT,
    'type': '',
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': """

      <div class="post pm-quote clearfix-small my-class">
        <span class="pm-quotation-marks"><i class="fa fa-quote-left fa-3x fa-pull-left" aria-hidden="true"></i></span>
            This is the body of the quote with various things in it
        <span class="pm-quote-ref">
          <a href="http://something/to/linkto/">John of Old</a>
        </span><!-- end of .pm-quote-ref -->
      </div><!-- end of .pm-quote -->


    """
    },
]

test_values_2 = [\
{   'remark': 'Test Case 1:pcom_add_header_content_to_head -  FOOTER placement, syntax',
    'syntax': """

    content={

    Something here
    Something there


    }:
    """,
    'custom_class': 'my-class',
    'placement': ct.PCOM_FOOTER_PLACEMENT,
    'type': '',
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': []
    },

{   'remark': 'Test Case 2:pcom_add_header_content_to_head -  HEADER placement, empty syntax',
    'syntax': """

    """,
    'custom_class': 'my-class',
    'placement': ct.PCOM_HEADER_PLACEMENT,
    'type': '',
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': []
    },

{   'remark': 'Test Case 3:pcom_add_header_content_to_head -  HEADER placement, syntax',
    'syntax': """

    content={

    Something here
    Something there


    }:
    """,
    'custom_class': 'my-class',
    'placement': ct.PCOM_HEADER_PLACEMENT,
    'type': '',
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': ['Something here\n    Something there']
    },

{   'remark': 'Test Case 4:pcom_add_header_content_to_head -  HEADER placement, syntax with custom added',
    'syntax': """

    content_CUSTOM: this thing ={

    Something here
    Something there


    }:
    """,
    'custom_class': 'my-class',
    'placement': ct.PCOM_HEADER_PLACEMENT,
    'type': '',
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': ['Something here\n    Something there']
    },

{   'remark': 'Test Case 5:pcom_add_header_content_to_head -  HEADER placement, syntax with custom added and other keywords',
    'syntax': """

    content_CUSTOM: this thing ={

    Something here
    Something there


    }:

    ref={ I know }:

    """,
    'custom_class': 'my-class',
    'placement': ct.PCOM_HEADER_PLACEMENT,
    'type': '',
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': ['Something here\n    Something there']
    },
]

test_values_3 = [\
{   'remark': 'Test Case 1:pcom_add_footer_content_to_footer -  HEADER placement, syntax',
    'syntax': """

    content={

    Something here
    Something there


    }:
    """,
    'custom_class': 'my-class',
    'placement': ct.PCOM_HEADER_PLACEMENT,
    'type': '',
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': []
    },

{   'remark': 'Test Case 2:pcom_add_footer_content_to_footer -  FOOTER placement, empty syntax',
    'syntax': """

    """,
    'custom_class': 'my-class',
    'placement': ct.PCOM_FOOTER_PLACEMENT,
    'type': '',
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': []
    },

{   'remark': 'Test Case 3:pcom_add_footer_content_to_footer -  FOOTER placement, syntax',
    'syntax': """

    content={

    Something here
    Something there


    }:
    """,
    'custom_class': 'my-class',
    'placement': ct.PCOM_FOOTER_PLACEMENT,
    'type': '',
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': ['Something here\n    Something there']
    },

{   'remark': 'Test Case 4:pcom_add_footer_content_to_footer -  FOOTER placement, syntax with custom added',
    'syntax': """

    content_CUSTOM: this thing ={

    Something here
    Something there


    }:
    """,
    'custom_class': 'my-class',
    'placement': ct.PCOM_FOOTER_PLACEMENT,
    'type': '',
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': ['Something here\n    Something there']
    },

{   'remark': 'Test Case 5:pcom_add_footer_content_to_footer -  FOOTER placement, syntax with custom added and other keywords',
    'syntax': """

    content_CUSTOM: this thing ={

    Something here
    Something there


    }:

    ref={ I know }:

    """,
    'custom_class': 'my-class',
    'placement': ct.PCOM_FOOTER_PLACEMENT,
    'type': '',
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': ['Something here\n    Something there']
    },
]

test_values_4 = [\
{   'remark': 'Test Case 1:pcom_process_section_command -  FOOTER placement, empty syntax',
    'syntax': """

    """,
    'custom_class': '',
    'placement': ct.PCOM_FOOTER_PLACEMENT,
    'type': '',
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': """


    """
    },
{   'remark': 'Test Case 2:pcom_process_section_command -  FOOTER placement, syntax - name identifier only but empty name',
    'syntax': """

    {{ }}

    """,
    'custom_class': '',
    'placement': ct.PCOM_FOOTER_PLACEMENT,
    'type': '',
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': """


    """
    },

{   'remark': 'Test Case 3:pcom_process_section_command -  FOOTER placement, syntax - name identifier',
    'syntax': """

    {{ section-1 }}

    """,
    'custom_class': '',
    'placement': ct.PCOM_FOOTER_PLACEMENT,
    'type': '',
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': ct.PCOM_NO_ENTRY
    },

{   'remark': 'Test Case 4:pcom_process_section_command -  FOOTER placement, syntax - name identifier, commands before and after but with wrong identifiers',
    'syntax': """

    %%CONTENT::
    {{ section-1 }}
    %%CONTENT_META::

    """,
    'custom_class': '',
    'placement': ct.PCOM_FOOTER_PLACEMENT,
    'type': '',
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': """

<div id="section-1" class="pm-section ">

  NONE
</div><!-- end of section -->

    """
    },

{   'remark': 'Test Case 5:pcom_process_section_command -  MAIN placement, syntax - name identifier, commands before and after but with wrong identifiers, custom class',
    'syntax': """

    [%CONTENT:]
    TEXT=[ Something here]:
    {{ section-1 }}
    [%CONTENT_META:]

    """,
    'custom_class': 'my-class',
    'placement': ct.PCOM_MAIN_PLACEMENT,
    'type': '',
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': '\
$$SIDEBAR_TAB%%<div id="section-1" class="pm-section my-class">\n\
\n\
  \n\
  <div class="main-outer clearfix-small">\n\
    <div class="main-inner clearfix-small">\n\
      <div class="post">\n\
      Something here\n\
      </div><!-- end of .post -->\n\
    </div><!-- end of .main-inner -->\n\
  </div><!-- end of .main-outer -->\n\
  \n\
  CONTENT_META=[MAIN:title,author,date_created,date_modified]:\n\
$$SIDEBAR_TAB%%</div><!-- end of section -->\n'

    },

{   'remark': 'Test Case 6:pcom_process_section_command -  MAIN WITH SIDEBAR placement, syntax - name identifier, commands before and after but with wrong identifiers, custom class',
    'syntax': """

    [%CONTENT:]
    TEXT=[ Something here]:
    {{ section-1 }}
    [%CONTENT_META:]

    """,
    'custom_class': 'my-class',
    'placement': ct.PCOM_MAIN_WITH_SIDEBAR_PLACEMENT,
    'type': '',
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': '\
<div id="section-1" class="pm-section my-class">\n\
\n\
      <div class="post">\n\
      Something here\n\
      </div><!-- end of .post -->\n\
  \n\
  CONTENT_META=[MAIN_WITH_SIDEBAR:title,author,date_created,date_modified]:\n\
</div><!-- end of section -->'

    },
]
