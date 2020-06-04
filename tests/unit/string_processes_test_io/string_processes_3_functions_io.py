#
import libraries.constants as ct
import libraries.globals as gb

from collections import OrderedDict
#

test_values_1 = [\
{   'remark': 'Test Case 1:pcom_create_template_fileroot - no separator',
    'text': 'This item here',
    'separator': '',
    'trim': True,
    'assertEqual': {\
        'command_found': False,
        'syntax_before': 'This item here',
        'syntax_after': ct.PCOM_NO_ENTRY
        }
    },

{   'remark': 'Test Case 2:pcom_create_template_fileroot - separator not in string',
    'text': 'This item here',
    'separator': '%',
    'trim': True,
    'assertEqual': {\
        'command_found': False,
        'syntax_before': 'This item here',
        'syntax_after': ct.PCOM_NO_ENTRY
        }
    },

{   'remark': 'Test Case 3:pcom_create_template_fileroot - separator in string - no trim',
    'text': 'This item here %   And then some',
    'separator': '%',
    'trim': False,
    'assertEqual': {\
        'command_found': True,
        'syntax_before': 'This item here ',
        'syntax_after': '   And then some'
        }
    },

{   'remark': 'Test Case 4:pcom_create_template_fileroot - separator in string - trim',
    'text': 'This item here %   And then some',
    'separator': '%',
    'trim': True,
    'assertEqual': {\
        'command_found': True,
        'syntax_before': 'This item here',
        'syntax_after': 'And then some'
        }
    },

{   'remark': 'Test Case 5:pcom_create_template_fileroot - 2 separators in string - trim',
    'text': 'This item here %   And then some % Again',
    'separator': '%',
    'trim': True,
    'assertEqual': {\
        'command_found': True,
        'syntax_before': 'This item here',
        'syntax_after': 'And then some % Again'
        }
    },
]

test_values_2 = [\
{   'remark': 'Test Case 1:pcom_get_first_command - empty string',
    'text': '',
    'args': {'open': '%%', 'close': '::'},
    'assertEqual': {\
        'command': ct.PCOM_NO_ENTRY,
        'command_syntax': ct.PCOM_NO_ENTRY,
        'next_command': ct.PCOM_NO_ENTRY
        }
    },
{   'remark': 'Test Case 2:pcom_get_first_command - no command',
    'text': 'COMMAND',
    'args': {'open': '%%', 'close': '::'},
    'assertEqual': {\
        'command': ct.PCOM_NO_ENTRY,
        'command_syntax': ct.PCOM_NO_ENTRY,
        'next_command': ct.PCOM_NO_ENTRY
        }
    },
{   'remark': 'Test Case 3:pcom_get_first_command - partial command',
    'text': '%%COMMAND',
    'args': {'open': '%%', 'close': '::'},
    'assertEqual': {\
        'command': ct.PCOM_NO_ENTRY,
        'command_syntax': ct.PCOM_NO_ENTRY,
        'next_command': ct.PCOM_NO_ENTRY
        }
    },
{   'remark': 'Test Case 4:pcom_get_first_command - command no syntax',
    'text': '%% COMMAND ::',
    'args': {'open': '%%', 'close': '::'},
    'assertEqual': {\
        'command': 'COMMAND',
        'command_syntax': ct.PCOM_NO_ENTRY,
        'next_command': ct.PCOM_NO_ENTRY
        }
    },
{   'remark': 'Test Case 5:pcom_get_first_command - command with syntax',
    'text': '%% COMMAND :: This',
    'args': {'open': '%%', 'close': '::'},
    'assertEqual': {\
        'command': 'COMMAND',
        'command_syntax': 'This',
        'next_command': ct.PCOM_NO_ENTRY
        }
    },
{   'remark': 'Test Case 6:pcom_get_first_command - command with syntax then other command start',
    'text': '%% COMMAND :: This %%NEXT',
    'args': {'open': '%%', 'close': '::'},
    'assertEqual': {\
        'command': 'COMMAND',
        'command_syntax': 'This',
        'next_command': '%%NEXT'
        }
    },
{   'remark': 'Test Case 7:pcom_get_first_command - command with syntax then other command full',
    'text': '%% COMMAND :: This %%NEXT::',
    'args': {'open': '%%', 'close': '::'},
    'assertEqual': {\
        'command': 'COMMAND',
        'command_syntax': 'This',
        'next_command': '%%NEXT::'
        }
    },
{   'remark': 'Test Case 8:pcom_get_first_command - command with syntax with different command identifiers',
    'text': '%] COMMAND []: This %%NEXT::',
    'args': {'open': '%]', 'close': '[]:'},
    'assertEqual': {\
        'command': 'COMMAND',
        'command_syntax': 'This %%NEXT::',
        'next_command': ct.PCOM_NO_ENTRY
        }
    },
]

test_values_3 = [\
{   'remark': 'Test Case 1:pcom_process_command_open_close_syntax - empty command and args',
    'syntax': '',
    'args': {},
    'assertEqual': {\
        'command_found': False,
        'command': ct.PCOM_NO_ENTRY,
        'command_syntax': ct.PCOM_NO_ENTRY,
        'syntax_after': ct.PCOM_NO_ENTRY
        }
    },
{   'remark': 'Test Case 2:pcom_process_command_open_close_syntax - command, no identifiers, no args',
    'syntax': 'COMMAND',
    'args': {},
    'assertEqual': {\
        'command_found': False,
        'command': ct.PCOM_NO_ENTRY,
        'command_syntax': ct.PCOM_NO_ENTRY,
        'syntax_after': ct.PCOM_NO_ENTRY
        }
    },
{   'remark': 'Test Case 3:pcom_process_command_open_close_syntax - command, start identifier, no args',
    'syntax': 'COMMAND=[ ',
    'args': {},
    'assertEqual': {\
        'command_found': False,
        'command': ct.PCOM_NO_ENTRY,
        'command_syntax': ct.PCOM_NO_ENTRY,
        'syntax_after': ct.PCOM_NO_ENTRY
        }
    },
{   'remark': 'Test Case 4:pcom_process_command_open_close_syntax - command, identifiers, no syntax, no args',
    'syntax': 'COMMAND=[ ]:',
    'args': {},
    'assertEqual': {\
        'command_found': True,
        'command': 'COMMAND',
        'command_syntax': ct.PCOM_NO_ENTRY,
        'syntax_after': ct.PCOM_NO_ENTRY
        }
    },
{   'remark': 'Test Case 5:pcom_process_command_open_close_syntax - command, identifiers, syntax, no args',
    'syntax': 'COMMAND=[ Syntax here ]:',
    'args': {},
    'assertEqual': {\
        'command_found': True,
        'command': 'COMMAND',
        'command_syntax': 'Syntax here',
        'syntax_after': ct.PCOM_NO_ENTRY
        }
    },
{   'remark': 'Test Case 6:pcom_process_command_open_close_syntax - command, identifiers, syntax, no args, text after',
    'syntax': 'COMMAND=[ Syntax here ]:    Something after',
    'args': {},
    'assertEqual': {\
        'command_found': True,
        'command': 'COMMAND',
        'command_syntax': 'Syntax here',
        'syntax_after': 'Something after'
        }
    },
{   'remark': 'Test Case 7:pcom_process_command_open_close_syntax - command, identifiers, syntax, different args, text after',
    'syntax': 'COMMAND^^ Syntax here --    Something after',
    'args': {'open': '^^', 'close': '--'},
    'assertEqual': {\
        'command_found': True,
        'command': 'COMMAND',
        'command_syntax': 'Syntax here',
        'syntax_after': 'Something after'
        }
    },
]

test_values_4 = [\
{   'remark': 'Test Case 1:pcom_create_html_from_array - empty array',
    'array': [],
    'assertEqual': ''
    },
{   'remark': 'Test Case 2:pcom_create_html_from_array - array 1',
    'array': ['This','That'],
    'assertEqual': 'This\nThat\n'
    },
{   'remark': 'Test Case 1:pcom_create_html_from_array - array 2',
    'array': ['This thing','That thing','More things'],
    'assertEqual': 'This thing\nThat thing\nMore things\n'
    },
]

test_values_5 = [\
{   'remark': 'Test Case 1:pcom_remove_empty_lines - empty',
    'content': '',
    'assertEqual': ''
    },
{   'remark': 'Test Case 2:pcom_remove_empty_lines - no empty lines',
    'content': 'This thing here',
    'assertEqual': 'This thing here'
    },
{   'remark': 'Test Case 3:pcom_remove_empty_lines - empty lines with spaces',
    'content': '\n\n\nThis thing here\n\n\n',
    'assertEqual': 'This thing here\n'
    },
]

test_values_6 = [\
{   'remark': 'Test Case 1:pcom_build_dictionary - empty',
    'dict': {},
    'assertEqual': {}
    },
{   'remark': 'Test Case 2:pcom_build_dictionary - dictionary 1',
    'dict': {\
        'first': ['this','that'],
        'second': {'one':'two'}
        },
    'assertEqual': {\
        'first': ['this','that'],
        'second': {'one':'two'}
        }
    },
{   'remark': 'Test Case 3:pcom_build_dictionary - dictionary 1',
    'dict': {'another': 'entry'},
    'assertEqual': {'another': 'entry'}
    },
]

test_values_7 = [\
{   'remark': 'Test Case 1:pcom_add_tab_to_content_line - empty',
    'content': '',
    'assertEqual': ''
    },
{   'remark': 'Test Case 2:pcom_add_tab_to_content_line - non empty',
    'content': 'What is going on here\nWhat is this about',
    'assertEqual': '  What is going on here\n  What is this about',
    },
]

test_values_8 = [\
{   'remark': 'Test Case 1:pcom_add_2tabs_to_content_line - empty',
    'content': '',
    'assertEqual': ''
    },
{   'remark': 'Test Case 2:pcom_add_2tabs_to_content_line - non empty',
    'content': 'What is going on here\nWhat is this about',
    'assertEqual': '    What is going on here\n    What is this about',
    },
]

test_values_9 = [\
{   'remark': 'Test Case 1:pcom_add_3tabs_to_content_line - empty',
    'content': '',
    'assertEqual': ''
    },
{   'remark': 'Test Case 2:pcom_add_3tabs_to_content_line - non empty',
    'content': 'What is going on here\nWhat is this about',
    'assertEqual': '      What is going on here\n      What is this about',
    },
]
