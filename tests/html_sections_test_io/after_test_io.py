#
import libraries.constants as ct
import libraries.globals as gb

# after data is an array

test_values = [\
{   'remark': 'Test Case 1:polimorf_add_after - After data as array, meta present, wrap FALSE',
    'inputs': { 'after_data':       ['<div class="after-out"></div>'],
                'meta_present':     True,
                'wrap':             False },
    'assertIn': ['div class="after-out'],
    'assertNotIn': ['main-outer', 'header-inner', 'with-sidebar','section id="main'] },

{   'remark': 'Test Case 2:polimorf_add_after - After data as array, NOT meta present, wrap FALSE',
    'inputs': { 'after_data':       ['<div class="after-out"></div>'],
                'meta_present':     False,
                'wrap':             False },
    'assertIn': [ct.PCOM_NO_ENTRY],
    'assertNotIn': ['div class="after-out', 'section id="main']  },

{   'remark': 'Test Case 3:polimorf_add_after - After data not as array, meta present',
    'inputs': { 'after_data':       'ANO',
                'meta_present':     True,
                'wrap':             False },
    'assertIn': [\
                'A\n',
                'N\n',
                'O\n',],
    'assertNotIn': ['ANO','main-outer','main-inner'] },

{   'remark': 'Test Case 4:polimorf_add_after - After data as array, meta present, wrap TRUE',
    'inputs': { 'after_data':       ['<div class="after-out"></div>'],
                'meta_present':     True,
                'wrap':             True },
    'assertIn': ['div class="after-out','main-wrap', 'end', 'section id="main'],
    'assertNotIn': ['ANO','main-outer'] }
]
