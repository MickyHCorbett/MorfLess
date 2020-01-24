# test values of header - polimorf_add_header and polimorf_head_and_title
import libraries.constants as ct
import libraries.globals as gb

# header data is an array

test_values = [\
{   'remark': 'Test Case 1:polimorf_add_header - Header data as array, meta present',
    'inputs': { 'header_data':    ['<div class="header-out"></div>'],
                'meta_present': True },
    'assertIn': ['div class="header-out','header-fixed','header-outer','header-inner'],
    'assertNotIn': ['main-outer', 'footer-inner', 'with-sidebar'] },

{   'remark': 'Test Case 2:polimorf_add_header - Header data as array, NOT meta present',
    'inputs': { 'header_data':    ['<div class="header-out"></div>'],
                'meta_present': False },
    'assertIn': [ct.PCOM_NO_ENTRY],
    'assertNotIn': ['div class="header-out'] },

{   'remark': 'Test Case 3:polimorf_add_header - Header data not as array, meta present',
    'inputs': { 'header_data':  'ANO',
                'meta_present': True },
    'assertIn': [\
                'A\n',
                'N\n',
                'O\n',
                'header-fixed'],
    'assertNotIn': ['ANO'] }

]
