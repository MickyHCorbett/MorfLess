#
import libraries.constants as ct
import libraries.globals as gb

from collections import OrderedDict
#

test_values_1 = [\
{   'remark': 'Test Case 1:pcom_process_json - JSON compliant data',
    'input': """
                {
                    "variable1": [
                        "variable2"
                    ],
                    "variable3": {
                        "variable4" : "this",
                        "variable5" : "that"
                    }
                }
            """,
    'assertEqual': (OrderedDict([('variable1', ['variable2']), ('variable3', OrderedDict([('variable4', 'this'), ('variable5', 'that')]))]), ''),
    'assertNotEqual': { 'variable1': ['variable2'],
    'variable3': { 'variable4': 'this', 'variable5': 'that'} }
    },


{   'remark': 'Test Case 2:pcom_process_json - non-compliant data',
    'input': """
                {
                    "variable1" [
                        'variable2'
                    ]
                    "variable3": {
                        "variable4" : "this"
                        "variable5" : "that"
                    }
                }

                """,
    'assertEqual': ('NONE', 'JSON_FILE load error'),
    'assertNotEqual': (OrderedDict([('variable1', ['variable2']), ('variable3', OrderedDict([('variable4', 'this'), ('variable5', 'that')]))]), '')
    },

{   'remark': 'Test Case 3:pcom_process_json - no data',
    'input': '',
    'assertEqual': ('NONE', 'JSON_FILE load error'),
    'assertNotEqual': (OrderedDict([('variable1', ['variable2']), ('variable3', OrderedDict([('variable4', 'this'), ('variable5', 'that')]))]), '')
    },

{   'remark': 'Test Case 4:pcom_process_json - data = NONE',
    'input': ct.PCOM_NO_ENTRY,
    'assertEqual': ('NONE', ''),
    'assertNotEqual': (OrderedDict([('variable1', ['variable2']), ('variable3', OrderedDict([('variable4', 'this'), ('variable5', 'that')]))]), '')
    },

{   'remark': 'Test Case 5:pcom_process_json - JSON compliant data',
    'input': """
                {
                    "variable1": [
                        "variable2"
                    ],
                    "variable3": "that",
                    "variable4": "that again",
                    "variable5": "something"
                }
            """,
    'assertEqual': (OrderedDict([('variable1', ['variable2']), ('variable3', 'that'),('variable4', 'that again'),('variable5', 'something') ]),''),
    'assertNotEqual': { 'variable1': ['variable2'],
    'variable3': { 'variable4': 'this', 'variable5': 'that'} }
    }
]
