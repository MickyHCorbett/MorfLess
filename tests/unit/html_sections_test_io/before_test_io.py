#
import libraries.constants as ct
import libraries.globals as gb

# before data is an array

test_values = [\
{   'remark': 'Test Case 1:polimorf_add_before - After data as array, meta present',
    'inputs': { 'before_data':       ['<div class="before-out"></div>'],
                'meta_present':     True },
    'assertIn': ['div class="before-out','section id="main'],
    'assertNotIn': ['main-outer', 'header-inner', 'with-sidebar'] },

{   'remark': 'Test Case 2:polimorf_add_before - After data as array, NOT meta present',
    'inputs': { 'before_data':       ['<div class="before-out"></div>'],
                'meta_present':     False},
    'assertIn': [ct.PCOM_NO_ENTRY],
    'assertNotIn': ['div class="before-out', 'section id="main']  },

{   'remark': 'Test Case 3:polimorf_add_before - After data not as array, meta present',
    'inputs': { 'before_data':       'ANO',
                'meta_present':     True },
    'assertIn': [\
                'A\n',
                'N\n',
                'O',
                'section id="main'],
    'assertNotIn': ['ANO','main-outer','main-inner'] }
]
