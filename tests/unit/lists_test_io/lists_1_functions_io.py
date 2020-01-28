#
import libraries.constants as ct
import libraries.globals as gb
import libraries.schematics as sch

from collections import OrderedDict
#

test_values_1 = [\
{   'remark': 'Test Case 1:pcom_update_authors_from_settings - new author from settings - authors array empty',
    'inputs': {\
            'authors': {\
                "no_of_author_pages": 1,
                "authors": []
            },
            'settings_authors': [\
            { "name":           "Bill",
              "shortname":      "",
              "thumbnail":      "",
              "description":    "" }
            ],
            "ppp": 3
    },
    'assertEqual': { 'no_of_author_pages': 1,
                    'authors': [ OrderedDict([('name', 'Bill'), ('shortname', 'Bill'),
                    ('thumbnail', sch.PM_DEFAULT_THUMBNAIL_IMAGE_LINK), ('description', '') ])]
                    },
    'assertNotEqual': []
    },

{   'remark': 'Test Case 2:pcom_update_authors_from_settings - new author from settings - authors array not empty\
- posts per page = 1, no_author_pages = 2',
    'inputs': {\
            'authors': {\
                "no_of_author_pages": 1,
                "authors": [\
                    {
                        "name": "anon",
                        "shortname": "anon",
                        "thumbnail": "/images/Polimorf-shapes-background.jpg",
                        "description": ""
                    }
                ]
            },
            'settings_authors': [\
            { "name":           "Bill",
              "shortname":      "",
              "thumbnail":      "",
              "description":    "" }
            ],
            "ppp": 1
    },
    'assertEqual': { 'no_of_author_pages': 2,
                    'authors': [\
                    OrderedDict([('name', 'anon'), ('shortname', 'anon'),
                   ('thumbnail', '/images/Polimorf-shapes-background.jpg'), ('description', '') ]),
                    OrderedDict([('name', 'Bill'), ('shortname', 'Bill'),
                    ('thumbnail', sch.PM_DEFAULT_THUMBNAIL_IMAGE_LINK), ('description', '') ])
                    ]
                    },
    'assertNotEqual': []
    },



]
