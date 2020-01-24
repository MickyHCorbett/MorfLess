#
import libraries.constants as ct
import libraries.globals as gb

#
test_values = [\
{   'remark': 'Test Case 1:pcom_get_schematic_tags - only META, HEADER, MAIN and FOOTER tags - no content',
    'inputs': { 'format':"""
        ///META:

        ///HEADER:

        ///MAIN:

        ///FOOTER:

        ///"""},
    'assertIn': {\
            'meta': [' '],
            'header': [' '],
            'before': [ct.PCOM_NO_ENTRY],
            'main': [' '],
            'after': [ct.PCOM_NO_ENTRY] ,
            'sidebar': [ct.PCOM_NO_ENTRY],
            'footer': [' '] },
    'assertNotIn': {\
            'meta': [ct.PCOM_NO_ENTRY],
            'header': [ct.PCOM_NO_ENTRY],
            'before': [' '],
            'main': [ct.PCOM_NO_ENTRY],
            'after': [' '],
            'sidebar': [' '],
            'footer': [ct.PCOM_NO_ENTRY]},
    'assertEqual': {\
            'sidebar_found': False,
            'before_found': False,
            'after_found': False }\
    },

{   'remark': 'Test Case 2:pcom_get_schematic_tags - only META, HEADER, MAIN  tags - no content - all NONE outputs',
    'inputs': { 'format':"""
        ///META:

        ///HEADER:

        ///MAIN:

        ///"""},
    'assertIn': {\
            'meta': [ct.PCOM_NO_ENTRY],
            'header': [ct.PCOM_NO_ENTRY],
            'before': [ct.PCOM_NO_ENTRY],
            'main': [ct.PCOM_NO_ENTRY],
            'after': [ct.PCOM_NO_ENTRY] ,
            'sidebar': [ct.PCOM_NO_ENTRY],
            'footer': [ct.PCOM_NO_ENTRY] },
    'assertNotIn': {\
            'meta': [' '],
            'header': [' '],
            'before': [' '],
            'main': [' '],
            'after': [' '],
            'sidebar': [' '],
            'footer': [' ']},
    'assertEqual': {\
            'sidebar_found': False,
            'before_found': False,
            'after_found': False }\
    },

{   'remark': 'Test Case 3:pcom_get_schematic_tags - only META, HEADER, FOOTER  tags - no content - all NONE outputs',
    'inputs': { 'format':"""
        ///META:

        ///HEADER:

        ///FOOTER:

        ///"""},
    'assertIn': {\
            'meta': [ct.PCOM_NO_ENTRY],
            'header': [ct.PCOM_NO_ENTRY],
            'before': [ct.PCOM_NO_ENTRY],
            'main': [ct.PCOM_NO_ENTRY],
            'after': [ct.PCOM_NO_ENTRY] ,
            'sidebar': [ct.PCOM_NO_ENTRY],
            'footer': [ct.PCOM_NO_ENTRY] },
    'assertNotIn': {\
            'meta': [' '],
            'header': [' '],
            'before': [' '],
            'main': [' '],
            'after': [' '],
            'sidebar': [' '],
            'footer': [' ']},
    'assertEqual': {\
            'sidebar_found': False,
            'before_found': False,
            'after_found': False }\
    },

{   'remark': 'Test Case 4:pcom_get_schematic_tags - only META, MAIN, FOOTER  tags - no content - all NONE outputs',
    'inputs': { 'format':"""
        ///META:

        ///MAIN:

        ///FOOTER:

        ///"""},
    'assertIn': {\
            'meta': [ct.PCOM_NO_ENTRY],
            'header': [ct.PCOM_NO_ENTRY],
            'before': [ct.PCOM_NO_ENTRY],
            'main': [ct.PCOM_NO_ENTRY],
            'after': [ct.PCOM_NO_ENTRY] ,
            'sidebar': [ct.PCOM_NO_ENTRY],
            'footer': [ct.PCOM_NO_ENTRY] },
    'assertNotIn': {\
            'meta': [' '],
            'header': [' '],
            'before': [' '],
            'main': [' '],
            'after': [' '],
            'sidebar': [' '],
            'footer': [' ']},
    'assertEqual': {\
            'sidebar_found': False,
            'before_found': False,
            'after_found': False }\
    },

{   'remark': 'Test Case 5:pcom_get_schematic_tags - only HEADER, MAIN, FOOTER  tags - no content - all NONE outputs',
    'inputs': { 'format':"""
        ///HEADER:

        ///MAIN:

        ///FOOTER:

        ///"""},
    'assertIn': {\
            'meta': [ct.PCOM_NO_ENTRY],
            'header': [ct.PCOM_NO_ENTRY],
            'before': [ct.PCOM_NO_ENTRY],
            'main': [ct.PCOM_NO_ENTRY],
            'after': [ct.PCOM_NO_ENTRY] ,
            'sidebar': [ct.PCOM_NO_ENTRY],
            'footer': [ct.PCOM_NO_ENTRY] },
    'assertNotIn': {\
            'meta': [' '],
            'header': [' '],
            'before': [' '],
            'main': [' '],
            'after': [' '],
            'sidebar': [' '],
            'footer': [' ']},
    'assertEqual': {\
            'sidebar_found': False,
            'before_found': False,
            'after_found': False }\
    },

{   'remark': 'Test Case 6:pcom_get_schematic_tags - all tags with content in correct order',
    'inputs': { 'format':"""
        ///META:
        Meta content
        ///HEADER:
        Header content
        ///BEFORE:
        Before content
        ///MAIN:
        Main content
        ///AFTER:
        After content
        ///SIDEBAR:
        Sidebar content
        ///FOOTER:
        Footer content
        ///

        """},
    'assertIn': {\
            'meta': ['Meta content'],
            'header': ['Header content'],
            'before': ['Before content'],
            'main': ['Main content'],
            'after': ['After content'] ,
            'sidebar': ['Sidebar content'],
            'footer': ['Footer content'] },
    'assertNotIn': {\
            'meta': [ct.PCOM_NO_ENTRY, 'Main content'],
            'header': [ct.PCOM_NO_ENTRY, 'After content'],
            'before': [ct.PCOM_NO_ENTRY, 'Header content'],
            'main': [ct.PCOM_NO_ENTRY, 'Footer content'],
            'after': [ct.PCOM_NO_ENTRY, 'Main content'] ,
            'sidebar': [ct.PCOM_NO_ENTRY, 'Header content'],
            'footer': [ct.PCOM_NO_ENTRY, 'Main content'] },
    'assertEqual': {\
            'sidebar_found': True,
            'before_found': True,
            'after_found': True }\
    },

{   'remark': 'Test Case 7:pcom_get_schematic_tags - all tags with content, BEFORE before HEADER, SIDEBAR before AFTER\
    Sidebar and After found, Before NOT',
    'inputs': { 'format':"""
        ///META:
        Meta content

        ///BEFORE:
        Before content

        ///HEADER:
        Header content

        ///MAIN:
        Main content

        ///SIDEBAR:
        Sidebar content

        ///AFTER:
        After content

        ///FOOTER:
        Footer content
        ///

        """},
    'assertIn': {\
            'meta': ['Meta content'],
            'header': ['Header content'],
            'before': [ct.PCOM_NO_ENTRY],
            'main': ['Main content'],
            'after': ['After content'] ,
            'sidebar': ['Sidebar content'],
            'footer': ['Footer content'] },
    'assertNotIn': {\
            'meta': [ct.PCOM_NO_ENTRY, 'Main content'],
            'header': [ct.PCOM_NO_ENTRY, 'After content'],
            'before': ['Before content'],
            'main': [ct.PCOM_NO_ENTRY, 'Footer content'],
            'after': [ct.PCOM_NO_ENTRY, 'Main content'] ,
            'sidebar': [ct.PCOM_NO_ENTRY, 'Header content'],
            'footer': [ct.PCOM_NO_ENTRY, 'Main content'] },
    'assertEqual': {\
            'sidebar_found': True,
            'before_found': False,
            'after_found': True }\
    },

{   'remark': 'Test Case 6:pcom_get_schematic_tags - all tags with content, SIDEBAR and AFTER after FOOTER\
    Sidebar and After not found',
    'inputs': { 'format':"""
        ///META:
        Meta content
        ///HEADER:
        Header content
        ///BEFORE:
        Before content
        ///MAIN:
        Main content

        ///FOOTER:
        Footer content

        ///AFTER:
        After content
        ///SIDEBAR:
        Sidebar content

        ///

        """},
    'assertIn': {\
            'meta': ['Meta content'],
            'header': ['Header content'],
            'before': ['Before content'],
            'main': ['Main content'],
            'after': [ct.PCOM_NO_ENTRY] ,
            'sidebar': [ct.PCOM_NO_ENTRY],
            'footer': ['Footer content'] },
    'assertNotIn': {\
            'meta': [ct.PCOM_NO_ENTRY, 'Main content'],
            'header': [ct.PCOM_NO_ENTRY, 'After content'],
            'before': [ct.PCOM_NO_ENTRY, 'Header content'],
            'main': [ct.PCOM_NO_ENTRY, 'Footer content'],
            'after': ['After content'] ,
            'sidebar': ['Sidebar content'],
            'footer': [ct.PCOM_NO_ENTRY, 'Main content'] },
    'assertEqual': {\
            'sidebar_found': False,
            'before_found': True,
            'after_found': False }\
    },

{   'remark': 'Test Case 7:pcom_get_schematic_tags - all tags with content, BEFORE before HEADER, SIDEBAR before AFTER\
    Sidebar and After found, Before NOT',
    'inputs': { 'format':"""
        ///META:
        Meta content

        ///BEFORE:
        Before content

        ///HEADER:
        Header content

        ///MAIN:
        Main content

        ///SIDEBAR:
        Sidebar content

        ///AFTER:
        After content

        ///FOOTER:
        Footer content
        ///

        """},
    'assertIn': {\
            'meta': ['Meta content'],
            'header': ['Header content'],
            'before': [ct.PCOM_NO_ENTRY],
            'main': ['Main content'],
            'after': ['After content'] ,
            'sidebar': ['Sidebar content'],
            'footer': ['Footer content'] },
    'assertNotIn': {\
            'meta': [ct.PCOM_NO_ENTRY, 'Main content'],
            'header': [ct.PCOM_NO_ENTRY, 'After content'],
            'before': ['Before content'],
            'main': [ct.PCOM_NO_ENTRY, 'Footer content'],
            'after': [ct.PCOM_NO_ENTRY, 'Main content'] ,
            'sidebar': [ct.PCOM_NO_ENTRY, 'Header content'],
            'footer': [ct.PCOM_NO_ENTRY, 'Main content'] },
    'assertEqual': {\
            'sidebar_found': True,
            'before_found': False,
            'after_found': True }\
    },

{   'remark': 'Test Case 8:pcom_get_schematic_tags - all tags with content, MAIN before HEADER - no outputs',
    'inputs': { 'format':"""
        ///META:
        Meta content
        ///MAIN:
        Main content

        ///HEADER:
        Header content
        ///BEFORE:
        Before content

        ///AFTER:
        After content
        ///SIDEBAR:
        Sidebar content
        ///FOOTER:
        Footer content

        ///

        """},
    'assertIn': {\
            'meta': [ct.PCOM_NO_ENTRY],
            'header': [ct.PCOM_NO_ENTRY],
            'before': [ct.PCOM_NO_ENTRY],
            'main': [ct.PCOM_NO_ENTRY],
            'after': [ct.PCOM_NO_ENTRY] ,
            'sidebar': [ct.PCOM_NO_ENTRY],
            'footer': [ct.PCOM_NO_ENTRY] },
    'assertNotIn': {\
            'meta': ['Meta content'],
            'header': ['Header content'],
            'before': ['Before content'],
            'main': ['Main content'],
            'after': ['After content'] ,
            'sidebar': ['Sidebar content'],
            'footer': ['Footer content'] },
    'assertEqual': {\
            'sidebar_found': False,
            'before_found': False,
            'after_found': False }\
    },


{   'remark': 'Test Case 9:pcom_get_schematic_tags - all tags with content, FOOTER before MAIN - no outputs',
    'inputs': { 'format':"""
        ///META:
        Meta content

        ///HEADER:
        Header content
        ///FOOTER:
        Footer content

        ///BEFORE:
        Before content
        ///MAIN:
        Main content
        ///AFTER:
        After content
        ///SIDEBAR:
        Sidebar content

        ///

        """},
    'assertIn': {\
            'meta': [ct.PCOM_NO_ENTRY],
            'header': [ct.PCOM_NO_ENTRY],
            'before': [ct.PCOM_NO_ENTRY],
            'main': [ct.PCOM_NO_ENTRY],
            'after': [ct.PCOM_NO_ENTRY] ,
            'sidebar': [ct.PCOM_NO_ENTRY],
            'footer': [ct.PCOM_NO_ENTRY] },
    'assertNotIn': {\
            'meta': ['Meta content'],
            'header': ['Header content'],
            'before': ['Before content'],
            'main': ['Main content'],
            'after': ['After content'] ,
            'sidebar': ['Sidebar content'],
            'footer': ['Footer content'] },
    'assertEqual': {\
            'sidebar_found': False,
            'before_found': False,
            'after_found': False }\
    },

{   'remark': 'Test Case 10:pcom_get_schematic_tags - all tags with content, META after HEADER - no outputs',
    'inputs': { 'format':"""
        
        ///HEADER:
        Header content

        ///META:
        Meta content


        ///BEFORE:
        Before content
        ///MAIN:
        Main content
        ///AFTER:
        After content
        ///SIDEBAR:
        Sidebar content

        ///FOOTER:
        Footer content

        ///

        """},
    'assertIn': {\
            'meta': [ct.PCOM_NO_ENTRY],
            'header': [ct.PCOM_NO_ENTRY],
            'before': [ct.PCOM_NO_ENTRY],
            'main': [ct.PCOM_NO_ENTRY],
            'after': [ct.PCOM_NO_ENTRY] ,
            'sidebar': [ct.PCOM_NO_ENTRY],
            'footer': [ct.PCOM_NO_ENTRY] },
    'assertNotIn': {\
            'meta': ['Meta content'],
            'header': ['Header content'],
            'before': ['Before content'],
            'main': ['Main content'],
            'after': ['After content'] ,
            'sidebar': ['Sidebar content'],
            'footer': ['Footer content'] },
    'assertEqual': {\
            'sidebar_found': False,
            'before_found': False,
            'after_found': False }\
    }
]
