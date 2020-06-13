#
import libraries.constants as ct
import libraries.globals as gb
import libraries.schematics as sch

from collections import OrderedDict
#

test_values_1 = [\
{   'remark': 'Test Case 1:pcom_process_custom_command - empty',
    'command': '',
    'assertEqual': {\
        'command': '',
        'custom_class': ct.PCOM_NO_ENTRY
        }
    },
{   'remark': 'Test Case 2:pcom_process_custom_command -  not custom',
    'command': 'READ',
    'assertEqual': {\
        'command': 'READ',
        'custom_class': ct.PCOM_NO_ENTRY
        }
    },
{   'remark': 'Test Case 3:pcom_process_custom_command -  custom 1',
    'command': 'READ_CUSTOM: something ',
    'assertEqual': {\
        'command': 'READ',
        'custom_class': 'something'
        }
    },
{   'remark': 'Test Case 4:pcom_process_custom_command -  custom 2',
    'command': 'ENJOY_CUSTOM: this-thing here ',
    'assertEqual': {\
        'command': 'ENJOY',
        'custom_class': 'this-thing here'
        }
    },
]

test_values_2 = [\
{   'remark': 'Test Case 1:pcom_process_custom_command -  empty placement',
    'command': '',
    'syntax': '',
    'placement': '',
    'type': '',
    'settings': gb.DEFAULT_SETTINGS,
    'default_type': 'default_main',
    'default_entry': '%%SOMETHING:: Next',
    'assertEqual': {\
        'syntax': ''
        }
    },
{   'remark': 'Test Case 2:pcom_use_defaults - header placement',
    'command': '',
    'syntax': '',
    'placement': ct.PCOM_HEADER_PLACEMENT,
    'type': '',
    'settings': gb.DEFAULT_SETTINGS,
    'default_type': 'default_header',
    'default_entry': '%%SOMETHING:: Next HEADER',
    'assertEqual': {\
        'syntax': '%%SOMETHING:: Next HEADER'
        }
    },
{   'remark': 'Test Case 3:pcom_use_defaults - main only placement - type empty',
    'command': '',
    'syntax': '',
    'placement': ct.PCOM_MAIN_PLACEMENT,
    'type': '',
    'settings': gb.DEFAULT_SETTINGS,
    'default_type': 'default_main',
    'default_entry': '%%SOMETHING:: Next MAIN',
    'assertEqual': {\
        'syntax': '%%SOMETHING:: Next MAIN'
        }
    },
{   'remark': 'Test Case 4:pcom_use_defaults - before placement - entry empty',
    'command': '',
    'syntax': '',
    'placement': ct.PCOM_MAIN_PLACEMENT,
    'type': ct.PCOM_BEFORE_TYPE,
    'settings': gb.DEFAULT_SETTINGS,
    'default_type': 'default_main',
    'default_entry': '%%SOMETHING:: Next MAIN',
    'assertEqual': {\
        'syntax': ''
        }
    },
{   'remark': 'Test Case 5:pcom_use_defaults - before placement - entry not empty',
    'command': '',
    'syntax': '',
    'placement': ct.PCOM_MAIN_PLACEMENT,
    'type': ct.PCOM_BEFORE_TYPE,
    'settings': gb.DEFAULT_SETTINGS,
    'default_type': 'default_before',
    'default_entry': '%%SOMETHING:: Next BEFORE',
    'assertEqual': {\
        'syntax': '%%SOMETHING:: Next BEFORE'
        }
    },
{   'remark': 'Test Case 6:pcom_use_defaults - after placement - entry empty',
    'command': '',
    'syntax': '',
    'placement': ct.PCOM_MAIN_PLACEMENT,
    'type': ct.PCOM_AFTER_TYPE,
    'settings': gb.DEFAULT_SETTINGS,
    'default_type': 'default_main',
    'default_entry': '%%SOMETHING:: Next MAIN',
    'assertEqual': {\
        'syntax': ''
        }
    },
{   'remark': 'Test Case 7:pcom_use_defaults - after placement - entry not empty',
    'command': '',
    'syntax': '',
    'placement': ct.PCOM_MAIN_PLACEMENT,
    'type': ct.PCOM_AFTER_TYPE,
    'settings': gb.DEFAULT_SETTINGS,
    'default_type': 'default_after',
    'default_entry': '%%SOMETHING:: Next AFTER',
    'assertEqual': {\
        'syntax': '%%SOMETHING:: Next AFTER'
        }
    },
{   'remark': 'Test Case 8:pcom_use_defaults - sidebar placement',
    'command': '',
    'syntax': '',
    'placement': ct.PCOM_SIDEBAR_PLACEMENT,
    'type': '',
    'settings': gb.DEFAULT_SETTINGS,
    'default_type': 'default_sidebar',
    'default_entry': '%%SOMETHING:: Next SIDEBAR',
    'assertEqual': {\
        'syntax': '%%SOMETHING:: Next SIDEBAR'
        }
    },
{   'remark': 'Test Case 9:pcom_use_defaults - footer placement',
    'command': '',
    'syntax': '',
    'placement': ct.PCOM_FOOTER_PLACEMENT,
    'type': 'This',
    'settings': gb.DEFAULT_SETTINGS,
    'default_type': 'default_footer',
    'default_entry': '%%SOMETHING:: Next FOOTER',
    'assertEqual': {\
        'syntax': '%%SOMETHING:: Next FOOTER'
        }
    },
]

test_values_3 = [\
{   'remark': 'Test Case 1:pcom_use_settings_defaults -  empty placement',
    'placement': '',
    'settings': gb.DEFAULT_SETTINGS,
    'default_type': 'default_main',
    'default_entry': '%%SOMETHING:: Next',
    'assertEqual': ''
    },
{   'remark': 'Test Case 2:pcom_use_settings_defaults - header placement',
    'placement': ct.PCOM_SETTINGS_HEADER,
    'settings': gb.DEFAULT_SETTINGS,
    'default_type': 'default_header',
    'default_entry': '%%SOMETHING:: Header',
    'assertEqual': '%%SOMETHING:: Header'
    },
{   'remark': 'Test Case 3:pcom_use_settings_defaults - Before placement',
    'placement': ct.PCOM_SETTINGS_BEFORE,
    'settings': gb.DEFAULT_SETTINGS,
    'default_type': 'default_before',
    'default_entry': '%%SOMETHING:: Before',
    'assertEqual': '%%SOMETHING:: Before'
    },
{   'remark': 'Test Case 4:pcom_use_settings_defaults - After placement',
    'placement': ct.PCOM_SETTINGS_AFTER,
    'settings': gb.DEFAULT_SETTINGS,
    'default_type': 'default_after',
    'default_entry': '%%SOMETHING:: Main',
    'assertEqual': '%%SOMETHING:: Main'
    },
{   'remark': 'Test Case 5:pcom_use_settings_defaults - Sidebar placement',
    'placement': ct.PCOM_SETTINGS_SIDEBAR,
    'settings': gb.DEFAULT_SETTINGS,
    'default_type': 'default_sidebar',
    'default_entry': '%%SOMETHING:: Sidebar',
    'assertEqual': '%%SOMETHING:: Sidebar'
    },
{   'remark': 'Test Case 6:pcom_use_settings_defaults - Footer placement',
    'placement': ct.PCOM_SETTINGS_FOOTER,
    'settings': gb.DEFAULT_SETTINGS,
    'default_type': 'default_footer',
    'default_entry': '%%SOMETHING:: Footer',
    'assertEqual': '%%SOMETHING:: Footer'
    },
]

test_values_4 = [\
{   'remark': 'Test Case 1:pcom_process_nav_command - footer placement',
    'syntax': '',
    'custom_class': '',
    'placement': ct.PCOM_FOOTER_PLACEMENT,
    'type': 'This',
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': """

  <div class="pm-nav clearfix-small">
    <div class="pm-nav-menu-search clearfix-small">
    <div class="pm-nav-menu clearfix-small">
      <ul>
      </ul>
    </div><!-- end of NAV menu -->
    </div><!-- end of .pm-nav-menu-search -->
  </div><!-- end of .pm-nav -->

    """
    },
{   'remark': 'Test Case 2:pcom_process_nav_command - main placement wiht custom class',
    'syntax': '',
    'custom_class': 'my-class',
    'placement': ct.PCOM_MAIN_PLACEMENT,
    'type': 'This',
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': """

  <div class="pm-nav clearfix-small my-class">
    <div class="pm-nav-menu-search clearfix-small">
    <div class="pm-nav-menu clearfix-small">
      <ul>
      </ul>
    </div><!-- end of NAV menu -->
    </div><!-- end of .pm-nav-menu-search -->
  </div><!-- end of .pm-nav -->

    """
    },
{   'remark': 'Test Case 3:pcom_process_nav_command - header placement with custom class',
    'syntax': '',
    'custom_class': 'my-class',
    'placement': ct.PCOM_HEADER_PLACEMENT,
    'type': 'This',
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': """

  <div class="pm-nav clearfix-small my-class">
    <div class="pm-responsive-icon">
      <div class="pm-resp-icon">
      <i class="fa fa-bars fa-x" aria-hidden="true"></i>
      </div>
    </div>
    <div class="pm-nav-menu-search clearfix-small">
    <div class="pm-nav-menu clearfix-small">
      <ul>
      </ul>
    </div><!-- end of NAV menu -->
    </div><!-- end of .pm-nav-menu-search -->
  </div><!-- end of .pm-nav -->

    """
    },
]

test_values_5 = [\
{   'remark': 'Test Case 1:pcom_process_menu_command - footer placement',
    'syntax': '',
    'custom_class': '',
    'placement': ct.PCOM_FOOTER_PLACEMENT,
    'type': 'This',
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': """

  <div class="pm-nav clearfix-small">
  <div class="pm-general-menu clearfix-small">
    <div class="pm-nav-menu clearfix-small">
      <ul>
      </ul>
    </div><!-- end of NAV menu -->
  </div><!-- end of .pm-general-menu -->
  </div><!-- end of .pm-nav -->

    """
    },
{   'remark': 'Test Case 2:pcom_process_menu_command - main placement with custom class',
    'syntax': '',
    'custom_class': 'my-class',
    'placement': ct.PCOM_MAIN_PLACEMENT,
    'type': 'This',
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': """

<div class="main-outer clearfix-small my-class">
  <div class="main-inner clearfix-small my-class">
  <div class="pm-nav clearfix-small my-class">
  <div class="pm-general-menu clearfix-small my-class">
    <div class="pm-nav-menu clearfix-small">
      <ul>
      </ul>
    </div><!-- end of NAV menu -->
  </div><!-- end of .pm-general-menu -->
  </div><!-- end of .pm-nav -->
  </div><!-- end of .main-inner -->
</div><!-- end of .main-outer -->

    """
    },
{   'remark': 'Test Case 3:pcom_process_menu_command - header placement wiht custom class',
    'syntax': '',
    'custom_class': 'my-class',
    'placement': ct.PCOM_HEADER_PLACEMENT,
    'type': 'This',
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': """

  <div class="pm-nav clearfix-small my-class">
  </div><!-- end of .pm-nav -->

    """
    },
]

test_values_6 = [\
{   'remark': 'Test Case 1:pcom_process_menu_command_syntax - footer placement',
    'syntax': '',
    'custom_class': '',
    'placement': ct.PCOM_FOOTER_PLACEMENT,
    'type': 'This',
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': """

    """
    },
{   'remark': 'Test Case 2:pcom_process_menu_command_syntax - empty syntax - NAV',
    'syntax': '',
    'custom_class': '',
    'placement': ct.PCOM_HEADER_PLACEMENT,
    'type': ct.PCOM_NAV_COMMAND,
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': """

    <div class="pm-responsive-icon">
      <div class="pm-resp-icon">
      <i class="fa fa-bars fa-x" aria-hidden="true"></i>
      </div>
    </div>
    <div class="pm-nav-menu-search clearfix-small">
    <div class="pm-nav-menu clearfix-small">
      <ul>
      </ul>
    </div><!-- end of NAV menu -->
    </div><!-- end of .pm-nav-menu-search -->

    """
    },

{   'remark': 'Test Case 3:pcom_process_menu_command_syntax - NAV in header - 1 link',
    'syntax': """
mlk={ href="something" name="this"}:
    """,
    'custom_class': '',
    'placement': ct.PCOM_HEADER_PLACEMENT,
    'type': ct.PCOM_NAV_COMMAND,
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': """

    <div class="pm-responsive-icon">
      <div class="pm-resp-icon">
      <i class="fa fa-bars fa-x" aria-hidden="true"></i>
      </div>
    </div>
    <div class="pm-nav-menu-search clearfix-small">
    <div class="pm-nav-menu clearfix-small">
      <ul>
      <li><a href="something" name="this">this</a></li>
      </ul>
    </div><!-- end of NAV menu -->
    </div><!-- end of .pm-nav-menu-search -->

    """
    },

{   'remark': 'Test Case 4:pcom_process_menu_command_syntax - NAV in header - 2 links',
    'syntax': """
mlk={ href="something" name="this"}:
mlk={ href="something-else" name="this again"}:
    """,
    'custom_class': '',
    'placement': ct.PCOM_HEADER_PLACEMENT,
    'type': ct.PCOM_NAV_COMMAND,
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': """

    <div class="pm-responsive-icon">
      <div class="pm-resp-icon">
      <i class="fa fa-bars fa-x" aria-hidden="true"></i>
      </div>
    </div>
    <div class="pm-nav-menu-search clearfix-small">
    <div class="pm-nav-menu clearfix-small">
      <ul>
      <li><a href="something" name="this">this</a></li>
      <li><a href="something-else" name="this again">this again</a></li>
      </ul>
    </div><!-- end of NAV menu -->
    </div><!-- end of .pm-nav-menu-search -->

    """
    },

{   'remark': 'Test Case 5:pcom_process_menu_command_syntax - NAV not in header - 2 links',
    'syntax': """
mlk={ href="something" name="this"}:
mlk={ href="something-else" name="this again"}:
    """,
    'custom_class': '',
    'placement': ct.PCOM_MAIN_PLACEMENT,
    'type': ct.PCOM_NAV_COMMAND,
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': """

    <div class="pm-nav-menu-search clearfix-small">
    <div class="pm-nav-menu clearfix-small">
      <ul>
      <li><a href="something" name="this">this</a></li>
      <li><a href="something-else" name="this again">this again</a></li>
      </ul>
    </div><!-- end of NAV menu -->
    </div><!-- end of .pm-nav-menu-search -->

    """
    },

{   'remark': 'Test Case 6:pcom_process_menu_command_syntax - NAV not in header - 2 links custom class',
    'syntax': """
mlk={ href="something" name="this"}:
mlk={ href="something-else" name="this again"}:
    """,
    'custom_class': 'my-class',
    'placement': ct.PCOM_MAIN_PLACEMENT,
    'type': ct.PCOM_NAV_COMMAND,
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': """

    <div class="pm-nav-menu-search clearfix-small">
    <div class="pm-nav-menu clearfix-small">
      <ul>
      <li><a href="something" name="this">this</a></li>
      <li><a href="something-else" name="this again">this again</a></li>
      </ul>
    </div><!-- end of NAV menu -->
    </div><!-- end of .pm-nav-menu-search -->

    """
    },

{   'remark': 'Test Case 7:pcom_process_menu_command_syntax - NAV in header - 2 links and logo',
    'syntax': """
mlk={ href="something" name="this"}:
mlk={ href="something-else" name="this again"}:
logo={ src="a-logo.png" }:
    """,
    'custom_class': '',
    'placement': ct.PCOM_HEADER_PLACEMENT,
    'type': ct.PCOM_NAV_COMMAND,
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': """

    <div class="pm-responsive-icon">
      <div class="pm-resp-icon">
      <i class="fa fa-bars fa-x" aria-hidden="true"></i>
      </div>
    </div>
    <div class="pm-nav-logo">
      <a href="/" name="A Morfless Site"><img src="a-logo.png" alt="A Morfless Site" /></a>
    </div><!-- end of logo -->
    <div class="pm-nav-menu-search with-logo clearfix-small">
    <div class="pm-nav-menu nav-with-logo clearfix-small">
      <ul>
      <li><a href="something" name="this">this</a></li>
      <li><a href="something-else" name="this again">this again</a></li>
      </ul>
    </div><!-- end of NAV menu -->
    </div><!-- end of .pm-nav-menu-search -->

    """
    },

{   'remark': 'Test Case 8:pcom_process_menu_command_syntax - NAV in header - 2 links, logo searchbar, custom class',
    'syntax': """
mlk={ href="something" name="this"}:
mlk={ href="something-else" name="this again"}:
logo={ src="a-logo.png" }:
searchbar={}:
    """,
    'custom_class': 'my-class',
    'placement': ct.PCOM_HEADER_PLACEMENT,
    'type': ct.PCOM_NAV_COMMAND,
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': """

    <div class="pm-responsive-icon">
      <div class="pm-resp-icon">
      <i class="fa fa-bars fa-x" aria-hidden="true"></i>
      </div>
    </div>
    <div class="pm-nav-logo">
      <a href="/" name="A Morfless Site"><img src="a-logo.png" alt="A Morfless Site" /></a>
    </div><!-- end of logo -->
    <div class="pm-nav-menu-search with-logo clearfix-small">
    <div class="pm-nav-menu nav-with-logo clearfix-small">
      <ul>
      <li><a href="something" name="this">this</a></li>
      <li><a href="something-else" name="this again">this again</a></li>
      </ul>
    </div><!-- end of NAV menu -->

    <div id="pm-nav-searchbar" class="clearfix-small">

    <div class="pm-searchbar clearfix-small">
      <form action="/$$SEARCH$$/" autocomplete="on">
      <input id="search" type="text" name="s" />
      </form>
      <span id="search-submit" class="pm-search-button" name="search-submit"></span>
    </div><!-- end of #pm-searchbar -->
    </div><!-- end of #pm-nav-searchbar-->
    </div><!-- end of .pm-nav-menu-search -->

    """
    },

{   'remark': 'Test Case 9:pcom_process_menu_command_syntax - NAV in header - 2 links, logo, searchbar, title, custom class',
    'syntax': """
mlk={ href="something" name="this"}:
mlk={ href="something-else" name="this again"}:
logo={ src="a-logo.png" }:
searchbar={}:
title={ My title }:
    """,
    'custom_class': 'my-class',
    'placement': ct.PCOM_HEADER_PLACEMENT,
    'type': ct.PCOM_NAV_COMMAND,
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': """

    <div class="pm-responsive-icon">
      <div class="pm-resp-icon">
      <i class="fa fa-bars fa-x" aria-hidden="true"></i>
      </div>
    </div>
    <div class="pm-nav-logo">
      <a href="/" name="A Morfless Site"><img src="a-logo.png" alt="A Morfless Site" /></a>
    </div><!-- end of logo -->
    <div class="pm-nav-menu-search with-logo clearfix-small">
    <div class="pm-nav-menu nav-with-logo clearfix-small">
      <ul>
      <li><a href="something" name="this">this</a></li>
      <li><a href="something-else" name="this again">this again</a></li>
      </ul>
    </div><!-- end of NAV menu -->

    <div id="pm-nav-searchbar" class="clearfix-small">

    <div class="pm-searchbar clearfix-small">
      <form action="/$$SEARCH$$/" autocomplete="on">
      <input id="search" type="text" name="s" />
      </form>
      <span id="search-submit" class="pm-search-button" name="search-submit"></span>
    </div><!-- end of #pm-searchbar -->
    </div><!-- end of #pm-nav-searchbar-->
    </div><!-- end of .pm-nav-menu-search -->

    """
    },

{   'remark': 'Test Case 10:pcom_process_menu_command_syntax - MENU in header - 2 links, logo, searchbar, title, custom class',
    'syntax': """
mlk={ href="something" name="this"}:
mlk={ href="something-else" name="this again"}:
logo={ src="a-logo.png" }:
searchbar={}:
title={ My title }:
    """,
    'custom_class': 'my-class',
    'placement': ct.PCOM_HEADER_PLACEMENT,
    'type': ct.PCOM_MENU_COMMAND,
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': """

    """
    },

{   'remark': 'Test Case 11:pcom_process_menu_command_syntax - MENU in main - 2 links, logo, searchbar, title, custom class',
    'syntax': """
mlk={ href="something" name="this"}:
mlk={ href="something-else" name="this again"}:
logo={ src="a-logo.png" }:
searchbar={}:
title={ My title }:
    """,
    'custom_class': 'my-class',
    'placement': ct.PCOM_MAIN_PLACEMENT,
    'type': ct.PCOM_MENU_COMMAND,
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': """

  <div class="pm-general-menu clearfix-small my-class">
    <div class="pm-title-nav">My title</div><!-- end of .pm-title-nav -->
    <div class="pm-nav-menu nav-with-logo clearfix-small">
      <ul>
      <li><a href="something" name="this">this</a></li>
      <li><a href="something-else" name="this again">this again</a></li>
      </ul>
    </div><!-- end of NAV menu -->
  </div><!-- end of .pm-general-menu -->

    """
    },

{   'remark': 'Test Case 12:pcom_process_menu_command_syntax - MENU in main with sidebar- 2 links, logo, searchbar, title, custom class',
    'syntax': """
mlk={ href="something" name="this"}:
mlk={ href="something-else" name="this again"}:
logo={ src="a-logo.png" }:
searchbar={}:
title={ My title }:
    """,
    'custom_class': 'my-class',
    'placement': ct.PCOM_MAIN_WITH_SIDEBAR_PLACEMENT,
    'type': ct.PCOM_MENU_COMMAND,
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': """

  <div class="pm-general-menu clearfix-small my-class">
    <div class="pm-title-nav">My title</div><!-- end of .pm-title-nav -->
    <div class="pm-nav-menu nav-with-logo clearfix-small">
      <ul>
      <li><a href="something" name="this">this</a></li>
      <li><a href="something-else" name="this again">this again</a></li>
      </ul>
    </div><!-- end of NAV menu -->
  </div><!-- end of .pm-general-menu -->

    """
    },

{   'remark': 'Test Case 13:pcom_process_menu_command_syntax - MENU in footer - 2 links, logo, searchbar, title, custom class',
    'syntax': """
mlk={ href="something" name="this"}:
mlk={ href="something-else" name="this again"}:
logo={ src="a-logo.png" }:
searchbar={}:
title={ My title }:
    """,
    'custom_class': 'my-class',
    'placement': ct.PCOM_FOOTER_PLACEMENT,
    'type': ct.PCOM_MENU_COMMAND,
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': """

  <div class="pm-general-menu clearfix-small my-class">
    <div class="pm-title-nav">My title</div><!-- end of .pm-title-nav -->
    <div class="pm-nav-menu nav-with-logo clearfix-small">
      <ul>
      <li><a href="something" name="this">this</a></li>
      <li><a href="something-else" name="this again">this again</a></li>
      </ul>
    </div><!-- end of NAV menu -->
  </div><!-- end of .pm-general-menu -->

    """
    },

{   'remark': 'Test Case 14:pcom_process_menu_command_syntax - MENU in sidebar - 2 links, logo, searchbar, title, custom class',
    'syntax': """
mlk={ href="something" name="this"}:
mlk={ href="something-else" name="this again"}:
logo={ src="a-logo.png" }:
searchbar={}:
title={ My title }:
    """,
    'custom_class': 'my-class',
    'placement': ct.PCOM_SIDEBAR_PLACEMENT,
    'type': ct.PCOM_MENU_COMMAND,
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': """

<div class="pm-sidebar-content clearfix-small my-class">
    <div class="pm-title-nav">My title</div><!-- end of .pm-title-nav -->
    <div class="pm-nav-menu nav-with-logo clearfix-small">
      <ul>
      <li><a href="something" name="this">this</a></li>
      <li><a href="something-else" name="this again">this again</a></li>
      </ul>
    </div><!-- end of NAV menu -->
</div><!-- end of .pm-sidebar-content -->

    """
    },

]
