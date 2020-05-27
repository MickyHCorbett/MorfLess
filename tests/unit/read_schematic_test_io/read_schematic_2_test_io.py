#
import libraries.constants as ct
import libraries.globals as gb

#
test_values = [\
{   'remark': 'Test Case 1:pcom_determine_placement - Settings HEADER PLACEMENT',
    'inputs': { 'placement': ct.PCOM_SETTINGS_HEADER },
    'assertIn': [ct.PCOM_HEADER_PLACEMENT],
    'assertNotIn': [ct.PCOM_MAIN_PLACEMENT, ct.PCOM_SIDEBAR_PLACEMENT, ct.PCOM_FOOTER_PLACEMENT]
    },

{   'remark': 'Test Case 2:pcom_determine_placement - Settings BEFORE PLACEMENT',
    'inputs': { 'placement': ct.PCOM_SETTINGS_BEFORE },
    'assertIn': [ct.PCOM_MAIN_PLACEMENT],
    'assertNotIn': [ct.PCOM_HEADER_PLACEMENT, ct.PCOM_SIDEBAR_PLACEMENT, ct.PCOM_FOOTER_PLACEMENT]
    },

{   'remark': 'Test Case 3:pcom_determine_placement - Settings MAIN PLACEMENT',
    'inputs': { 'placement': ct.PCOM_SETTINGS_MAIN },
    'assertIn': [ct.PCOM_MAIN_PLACEMENT],
    'assertNotIn': [ct.PCOM_HEADER_PLACEMENT, ct.PCOM_SIDEBAR_PLACEMENT, ct.PCOM_FOOTER_PLACEMENT]
    },

{   'remark': 'Test Case 4:pcom_determine_placement - Settings AFTER PLACEMENT',
    'inputs': { 'placement': ct.PCOM_SETTINGS_AFTER },
    'assertIn': [ct.PCOM_MAIN_PLACEMENT],
    'assertNotIn': [ct.PCOM_HEADER_PLACEMENT, ct.PCOM_SIDEBAR_PLACEMENT, ct.PCOM_FOOTER_PLACEMENT]
    },

{   'remark': 'Test Case 5:pcom_determine_placement - Settings SIDEBAR PLACEMENT',
    'inputs': { 'placement': ct.PCOM_SETTINGS_SIDEBAR },
    'assertIn': [ct.PCOM_SIDEBAR_PLACEMENT],
    'assertNotIn': [ct.PCOM_MAIN_PLACEMENT, ct.PCOM_HEADER_PLACEMENT, ct.PCOM_FOOTER_PLACEMENT]
    },

{   'remark': 'Test Case 6:pcom_determine_placement - Settings FOOTER PLACEMENT',
    'inputs': { 'placement': ct.PCOM_SETTINGS_FOOTER},
    'assertIn': [ct.PCOM_FOOTER_PLACEMENT],
    'assertNotIn': [ct.PCOM_MAIN_PLACEMENT, ct.PCOM_SIDEBAR_PLACEMENT, ct.PCOM_HEADER_PLACEMENT]
    }
]
