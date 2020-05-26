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
            { "name":           "Bill O'Reilly",
              "shortname":      "Bill",
              "thumbnail":      "",
              "description":    "Something here" }
            ],
            "ppp": 3,
            "default_thumb_link": sch.PM_DEFAULT_THUMBNAIL_IMAGE_LINK,
            "default_author": gb.DEFAULT_AUTHOR
    },
    'assertEqual': { 'no_of_author_pages': 1,
                    'authors': [
                    OrderedDict([('name', 'anon'), ('shortname', 'anon'),
                   ('thumbnail', '/images/Polimorf-shapes-background.jpg'), ('description', '') ]),
                   OrderedDict([('name', "Bill O'Reilly"), ('shortname', 'Bill'),
                    ('thumbnail', sch.PM_DEFAULT_THUMBNAIL_IMAGE_LINK), ('description', 'Something here') ])]
                    },
    'assertNotEqual': []
    },

{   'remark': 'Test Case 2:pcom_update_authors_from_settings - new author from settings with no shortname - authors array not empty\
- posts per page = 1, no_author_pages = 1',
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
              "thumbnail":      "",
              "description":    "" }
            ],
            "ppp": 1,
            "default_thumb_link": sch.PM_DEFAULT_THUMBNAIL_IMAGE_LINK,
            "default_author": gb.DEFAULT_AUTHOR
    },
    'assertEqual': { 'no_of_author_pages': 1,
                    'authors': [\
                    OrderedDict([('name', 'anon'), ('shortname', 'anon'),
                   ('thumbnail', '/images/Polimorf-shapes-background.jpg'), ('description', '') ])
                    ]
                    },
    'assertNotEqual': []
    },

{   'remark': 'Test Case 3:pcom_update_authors_from_settings - new author from settings with no name - authors array not empty\
- posts per page = 1, no_author_pages = 1',
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
            { "shortname":           "Bill",
              "thumbnail":      "",
              "description":    "" }
            ],
            "ppp": 1,
            "default_thumb_link": sch.PM_DEFAULT_THUMBNAIL_IMAGE_LINK,
            "default_author": gb.DEFAULT_AUTHOR
    },
    'assertEqual': { 'no_of_author_pages': 1,
                    'authors': [\
                    OrderedDict([('name', 'anon'), ('shortname', 'anon'),
                   ('thumbnail', '/images/Polimorf-shapes-background.jpg'), ('description', '') ])
                    ]
                    },
    'assertNotEqual': []
    },

{   'remark': 'Test Case 4:pcom_update_authors_from_settings - new author from settings - characters in description',
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
              "shortname":      "Bill Maguire",
              "thumbnail":      "/my-link.png",
              "description":    "Something %here?&" }
            ],
            "ppp": 1,
            "default_thumb_link": sch.PM_DEFAULT_THUMBNAIL_IMAGE_LINK,
            "default_author": gb.DEFAULT_AUTHOR
    },
    'assertEqual': { 'no_of_author_pages': 2,
                    'authors': [\
                    OrderedDict([('name', 'anon'), ('shortname', 'anon'),
                   ('thumbnail', '/images/Polimorf-shapes-background.jpg'), ('description', '') ]),
                   OrderedDict([('name', "Bill"), ('shortname', 'Bill Maguire'),
                   ('thumbnail', '/my-link.png'), ('description', 'Something %here?&') ])
                    ]
                    },
    'assertNotEqual': []
    }

]

test_values_2 = [\
{   'remark': 'Test Case 1:pcom_update_categories_from_settings - new category from settings - categories array empty',
    'inputs': {\
            'categories': {\
                "no_of_category_pages": 1,
                "categories": []
            },
            'settings_categories': [\
            { "name":           "Bill O'Reilly",
              "thumbnail":      "",
              "description":    "Something here" }
            ],
            "ppp": 3,
            "default_thumb_link": sch.PM_DEFAULT_THUMBNAIL_IMAGE_LINK
    },
    'assertEqual': { 'no_of_category_pages': 1,
                    'categories': [
                   OrderedDict([('name', "Bill O'Reilly"),
                    ('thumbnail', sch.PM_DEFAULT_THUMBNAIL_IMAGE_LINK), ('description', 'Something here') ])]
                    },
    'assertNotEqual': []
    },

{   'remark': 'Test Case 2:pcom_update_categories_from_settings - new category from settings - name only - categories array not empty\
- posts per page = 1, no_of_category_pages = 1',
    'inputs': {\
            'categories': {\
                "no_of_category_pages": 1,
                "categories": [\
                    {
                        "name": "anon",
                        "thumbnail": "/images/Polimorf-shapes-background.jpg",
                        "description": ""
                    }
                ]
            },
            'settings_categories': [\
            { "name":           "Bill",
              "thumbnail":      "",
              "description":    "" }
            ],
            "ppp": 1,
            "default_thumb_link": sch.PM_DEFAULT_THUMBNAIL_IMAGE_LINK
    },
    'assertEqual': { 'no_of_category_pages': 2,
                    'categories': [\
                    {'name': 'anon', 'thumbnail': '/images/Polimorf-shapes-background.jpg', 'description': ''},
                    OrderedDict([('name', 'Bill'),
                   ('thumbnail', '/images/Polimorf-shapes-background.jpg'), ('description', '') ])
                    ]
                    },
    'assertNotEqual': []
    },

{   'remark': 'Test Case 3:pcom_update_categories_from_settings - new category from settings with no name - categories array not empty\
- posts per page = 1, no_of_category_pages = 1',
    'inputs': {\
            'categories': {\
                "no_of_category_pages": 1,
                "categories": [\
                    {
                        "name": "anon",
                        "thumbnail": "/images/Polimorf-shapes-background.jpg",
                        "description": ""
                    }
                ]
            },
            'settings_categories': [\
            { "shortname":           "Bill",
              "thumbnail":      "",
              "description":    "" }
            ],
            "ppp": 1,
            "default_thumb_link": sch.PM_DEFAULT_THUMBNAIL_IMAGE_LINK,
            "default_author": gb.DEFAULT_AUTHOR
    },
    'assertEqual': { 'no_of_category_pages': 1,
                    'categories': [\
                    OrderedDict([('name', 'anon'),
                   ('thumbnail', '/images/Polimorf-shapes-background.jpg'), ('description', '') ])
                    ]
                    },
    'assertNotEqual': []
    },

{   'remark': 'Test Case 4:pcom_update_categories_from_settings - new category from settings - characters in description',
    'inputs': {\
            'categories': {\
                "no_of_category_pages": 1,
                "categories": [\
                    {
                        "name": "anon",
                        "thumbnail": "/images/Polimorf-shapes-background.jpg",
                        "description": ""
                    }
                ]
            },
            'settings_categories': [\
            { "name":           "Bill",
              "thumbnail":      "/my-link.png",
              "description":    "Something %here?&" }
            ],
            "ppp": 1,
            "default_thumb_link": sch.PM_DEFAULT_THUMBNAIL_IMAGE_LINK
    },
    'assertEqual': { 'no_of_category_pages': 2,
                    'categories': [\
                    {'name': 'anon', 'thumbnail': '/images/Polimorf-shapes-background.jpg', 'description': ''},
                   OrderedDict([('name', "Bill"),
                   ('thumbnail', '/my-link.png'), ('description', 'Something %here?&') ])
                    ]
                    },
    'assertNotEqual': []
    }

]


test_values_3 = [\
{   'remark': 'Test Case 1:test_pcom_update_authors_from_postlist_data  - authors array empty',
    'inputs': {\
            'authors': {\
                "no_of_author_pages": 1,
                "authors": []
            },
            'author_list': [],
            "ppp": 3,
            "default_thumb_link": sch.PM_DEFAULT_THUMBNAIL_IMAGE_LINK
    },
    'assertEqual': { 'no_of_author_pages': 1,
                    'authors': []
                    },
    'assertNotEqual': []
    },
{   'remark': 'Test Case 2:test_pcom_update_authors_from_postlist_data - authors but author list empty',
    'inputs': {\
            'authors': {\
                "no_of_author_pages": 1,
                "authors": [
                    {
                        "name": "anon",
                        "shortname": "anon",
                        "thumbnail": "/images/Polimorf-shapes-background.jpg",
                        "description": ""
                    }
                ]
            },
            'author_list': [],
            "ppp": 3,
            "default_thumb_link": sch.PM_DEFAULT_THUMBNAIL_IMAGE_LINK
    },
    'assertEqual': { 'no_of_author_pages': 1,
                    'authors': [
                        {
                            "name": "anon",
                            "shortname": "anon",
                            "thumbnail": "/images/Polimorf-shapes-background.jpg",
                            "description": ""
                        }
                    ]
                    },
    'assertNotEqual': []
    },
{   'remark': 'Test Case 3:test_pcom_update_authors_from_postlist_data - authors, author list author (name) already present',
    'inputs': {\
            'authors': {\
                "no_of_author_pages": 1,
                "authors": [
                    {
                        "name": "anon person",
                        "shortname": "anon",
                        "thumbnail": "/images/Polimorf-shapes-background.jpg",
                        "description": ""
                    }
                ]
            },
            'author_list': ['anon person'],
            "ppp": 3,
            "default_thumb_link": sch.PM_DEFAULT_THUMBNAIL_IMAGE_LINK
    },
    'assertEqual': { 'no_of_author_pages': 1,
                    'authors': [
                        {
                            "name": "anon person",
                            "shortname": "anon",
                            "thumbnail": "/images/Polimorf-shapes-background.jpg",
                            "description": ""
                        }
                    ]
                    },
    'assertNotEqual': []
    },
{   'remark': 'Test Case 4:test_pcom_update_authors_from_postlist_data - authors, author list author (shortname) already present',
    'inputs': {\
            'authors': {\
                "no_of_author_pages": 1,
                "authors": [
                    {
                        "name": "anon person",
                        "shortname": "anon",
                        "thumbnail": "/images/Polimorf-shapes-background.jpg",
                        "description": ""
                    }
                ]
            },
            'author_list': ['anon'],
            'type': 'post',
            "ppp": 3,
            "default_thumb_link": sch.PM_DEFAULT_THUMBNAIL_IMAGE_LINK
    },
    'assertEqual': { 'no_of_author_pages': 1,
                    'authors': [
                        {
                            "name": "anon person",
                            "shortname": "anon",
                            "thumbnail": "/images/Polimorf-shapes-background.jpg",
                            "description": ""
                        }
                    ]
                    },
    'assertNotEqual': []
    },
{   'remark': 'Test Case 5:test_pcom_update_authors_from_postlist_data - authors, author list author already present plus one more - ppp = 1',
    'inputs': {\
            'authors': {\
                "no_of_author_pages": 1,
                "authors": [
                    {
                        "name": "anon",
                        "shortname": "anon",
                        "thumbnail": "/images/Polimorf-shapes-background.jpg",
                        "description": ""
                    }
                ]
            },
            'author_list': ['anon','things'],
            "ppp": 1,
            "default_thumb_link": sch.PM_DEFAULT_THUMBNAIL_IMAGE_LINK
    },
    'assertEqual': { 'no_of_author_pages': 2,
                    'authors': [
                        {
                            "name": "anon",
                            "shortname": "anon",
                            "thumbnail": "/images/Polimorf-shapes-background.jpg",
                            "description": ""
                        },
                        OrderedDict([('name', "things"),('shortname', "things"),
                        ('thumbnail', sch.PM_DEFAULT_THUMBNAIL_IMAGE_LINK), ('description', '') ])
                    ]
                    },
    'assertNotEqual': []
    },
{   'remark': 'Test Case 5:test_pcom_update_authors_from_postlist_data - authors, cat list author already present plus one more - ppp = 1 - default thumbnail different',
    'inputs': {\
            'authors': {\
                "no_of_author_pages": 1,
                "authors": [
                    {
                        "name": "anon",
                        "shortname": "anon",
                        "thumbnail": "/images/Polimorf-shapes-background.jpg",
                        "description": ""
                    }
                ]
            },
            'author_list': ['anon','things'],
            "ppp": 1,
            "default_thumb_link": 'this/link.png'
    },
    'assertEqual': { 'no_of_author_pages': 2,
                    'authors': [
                        {
                            "name": "anon",
                            "shortname": "anon",
                            "thumbnail": "/images/Polimorf-shapes-background.jpg",
                            "description": ""
                        },
                        OrderedDict([('name', "things"),('shortname', "things"),
                        ('thumbnail', 'this/link.png'), ('description', '') ])
                    ]
                    },
    'assertNotEqual': []
    },
]

test_values_4 = [\
{   'remark': 'Test Case 1:test_pcom_update_categories_from_postlist_data  - categories array empty',
    'inputs': {\
            'categories': {\
                "no_of_category_pages": 1,
                "categories": []
            },
            'cat_list': [],
            'type': 'post',
            "ppp": 3,
            "default_thumb_link": sch.PM_DEFAULT_THUMBNAIL_IMAGE_LINK
    },
    'assertEqual': { 'no_of_category_pages': 1,
                    'categories': []
                    },
    'assertNotEqual': []
    },
{   'remark': 'Test Case 2:test_pcom_update_categories_from_postlist_data - categories but cat list empty',
    'inputs': {\
            'categories': {\
                "no_of_category_pages": 1,
                "categories": [
                    {
                        "name": "anon",
                        "thumbnail": "/images/Polimorf-shapes-background.jpg",
                        "description": ""
                    }
                ]
            },
            'cat_list': [],
            'type': 'post',
            "ppp": 3,
            "default_thumb_link": sch.PM_DEFAULT_THUMBNAIL_IMAGE_LINK
    },
    'assertEqual': { 'no_of_category_pages': 1,
                    'categories': [
                        {
                            "name": "anon",
                            "thumbnail": "/images/Polimorf-shapes-background.jpg",
                            "description": ""
                        }
                    ]
                    },
    'assertNotEqual': []
    },
{   'remark': 'Test Case 3:test_pcom_update_categories_from_postlist_data - categories, cat list category already present',
    'inputs': {\
            'categories': {\
                "no_of_category_pages": 1,
                "categories": [
                    {
                        "name": "anon",
                        "thumbnail": "/images/Polimorf-shapes-background.jpg",
                        "description": ""
                    }
                ]
            },
            'cat_list': ['anon'],
            'type': 'post',
            "ppp": 3,
            "default_thumb_link": sch.PM_DEFAULT_THUMBNAIL_IMAGE_LINK
    },
    'assertEqual': { 'no_of_category_pages': 1,
                    'categories': [
                        {
                            "name": "anon",
                            "thumbnail": "/images/Polimorf-shapes-background.jpg",
                            "description": ""
                        }
                    ]
                    },
    'assertNotEqual': []
    },
{   'remark': 'Test Case 4:test_pcom_update_categories_from_postlist_data - categories, cat list category already present plus one more - ppp = 1',
    'inputs': {\
            'categories': {\
                "no_of_category_pages": 1,
                "categories": [
                    {
                        "name": "anon",
                        "thumbnail": "/images/Polimorf-shapes-background.jpg",
                        "description": ""
                    }
                ]
            },
            'cat_list': ['anon','things'],
            'type': 'post',
            "ppp": 1,
            "default_thumb_link": sch.PM_DEFAULT_THUMBNAIL_IMAGE_LINK
    },
    'assertEqual': { 'no_of_category_pages': 2,
                    'categories': [
                        {
                            "name": "anon",
                            "thumbnail": "/images/Polimorf-shapes-background.jpg",
                            "description": ""
                        },
                        OrderedDict([('name', "things"),
                        ('thumbnail', sch.PM_DEFAULT_THUMBNAIL_IMAGE_LINK), ('description', '') ])
                    ]
                    },
    'assertNotEqual': []
    },
{   'remark': 'Test Case 5:test_pcom_update_categories_from_postlist_data - categories, cat list category already present plus one more - ppp = 1 - default thumbnail different',
    'inputs': {\
            'categories': {\
                "no_of_category_pages": 1,
                "categories": [
                    {
                        "name": "anon",
                        "thumbnail": "/images/Polimorf-shapes-background.jpg",
                        "description": ""
                    }
                ]
            },
            'cat_list': ['anon','things'],
            'type': 'post',
            "ppp": 1,
            "default_thumb_link": 'this/link.png'
    },
    'assertEqual': { 'no_of_category_pages': 2,
                    'categories': [
                        {
                            "name": "anon",
                            "thumbnail": "/images/Polimorf-shapes-background.jpg",
                            "description": ""
                        },
                        OrderedDict([('name', "things"),
                        ('thumbnail', 'this/link.png'), ('description', '') ])
                    ]
                    },
    'assertNotEqual': []
    },
{   'remark': 'Test Case 6:test_pcom_update_categories_from_postlist_data - categories, cat list category already present plus one more - ppp = 1 - default thumbnail different - type not post',
    'inputs': {\
            'categories': {\
                "no_of_category_pages": 1,
                "categories": [
                    {
                        "name": "anon",
                        "thumbnail": "/images/Polimorf-shapes-background.jpg",
                        "description": ""
                    }
                ]
            },
            'cat_list': ['anon','things'],
            'type': 'post1',
            "ppp": 1,
            "default_thumb_link": 'this/link.png'
    },
    'assertEqual': { 'no_of_category_pages': 1,
                    'categories': [
                        {
                            "name": "anon",
                            "thumbnail": "/images/Polimorf-shapes-background.jpg",
                            "description": ""
                        }
                    ]
                    },
    'assertNotEqual': []
    },
]
