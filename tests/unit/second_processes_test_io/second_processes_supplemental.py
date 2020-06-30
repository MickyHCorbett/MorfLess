#
import libraries.constants as ct
import libraries.globals as gb
import libraries.schematics as sch

from collections import OrderedDict
#

LIST_META_1 = {\
    'categories': {\
        "no_of_category_pages": 1,
        "categories": [
            {
                "name": "something",
                "thumbnail": "/images/Polimorf-shapes-background.jpg",
                "description": ""
            },
            {
                "name": "another category",
                "thumbnail": "/images/Polimorf-shapes-background.jpg",
                "description": ""
            },
            {
                "name": "interesting",
                "thumbnail": "/images/Polimorf-shapes-background-2.jpg",
                "description": ""
            },
            {
                "name": "things to write about",
                "thumbnail": "/images/Polimorf-shapes-background-2.jpg",
                "description": ""
            }
        ]
    },
    'authors': {\
        "no_of_author_pages": 1,
        "authors": [
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
                "shortname": "Jim O'Neill",
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
        }
}

LIST_META_BLANK_1 = {\
    'categories': {\
        "no_of_category_pages": 1,
        "categories": []
        },
    'authors': {\
        "no_of_author_pages": 1,
        "authors": []
    }
}

LIST_META_BLANK_2 = {\
    'categories': {\
        "no_of_category_pages": 1,
        "categories": []
        },
    'authors': {\
        "no_of_author_pages": 1,
        "authors": []
    }
}

LIST_META_2 = {\
    'categories': {\
        "no_of_category_pages": 1,
        "categories": []
        },
    'authors': {\
        "no_of_author_pages": 1,
        "authors": []
    }
}

POSTLIST_BLANK = \
{
    "no_posts": 0,
    "post_index": 0,
    "no_of_post_pages": 3,
    "posts": [
    ]
}

POSTLIST_BLANK_2 = \
{
    "no_posts": 0,
    "post_index": 0,
    "no_of_post_pages": 3,
    "posts": [
    ]
}


POSTLIST_SINGLE = \
{
    "no_posts": 6,
    "post_index": 6,
    "no_of_post_pages": 3,
    "posts": [
        {
            "index": 1,
            "type": "post",
            "url": "/contact/",
            "title": "Contact",
            "postname": "contact.post",
            "description": "Morfless Contact page",
            "categories": [
                "stuff"
            ],
            "authors": [
                "Clive"
            ],
            "extract": "Contact Morfless",
            "thumbnail": "/images/Polimorf-shapes-background.jpg",
            "creation_date": "12/09/2018",
            "creation_time": "12:18:10",
            "date_modified": "13/01/2020",
            "time_modified": "12:18:10",
            "sticky": ""
        },
    ]
}

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

ARCHIVE_1 = {\
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
            "name": "06-2020",
            "fileroot": "06_2020",
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
            "name": "06-2020",
            "fileroot": "06_2020",
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

ARCHIVE_2 = {\
    "created": [
    ],
    "modified": [
        {
            "name": "06-2020",
            "fileroot": "06_2020",
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

ARCHIVE_3 = {\
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
        }
    ],
    "modified": [
    ]
}

TEMP_CONTENT_1 = """

<!doctype html>
<html class="" lang="en">
<head>
  <title>Archive%%#TITLE#%%</title>
  <meta name="description" content="Archive%%#DESCRIPTION#%%">
</head>
<body class="body-archive%%$TEMPLATE_JS_NAME$%%">
<script src="/js/js-lists/postlist--archive%%$TEMPLATE_JS_NAME$%%.js" data-template-constant-name="_postlist_archive%%$TEMPLATE_CONSTANT_NAME$%%"></script>
</body>
</html>

"""

TEMP_CONTENT_2 = """

<!doctype html>
<html class="" lang="en">
<head>
  <title>Archive%%#TITLE#%%</title>
  <meta name="description" content="Archive%%#DESCRIPTION#%%">
</head>
<body class="body-archive%%$TEMPLATE_JS_NAME$%%">
<script src="/js/js-lists/postlist--archive%%$TEMPLATE_JS_NAME$%%.js" data-template-constant-name="_postlist_archive%%$TEMPLATE_CONSTANT_NAME$%%"></script>
</body>
</html>

"""
