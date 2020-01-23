#
import libraries.constants as ct
import libraries.globals as gb

# footer data is an array

test_values = [\
{   'remark': 'Test Case 1:polimorf_add_footer - Footer data as array, meta present',
    'inputs': { 'footer_data':    ['<div class="footer-out"></div>'],
                'meta_present': True },
    'assertIn': ['div class="footer-out','footer-outer','footer-inner'],
    'assertNotIn': ['main-outer', 'header-inner', 'with-sidebar'] },

{   'remark': 'Test Case 2:polimorf_add_footer - Footer data as array, NOT meta present',
    'inputs': { 'footer_data':    ['<div class="footer-out"></div>'],
                'meta_present': False },
    'assertIn': [ct.PCOM_NO_ENTRY],
    'assertNotIn': ['div class="footer-out'] },

{   'remark': 'Test Case 3:polimorf_add_footer - Footer data not as array, meta present',
    'inputs': { 'footer_data':  'ANO',
                'meta_present': True },
    'assertIn': [\
                'A\n',
                'N\n',
                'O\n',
                'footer-outer'],
    'assertNotIn': ['ANO'] }

]
