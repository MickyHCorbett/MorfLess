#
import libraries.constants as ct
import libraries.globals as gb

# before data is an array

test_values = [\
{   'remark': 'Test Case 1:polimorf_add_before - Before data as array, meta present',
    'inputs': { 'before_data':       ['<div class="before-out"></div>'],
                'sidebar_data': [ct.PCOM_NO_ENTRY],
                'meta_present':     True },
    'assertIn': ['div class="before-out','section id="main'],
    'assertNotIn': ['main-outer', 'header-inner', 'with-sidebar'] },

{   'remark': 'Test Case 2:polimorf_add_before - Before data as array, NOT meta present, sidebar data',
    'inputs': { 'before_data':       ['<div class="before-out"></div>'],
                'sidebar_data': ['<div class="something"></div>'],
                'meta_present':     False},
    'assertIn': [ct.PCOM_NO_ENTRY],
    'assertNotIn': ['div class="before-out', 'section id="main']  },

{   'remark': 'Test Case 3:polimorf_add_before - Before data not as array, meta present',
    'inputs': { 'before_data':       'ANO',
                'sidebar_data': [ct.PCOM_NO_ENTRY],
                'meta_present':     True },
    'assertIn': [\
                'A\n',
                'N\n',
                'O',
                'section id="main'],
    'assertNotIn': ['ANO','main-outer','main-inner'] },

{   'remark': 'Test Case 4:polimorf_add_before - Before data as array, meta present,sidebar data',
    'inputs': { 'before_data':       ['<div class="before-out"></div>'],
                'sidebar_data': ['<div class="something"></div>'],
                'meta_present':     True },
    'assertIn': ['div class="before-out','section id="main'],
    'assertNotIn': ['main-outer', 'header-inner', 'with-sidebar'] },

{   'remark': 'Test Case 5:polimorf_add_before - Before data as array with SIDEBAR SECTION sub, meta present, sidebar data',
    'inputs': { 'before_data':       ['<div class="before-out">'+ ct.PCOM_SECTION_SIDEBAR_TAB + '</div>'],
                'sidebar_data': ['<div class="something"></div>'],
                'meta_present':     True},
    'assertIn': ['<div class="before-out">' + ct.T2 + '</div>'],
    'assertNotIn': ['main-outer', 'header-inner', 'with-sidebar'] },

{   'remark': 'Test Case 6:polimorf_add_before - Before data as array with SIDEBAR SECTION sub, meta present, NO sidebar data',
    'inputs': { 'before_data':       ['<div class="before-out">'+ ct.PCOM_SECTION_SIDEBAR_TAB + '</div>'],
                'sidebar_data': [ct.PCOM_NO_ENTRY],
                'meta_present':     True},
    'assertIn': ['<div class="before-out"></div>'],
    'assertNotIn': ['main-outer', 'header-inner', 'with-sidebar'] }
]
