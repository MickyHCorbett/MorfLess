#
from collections import OrderedDict

POSTLIST_1 = \
{
    "no_posts": 6,
    "post_index": 6,
    "no_of_post_pages": 3,
    "posts": [
        {
            "index": 1,
            "type": "page",
            "url": "/contact/",
            "title": "Contact",
            "postname": "contact.page",
            "description": "Morfless Contact page",
            "categories": [
                "NA"
            ],
            "authors": [
                "Micky"
            ],
            "extract": "Contact Morfless",
            "thumbnail": "/images/Polimorf-shapes-background.jpg",
            "creation_date": "12/09/2018",
            "creation_time": "12:18:10",
            "date_modified": "13/01/2020",
            "time_modified": "12:18:10",
            "sticky": ""
        },
        {
            "index": 2,
            "type": "post",
            "url": "/test3-post-something-new/",
            "title": "A new post",
            "postname": "test3.post",
            "description": "A new post about something again",
            "categories": [
                "something"
            ],
            "authors": [
                "anon"
            ],
            "extract": "Something longer here to describe what is going on. And to see if it is included in a search",
            "thumbnail": "/images/Polimorf-shapes-background.jpg",
            "creation_date": "12/10/2018",
            "creation_time": "12:18:10",
            "date_modified": "13/01/2020",
            "time_modified": "12:18:10",
            "sticky": ""
        },
        {
            "index": 3,
            "type": "page",
            "url": "/about/",
            "title": "About Morfless",
            "postname": "about.page",
            "description": "About Morfless",
            "categories": [
                "NA"
            ],
            "authors": [
                "Jim O'Neill"
            ],
            "extract": "An about page - describe yourself in as much detail as you like!\nYou can also add more to this extract.",
            "thumbnail": "/images/Polimorf-shapes-background.jpg",
            "creation_date": "12/10/2018",
            "creation_time": "12:18:10",
            "date_modified": "13/01/2020",
            "time_modified": "12:18:10",
            "sticky": ""
        },
        {
            "index": 4,
            "type": "post",
            "url": "/test2/",
            "title": "A new post - second coming - redux",
            "postname": "test2.post",
            "description": "A new post about something else",
            "categories": [
                "something",
                "interesting"
            ],
            "authors": [
                "Micky",
                "Albert"
            ],
            "extract": "Something longer here to describe what is going on",
            "thumbnail": "/images/Polimorf-shapes-background.jpg",
            "creation_date": "12/09/2019",
            "creation_time": "12:18:10",
            "date_modified": "13/01/2020",
            "time_modified": "12:18:10",
            "sticky": ""
        },
        {
            "index": 5,
            "type": "post",
            "url": "/test1-the-first-post/",
            "title": "A new post",
            "postname": "test1.post",
            "description": "A new post about something",
            "categories": [
                "something",
                "another category",
                "things to write about"
            ],
            "authors": [
                "anon"
            ],
            "extract": "Something longer here to describe what is going on.\nLike we can see there are more lines to add.\nThen more again!",
            "thumbnail": "/images/Polimorf-shapes-background.jpg",
            "creation_date": "12/10/2019",
            "creation_time": "12:18:10",
            "date_modified": "13/01/2020",
            "time_modified": "12:18:10",
            "sticky": "sticky"
        },
        {
            "index": 6,
            "type": "post",
            "url": "/about-this/",
            "title": "About Morfless and more",
            "postname": "about-this.post",
            "description": "About Morfless",
            "categories": [
                "NA"
            ],
            "authors": [
                "Jim O'Neill"
            ],
            "extract": "An about page - describe yourself in as much detail as you like!\nYou can also add more to this extract.",
            "thumbnail": "/images/Polimorf-shapes-background.jpg",
            "creation_date": "12/10/2018",
            "creation_time": "12:18:10",
            "date_modified": "13/01/2020",
            "time_modified": "12:18:10",
            "sticky": "sticky"
        }
    ]
}

POSTLIST_2 = \
{
    "no_posts": 2,
    "post_index": 6,
    "no_of_post_pages": 1,
    "posts": [
        {
            "index": 1,
            "type": "page",
            "url": "/contact/",
            "title": "Contact",
            "postname": "contact.page",
            "description": "Morfless Contact page",
            "categories": [
                "NA"
            ],
            "authors": [
                "Micky"
            ],
            "extract": "Contact Morfless",
            "thumbnail": "/images/Polimorf-shapes-background.jpg",
            "creation_date": "12/09/2018",
            "creation_time": "12:18:10",
            "date_modified": "13/01/2020",
            "time_modified": "12:18:10",
            "sticky": ""
        },
        {
            "index": 2,
            "type": "post",
            "url": "/test3-post-something-new/",
            "title": "A new post",
            "postname": "test5.post",
            "description": "A new post about something again",
            "categories": [
                "something"
            ],
            "authors": [
                "anon"
            ],
            "extract": "Something longer here to describe what is going on. And to see if it is included in a search",
            "thumbnail": "/images/Polimorf-shapes-background.jpg",
            "creation_date": "12/10/2018",
            "creation_time": "12:18:10",
            "date_modified": "13/01/2020",
            "time_modified": "12:18:10",
            "sticky": ""
        }
    ]
}

POSTLIST_3 = \
{
    "no_posts": 1,
    "post_index": 6,
    "no_of_post_pages": 1,
    "posts": [
        {
            "index": 1,
            "type": "page",
            "url": "/contact/",
            "title": "Contact",
            "postname": "contact.page",
            "description": "Morfless Contact page",
            "categories": [
                "NA"
            ],
            "authors": [
                "Micky"
            ],
            "extract": "Contact Morfless",
            "thumbnail": "/images/Polimorf-shapes-background.jpg",
            "creation_date": "12/09/2018",
            "creation_time": "12:18:10",
            "date_modified": "13/01/2020",
            "time_modified": "12:18:10",
            "sticky": ""
        }
    ]
}

POST_ENTRY_1 = \
{
    "index": 14,
    "type": "post",
    "url": "/contact/",
    "title": "Contact",
    "postname": "test5.post",
    "description": "Morfless Contact page",
    "categories": [
        "NA"
    ],
    "authors": [
        "Micky"
    ],
    "extract": "Contact Morfless",
    "thumbnail": "/images/Polimorf-shapes-background.jpg",
    "creation_date": "12/09/2018",
    "creation_time": "12:18:10",
    "date_modified": "13/01/2020",
    "time_modified": "12:18:10",
    "sticky": ""
}

CONTACT_PAGE_POST = \
{
    "index": 1,
    "type": "page",
    "url": "/contact/",
    "title": "Contact",
    "postname": "contact.page",
    "description": "Morfless Contact page",
    "categories": [
        "NA"
    ],
    "authors": [
        "Micky"
    ],
    "extract": "Contact Morfless",
    "thumbnail": "/images/Polimorf-shapes-background.jpg",
    "creation_date": "12/09/2018",
    "creation_time": "12:18:10",
    "date_modified": "13/01/2020",
    "time_modified": "12:18:10",
    "sticky": ""
}

TEMPLATE_SEARCH_CONTENT = \
{
    "categories": {
        "name": "Categories",
        "thumbnail": "/images/Polimorf-shapes-background-orange.jpg",
        "description": "Posts listed by category"
    },
    "authors": {
        "name": "Authors",
        "thumbnail": "/images/Polimorf-shapes-background-yellow.jpg",
        "description": "Posts and pages listed by author"
    },
    "archive": {
        "name": "Archive",
        "thumbnail": "/images/Polimorf-shapes-background-black.jpg",
        "description": "Monthly archives arranged by most recent to older"
    },
    "posts": {
        "name": "Entries",
        "thumbnail": "/images/Polimorf-shapes-background-darkblue-thing.jpg",
        "description": "Entries for each image with a description of how it was done and some"
    },
    "index": {
        "name": "Home page",
        "thumbnail": "/images/Polimorf-shapes-background.jpg",
        "description": "Welcome to the site! Feel free to browse around and follow the links to other pages and posts"
    },
    "404": {
        "name": "Not Found",
        "thumbnail": "/images/Polimorf-shapes-background.jpg",
        "description": "When you can't find anything you always end up here!"
    }
}

TEMPLATE_POSTS = \
{
    "name": "Entries",
    "thumbnail": "/images/Polimorf-shapes-background-darkblue-thing.jpg",
    "description": "Entries for each image with a description of how it was done and some"
}

TEMPLATE_INDEX = \
{
    "name": "Home page",
    "thumbnail": "/images/Polimorf-shapes-background.jpg",
    "description": "Welcome to the site! Feel free to browse around and follow the links to other pages and posts"
}

AUTHORS_1 = \
[
    {
    "name": "Corvos AE Team",
    "shortname": "Team_CAE",
    "thumbnail": "/images/CorvosTeam.jpg",
    "description": "General information and content from the Corvos Astro Engineering site"
    },
    {
    "name": "Micky H Corbett",
    "shortname": "Micky",
    "thumbnail": "/images/CorvosDefaultImage.jpg",
    "description": "Aerospace and Space engineer with over 20 years experience in various fields including ion propulsion, aerospace systems, flight control, thruster control, prototype development. \nOther skills include cloud application development coding in multiple languages and enjoying the creative process!"
    },
    {
    "name": "Albert",
    "shortname": "Albert",
    "thumbnail": "/images/Polimorf-shapes-background-2.jpg",
    "description": ""
    },
    {
    "name": "Jim O'Neill",
    "shortname": "Jimbo",
    "thumbnail": "/images/Polimorf-shapes-background-2.jpg",
    "description": ""
    },
    {
    "name": "Contact",
    "shortname": "Contact",
    "thumbnail": "/images/Polimorf-shapes-background-2.jpg",
    "description": ""
    }

]

ARCHIVE_1 = \
{
    "created": [
        {
            "name": "09-2018",
            "fileroot": "09_2018",
            "posts": [],
            "pages": [
                "contact.page"
            ]
        },
        {
            "name": "10-2018",
            "fileroot": "10_2018",
            "posts": [
                "test3.post"
            ],
            "pages": [
                "about.page"
            ]
        },
        {
            "name": "09-2019",
            "fileroot": "09_2019",
            "posts": [
                "test2.post"
            ],
            "pages": []
        },
        {
            "name": "10-2019",
            "fileroot": "10_2019",
            "posts": [
                "test1.post"
            ],
            "pages": []
        },
        {
            "name": "02-2020",
            "fileroot": "02_2020",
            "posts": [
                "test5.post",
                "test6.post"
            ],
            "pages": [
                "about-polimorfic.page"
            ]
        }
    ],
    "modified": [
        {
            "name": "02-2020",
            "fileroot": "02_2020",
            "posts": [
                "test3.post",
                "test2.post",
                "test1.post",
                "test5.post",
                "test6.post"
            ],
            "pages": [
                "contact.page",
                "about.page",
                "about-polimorfic.page"
            ]
        }
    ]
}

DEPENDENCIES_1 = \
[
    {
        "filename": "index.page",
        "dependencies": [
            "settings.txt",
            "extra.txt"
        ]
    },
    {
        "filename": "404.page",
        "dependencies": [
            "settings.txt",
            "extra.txt"
        ]
    },
    {
        "filename": "search.page",
        "dependencies": [
            "settings.txt",
            "search_insert.dat"
        ]
    },
    {
        "filename": "categories.page",
        "dependencies": [
            "settings.txt"
        ]
    },
    {
        "filename": "test1.post",
        "dependencies": [
            "puppies.txt",
            "settings.txt"
        ]
    },
    {
        "filename": "about.page",
        "dependencies": [
            "puppies.txt"
        ]
    },
    {
        "filename": "test2.post",
        "dependencies": [
            "puppies.txt",
            "settings.txt"
        ]
    },
    {
        "filename": "test3.post",
        "dependencies": [
            "puppies_2.txt"
        ]
    },
    {
        "filename": "details/test1.post",
        "dependencies": [
            "puppies.txt",
            "settings.txt"
        ]
    }
]

DEPENDENCIES_2 = \
[
    {
        "filename": "index.page",
        "dependencies": [
            "settings.txt",
            "extra1.txt"
        ]
    },
    {
        "filename": "404.page",
        "dependencies": [
            "settings.txt",
            "extra2.txt"
        ]
    }
]

DEPENDENCIES_3 = \
[
    {
        "filename": "404.page",
        "dependencies": [
            "settings.txt",
            "extra2.txt"
        ]
    }
]

DEPENDENCIES_4 = \
[
    {
        "filename": "index.page",
        "dependencies": [
            "settings.txt",
            "extra1.txt",
            "something.else"
        ]
    },
    {
        "filename": "404.page",
        "dependencies": [
            "settings.txt",
            "extra2.txt"
        ]
    }
]

POST_LISTS_INFO_1 = [\
    {
        "name": "postlist--test1.js",
        "fileroot": "test1",
        "postlists": [
            {
                "index": 68,
                "fileroot": "test1",
                "ppp": "5",
                "content": "about.page"
            },
            {
                "index": 76,
                "fileroot": "test1",
                "ppp": "3",
                "content": "test1.post, test2.post"
            },
            {
                "index": 108,
                "fileroot": "test1",
                "ppp": "2",
                "content": "about.page, test2.post"
            }
        ]
    },
    {
        "name": "postlist--about.js",
        "fileroot": "about",
        "postlists": [
            {
                "index": 62,
                "fileroot": "about",
                "ppp": "5",
                "content": "about.page"
            }
        ]
    },
    {
        "name": "postlist--search.js",
        "fileroot": "search",
        "postlists": [
            {
                "index": 62,
                "fileroot": "search",
                "ppp": "5",
                "content": "search.page"
            }
        ]
    },
    {
        "name": "postlist--test2.js",
        "fileroot": "test2",
        "postlists": [
            {
                "index": 88,
                "fileroot": "test2",
                "ppp": "5",
                "content": "about.page"
            }
        ]
    },
    {
        "name": "postlist--test3.js",
        "fileroot": "test3",
        "postlists": [
            {
                "index": 51,
                "fileroot": "test3",
                "ppp": "5",
                "content": "about.page"
            }
        ]
    },
    {
        "name": "postlist--details_test1.js",
        "fileroot": "details_test1",
        "postlists": [
            {
                "index": 58,
                "fileroot": "details_test1",
                "ppp": "5",
                "content": "about.page"
            }
        ]
    }
]

POST_LISTS_INFO_2 = [\
    {
        "name": "postlist--test1.js",
        "fileroot": "test1",
        "postlists": [
            {
                "index": 68,
                "fileroot": "test1",
                "ppp": "5",
                "content": "about.page"
            },
            {
                "index": 76,
                "fileroot": "test1",
                "ppp": "3",
                "content": "test1.post, test2.post"
            },
            {
                "index": 108,
                "fileroot": "test1",
                "ppp": "2",
                "content": "about.page, test2.post"
            }
        ]
    }
]

POST_LISTS_INFO_3 = [\
    {
        "name": "postlist--test1.js",
        "fileroot": "test1",
        "postlists": [
            {
                "index": 68,
                "fileroot": "test1",
                "ppp": "5",
                "content": "about.page"
            },
            {
                "index": 76,
                "fileroot": "test1",
                "ppp": "3",
                "content": "test1.post, test2.post"
            },
            {
                "index": 108,
                "fileroot": "test1",
                "ppp": "2",
                "content": "about.page, test2.post"
            }
        ]
    },
    OrderedDict([('name', 'postlist__post1.js'), ('fileroot', 'test1'), ('postlists', ['this'])])
]


POST_LISTS_INFO_4 = [\
    {
        "name": "postlist--test1.js",
        "fileroot": "test1",
        "postlists": [
            {
                "index": 68,
                "fileroot": "test1",
                "ppp": "5",
                "content": "about.page"
            },
            {
                "index": 76,
                "fileroot": "test1",
                "ppp": "3",
                "content": "test1.post, test2.post"
            },
            {
                "index": 108,
                "fileroot": "test1",
                "ppp": "2",
                "content": "about.page, test2.post"
            }
        ]
    }
]

POST_LISTS_INFO_5 = [\
    {
        "name": "postlist--test1.js",
        "fileroot": "test1",
        "postlists": [
            {
                "index": 76,
                "fileroot": "test1",
                "ppp": "3",
                "content": "test1.post, test2.post"
            }
        ]
    }
]

POST_LISTS_INFO_6 = [\
    OrderedDict([('name', 'postlist__post1.js'), ('fileroot', 'test1'), ('postlists', ['this'])])
]

POST_LISTS_INFO_7 = [\
    {
        "name": "postlist--test1.js",
        "fileroot": "test1",
        "postlists": [
            {
                "index": 76,
                "fileroot": "test1",
                "ppp": "3",
                "content": "test1.post, test2.post"
            }
        ]
    },
    OrderedDict([('name', 'postlist__post1.js'), ('fileroot', 'test1'), ('postlists', ['this'])])
]

POST_LISTS_INFO_8 = [\
    {
        "name": "postlist--test2.js",
        "fileroot": "test1",
        "postlists": [
            {
                "index": 76,
                "fileroot": "test1",
                "ppp": "3",
                "content": "test1.post, test2.post"
            }
        ]
    }
]

PAGINATION_1 = [\
    {
        "name": "pagination--test2.js",
        "fileroot": "test2",
        "pagination": {
            "index": 70,
            "fileroot": "test2",
            "next_ref": "",
            "prev_ref": "",
            "postname": "test2.post",
            "type": True
        }
    },
    {
        "name": "pagination--test1.js",
        "fileroot": "test1",
        "pagination": {
            "index": 186,
            "fileroot": "test1",
            "next_ref": "about.page",
            "prev_ref": "test3.post",
            "postname": "test1.post",
            "type": True
        }
    },
    {
        "name": "pagination--test5.js",
        "fileroot": "test5",
        "pagination": {
            "index": 64,
            "fileroot": "test5",
            "next_ref": "",
            "prev_ref": "",
            "postname": "test5.post",
            "type": True
        }
    },
    {
        "name": "pagination--contact.js",
        "fileroot": "contact",
        "pagination": {
            "index": 59,
            "fileroot": "contact",
            "next_ref": "",
            "prev_ref": "",
            "postname": "contact.page",
            "type": False
        }
    },
    {
        "name": "pagination--test3.js",
        "fileroot": "test3",
        "pagination": {
            "index": 71,
            "fileroot": "test3",
            "next_ref": "",
            "prev_ref": "",
            "postname": "test3.post",
            "type": True
        }
    }
]

PAGINATION_2 = [\
    {
        "name": "pagination--test2.js",
        "fileroot": "test2",
        "pagination": {
            "index": 70,
            "fileroot": "test2",
            "next_ref": "",
            "prev_ref": "",
            "postname": "test2.post",
            "type": True
        }
    }
]

PAGINATION_3 = [\
    {
        "name": "pagination--test2.js",
        "fileroot": "test2",
        "pagination": {
            "index": 70,
            "fileroot": "test2",
            "next_ref": "",
            "prev_ref": "",
            "postname": "test2.post",
            "type": True
        }
    },
    OrderedDict([('name', 'pagination__post1.js'), ('fileroot', 'test1'), ('pagination', ['this'])])
]

PAGINATION_4 = [\
    {
        "name": "pagination--test1.js",
        "fileroot": "test1",
        "pagination": {
            "index": 70,
            "fileroot": "test1",
            "next_ref": "",
            "prev_ref": "",
            "postname": "test1.post",
            "type": True
        }
    }
]
PAGINATION_5 = [\
    {
        "name": "pagination--test1.js",
        "fileroot": "test1",
        "pagination": {
            'index': 1,
            'fileroot': 'test1-here',
            'next_ref': 'this.ref',
            'prev_ref': 'that.ref',
            'postname': 'test1-here.post',
            'type': False
        }
    }
]

PAGINATION_6 = [\
    OrderedDict([('name', 'pagination__post1.js'), ('fileroot', 'test1'), ('pagination', ['this'])])
]

PAGINATION_7 = [\
    {
        "name": "pagination--test2.js",
        "fileroot": "test2",
        "pagination": {
            "index": 70,
            "fileroot": "test2",
            "next_ref": "",
            "prev_ref": "",
            "postname": "test2.post",
            "type": True
        }
    }
]

ARCHIVE_POSTLIST_1 = \
{
    "no_posts": 2,
    "post_index": 6,
    "no_of_post_pages": 1,
    "posts": [
        {
            "index": 1,
            "type": "page",
            "url": "/contact/",
            "title": "Contact",
            "postname": "contact.page",
            "description": "Morfless Contact page",
            "categories": [
                "NA"
            ],
            "authors": [
                "Micky"
            ],
            "extract": "Contact Morfless",
            "thumbnail": "/images/Polimorf-shapes-background.jpg",
            "creation_date": "12/09/2018",
            "creation_time": "12:18:10",
            "date_modified": "13/02/2020",
            "time_modified": "12:18:10",
            "sticky": ""
        },
        {
            "index": 6,
            "type": "post",
            "url": "/test3-post-something-new/",
            "title": "A new post",
            "postname": "test5.post",
            "description": "A new post about something again",
            "categories": [
                "something"
            ],
            "authors": [
                "anon"
            ],
            "extract": "Something longer here to describe what is going on. And to see if it is included in a search",
            "thumbnail": "/images/Polimorf-shapes-background.jpg",
            "creation_date": "12/10/2018",
            "creation_time": "12:18:10",
            "date_modified": "13/01/2020",
            "time_modified": "12:18:10",
            "sticky": ""
        }
    ]
}

ARCHIVE_UPDATE_1 = {\
    'created': [OrderedDict([('name', '09-2018'), ('fileroot', '09_2018'), ('posts', []), ('pages', ['contact.page'])]),
    OrderedDict([('name', '10-2018'), ('fileroot', '10_2018'), ('posts', ['test5.post']), ('pages', [])])], 'modified': [OrderedDict([('name', '02-2020'), ('fileroot', '02_2020'), ('posts', []), ('pages', ['contact.page'])]),
    OrderedDict([('name', '01-2020'), ('fileroot', '01_2020'), ('posts', ['test5.post']), ('pages', [])])]
}

ARCHIVE_UPDATE_2 = {\
    "created": [
        {
            "name": "09-2016",
            "fileroot": "09_2016",
            "posts": [],
            "pages": [
                "test5.post"
            ]
        },
        {
            "name": "10-2016",
            "fileroot": "10_2016",
            "posts": [
                "contact.page"
            ],
            "pages": []
        }
    ],
    "modified": [
        {
            "name": "04-2020",
            "fileroot": "04_2020",
            "posts": [],
            "pages": [
                "test7.post"
            ]
        },
        {
            "name": "05-2020",
            "fileroot": "05_2020",
            "posts": [
                "contact.page"
            ],
            "pages": []
        }
    ]
}

ARCHIVE_UPDATE_3 = {\
    "created": [
        {
            "name": "09-2016",
            "fileroot": "09_2016",
            "posts": [],
            "pages": [
                "test5.post"
            ]
        },
        {
            "name": "10-2016",
            "fileroot": "10_2016",
            "posts": [
                "contact.page"
            ],
            "pages": []
        },
        OrderedDict([('name', '09-2018'), ('fileroot', '09_2018'), ('posts', []), ('pages', ['contact.page'])]),
        OrderedDict([('name', '10-2018'), ('fileroot', '10_2018'), ('posts', ['test5.post']), ('pages', [])])
    ],
    "modified": [
        {
            "name": "04-2020",
            "fileroot": "04_2020",
            "posts": [],
            "pages": [
                "test7.post"
            ]
        },
        {
            "name": "05-2020",
            "fileroot": "05_2020",
            "posts": [
                "contact.page"
            ],
            "pages": []
        },
        OrderedDict([('name', '02-2020'), ('fileroot', '02_2020'), ('posts', []), ('pages', ['contact.page'])]),
        OrderedDict([('name', '01-2020'), ('fileroot', '01_2020'), ('posts', ['test5.post']), ('pages', [])])
    ]
}

ARCHIVE_POSTLIST_2 = \
{
    "no_posts": 2,
    "post_index": 6,
    "no_of_post_pages": 1,
    "posts": [
        {
            "index": 1,
            "type": "page",
            "url": "/contact/",
            "title": "Contact3",
            "postname": "contact3.page",
            "description": "Morfless Contact page",
            "categories": [
                "NA"
            ],
            "authors": [
                "Micky"
            ],
            "extract": "Contact Morfless",
            "thumbnail": "/images/Polimorf-shapes-background.jpg",
            "creation_date": "15/09/2018",
            "creation_time": "12:18:10",
            "date_modified": "13/05/2020",
            "time_modified": "12:18:10",
            "sticky": ""
        }
    ]
}

ARCHIVE_UPDATE_4 = {\
    "created": [
        {
            "name": "09-2018",
            "fileroot": "09_2018",
            "posts": [
                'this.post'
            ],
            "pages": [
                "contact2.page"
            ]
        }
    ],
    "modified": [
        {
            "name": "05-2020",
            "fileroot": "05_2020",
            "posts": [
                "test3.post",
                "test2.post",
                "test1.post",
                "test5.post",
                "test6.post"
            ],
            "pages": [
                "contact.page",
                "about.page",
                "about-polimorfic.page"
            ]
        }
    ]
}

ARCHIVE_UPDATE_5 = {\
    "created": [
        {
            "name": "09-2018",
            "fileroot": "09_2018",
            "posts": [
                'this.post'
            ],
            "pages": [
                "contact2.page",
                "contact3.page"
            ]
        }
    ],
    "modified": [
        {
            "name": "05-2020",
            "fileroot": "05_2020",
            "posts": [
                "test3.post",
                "test2.post",
                "test1.post",
                "test5.post",
                "test6.post"
            ],
            "pages": [
                "contact.page",
                "about.page",
                "about-polimorfic.page",
                "contact3.page"
            ]
        }
    ]
}
