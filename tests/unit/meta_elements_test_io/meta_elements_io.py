#
import libraries.constants as ct
import libraries.globals as gb
import libraries.schematics as sch
import libraries.meta_defaults as md

from collections import OrderedDict
#

test_values_1 = [\
{   'remark': 'Test Case 1:pcom_process_settings_meta_syntax - empty settings',
    'input': """

    """,
    'assertEqual': gb.DEFAULT_SETTINGS,
    'assertNotEqual': []
    }
]


test_values_2 = [\
{   'remark': 'Test Case 1:pcom_process_settings_meta_syntax - posts_per_page = 2',
    'element': 'posts_per_page',
    'input': """
        posts_per_page={ 2 }:
    """,
    'assertEqual': 2,
    'assertNotEqual': 5
    },

{   'remark': 'Test Case 2:pcom_process_settings_meta_syntax - posts_per_page = 7',
    'element': 'posts_per_page',
    'input': """
        posts_per_page={ 7 }:
    """,
    'assertEqual': 7,
    'assertNotEqual': 5
    },

{   'remark': 'Test Case 3:pcom_process_settings_meta_syntax - site_title no data',
    'element': 'site_title',
    'input': """

    """,
    'assertEqual': md.DEFAULT_SITE_TITLE,
    'assertNotEqual': 'title'
    },


{   'remark': 'Test Case 4:pcom_process_settings_meta_syntax - site_title incorrect syntax',
    'element': 'site_title',
    'input': """
        this={ }
        title = { something else }
    """,
    'assertEqual': md.DEFAULT_SITE_TITLE,
    'assertNotEqual': 'something'
    },

{   'remark': 'Test Case 5:pcom_process_settings_meta_syntax - site_title',
    'element': 'site_title',
    'input': """
        title={ something }:
    """,
    'assertEqual': 'something',
    'assertNotEqual': md.DEFAULT_SITE_TITLE
    },

{   'remark': 'Test Case 6:pcom_process_settings_meta_syntax - site description no data',
    'element': 'site_description',
    'input': """
        description = { something }
    """,
    'assertEqual': md.DEFAULT_SITE_DESCRIPTION,
    'assertNotEqual': 'something'
    },


{   'remark': 'Test Case 7:pcom_process_settings_meta_syntax - site description incorrect syntax before - cascade',
    'element': 'site_description',
    'input': """
        this={ }
        description={ something else }:
    """,
    'assertEqual': md.DEFAULT_SITE_DESCRIPTION,
    'assertNotEqual': 'something'
    },

{   'remark': 'Test Case 8:pcom_process_settings_meta_syntax - site description',
    'element': 'site_description',
    'input': """
        this={ }:
        description={ something }:
    """,
    'assertEqual': 'something',
    'assertNotEqual': md.DEFAULT_SITE_DESCRIPTION
    },

{   'remark': 'Test Case 9:pcom_process_settings_meta_syntax - date format none',
    'element': 'date_format',
    'input': """
        date_format={ }:
    """,
    'assertEqual': ct.PCOM_NO_ENTRY,
    'assertNotEqual': ct.PCOM_UK_DATE_FORMAT
    },

{   'remark': 'Test Case 10:pcom_process_settings_meta_syntax - date format',
    'element': 'date_format',
    'input': """

        date_format={ this }:
    """,
    'assertEqual': 'this',
    'assertNotEqual': ct.PCOM_UK_DATE_FORMAT
    },

{   'remark': 'Test Case 11:pcom_process_settings_meta_syntax - search api none',
    'element': 'search_api_url',
    'input': """
        search_api_url={ }:
    """,
    'assertEqual': ct.PCOM_NO_ENTRY,
    'assertNotEqual': ''
    },

{   'remark': 'Test Case 12:pcom_process_settings_meta_syntax - search api',
    'element': 'search_api_url',
    'input': """

        search_api_url={ this }:
    """,
    'assertEqual': 'this',
    'assertNotEqual': ct.PCOM_NO_ENTRY
    },

{   'remark': 'Test Case 13:pcom_process_settings_meta_syntax - content meta post empty',
    'element': 'default_content_post_meta',
    'input': """
        post_meta_default={ }:
    """,
    'assertEqual': ct.PCOM_NO_ENTRY,
    'assertNotEqual': ''
    },

{   'remark': 'Test Case 14:pcom_process_settings_meta_syntax - content meta post',
    'element': 'default_content_post_meta',
    'input': """

        post_meta_default={ this }:
    """,
    'assertEqual': 'this',
    'assertNotEqual': ct.PCOM_NO_ENTRY
    },

{   'remark': 'Test Case 15:pcom_process_settings_meta_syntax - content meta page empty',
    'element': 'default_content_page_meta',
    'input': """
        page_meta_default={ }:
    """,
    'assertEqual': ct.PCOM_NO_ENTRY,
    'assertNotEqual': ''
    },

{   'remark': 'Test Case 16:pcom_process_settings_meta_syntax - content meta page',
    'element': 'default_content_page_meta',
    'input': """

        page_meta_default={ this }:
    """,
    'assertEqual': 'this',
    'assertNotEqual': ct.PCOM_NO_ENTRY
    }

]

test_values_3 = [\
{   'remark': 'Test Case 1:pcom_process_settings_meta_syntax - new author',
    'element': 'author_info',
    'input': """
        author={
            [
                { "name":           "Bill",
                  "shortname":      "Bill Maguire",
                  "thumbnail":      "/my-link.png",
                  "description":    "Something %here?&" }
            ]
        }:
    """,
    'assertEqual': [\
           OrderedDict([('name', "Bill"),
           ('shortname', 'Bill Maguire'),
           ('thumbnail', '/my-link.png'),
           ('description', 'Something %here?&') ])
            ],
    'assertNotEqual': []
    },

{   'remark': 'Test Case 2:pcom_process_settings_meta_syntax - new author 2',
    'element': 'author_info',
    'input': """

author={
[
    {
      "name": "Micky H Corbett",
      "shortname": "Mícky",
      "description": "Aerospace and Space engineer with over 20 years experience in various fields including: ion propulsion, aerospace systems, flight control, thruster control, prototype development. Other skills include cloud application development, coding in multiple languages and enjoying the creative process!"
    }
]
}:
    """,
    'assertEqual': [\
           OrderedDict([('name', "Micky H Corbett"),
           ('shortname', 'Mícky'),
           ('description', 'Aerospace and Space engineer with over 20 years experience in various fields including: ion propulsion, aerospace systems, flight control, thruster control, prototype development. Other skills include cloud application development, coding in multiple languages and enjoying the creative process!') ])
            ],
    'assertNotEqual': []
    },

{   'remark': 'Test Case 3:pcom_process_settings_meta_syntax - default author',
    'element': 'default_author',
    'input': """
        default_author={
                {  }
        }:
    """,
    'assertEqual': { 'name': 'anon',
           'shortname': 'anon',
           'thumbnail': sch.PM_DEFAULT_THUMBNAIL_IMAGE_LINK,
           'description': ''},
    'assertNotEqual': {}
    },

{   'remark': 'Test Case 4:pcom_process_settings_meta_syntax - default author - name and other parameter not in default',
    'element': 'default_author',
    'input': """
        default_author={
                {
                    "name": "this",
                    "othername": "something"
                }
        }:
    """,
    'assertEqual': { 'name': 'this',
           'shortname': 'anon',
           'thumbnail': sch.PM_DEFAULT_THUMBNAIL_IMAGE_LINK,
           'description': ''},
    'assertNotEqual': { 'name': 'this',
           'shortname': 'anon',
           'othername': 'something',
           'thumbnail': sch.PM_DEFAULT_THUMBNAIL_IMAGE_LINK,
           'description': ''}
    },

{   'remark': 'Test Case 5:pcom_process_settings_meta_syntax - default author - parameters ',
    'element': 'default_author',
    'input': """
        default_author={
                {
                    "name": "this",
                    "shortname": "something",
                    "thumbnail": "that.png",
                    "description": "hello"
                }
        }:
    """,
    'assertEqual': { 'name': 'this',
           'shortname': 'something',
           'thumbnail': 'that.png',
           'description': 'hello'},
    'assertNotEqual': { 'name': 'anon',
           'shortname': 'anon',
           'thumbnail': sch.PM_DEFAULT_THUMBNAIL_IMAGE_LINK,
           'description': ''}
    },

{   'remark': 'Test Case 6:pcom_process_settings_meta_syntax - new category',
    'element': 'category_info',
    'input': """
        categories={
            [
                { "name":           "Bill",
                  "thumbnail":      "/my-link.png",
                  "description":    "Something %here?&" }
            ]
        }:
    """,
    'assertEqual': [\
           OrderedDict([('name', "Bill"),
           ('thumbnail', '/my-link.png'),
           ('description', 'Something %here?&') ])
            ],
    'assertNotEqual': []
    },

{   'remark': 'Test Case 7:pcom_process_settings_meta_syntax - new category - name only',
    'element': 'category_info',
    'input': """
        categories={
            [
                { "name": "Bill" }
            ]
        }:
    """,
    'assertEqual': [\
           OrderedDict([('name', "Bill")])
            ],
    'assertNotEqual': []
    },

{   'remark': 'Test Case 8:pcom_process_settings_meta_syntax - new category - name and thumbnail only',
    'element': 'category_info',
    'input': """
        categories={
            [
                {
                    "name": "Bill",
                    "thumbnail": "thumbnail.png"
                }
            ]
        }:
    """,
    'assertEqual': [\
           OrderedDict([('name', 'Bill'),
           ('thumbnail', 'thumbnail.png')])
            ],
    'assertNotEqual': []
    },

{   'remark': 'Test Case 9:pcom_process_settings_meta_syntax - new category - name and thumbnail only - incorrect JSON',
    'element': 'category_info',
    'input': """
        categories={
            [
                {
                    "name": "Bill"
                    "thumbnail": "thumbnail.png"
                }
            ]
        }:
    """,
    'assertEqual': {'name': ct.PCOM_JSON_LOAD_ERROR },
    'assertNotEqual': []
    },

{   'remark': 'Test Case 10:pcom_process_settings_meta_syntax - template type empty',
    'element': 'template_types',
    'input': """
            templates={
              {
              }
            }:
    """,
    'assertEqual': {\
      "search": "search",
      "categories": "categories",
      "authors": "authors",
      "archive": "archive",
      "posts": "posts"
    },
    'assertNotEqual': {}
    },

{   'remark': 'Test Case 11:pcom_process_settings_meta_syntax - template type parameters with extras',
    'element': 'template_types',
    'input': """
            templates={
              {
                "search": "search2",
                "categories": "categories2",
                "authors": "authors2",
                "archive": "archive2",
                "posts": "posts2",
                "search1": "search",
                "categories1": "categories",
                "authors1": "authors",
                "archive1": "archive",
                "posts1": "posts"
              }
            }:
    """,
    'assertEqual': {\
      "search": "search2",
      "categories": "categories2",
      "authors": "authors2",
      "archive": "archive2",
      "posts": "posts2"
    },
    'assertNotEqual': {}
    },

{   'remark': 'Test Case 12:pcom_process_settings_meta_syntax - template main header text empty',
    'element': 'template_main_header_text',
    'input': """
            template_main_header_text={
              {
              }
            }:
    """,
    'assertEqual': gb.DEFAULT_TEMPLATE_MAIN_HEADER_TEXT,
    'assertNotEqual': {}
    },

{   'remark': 'Test Case 13:pcom_process_settings_meta_syntax - template main header text parameters with extras',
    'element': 'template_main_header_text',
    'input': """
            template_main_header_text={
              {
                "search": "Results for: 2",
                "categories": "Categories2",
                "authors": "Authors2",
                "archive": "Monthly Archives2",
                "posts": "Posts2",
                "search1": "Results for: ",
                "categories1": "Categories",
                "authors1": "Authors",
                "archive1": "Monthly Archives",
                "posts1": "Posts"
              }
            }:
    """,
    'assertEqual': {\
      "search": "Results for: 2",
      "categories": "Categories2",
      "authors": "Authors2",
      "archive": "Monthly Archives2",
      "posts": "Posts2"
    },
    'assertNotEqual': {}
    },

{   'remark': 'Test Case 14:pcom_process_settings_meta_syntax - template header sub text empty',
    'element': 'template_sub_header_text',
    'input': """
            template_sub_header_text={
              {
              }
            }:
    """,
    'assertEqual': gb.DEFAULT_TEMPLATE_SUB_HEADER_TEXT,
    'assertNotEqual': {}
    },

{   'remark': 'Test Case 15:pcom_process_settings_meta_syntax - template header sub text parameters with extras',
    'element': 'template_sub_header_text',
    'input': """
            template_sub_header_text={

              {
                "categories": "Posts for category: 2",
                "authors": "Posts by author: 2",
                "archive": "Posts for month: 2",
                "categories1": "Posts for category: ",
                "authors1": "Posts by author: ",
                "archive1": "Posts for month: "
              }
            }:
    """,
    'assertEqual': {\
      "categories": "Posts for category: 2",
      "authors": "Posts by author: 2",
      "archive": "Posts for month: 2"
    },
    'assertNotEqual': {}
    },

{   'remark': 'Test Case 16:pcom_process_settings_meta_syntax - template header back link text empty',
    'element': 'template_sub_header_back_link_text',
    'input': """
            template_sub_header_back_link_text={
              {
              }
            }:
    """,
    'assertEqual': gb.DEFAULT_TEMPLATE_SUB_HEADER_BACK_LINK_TEXT,
    'assertNotEqual': {}
    },

{   'remark': 'Test Case 17:pcom_process_settings_meta_syntax - template header back link text parameters with extras',
    'element': 'template_sub_header_back_link_text',
    'input': """
            template_sub_header_back_link_text={
              {
                "categories": "Back to Categories2",
                "authors": "Back to Authors2",
                "archive": "Back to Archives2",
                "categories1": "Back to Categories",
                "authors1": "Back to Authors",
                "archive1": "Back to Archives"
              }
            }:
    """,
    'assertEqual': {\
      "categories": "Back to Categories2",
      "authors": "Back to Authors2",
      "archive": "Back to Archives2"
    },
    'assertNotEqual': {}
    },

{   'remark': 'Test Case 18:pcom_process_settings_meta_syntax - default template search content empty',
    'element': 'template_search_content',
    'input': """
            template_search_content={
              {
              }
            }:
    """,
    'assertEqual': gb.DEFAULT_TEMPLATE_SEARCH_CONTENT,
    'assertNotEqual': {}
    },

{   'remark': 'Test Case 19:pcom_process_settings_meta_syntax - template header back link text parameters with extras',
    'element': 'template_search_content',
    'input': """
            template_search_content={
              {
                "index": {
                    "name": "Home Bird",
                    "thumbnail": "that.png",
                    "description": "More joy!"
                },
                "index2": {
                    "name": "Home Bird",
                    "thumbnail": "that.png",
                    "description": "More joy!"
                }
              }
            }:
    """,
    'assertEqual': {\
          ct.PCOM_SETTINGS_TYPE_CATEGORIES: {
              'name': ct.PCOM_SETTINGS_TYPE_CATEGORIES.capitalize(),
              'thumbnail': '/images/Polimorf-shapes-background-orange.jpg',
              'description': 'Posts listed by category'
          },
          ct.PCOM_SETTINGS_TYPE_AUTHORS: {
              'name': ct.PCOM_SETTINGS_TYPE_AUTHORS.capitalize(),
              'thumbnail': '/images/Polimorf-shapes-background-yellow.jpg',
              'description': 'Posts and pages listed by author'
          },
          ct.PCOM_SETTINGS_TYPE_ARCHIVE: {
              'name': ct.PCOM_SETTINGS_TYPE_ARCHIVE.capitalize(),
              'thumbnail': '/images/Polimorf-shapes-background-black.jpg',
              'description': 'Monthly archives arranged by most recent to older'
          },
          ct.PCOM_SETTINGS_TYPE_POSTS: {
              'name': ct.PCOM_SETTINGS_TYPE_POSTS.capitalize(),
              'thumbnail': '/images/Polimorf-shapes-background-darkblue.jpg',
              'description': 'Posts by various authors and in various categories'
          },
          "index": {
              "name": "Home Bird",
              "thumbnail": "that.png",
              "description": "More joy!"
          },
          '404': {
              'name': 'Not Found',
              'thumbnail': sch.PM_DEFAULT_THUMBNAIL_IMAGE_LINK,
              'description': "When you can't find anything you end up here!"
          }
    },
    'assertNotEqual': {}
    }
]

test_values_4 = [\
{   'remark': 'Test Case 1:pcom_process_meta_syntax - content empty',
    'input': """

    """,
    'assertEqual': {\
        'page_title': md.DEFAULT_PAGE_TITLE,
        'page_description': md.DEFAULT_PAGE_DESCRIPTION,
        'authors': md.DEFAULT_AUTHOR,
        'categories': md.DEFAULT_CATEGORY,
        'thumb_link': sch.PM_DEFAULT_THUMBNAIL_IMAGE_LINK,
        'page_extract': '',
        'url': '',
        'meta_valid': ct.PCOM_META_VALID,
        'sticky': '',
        'unlisted': False
        },
    'assertNotEqual': {}
    },
{   'remark': 'Test Case 2:pcom_process_meta_syntax - title but empty content',
    'input': """
        title={ }:
    """,
    'assertEqual': {\
        'page_title': md.DEFAULT_PAGE_TITLE,
        'page_description': md.DEFAULT_PAGE_DESCRIPTION,
        'authors': md.DEFAULT_AUTHOR,
        'categories': md.DEFAULT_CATEGORY,
        'thumb_link': sch.PM_DEFAULT_THUMBNAIL_IMAGE_LINK,
        'page_extract': '',
        'url': '',
        'meta_valid': ct.PCOM_META_NOT_VALID,
        'sticky': '',
        'unlisted': False
        },
    'assertNotEqual': {}
    },

{   'remark': 'Test Case 3:pcom_process_meta_syntax - title and url but empty content',
    'input': """
        title={ }:
        url={ }:
    """,
    'assertEqual': {\
        'page_title': md.DEFAULT_PAGE_TITLE,
        'page_description': md.DEFAULT_PAGE_DESCRIPTION,
        'authors': md.DEFAULT_AUTHOR,
        'categories': md.DEFAULT_CATEGORY,
        'thumb_link': sch.PM_DEFAULT_THUMBNAIL_IMAGE_LINK,
        'page_extract': '',
        'url': '',
        'meta_valid': ct.PCOM_META_NOT_VALID,
        'sticky': '',
        'unlisted': False
        },
    'assertNotEqual': {}
    },

{   'remark': 'Test Case 4:pcom_process_meta_syntax - title and url not empty',
    'input': """
        title={ A post }:
        url={ /post-post/}:
    """,
    'assertEqual': {\
        'page_title': 'A post',
        'page_description': md.DEFAULT_PAGE_DESCRIPTION,
        'authors': md.DEFAULT_AUTHOR,
        'categories': md.DEFAULT_CATEGORY,
        'thumb_link': sch.PM_DEFAULT_THUMBNAIL_IMAGE_LINK,
        'page_extract': '',
        'url': '/post-post/',
        'meta_valid': ct.PCOM_META_VALID,
        'sticky': '',
        'unlisted': False
        },
    'assertNotEqual': {\
        'page_title': md.DEFAULT_PAGE_TITLE,
        'page_description': md.DEFAULT_PAGE_DESCRIPTION,
        'authors': md.DEFAULT_AUTHOR,
        'categories': md.DEFAULT_CATEGORY,
        'thumb_link': sch.PM_DEFAULT_THUMBNAIL_IMAGE_LINK,
        'page_extract': '',
        'url': '',
        'meta_valid': ct.PCOM_META_NOT_VALID,
        'sticky': '',
        'unlisted': False
        }
    },

{   'remark': 'Test Case 4:pcom_process_meta_syntax - all',
    'input': """
        title={ A post }:
        url={ /post-post/}:
        author={ Bill,Micky }:
        description={ Something to talk about }:
        categories={ this, that, again}:
        thumbnail={ /link-here/ }:
        extract={

        Some text and description of what's going on\\n

        }:
        sticky={}:
        unlisted={}:
    """,
    'assertEqual': {\
        'page_title': 'A post',
        'page_description': 'Something to talk about',
        'authors': 'Bill,Micky',
        'categories': 'this, that, again',
        'thumb_link': '/link-here/',
        'page_extract': "Some text and description of what's going on\\n",
        'url': '/post-post/',
        'meta_valid': ct.PCOM_META_VALID,
        'sticky': 'sticky',
        'unlisted': True
        },
    'assertNotEqual': {\
        'page_title': md.DEFAULT_PAGE_TITLE,
        'page_description': md.DEFAULT_PAGE_DESCRIPTION,
        'authors': md.DEFAULT_AUTHOR,
        'categories': md.DEFAULT_CATEGORY,
        'thumb_link': sch.PM_DEFAULT_THUMBNAIL_IMAGE_LINK,
        'page_extract': '',
        'url': '',
        'meta_valid': ct.PCOM_META_NOT_VALID,
        'sticky': '',
        'unlisted': False
        }
    }
]

test_values_5 = [\
{   'remark': 'Test Case 1:pcom_update_json_based_settings - no_array simple - update does not match any settings ',
    'input': { "1": "thing" },
    'settings_element': { "2" : "box"},
    'json_type': 'no_array',
    'assertEqual': {\
        "2" : "box"
        },
    'assertNotEqual': {\
        "1": "thing"
        }
    },

{   'remark': 'Test Case 2:pcom_update_json_based_settings - no_array simple - update match',
    'input': { "2": "thing" },
    'settings_element': { "2" : "box"},
    'json_type': 'no_array',
    'assertEqual': {\
        "2" : "thing"
        },
    'assertNotEqual': {\
        "2": "box"
        }
    },

{   'remark': 'Test Case 3:pcom_update_json_based_settings - no_array simple - update match with extra',
    'input': {\
        "2": "thing",
        "3": "things"
    },
    'settings_element': { "2" : "box"},
    'json_type': 'no_array',
    'assertEqual': {\
        "2" : "thing"
        },
    'assertNotEqual': {\
        "3": "things"
        }
    },

{   'remark': 'Test Case 4:pcom_update_json_based_settings - no_array simple - update both',
    'input': {\
        "2": "thing",
        "3": "things"
    },
    'settings_element': {\
        "2" : "box",
        "3" : "boxes"
    },
    'json_type': 'no_array',
    'assertEqual': {\
        "2" : "thing",
        "3": "things"
        },
    'assertNotEqual': {\
        "2" : "box",
        "3" : "boxes"
        }
    },

{   'remark': 'Test Case 5:pcom_update_json_based_settings - nested - update both',
    'input': {\
        "2": {
            "3": "thing",
            "4": "things"
        }
    },
    'settings_element': {\
        "2": {
            "3" : "box",
            "4" : "boxes"
        }
    },
    'json_type': 'nested',
    'assertEqual': {\
        "2": {
            "3": "thing",
            "4": "things"
        }
    },
    'assertNotEqual': {\
        "2": {
            "3" : "box",
            "4" : "boxes"
            }
        }
    },

{   'remark': 'Test Case 6:pcom_update_json_based_settings - nested - update does not match by entry',
    'input': {\
        "2": {
            "5": "thing",
            "6": "things"
        }
    },
    'settings_element': {\
        "2": {
            "3" : "box",
            "4" : "boxes"
        }
    },
    'json_type': 'nested',
    'assertEqual': {\
        "2": {
            "3" : "box",
            "4" : "boxes"
        }
    },
    'assertNotEqual': {\
        "2": {
            "5": "thing",
            "6": "things"
        }
        }
    },

{   'remark': 'Test Case 7:pcom_update_json_based_settings - nested - update does not match ',
    'input': {\
        "7": "this"
        },
    'settings_element': {\
        "2": {
            "3" : "box",
            "4" : "boxes"
        }
    },
    'json_type': 'nested',
    'assertEqual': {\
        "2": {
            "3" : "box",
            "4" : "boxes"
        }
    },
    'assertNotEqual': {\
        "7": "this"
        }
    }
]
