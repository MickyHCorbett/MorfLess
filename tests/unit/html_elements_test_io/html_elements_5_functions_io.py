#
import libraries.constants as ct
import libraries.globals as gb
import libraries.schematics as sch

from collections import OrderedDict
#

test_values_1 = [\
{   'remark': 'Test Case 1:pcom_add_post_list_command -  empty syntax',
    'syntax': '',
    'custom_class': '',
    'placement': '',
    'type': '',
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': """


    """
    },
{   'remark': 'Test Case 2:pcom_add_post_list_command -  non empty syntax',
    'syntax': 'something',
    'custom_class': '',
    'placement': '',
    'type': '',
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': """

<div class="pm-post-list-custom clearfix-small">
POSTLIST=[:5:False]:
    </div><!-- end of .pm-post-list -->

    """
    },
{   'remark': 'Test Case 3:pcom_add_post_list_command -  posts_per_page = 4',
    'syntax': 'posts_per_page={ 4 }:',
    'custom_class': '',
    'placement': '',
    'type': '',
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': """

<div class="pm-post-list-custom clearfix-small">
POSTLIST=[:4:False]:
    </div><!-- end of .pm-post-list -->

    """
    },

{   'remark': 'Test Case 3:pcom_add_post_list_command -  list 1',
    'syntax': 'list={ test1.post, test2.page }:',
    'custom_class': '',
    'placement': '',
    'type': '',
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': """

<div class="pm-post-list-custom clearfix-small">
POSTLIST=[test1.post,test2.page:5:False]:
    </div><!-- end of .pm-post-list -->

    """
    },

{   'remark': 'Test Case 4:pcom_add_post_list_command -  list 2 manual sticky',
    'syntax': 'list={ !!test1.post, test2.page }: manual_sticky={}:',
    'custom_class': '',
    'placement': '',
    'type': '',
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': """

<div class="pm-post-list-custom clearfix-small">
POSTLIST=[!!test1.post,test2.page:5:True]:
    </div><!-- end of .pm-post-list -->

    """
    },

{   'remark': 'Test Case 5:pcom_add_post_list_command -  list 3 - title',
    'syntax': 'list={ test3.post, test4.page }: title={ Post List 1 }:',
    'custom_class': '',
    'placement': '',
    'type': '',
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': """

<div class="pm-post-list-custom clearfix-small">
    <div class="pm-title-nav">Post List 1</div><!-- end of .pm-title-nav -->
POSTLIST=[test3.post,test4.page:5:False]:
    </div><!-- end of .pm-post-list -->

    """
    },
]

test_values_2 = [\
{   'remark': 'Test Case 1:pcom_add_post_list_command -  empty syntax',
    'syntax': '',
    'assertEqual': {\
        'title': '',
        'list': '',
        'posts_per_page': '',
        'manual_sticky': 'False'
        }
    },
{   'remark': 'Test Case 2:pcom_add_post_list_command -  list 1 - title',
    'syntax': 'list={ test3.post, test4.page }: title={ Post List 1 }:',
    'assertEqual': {\
        'title': '    <div class="pm-title-nav">Post List 1</div><!-- end of .pm-title-nav -->',
        'list': 'test3.post,test4.page',
        'posts_per_page': '',
        'manual_sticky': 'False'
        }
    },

{   'remark': 'Test Case 3:pcom_add_post_list_command -  manual sticky with arguments',
    'syntax': 'manual_sticky={ Post List 1 }:',
    'assertEqual': {\
        'title': '',
        'list': '',
        'posts_per_page': '',
        'manual_sticky': 'True'
        }
    },

{   'remark': 'Test Case 4:pcom_add_post_list_command -  posts_per_page = 4',
    'syntax': 'posts_per_page={ 4 }:',
    'assertEqual': {\
        'title': '',
        'list': '',
        'posts_per_page': '4',
        'manual_sticky': 'False'
        }
    },
]

test_values_3 = [\
{   'remark': 'Test Case 1:pcom_create_post_list_entry - no manual sticky, post has no sticky',
    'settings': gb.DEFAULT_SETTINGS,
    'list_meta': {\
          "authors": {
            "authors":
                [
                    {
                        "name": "anon",
                        "shortname": "anon",
                        "thumbnail": "/images/Polimorf-shapes-background.jpg",
                        "description": ""
                    }
                ]
           },
          "categories": {
            "categories":
                [
                    {
                        "name": "things",
                        "thumbnail": "/images/Polimorf-shapes-background.jpg",
                        "description": ""
                    }
                ]
            }
    },
    'post': {\
        "index": 1,
        "type": "post",
        "url": "/contact/",
        "title": "Contact",
        "postname": 'contact.post',
        "description": "Morfless Contact page",
        "categories": [
            "things"
        ],
        "authors": [
            "anon"
        ],
        "extract": "Contact Morfless",
        "thumbnail": "/images/Polimorf-shapes-background-2.jpg",
        "creation_date": "12/09/2018",
        "creation_time": "12:18:10",
        "date_modified": "17/06/2020",
        "time_modified": "12:22:06",
        "sticky": ""
    },
    'list_end': False,
    'manual_sticky': False,
    'ignore_meta': False,
    'no_js': False,
    'test_assertNotIn': False,
    'assertIn': [\
        '  <div class="pm-post-content clearfix-small">',
        '    <div class="pm-post-image">',
        '    <a href="/contact/">',
        '      <img src="/images/Polimorf-shapes-background-2.jpg" alt="Contact"  />',
        '    </a></div><!-- end of .pm-post-image -->',
        '    <div class="pm-blog-entry">',
        '      <h2><a href="/contact/">Contact</a></h2>',
        '    <div class="pm-author-category-meta">',
        '      <span class="pm-meta-icon"><i class="fa fa-list" aria-hidden="true"></i></span>',
        '      <a href="/categories/things/" alt="things">things</a>',
        '    </div><!-- end of .pm-author-category-meta -->',
        '    <div class="pm-author-category-meta">',
        '      <span class="pm-meta-icon"><i class="fa fa-user" aria-hidden="true"></i></span>',
        '      <a href="/authors/anon/" alt="anon">anon</a>',
        '    </div><!-- end of .pm-author-category-meta -->',
        '      <p>Contact Morfless</p>',
        '    </div><!-- end of .pm-blog_entry -->',
        "  </div><!-- end of .pm-post-content -->',"
        ]
    },

{   'remark': 'Test Case 2:pcom_create_post_list_entry - no manual sticky, post has sticky, list end',
    'settings': gb.DEFAULT_SETTINGS,
    'list_meta': {\
          "authors": {
            "authors":
                [
                    {
                        "name": "anon",
                        "shortname": "anon",
                        "thumbnail": "/images/Polimorf-shapes-background.jpg",
                        "description": ""
                    }
                ]
           },
          "categories": {
            "categories":
                [
                    {
                        "name": "things",
                        "thumbnail": "/images/Polimorf-shapes-background.jpg",
                        "description": ""
                    }
                ]
            }
    },
    'post': {\
        "index": 1,
        "type": "post",
        "url": "/contact/",
        "title": "Contact",
        "postname": 'contact.post',
        "description": "Morfless Contact page",
        "categories": [
            "things"
        ],
        "authors": [
            "anon"
        ],
        "extract": "Contact Morfless",
        "thumbnail": "/images/Polimorf-shapes-background-2.jpg",
        "creation_date": "12/09/2018",
        "creation_time": "12:18:10",
        "date_modified": "17/06/2020",
        "time_modified": "12:22:06",
        "sticky": "sticky"
    },
    'list_end': True,
    'manual_sticky': False,
    'ignore_meta': False,
    'no_js': False,
    'test_assertNotIn': False,
    'assertIn': [\
        '  <div class="pm-post-content clearfix-small">\\',
        '    <div class="pm-post-image">\\',
        '    <a href="/contact/">',
        '      <img src="/images/Polimorf-shapes-background-2.jpg" alt="Contact"  />',
        '    </a></div><!-- end of .pm-post-image -->',
        '    <div class="pm-blog-entry sticky">',
        '      <h2><a href="/contact/">Contact</a></h2>',
        '    <div class="pm-author-category-meta">',
        '      <span class="pm-meta-icon"><i class="fa fa-list" aria-hidden="true"></i></span>',
        '      <a href="/categories/things/" alt="things">things</a>',
        '    </div><!-- end of .pm-author-category-meta -->',
        '    <div class="pm-author-category-meta">',
        '      <span class="pm-meta-icon"><i class="fa fa-user" aria-hidden="true"></i></span>',
        '      <a href="/authors/anon/" alt="anon">anon</a>',
        '    </div><!-- end of .pm-author-category-meta -->',
        '      <p>Contact Morfless</p>',
        '    </div><!-- end of .pm-blog_entry -->',
        "  </div><!-- end of .pm-post-content -->'"
        ]
    },

{   'remark': 'Test Case 3:pcom_create_post_list_entry - no manual sticky, post has sticky, list end. no_js',
    'settings': gb.DEFAULT_SETTINGS,
    'list_meta': {\
          "authors": {
            "authors":
                [
                    {
                        "name": "anon",
                        "shortname": "anon",
                        "thumbnail": "/images/Polimorf-shapes-background.jpg",
                        "description": ""
                    }
                ]
           },
          "categories": {
            "categories":
                [
                    {
                        "name": "things",
                        "thumbnail": "/images/Polimorf-shapes-background.jpg",
                        "description": ""
                    }
                ]
            }
    },
    'post': {\
        "index": 1,
        "type": "post",
        "url": "/contact/",
        "title": "Contact",
        "postname": 'contact.post',
        "description": "Morfless Contact page",
        "categories": [
            "things"
        ],
        "authors": [
            "anon"
        ],
        "extract": "Contact Morfless",
        "thumbnail": "/images/Polimorf-shapes-background-2.jpg",
        "creation_date": "12/09/2018",
        "creation_time": "12:18:10",
        "date_modified": "17/06/2020",
        "time_modified": "12:22:06",
        "sticky": "sticky"
    },
    'list_end': True,
    'manual_sticky': False,
    'ignore_meta': False,
    'no_js': True,
    'test_assertNotIn': False,
    'assertIn': [\
        '  <div class="pm-post-content clearfix-small">',
        '    <div class="pm-post-image">',
        '    <a href="/contact/">',
        '      <img src="/images/Polimorf-shapes-background-2.jpg" alt="Contact"  />',
        '    </a></div><!-- end of .pm-post-image -->',
        '    <div class="pm-blog-entry sticky">',
        '      <h2><a href="/contact/">Contact</a></h2>',
        '    <div class="pm-author-category-meta">',
        '      <span class="pm-meta-icon"><i class="fa fa-list" aria-hidden="true"></i></span>',
        '      <a href="/categories/things/" alt="things">things</a>',
        '    </div><!-- end of .pm-author-category-meta -->',
        '    <div class="pm-author-category-meta">',
        '      <span class="pm-meta-icon"><i class="fa fa-user" aria-hidden="true"></i></span>',
        '      <a href="/authors/anon/" alt="anon">anon</a>',
        '    </div><!-- end of .pm-author-category-meta -->',
        '      <p>Contact Morfless</p>',
        '    </div><!-- end of .pm-blog_entry -->',
        "  </div><!-- end of .pm-post-content -->'"
        ]
    },

{   'remark': 'Test Case 4:pcom_create_post_list_entry - no manual sticky, post has sticky, list end, no_js, ignore meta',
    'settings': gb.DEFAULT_SETTINGS,
    'list_meta': {\
          "authors": {
            "authors":
                [
                    {
                        "name": "anon",
                        "shortname": "anon",
                        "thumbnail": "/images/Polimorf-shapes-background.jpg",
                        "description": ""
                    }
                ]
           },
          "categories": {
            "categories":
                [
                    {
                        "name": "things",
                        "thumbnail": "/images/Polimorf-shapes-background.jpg",
                        "description": ""
                    }
                ]
            }
    },
    'post': {\
        "index": 1,
        "type": "post",
        "url": "/contact/",
        "title": "Contact",
        "postname": 'contact.post',
        "description": "Morfless Contact page",
        "categories": [
            "things"
        ],
        "authors": [
            "anon"
        ],
        "extract": "Contact Morfless",
        "thumbnail": "/images/Polimorf-shapes-background-2.jpg",
        "creation_date": "12/09/2018",
        "creation_time": "12:18:10",
        "date_modified": "17/06/2020",
        "time_modified": "12:22:06",
        "sticky": "sticky"
    },
    'list_end': True,
    'manual_sticky': False,
    'ignore_meta': True,
    'no_js': True,
    'test_assertNotIn': False,
    'assertIn': [\
        '  <div class="pm-post-content clearfix-small">',
        '    <div class="pm-post-image">',
        '    <a href="/contact/">',
        '      <img src="/images/Polimorf-shapes-background-2.jpg" alt="Contact"  />',
        '    </a></div><!-- end of .pm-post-image -->',
        '    <div class="pm-blog-entry">',
        '      <h2><a href="/contact/">Contact</a></h2>',
        '    <div class="pm-author-category-meta">',
        '      <span class="pm-meta-icon"><i class="fa fa-list" aria-hidden="true"></i></span>',
        '      <a href="/categories/things/" alt="things">things</a>',
        '    </div><!-- end of .pm-author-category-meta -->',
        '    <div class="pm-author-category-meta">',
        '      <span class="pm-meta-icon"><i class="fa fa-user" aria-hidden="true"></i></span>',
        '      <a href="/authors/anon/" alt="anon">anon</a>',
        '    </div><!-- end of .pm-author-category-meta -->',
        '      <p>Contact Morfless</p>',
        '    </div><!-- end of .pm-blog_entry -->',
        "  </div><!-- end of .pm-post-content -->'"
        ]
    },

{   'remark': 'Test Case 5:pcom_create_post_list_entry - manual sticky, post has sticky, list end, no_js, ignore meta',
    'settings': gb.DEFAULT_SETTINGS,
    'list_meta': {\
          "authors": {
            "authors":
                [
                    {
                        "name": "anon",
                        "shortname": "anon",
                        "thumbnail": "/images/Polimorf-shapes-background.jpg",
                        "description": ""
                    }
                ]
           },
          "categories": {
            "categories":
                [
                    {
                        "name": "things",
                        "thumbnail": "/images/Polimorf-shapes-background.jpg",
                        "description": ""
                    }
                ]
            }
    },
    'post': {\
        "index": 1,
        "type": "post",
        "url": "/contact/",
        "title": "Contact",
        "postname": 'contact.post',
        "description": "Morfless Contact page",
        "categories": [
            "things"
        ],
        "authors": [
            "anon"
        ],
        "extract": "Contact Morfless",
        "thumbnail": "/images/Polimorf-shapes-background-2.jpg",
        "creation_date": "12/09/2018",
        "creation_time": "12:18:10",
        "date_modified": "17/06/2020",
        "time_modified": "12:22:06",
        "sticky": "sticky"
    },
    'list_end': True,
    'manual_sticky': True,
    'ignore_meta': True,
    'no_js': True,
    'test_assertNotIn': False,
    'assertIn': [\
        '  <div class="pm-post-content clearfix-small">',
        '    <div class="pm-post-image">',
        '    <a href="/contact/">',
        '      <img src="/images/Polimorf-shapes-background-2.jpg" alt="Contact"  />',
        '    </a></div><!-- end of .pm-post-image -->',
        '    <div class="pm-blog-entry sticky">',
        '      <h2><a href="/contact/">Contact</a></h2>',
        '    <div class="pm-author-category-meta">',
        '      <span class="pm-meta-icon"><i class="fa fa-list" aria-hidden="true"></i></span>',
        '      <a href="/categories/things/" alt="things">things</a>',
        '    </div><!-- end of .pm-author-category-meta -->',
        '    <div class="pm-author-category-meta">',
        '      <span class="pm-meta-icon"><i class="fa fa-user" aria-hidden="true"></i></span>',
        '      <a href="/authors/anon/" alt="anon">anon</a>',
        '    </div><!-- end of .pm-author-category-meta -->',
        '      <p>Contact Morfless</p>',
        '    </div><!-- end of .pm-blog_entry -->',
        "  </div><!-- end of .pm-post-content -->'"
        ]
    },

{   'remark': 'Test Case 6:pcom_create_post_list_entry - manual sticky, post has sticky, list end, no_js, ignore meta - no post thumbnai',
    'settings': gb.DEFAULT_SETTINGS,
    'list_meta': {\
          "authors": {
            "authors":
                [
                    {
                        "name": "anon",
                        "shortname": "anon",
                        "thumbnail": "/images/Polimorf-shapes-background.jpg",
                        "description": ""
                    }
                ]
           },
          "categories": {
            "categories":
                [
                    {
                        "name": "things",
                        "thumbnail": "/images/Polimorf-shapes-background.jpg",
                        "description": ""
                    }
                ]
            }
    },
    'post': {\
        "index": 1,
        "type": "post",
        "url": "/contact/",
        "title": "Contact",
        "postname": 'contact.post',
        "description": "Morfless Contact page",
        "categories": [
            "things"
        ],
        "authors": [
            "anon"
        ],
        "extract": "Contact Morfless",
        "thumbnail": "",
        "creation_date": "12/09/2018",
        "creation_time": "12:18:10",
        "date_modified": "17/06/2020",
        "time_modified": "12:22:06",
        "sticky": "sticky"
    },
    'list_end': True,
    'manual_sticky': True,
    'ignore_meta': True,
    'no_js': True,
    'test_assertNotIn': False,
    'assertIn': [\
        '  <div class="pm-post-content clearfix-small">',
        '    <div class="pm-post-image">',
        '    <a href="/contact/">',
        '      <img src="' + sch.PM_DEFAULT_THUMBNAIL_IMAGE_LINK + '" alt="Contact"  />',
        '    </a></div><!-- end of .pm-post-image -->',
        '    <div class="pm-blog-entry sticky">',
        '      <h2><a href="/contact/">Contact</a></h2>',
        '    <div class="pm-author-category-meta">',
        '      <span class="pm-meta-icon"><i class="fa fa-list" aria-hidden="true"></i></span>',
        '      <a href="/categories/things/" alt="things">things</a>',
        '    </div><!-- end of .pm-author-category-meta -->',
        '    <div class="pm-author-category-meta">',
        '      <span class="pm-meta-icon"><i class="fa fa-user" aria-hidden="true"></i></span>',
        '      <a href="/authors/anon/" alt="anon">anon</a>',
        '    </div><!-- end of .pm-author-category-meta -->',
        '      <p>Contact Morfless</p>',
        '    </div><!-- end of .pm-blog_entry -->',
        "  </div><!-- end of .pm-post-content -->'"
        ]
    },

{   'remark': 'Test Case 7:pcom_create_post_list_entry - page, manual sticky, post has sticky, list end, no_js, ignore meta - no post thumbnai',
    'settings': gb.DEFAULT_SETTINGS,
    'list_meta': {\
          "authors": {
            "authors":
                [
                    {
                        "name": "anon",
                        "shortname": "anon",
                        "thumbnail": "/images/Polimorf-shapes-background.jpg",
                        "description": ""
                    }
                ]
           },
          "categories": {
            "categories":
                [
                    {
                        "name": "things",
                        "thumbnail": "/images/Polimorf-shapes-background.jpg",
                        "description": ""
                    }
                ]
            }
    },
    'post': {\
        "index": 1,
        "type": "page",
        "url": "/contact/",
        "title": "Contact",
        "postname": 'contact.page',
        "description": "Morfless Contact page",
        "categories": [
            "things"
        ],
        "authors": [
            "anon"
        ],
        "extract": "Contact Morfless",
        "thumbnail": "",
        "creation_date": "12/09/2018",
        "creation_time": "12:18:10",
        "date_modified": "17/06/2020",
        "time_modified": "12:22:06",
        "sticky": "sticky"
    },
    'list_end': True,
    'manual_sticky': True,
    'ignore_meta': True,
    'no_js': True,
    'test_assertNotIn': True,
    'assertIn': [\
        '  <div class="pm-post-content clearfix-small">',
        '    <div class="pm-post-image">',
        '    <a href="/contact/">',
        '      <img src="' + sch.PM_DEFAULT_THUMBNAIL_IMAGE_LINK + '" alt="Contact"  />',
        '    </a></div><!-- end of .pm-post-image -->',
        '    <div class="pm-blog-entry sticky">',
        '      <h2><a href="/contact/">Contact</a></h2>',
        '    <div class="pm-author-category-meta">',
        '      <span class="pm-meta-icon"><i class="fa fa-user" aria-hidden="true"></i></span>',
        '      <a href="/authors/anon/" alt="anon">anon</a>',
        '    </div><!-- end of .pm-author-category-meta -->',
        '      <p>Contact Morfless</p>',
        '    </div><!-- end of .pm-blog_entry -->',
        "  </div><!-- end of .pm-post-content -->'"
        ],
    'assertNotIn': [\
        '      <span class="pm-meta-icon"><i class="fa fa-list" aria-hidden="true"></i></span>',
        '      <a href="/categories/things/" alt="things">things</a>',
        ]

    },
]

test_values_4 = [\
{   'remark': 'Test Case 1:pcom_create_search_post_list_entry - post has no sticky',
    'settings': gb.DEFAULT_SETTINGS,
    'list_meta': {\
          "authors": {
            "authors":
                [
                    {
                        "name": "anon",
                        "shortname": "anon",
                        "thumbnail": "/images/Polimorf-shapes-background.jpg",
                        "description": ""
                    }
                ]
           },
          "categories": {
            "categories":
                [
                    {
                        "name": "things",
                        "thumbnail": "/images/Polimorf-shapes-background.jpg",
                        "description": ""
                    }
                ]
            }
    },
    'post_search': {\
        "index": 1,
        "type": "post",
        "url": "/contact/",
        "title": "Contact",
        "postname": 'contact.post',
        "description": "Morfless Contact page",
        "categories": [
            "things"
        ],
        "authors": [
            "anon"
        ],
        "extract": "Contact Morfless",
        "thumbnail": "/images/Polimorf-shapes-background-2.jpg",
        "creation_date": "12/09/2018",
        "creation_time": "12:18:10",
        "date_modified": "17/06/2020",
        "time_modified": "12:22:06",
        "sticky": "sticky"
    },
    'ignore_meta': False,
    'test_assertNotIn': False,
    'assertIn': [\
        '  <div class="pm-post-content clearfix-small">',
        '    <div class="pm-post-image">',
        '    <a href="/contact/">',
        '      <img src="/images/Polimorf-shapes-background-2.jpg" alt="Contact"  />',
        '    </a></div><!-- end of .pm-post-image -->',
        '    <div class="pm-blog-entry sticky">',
        '      <h2><a href="/contact/">Contact</a></h2>',
        '    <div class="pm-author-category-meta">',
        '      <span class="pm-meta-icon"><i class="fa fa-list" aria-hidden="true"></i></span>',
        '      <a href="/categories/things/" alt="things">things</a>',
        '    </div><!-- end of .pm-author-category-meta -->',
        '    <div class="pm-author-category-meta">',
        '      <span class="pm-meta-icon"><i class="fa fa-user" aria-hidden="true"></i></span>',
        '      <a href="/authors/anon/" alt="anon">anon</a>',
        '    </div><!-- end of .pm-author-category-meta -->',
        '      <p>Contact Morfless</p>',
        '    </div><!-- end of .pm-blog_entry -->',
        '  </div><!-- end of .pm-post-content -->'
        ]
    },

{   'remark': 'Test Case 2:pcom_create_search_post_list_entry - page has no sticky, ignore meta',
    'settings': gb.DEFAULT_SETTINGS,
    'list_meta': {\
          "authors": {
            "authors":
                [
                    {
                        "name": "anon",
                        "shortname": "anon",
                        "thumbnail": "/images/Polimorf-shapes-background.jpg",
                        "description": ""
                    }
                ]
           },
          "categories": {
            "categories":
                [
                    {
                        "name": "things",
                        "thumbnail": "/images/Polimorf-shapes-background.jpg",
                        "description": ""
                    }
                ]
            }
    },
    'post_search': {\
        "index": 1,
        "type": "page",
        "url": "/contact/",
        "title": "Contact",
        "postname": 'contact.post',
        "description": "Morfless Contact page",
        "categories": [
            "things"
        ],
        "authors": [
            "anon"
        ],
        "extract": "Contact Morfless",
        "thumbnail": "/images/Polimorf-shapes-background-2.jpg",
        "creation_date": "12/09/2018",
        "creation_time": "12:18:10",
        "date_modified": "17/06/2020",
        "time_modified": "12:22:06",
        "sticky": ""
    },
    'ignore_meta': True,
    'test_assertNotIn': True,
    'assertIn': [\
        '  <div class="pm-post-content clearfix-small">',
        '    <div class="pm-post-image">',
        '    <a href="/contact/">',
        '      <img src="/images/Polimorf-shapes-background-2.jpg" alt="Contact"  />',
        '    </a></div><!-- end of .pm-post-image -->',
        '    <div class="pm-blog-entry">',
        '      <h2><a href="/contact/">Contact</a></h2>',
        '    <div class="pm-author-category-meta">',
        '      <span class="pm-meta-icon"><i class="fa fa-user" aria-hidden="true"></i></span>',
        '      <a href="/authors/anon/" alt="anon">anon</a>',
        '    </div><!-- end of .pm-author-category-meta -->',
        '      <p>Contact Morfless</p>',
        '    </div><!-- end of .pm-blog_entry -->',
        '  </div><!-- end of .pm-post-content -->'
        ],
    'assertNotIn': [\
        '      <span class="pm-meta-icon"><i class="fa fa-list" aria-hidden="true"></i></span>',
        '      <a href="/categories/things/" alt="things">things</a>',
        ]
    },

{   'remark': 'Test Case 3:pcom_create_search_post_list_entry - page has no sticky, ignore meta, no thumbnail',
    'settings': gb.DEFAULT_SETTINGS,
    'list_meta': {\
          "authors": {
            "authors":
                [
                    {
                        "name": "anon",
                        "shortname": "anon",
                        "thumbnail": "/images/Polimorf-shapes-background.jpg",
                        "description": ""
                    }
                ]
           },
          "categories": {
            "categories":
                [
                    {
                        "name": "things",
                        "thumbnail": "/images/Polimorf-shapes-background.jpg",
                        "description": ""
                    }
                ]
            }
    },
    'post_search': {\
        "index": 1,
        "type": "page",
        "url": "/contact/",
        "title": "Contact",
        "postname": 'contact.post',
        "description": "Morfless Contact page",
        "categories": [
            "things"
        ],
        "authors": [
            "anon"
        ],
        "extract": "Contact Morfless",
        "thumbnail": "",
        "creation_date": "12/09/2018",
        "creation_time": "12:18:10",
        "date_modified": "17/06/2020",
        "time_modified": "12:22:06",
        "sticky": ""
    },
    'ignore_meta': True,
    'test_assertNotIn': True,
    'assertIn': [\
        '  <div class="pm-post-content clearfix-small">',
        '    <div class="pm-post-image">',
        '    <a href="/contact/">',
        '      <img src="'+ sch.PM_DEFAULT_THUMBNAIL_IMAGE_LINK + '" alt="Contact"  />',
        '    </a></div><!-- end of .pm-post-image -->',
        '    <div class="pm-blog-entry">',
        '      <h2><a href="/contact/">Contact</a></h2>',
        '    <div class="pm-author-category-meta">',
        '      <span class="pm-meta-icon"><i class="fa fa-user" aria-hidden="true"></i></span>',
        '      <a href="/authors/anon/" alt="anon">anon</a>',
        '    </div><!-- end of .pm-author-category-meta -->',
        '      <p>Contact Morfless</p>',
        '    </div><!-- end of .pm-blog_entry -->',
        '  </div><!-- end of .pm-post-content -->'
        ],
    'assertNotIn': [\
        '      <span class="pm-meta-icon"><i class="fa fa-list" aria-hidden="true"></i></span>',
        '      <a href="/categories/things/" alt="things">things</a>',
        ]
    },
]

test_values_5 = [\
{   'remark': 'Test Case 1:pcom_create_search_post_list_entry - url and entry, not list end and not no_js',
    'settings': gb.DEFAULT_SETTINGS,
    'url': 'something/here/link',
    'entry': {\
        'name': 'An entry',
        'thumbnail': 'image.png',
        'description': 'Something to read',
    },
    'no_js': False,
    'list_end': False,
    'test_assertNotIn': False,
    'assertIn': [\
        '  <div class="pm-post-content clearfix-small">\\',
        '    <div class="pm-post-image">\\',
        '    <a href="something/here/link">\\',
        '      <img src="image.png" alt="An-entry"  />\\',
        '    </a></div><!-- end of .pm-post-image -->\\',
        '    <div class="pm-blog-entry">\\',
        '      <h2><a href="something/here/link">An entry</a></h2>\\',
        '      <p>Something to read</p>\\',
        '    </div><!-- end of .pm-blog_entry -->\\',
        "  </div><!-- end of .pm-post-content -->',"
        ]
    },

{   'remark': 'Test Case 2:pcom_create_search_post_list_entry - url and entry, list end and no_js',
    'settings': gb.DEFAULT_SETTINGS,
    'url': 'something/here/links',
    'entry': {\
        'name': 'An entry 2',
        'thumbnail': 'image2.png',
        'description': 'Something to read 2',
    },
    'no_js': True,
    'list_end': True,
    'test_assertNotIn': False,
    'assertIn': [\
        '  <div class="pm-post-content clearfix-small">',
        '    <div class="pm-post-image">',
        '    <a href="something/here/links">',
        '      <img src="image2.png" alt="An-entry-2"  />',
        '    </a></div><!-- end of .pm-post-image -->',
        '    <div class="pm-blog-entry">',
        '      <h2><a href="something/here/links">An entry 2</a></h2>',
        '      <p>Something to read 2</p>',
        '    </div><!-- end of .pm-blog_entry -->',
        "  </div><!-- end of .pm-post-content -->'"
        ]
    },

{   'remark': 'Test Case 2:pcom_create_search_post_list_entry - url and entry, list end and no_js, thumbnail empty',
    'settings': gb.DEFAULT_SETTINGS,
    'url': 'something/here/links',
    'entry': {\
        'name': 'An entry 2',
        'thumbnail': '',
        'description': 'Something to read 2',
    },
    'no_js': True,
    'list_end': True,
    'test_assertNotIn': False,
    'assertIn': [\
        '  <div class="pm-post-content clearfix-small">',
        '    <div class="pm-post-image">',
        '    <a href="something/here/links">',
        '      <img src="'+ sch.PM_DEFAULT_THUMBNAIL_IMAGE_LINK + '" alt="An-entry-2"  />',
        '    </a></div><!-- end of .pm-post-image -->',
        '    <div class="pm-blog-entry">',
        '      <h2><a href="something/here/links">An entry 2</a></h2>',
        '      <p>Something to read 2</p>',
        '    </div><!-- end of .pm-blog_entry -->',
        "  </div><!-- end of .pm-post-content -->'"
        ]
    },

]

test_values_6 = [\
{   'remark': 'Test Case 1:pcom_create_template_search_list_entry - url and entry, thumbnail empty',
    'settings': gb.DEFAULT_SETTINGS,
    'url': 'something/here/links',
    'entry': {\
        'name': 'An entry 2',
        'thumbnail': '',
        'description': 'Something to read 2',
    },
    'assertIn': [\
        '  <div class="pm-post-content clearfix-small">',
        '    <div class="pm-post-image">',
        '    <a href="something/here/links">',
        '      <img src="'+ sch.PM_DEFAULT_THUMBNAIL_IMAGE_LINK + '" alt="An-entry-2"  />',
        '    </a></div><!-- end of .pm-post-image -->',
        '    <div class="pm-blog-entry">',
        '      <h2><a href="something/here/links">An entry 2</a></h2>',
        '      <p>Something to read 2</p>',
        '    </div><!-- end of .pm-blog_entry -->',
        "  </div><!-- end of .pm-post-content -->"
        ]
    },

{   'remark': 'Test Case 2:pcom_create_template_search_list_entry - url and entry, thumbnail',
    'settings': gb.DEFAULT_SETTINGS,
    'url': 'something/here/link',
    'entry': {\
        'name': 'An entry',
        'thumbnail': 'image2.jpg',
        'description': 'Something to read',
    },
    'assertIn': [\
        '  <div class="pm-post-content clearfix-small">',
        '    <div class="pm-post-image">',
        '    <a href="something/here/link">',
        '      <img src="image2.jpg" alt="An-entry"  />',
        '    </a></div><!-- end of .pm-post-image -->',
        '    <div class="pm-blog-entry">',
        '      <h2><a href="something/here/link">An entry</a></h2>',
        '      <p>Something to read</p>',
        '    </div><!-- end of .pm-blog_entry -->',
        "  </div><!-- end of .pm-post-content -->"
        ]
    },
]

test_values_7 = [\
{   'remark': 'Test Case 1:pcom_create_archive_entry',
    'settings': gb.DEFAULT_SETTINGS,
    'base_name': 'something/here',
    'entry': {\
        'name': '09-088',
    },
    'assertIn': [\
        '<p class="pm-archive-links"><a href="/something/here/09-088">09-088</a></p>\\'
        ]
    },
]

test_values_8 = [\
{   'remark': 'Test Case 1:pcom_insert_content_meta_data - authors',
    'settings': gb.DEFAULT_SETTINGS,
    'type': 'authors',
    'list_meta_array': [\
            {
                "name": "anonymous",
                "shortname": "anon",
                "thumbnail": "/images/Polimorf-shapes-background.jpg",
                "description": ""
            },
            {
                "name": "Jack O'Reilly'",
                "shortname": "myname",
                "thumbnail": "/images/Polimorf-shapes-background.jpg",
                "description": ""
            }
    ],
    'post': {\
        "index": 1,
        "type": "post",
        "url": "/contact/",
        "title": "Contact",
        "postname": 'contact.post',
        "description": "Morfless Contact page",
        "categories": [
            "things",
            "other things"
        ],
        "authors": [
            "anon",
            "myname"
        ],
        "extract": "Contact Morfless",
        "thumbnail": "/images/Polimorf-shapes-background-2.jpg",
        "creation_date": "12/09/2018",
        "creation_time": "12:18:10",
        "date_modified": "17/06/2020",
        "time_modified": "12:22:06",
        "sticky": ""
    },
    'add_escape': False,
    'no_js': False,
    'assertEqual': """

        <div class="pm-author-category-meta">\\
          <span class="pm-meta-icon"><i class="fa fa-user" aria-hidden="true"></i></span>\\
          <a href="/authors/anonymous/" alt="anonymous">anonymous</a>,&nbsp;\\
          <a href="/authors/jack-o-reilly-/" alt="jack-o-reilly-">Jack O&#39;Reilly&#39;</a>\\
        </div><!-- end of .pm-author-category-meta -->

    """
    },

{   'remark': 'Test Case 2:pcom_insert_content_meta_data - authors - add escape',
    'settings': gb.DEFAULT_SETTINGS,
    'type': 'authors',
    'list_meta_array': [\
            {
                "name": "anonymous",
                "shortname": "anon",
                "thumbnail": "/images/Polimorf-shapes-background.jpg",
                "description": ""
            },
            {
                "name": "Jack O'Reilly'",
                "shortname": "myname",
                "thumbnail": "/images/Polimorf-shapes-background.jpg",
                "description": ""
            }
    ],
    'post': {\
        "index": 1,
        "type": "post",
        "url": "/contact/",
        "title": "Contact",
        "postname": 'contact.post',
        "description": "Morfless Contact page",
        "categories": [
            "things",
            "other things"
        ],
        "authors": [
            "anon",
            "myname"
        ],
        "extract": "Contact Morfless",
        "thumbnail": "/images/Polimorf-shapes-background-2.jpg",
        "creation_date": "12/09/2018",
        "creation_time": "12:18:10",
        "date_modified": "17/06/2020",
        "time_modified": "12:22:06",
        "sticky": ""
    },
    'add_escape': True,
    'no_js': False,
    'assertEqual': """

        <div class="pm-author-category-meta">\\
          <span class="pm-meta-icon"><i class="fa fa-user" aria-hidden="true"></i></span>\\
          <a href="/authors/anonymous/" alt="anonymous">anonymous</a>,&nbsp;\\
          <a href="/authors/jack-o-reilly-/" alt="jack-o-reilly-">Jack O&#39;Reilly&#39;</a>\\
        </div><!-- end of .pm-author-category-meta -->\\

    """
    },

{   'remark': 'Test Case 3:pcom_insert_content_meta_data - authors - add escape, no_js',
    'settings': gb.DEFAULT_SETTINGS,
    'type': 'authors',
    'list_meta_array': [\
            {
                "name": "anonymous",
                "shortname": "anon",
                "thumbnail": "/images/Polimorf-shapes-background.jpg",
                "description": ""
            },
            {
                "name": "Jack O'Reilly'",
                "shortname": "myname",
                "thumbnail": "/images/Polimorf-shapes-background.jpg",
                "description": ""
            }
    ],
    'post': {\
        "index": 1,
        "type": "post",
        "url": "/contact/",
        "title": "Contact",
        "postname": 'contact.post',
        "description": "Morfless Contact page",
        "categories": [
            "things",
            "other things"
        ],
        "authors": [
            "anon",
            "myname"
        ],
        "extract": "Contact Morfless",
        "thumbnail": "/images/Polimorf-shapes-background-2.jpg",
        "creation_date": "12/09/2018",
        "creation_time": "12:18:10",
        "date_modified": "17/06/2020",
        "time_modified": "12:22:06",
        "sticky": ""
    },
    'add_escape': True,
    'no_js': True,
    'assertEqual': """

        <div class="pm-author-category-meta">
          <span class="pm-meta-icon"><i class="fa fa-user" aria-hidden="true"></i></span>
          <a href="/authors/anonymous/" alt="anonymous">anonymous</a>,&nbsp;
          <a href="/authors/jack-o-reilly-/" alt="jack-o-reilly-">Jack O&#39;Reilly&#39;</a>
        </div><!-- end of .pm-author-category-meta -->\\

    """
    },

{   'remark': 'Test Case 4:pcom_insert_content_meta_data - categories - add escape, no_js',
    'settings': gb.DEFAULT_SETTINGS,
    'type': 'categories',
    'list_meta_array': [\
            {
                "name": "anonymous",
                "shortname": "anon",
                "thumbnail": "/images/Polimorf-shapes-background.jpg",
                "description": ""
            },
            {
                "name": "Jack O'Reilly'",
                "shortname": "myname",
                "thumbnail": "/images/Polimorf-shapes-background.jpg",
                "description": ""
            }
    ],
    'post': {\
        "index": 1,
        "type": "post",
        "url": "/contact/",
        "title": "Contact",
        "postname": 'contact.post',
        "description": "Morfless Contact page",
        "categories": [
            "things",
            "other things"
        ],
        "authors": [
            "anon",
            "myname"
        ],
        "extract": "Contact Morfless",
        "thumbnail": "/images/Polimorf-shapes-background-2.jpg",
        "creation_date": "12/09/2018",
        "creation_time": "12:18:10",
        "date_modified": "17/06/2020",
        "time_modified": "12:22:06",
        "sticky": ""
    },
    'add_escape': True,
    'no_js': True,
    'assertEqual': """

        <div class="pm-author-category-meta">
          <span class="pm-meta-icon"><i class="fa fa-list" aria-hidden="true"></i></span>
          <a href="/categories/things/" alt="things">things</a>,&nbsp;
          <a href="/categories/other-things/" alt="other-things">other things</a>
        </div><!-- end of .pm-author-category-meta -->\\

    """
    },

{   'remark': 'Test Case 5:pcom_insert_content_meta_data - categories (no entries) - add escape, no_js',
    'settings': gb.DEFAULT_SETTINGS,
    'type': 'categories',
    'list_meta_array': [\
            {
                "name": "anonymous",
                "shortname": "anon",
                "thumbnail": "/images/Polimorf-shapes-background.jpg",
                "description": ""
            },
            {
                "name": "Jack O'Reilly'",
                "shortname": "myname",
                "thumbnail": "/images/Polimorf-shapes-background.jpg",
                "description": ""
            }
    ],
    'post': {\
        "index": 1,
        "type": "post",
        "url": "/contact/",
        "title": "Contact",
        "postname": 'contact.post',
        "description": "Morfless Contact page",
        "categories": [
        ],
        "authors": [
            "anon",
            "myname"
        ],
        "extract": "Contact Morfless",
        "thumbnail": "/images/Polimorf-shapes-background-2.jpg",
        "creation_date": "12/09/2018",
        "creation_time": "12:18:10",
        "date_modified": "17/06/2020",
        "time_modified": "12:22:06",
        "sticky": ""
    },
    'add_escape': True,
    'no_js': True,
    'assertEqual': """


    """
    },
]
