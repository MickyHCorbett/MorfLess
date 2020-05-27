#
import libraries.constants as ct
import libraries.globals as gb

#
test_values_1 = [\
{   'remark': 'Test Case 1:polimorf_process_settings_schematic - schematic empty, Settings HEADER PLACEMENT',
    'test_val': 'default_header_additions',
    'inputs': {\
        'schematic': '',
        'args': gb.DEFAULT_GET_FIRST_COMMAND_ARGS,
        'placement': ct.PCOM_SETTINGS_HEADER,
        'type': 'post',
        'settings': gb.DEFAULT_SETTINGS
    },
    'assertEqual': {
        'out': [ct.PCOM_NO_ENTRY],
        'default_header_additions': ''
        }
    },
{   'remark': 'Test Case 2:polimorf_process_settings_schematic - schematic NONE, Settings HEADER PLACEMENT',
    'test_val': 'default_header_additions',
    'inputs': {\
        'schematic': ct.PCOM_NO_ENTRY,
        'args': gb.DEFAULT_GET_FIRST_COMMAND_ARGS,
        'placement': ct.PCOM_SETTINGS_HEADER,
        'type': 'post',
        'settings': gb.DEFAULT_SETTINGS
    },
    'assertEqual': {
        'out': [ct.PCOM_NO_ENTRY],
        'default_header_additions': ''
        }
    },
{   'remark': 'Test Case 3:polimorf_process_settings_schematic - schematic, Settings HEADER PLACEMENT',
    'test_val': 'default_header_additions',
    'inputs': {\
        'schematic': '\
        %%CONTENT:: TEXT=[ <p>This is a test paragraph</p> ]:',
        'args': gb.DEFAULT_GET_FIRST_COMMAND_ARGS,
        'placement': ct.PCOM_SETTINGS_HEADER,
        'type': 'post',
        'settings': gb.DEFAULT_SETTINGS
    },
    'assertEqual': {
        'out': ['    <div class="post">\n    <p>This is a test paragraph</p>\n    </div><!-- end of .post -->'],
        'default_header_additions': ''
        }
    },
{   'remark': 'Test Case 4:polimorf_process_settings_schematic - schematic 2, Settings HEADER PLACEMENT',
    'test_val': 'default_header_additions',
    'inputs': {\
        'schematic': '\
        %%CONTENT:: TEXT=[ <p>This is a test paragraph</p> ]:\n\
        %%CONTENT:: TEXT=[ <p>This is another test paragraph</p> ]:',
        'args': gb.DEFAULT_GET_FIRST_COMMAND_ARGS,
        'placement': ct.PCOM_SETTINGS_HEADER,
        'type': 'post',
        'settings': gb.DEFAULT_SETTINGS
    },
    'assertEqual': {
        'out': ['    <div class="post">\n    <p>This is a test paragraph</p>\n    </div><!-- end of .post -->',
        '    <div class="post">\n    <p>This is another test paragraph</p>\n    </div><!-- end of .post -->'],
        'default_header_additions': ''
        }
    },
{   'remark': 'Test Case 5:polimorf_process_settings_schematic - header additions - schematic 2, Settings HEADER PLACEMENT',
    'test_val': 'default_header_additions',
    'inputs': {\
        'schematic': '\
        %%CONTENT:: TEXT=[ <p>This is a test paragraph</p> ]:\n\
        %%CONTENT:: TEXT=[ <p>This is another test paragraph</p> ]:\n\
        %%HEADER_ADDITIONS:: content={ <!-- something to comment --> }:',
        'args': gb.DEFAULT_GET_FIRST_COMMAND_ARGS,
        'placement': ct.PCOM_SETTINGS_HEADER,
        'type': 'post',
        'settings': gb.DEFAULT_SETTINGS
    },
    'assertEqual': {
        'out': ['    <div class="post">\n    <p>This is a test paragraph</p>\n    </div><!-- end of .post -->',
        '    <div class="post">\n    <p>This is another test paragraph</p>\n    </div><!-- end of .post -->', 'NONE'],
        'default_header_additions': ''
        }
    },
{   'remark': 'Test Case 6:polimorf_process_settings_schematic - footer additions - schematic 2, Settings FOOTER PLACEMENT',
    'test_val': 'default_footer_additions',
    'inputs': {\
        'schematic': '\
        %%CONTENT:: TEXT=[ <p>This is a test paragraph</p> ]:\n\
        %%CONTENT:: TEXT=[ <p>This is another test paragraph</p> ]:\n\
        %%FOOTER_ADDITIONS:: content={ <!-- something to comment --> }:',
        'args': gb.DEFAULT_GET_FIRST_COMMAND_ARGS,
        'placement': ct.PCOM_SETTINGS_FOOTER,
        'type': 'post',
        'settings': gb.DEFAULT_SETTINGS
    },
    'assertEqual': {
        'out': ['  <div class="post">\n    <p>This is a test paragraph</p>\n  </div><!-- end of .post -->', '  <div class="post">\n    <p>This is another test paragraph</p>\n  </div><!-- end of .post -->', 'NONE'],
        'default_footer_additions': ''
        }
    },
]

test_values_2 = [\
{   'remark': 'Test Case 1:polimorf_process_additions_schematic - schematic empty, Settings HEADER PLACEMENT',
    'test_val': 'header_additions',
    'inputs': {\
        'schematic': '',
        'args': gb.DEFAULT_GET_FIRST_COMMAND_ARGS,
        'placement': ct.PCOM_SETTINGS_HEADER,
        'type': 'post'
    },
    'assertEqual': {
        'out': [],
        }
    },
{   'remark': 'Test Case 2:polimorf_process_additions_schematic - schematic NONE, Settings HEADER PLACEMENT',
    'test_val': 'header_additions',
    'inputs': {\
        'schematic': ct.PCOM_NO_ENTRY,
        'args': gb.DEFAULT_GET_FIRST_COMMAND_ARGS,
        'placement': ct.PCOM_SETTINGS_HEADER,
        'type': 'post'
    },
    'assertEqual': {
        'out': ct.PCOM_NO_ENTRY,
        }
    },
{   'remark': 'Test Case 3:polimorf_process_additions_schematic - schematic, Settings HEADER PLACEMENT',
    'test_val': 'header_additions',
    'inputs': {\
        'schematic': '\
        %%CONTENT:: TEXT=[ <p>This is a test paragraph</p> ]:',
        'args': gb.DEFAULT_GET_FIRST_COMMAND_ARGS,
        'placement': ct.PCOM_SETTINGS_HEADER,
        'type': 'post'
    },
    'assertEqual': {
        'out': []
        }
    },
{   'remark': 'Test Case 4:polimorf_process_additions_schematic - schematic 2, Settings HEADER PLACEMENT',
    'test_val': 'header_additions',
    'inputs': {\
        'schematic': '\
        %%CONTENT:: TEXT=[ <p>This is a test paragraph</p> ]:\n\
        %%CONTENT:: TEXT=[ <p>This is another test paragraph</p> ]:',
        'args': gb.DEFAULT_GET_FIRST_COMMAND_ARGS,
        'placement': ct.PCOM_SETTINGS_HEADER,
        'type': 'post'
    },
    'assertEqual': {
        'out': []
        }
    },
{   'remark': 'Test Case 5:polimorf_process_additions_schematic - header additions - schematic 2, Settings HEADER PLACEMENT',
    'test_val': 'header_additions',
    'inputs': {\
        'schematic': '\
        %%CONTENT:: TEXT=[ <p>This is a test paragraph</p> ]:\n\
        %%CONTENT:: TEXT=[ <p>This is another test paragraph</p> ]:\n\
        %%HEADER_ADDITIONS:: content={ <!-- something to comment --> }:',
        'args': gb.DEFAULT_GET_FIRST_COMMAND_ARGS,
        'placement': ct.PCOM_SETTINGS_HEADER,
        'type': 'post'
    },
    'assertEqual': {
        'out': ['<!-- something to comment -->'],
        }
    },
{   'remark': 'Test Case 6:polimorf_process_additions_schematic - footer additions - schematic 2, Settings FOOTER PLACEMENT',
    'test_val': 'footer_additions',
    'inputs': {\
        'schematic': '\
        %%CONTENT:: TEXT=[ <p>This is a test paragraph</p> ]:\n\
        %%CONTENT:: TEXT=[ <p>This is another test paragraph</p> ]:\n\
        %%FOOTER_ADDITIONS:: content={ <!-- something else to comment --> }:',
        'args': gb.DEFAULT_GET_FIRST_COMMAND_ARGS,
        'placement': ct.PCOM_SETTINGS_FOOTER,
        'type': 'post'
    },
    'assertEqual': {
        'out': ['<!-- something else to comment -->'],
        }
    },
]
