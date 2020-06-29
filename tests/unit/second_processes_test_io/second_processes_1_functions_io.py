#
import libraries.constants as ct
import libraries.globals as gb
import libraries.schematics as sch

from unit.second_processes_test_io.second_processes_supplemental import LIST_META_1
from unit.second_processes_test_io.second_processes_supplemental import POSTLIST_1
from unit.second_processes_test_io.second_processes_supplemental import ARCHIVE_1

from collections import OrderedDict
#

test_values_1 = [\
{   'remark': 'Test Case 1:pcom_process_postlist - empty postlist info',
    'postlist_info': [],
    'postlist': [],
    'settings': gb.DEFAULT_SETTINGS,
    'list_meta': LIST_META_1,
    'fileroot': 'test5',
    'assertEqual': {\
        'result': ct.PCOM_NO_ENTRY,
        'processed': False
        }
    },

{   'remark': 'Test Case 2:pcom_process_postlist - postlist info no posts',
    'postlist_info': [\
            {
                "index": 68,
                "fileroot": "test1",
                "ppp": "5",
                "manual_sticky": "False",
                "content": ""
            }
    ],
    'postlist': POSTLIST_1,
    'settings': gb.DEFAULT_SETTINGS,
    'list_meta': LIST_META_1,
    'fileroot': 'test5',
    'assertEqual': {\
        'processed': True,
        'result': """

window._postlist_test5 = {
  identifier: 'postlist-list-',
  pagination_element: '        <span class="pm-page-numbers %%$_NUMBERIDENT_$%%">%%$_NUMBER_$%%</span>',
  page_numbers_selected_class: 'current',
  pagination_class: 'pm-postlist-pagination',
  pagination_selector_id: '-pm-page-numbers',
  pagination_number_sub: '%%$_NUMBER_$%%',
  pagination_number_ident: '%%$_NUMBERIDENT_$%%',
  entries: [
  {
    posts_per_page: 5,
    posts: [
    ],
    sticky: [
    ]
  }
  ]
};

        """
        }
    },

{   'remark': 'Test Case 3:pcom_process_postlist - postlist info with posts',
    'postlist_info': [\
            {
                "index": 68,
                "fileroot": "test1",
                "ppp": "5",
                "manual_sticky": "False",
                "content": "about.page,test1.post"
            }
    ],
    'postlist': POSTLIST_1,
    'settings': gb.DEFAULT_SETTINGS,
    'list_meta': LIST_META_1,
    'fileroot': 'test5',
    'assertEqual': {\
        'processed': True,
        'result': """

window._postlist_test5 = {
  identifier: 'postlist-list-',
  pagination_element: '        <span class="pm-page-numbers %%$_NUMBERIDENT_$%%">%%$_NUMBER_$%%</span>',
  page_numbers_selected_class: 'current',
  pagination_class: 'pm-postlist-pagination',
  pagination_selector_id: '-pm-page-numbers',
  pagination_number_sub: '%%$_NUMBER_$%%',
  pagination_number_ident: '%%$_NUMBERIDENT_$%%',
  entries: [
  {
    posts_per_page: 5,
    posts: [
      '\\
            <div class="pm-post-content clearfix-small">\\
              <div class="pm-post-image">\\
              <a href="/about/">\\
                <img src="/images/Polimorf-shapes-background.jpg" alt="About Morfless"  />\\
              </a></div><!-- end of .pm-post-image -->\\
              <div class="pm-blog-entry">\\
                <h2><a href="/about/">About Morfless</a></h2>\\
              <div class="pm-author-category-meta">\\
                <span class="pm-meta-icon"><i class="fa fa-user" aria-hidden="true"></i></span>\\
                <a href="/authors/jim-o-neill/" alt="jim-o-neill">Jim O&#39;Neill</a>\\
              </div><!-- end of .pm-author-category-meta -->\\
                <p>An about page - describe yourself in as much detail as you like!<br/>You can also add more to this extract.</p>\\
              </div><!-- end of .pm-blog_entry -->\\
            </div><!-- end of .pm-post-content -->',
      '\\
            <div class="pm-post-content clearfix-small">\\
              <div class="pm-post-image">\\
              <a href="/test1-the-first-post/">\\
                <img src="/images/Polimorf-shapes-background.jpg" alt="A new post"  />\\
              </a></div><!-- end of .pm-post-image -->\\
              <div class="pm-blog-entry sticky">\\
                <h2><a href="/test1-the-first-post/">A new post</a></h2>\\
              <div class="pm-author-category-meta">\\
                <span class="pm-meta-icon"><i class="fa fa-list" aria-hidden="true"></i></span>\\
                <a href="/categories/something/" alt="something">something</a>,&nbsp;\\
                <a href="/categories/another-category/" alt="another-category">another category</a>,&nbsp;\\
                <a href="/categories/things-to-write-about/" alt="things-to-write-about">things to write about</a>\\
              </div><!-- end of .pm-author-category-meta -->\\
              <div class="pm-author-category-meta">\\
                <span class="pm-meta-icon"><i class="fa fa-user" aria-hidden="true"></i></span>\\
                <a href="/authors/anon/" alt="anon">anon</a>\\
              </div><!-- end of .pm-author-category-meta -->\\
                <p>Something longer here to describe what is going on.<br/>Like we can see there are more lines to add.<br/>Then more again!</p>\\
              </div><!-- end of .pm-blog_entry -->\\
            </div><!-- end of .pm-post-content -->'
    ],
    sticky: [
    ]
  }
  ]
};

        """
        }
    },

{   'remark': 'Test Case 4:pcom_process_postlist - postlist info with posts and manual stickies',
    'postlist_info': [\
            {
                "index": 68,
                "fileroot": "test1",
                "ppp": "5",
                "manual_sticky": "True",
                "content": "!!about.page,test1.post,!!test2.post,contact.page"
            }
    ],
    'postlist': POSTLIST_1,
    'settings': gb.DEFAULT_SETTINGS,
    'list_meta': LIST_META_1,
    'fileroot': 'test5',
    'assertEqual': {\
        'processed': True,
        'result': """

window._postlist_test5 = {
  identifier: 'postlist-list-',
  pagination_element: '        <span class="pm-page-numbers %%$_NUMBERIDENT_$%%">%%$_NUMBER_$%%</span>',
  page_numbers_selected_class: 'current',
  pagination_class: 'pm-postlist-pagination',
  pagination_selector_id: '-pm-page-numbers',
  pagination_number_sub: '%%$_NUMBER_$%%',
  pagination_number_ident: '%%$_NUMBERIDENT_$%%',
  entries: [
  {
    posts_per_page: 5,
    posts: [
      '\\
            <div class="pm-post-content clearfix-small">\\
              <div class="pm-post-image">\\
              <a href="/test1-the-first-post/">\\
                <img src="/images/Polimorf-shapes-background.jpg" alt="A new post"  />\\
              </a></div><!-- end of .pm-post-image -->\\
              <div class="pm-blog-entry">\\
                <h2><a href="/test1-the-first-post/">A new post</a></h2>\\
              <div class="pm-author-category-meta">\\
                <span class="pm-meta-icon"><i class="fa fa-list" aria-hidden="true"></i></span>\\
                <a href="/categories/something/" alt="something">something</a>,&nbsp;\\
                <a href="/categories/another-category/" alt="another-category">another category</a>,&nbsp;\\
                <a href="/categories/things-to-write-about/" alt="things-to-write-about">things to write about</a>\\
              </div><!-- end of .pm-author-category-meta -->\\
              <div class="pm-author-category-meta">\\
                <span class="pm-meta-icon"><i class="fa fa-user" aria-hidden="true"></i></span>\\
                <a href="/authors/anon/" alt="anon">anon</a>\\
              </div><!-- end of .pm-author-category-meta -->\\
                <p>Something longer here to describe what is going on.<br/>Like we can see there are more lines to add.<br/>Then more again!</p>\\
              </div><!-- end of .pm-blog_entry -->\\
            </div><!-- end of .pm-post-content -->',
      '\\
            <div class="pm-post-content clearfix-small">\\
              <div class="pm-post-image">\\
              <a href="/contact/">\\
                <img src="/images/Polimorf-shapes-background.jpg" alt="Contact"  />\\
              </a></div><!-- end of .pm-post-image -->\\
              <div class="pm-blog-entry">\\
                <h2><a href="/contact/">Contact</a></h2>\\
              <div class="pm-author-category-meta">\\
                <span class="pm-meta-icon"><i class="fa fa-user" aria-hidden="true"></i></span>\\
                <a href="/authors/micky-h-corbett/" alt="micky-h-corbett">Micky H Corbett</a>\\
              </div><!-- end of .pm-author-category-meta -->\\
                <p>Contact Morfless</p>\\
              </div><!-- end of .pm-blog_entry -->\\
            </div><!-- end of .pm-post-content -->'
    ],
    sticky: [
      '\\
            <div class="pm-post-content clearfix-small">\\
              <div class="pm-post-image">\\
              <a href="/about/">\\
                <img src="/images/Polimorf-shapes-background.jpg" alt="About Morfless"  />\\
              </a></div><!-- end of .pm-post-image -->\\
              <div class="pm-blog-entry sticky">\\
                <h2><a href="/about/">About Morfless</a></h2>\\
              <div class="pm-author-category-meta">\\
                <span class="pm-meta-icon"><i class="fa fa-user" aria-hidden="true"></i></span>\\
                <a href="/authors/jim-o-neill/" alt="jim-o-neill">Jim O&#39;Neill</a>\\
              </div><!-- end of .pm-author-category-meta -->\\
                <p>An about page - describe yourself in as much detail as you like!<br/>You can also add more to this extract.</p>\\
              </div><!-- end of .pm-blog_entry -->\\
            </div><!-- end of .pm-post-content -->',
      '\\
            <div class="pm-post-content clearfix-small">\\
              <div class="pm-post-image">\\
              <a href="/test2/">\\
                <img src="/images/Polimorf-shapes-background.jpg" alt="A new post - second coming - redux"  />\\
              </a></div><!-- end of .pm-post-image -->\\
              <div class="pm-blog-entry sticky">\\
                <h2><a href="/test2/">A new post - second coming - redux</a></h2>\\
              <div class="pm-author-category-meta">\\
                <span class="pm-meta-icon"><i class="fa fa-list" aria-hidden="true"></i></span>\\
                <a href="/categories/something/" alt="something">something</a>,&nbsp;\\
                <a href="/categories/interesting/" alt="interesting">interesting</a>\\
              </div><!-- end of .pm-author-category-meta -->\\
              <div class="pm-author-category-meta">\\
                <span class="pm-meta-icon"><i class="fa fa-user" aria-hidden="true"></i></span>\\
                <a href="/authors/micky-h-corbett/" alt="micky-h-corbett">Micky H Corbett</a>,&nbsp;\\
                <a href="/authors/albert/" alt="albert">Albert</a>\\
              </div><!-- end of .pm-author-category-meta -->\\
                <p>Something longer here to describe what is going on</p>\\
              </div><!-- end of .pm-blog_entry -->\\
            </div><!-- end of .pm-post-content -->'
    ]
  }
  ]
};

        """
        }
    },

{   'remark': 'Test Case 5:pcom_process_postlist - postlist info with posts with sticky',
    'postlist_info': [\
            {
                "index": 64,
                "fileroot": "test1",
                "ppp": "5",
                "manual_sticky": "False",
                "content": "about-this.post"
            }
    ],
    'postlist': POSTLIST_1,
    'settings': gb.DEFAULT_SETTINGS,
    'list_meta': LIST_META_1,
    'fileroot': 'test5',
    'assertEqual': {\
        'processed': True,
        'result': """

window._postlist_test5 = {
  identifier: 'postlist-list-',
  pagination_element: '        <span class="pm-page-numbers %%$_NUMBERIDENT_$%%">%%$_NUMBER_$%%</span>',
  page_numbers_selected_class: 'current',
  pagination_class: 'pm-postlist-pagination',
  pagination_selector_id: '-pm-page-numbers',
  pagination_number_sub: '%%$_NUMBER_$%%',
  pagination_number_ident: '%%$_NUMBERIDENT_$%%',
  entries: [
  {
    posts_per_page: 5,
    posts: [
      '\\
            <div class="pm-post-content clearfix-small">\\
              <div class="pm-post-image">\\
              <a href="/about-this/">\\
                <img src="/images/Polimorf-shapes-background.jpg" alt="About Morfless and more"  />\\
              </a></div><!-- end of .pm-post-image -->\\
              <div class="pm-blog-entry sticky">\\
                <h2><a href="/about-this/">About Morfless and more</a></h2>\\
              <div class="pm-author-category-meta">\\
                <span class="pm-meta-icon"><i class="fa fa-list" aria-hidden="true"></i></span>\\
                <a href="/categories/na/" alt="na">NA</a>\\
              </div><!-- end of .pm-author-category-meta -->\\
              <div class="pm-author-category-meta">\\
                <span class="pm-meta-icon"><i class="fa fa-user" aria-hidden="true"></i></span>\\
                <a href="/authors/jim-o-neill/" alt="jim-o-neill">Jim O&#39;Neill</a>\\
              </div><!-- end of .pm-author-category-meta -->\\
                <p>An about page - describe yourself in as much detail as you like!<br/>You can also add more to this extract.</p>\\
              </div><!-- end of .pm-blog_entry -->\\
            </div><!-- end of .pm-post-content -->'
    ],
    sticky: [
    ]
  }
  ]
};

        """
        }
    },

{   'remark': 'Test Case 6:pcom_process_postlist - postlist with posts',
    'postlist_info': [\
            {
                "index": 64,
                "fileroot": "test1",
                "ppp": "5",
                "manual_sticky": "False",
                "content": ct.PCOM_SETTINGS_TYPE_POSTS
            }
    ],
    'postlist': POSTLIST_1,
    'settings': gb.DEFAULT_SETTINGS,
    'list_meta': LIST_META_1,
    'fileroot': 'test5',
    'assertEqual': {\
        'processed': True,
        'result': """

window._postlist_test5 = {
  identifier: 'postlist-list-',
  pagination_element: '        <span class="pm-page-numbers %%$_NUMBERIDENT_$%%">%%$_NUMBER_$%%</span>',
  page_numbers_selected_class: 'current',
  pagination_class: 'pm-postlist-pagination',
  pagination_selector_id: '-pm-page-numbers',
  pagination_number_sub: '%%$_NUMBER_$%%',
  pagination_number_ident: '%%$_NUMBERIDENT_$%%',
  entries: [
  {
    posts_per_page: 5,
    posts: [
      '\\
            <div class="pm-post-content clearfix-small">\\
              <div class="pm-post-image">\\
              <a href="/test2/">\\
                <img src="/images/Polimorf-shapes-background.jpg" alt="A new post - second coming - redux"  />\\
              </a></div><!-- end of .pm-post-image -->\\
              <div class="pm-blog-entry">\\
                <h2><a href="/test2/">A new post - second coming - redux</a></h2>\\
              <div class="pm-author-category-meta">\\
                <span class="pm-meta-icon"><i class="fa fa-list" aria-hidden="true"></i></span>\\
                <a href="/categories/something/" alt="something">something</a>,&nbsp;\\
                <a href="/categories/interesting/" alt="interesting">interesting</a>\\
              </div><!-- end of .pm-author-category-meta -->\\
              <div class="pm-author-category-meta">\\
                <span class="pm-meta-icon"><i class="fa fa-user" aria-hidden="true"></i></span>\\
                <a href="/authors/micky-h-corbett/" alt="micky-h-corbett">Micky H Corbett</a>,&nbsp;\\
                <a href="/authors/albert/" alt="albert">Albert</a>\\
              </div><!-- end of .pm-author-category-meta -->\\
                <p>Something longer here to describe what is going on</p>\\
              </div><!-- end of .pm-blog_entry -->\\
            </div><!-- end of .pm-post-content -->',
      '\\
            <div class="pm-post-content clearfix-small">\\
              <div class="pm-post-image">\\
              <a href="/test3-post-something-new/">\\
                <img src="/images/Polimorf-shapes-background.jpg" alt="A new post"  />\\
              </a></div><!-- end of .pm-post-image -->\\
              <div class="pm-blog-entry">\\
                <h2><a href="/test3-post-something-new/">A new post</a></h2>\\
              <div class="pm-author-category-meta">\\
                <span class="pm-meta-icon"><i class="fa fa-list" aria-hidden="true"></i></span>\\
                <a href="/categories/something/" alt="something">something</a>\\
              </div><!-- end of .pm-author-category-meta -->\\
              <div class="pm-author-category-meta">\\
                <span class="pm-meta-icon"><i class="fa fa-user" aria-hidden="true"></i></span>\\
                <a href="/authors/anon/" alt="anon">anon</a>\\
              </div><!-- end of .pm-author-category-meta -->\\
                <p>Something longer here to describe what is going on. And to see if it is included in a search</p>\\
              </div><!-- end of .pm-blog_entry -->\\
            </div><!-- end of .pm-post-content -->'
    ],
    sticky: [
      '\\
            <div class="pm-post-content clearfix-small">\\
              <div class="pm-post-image">\\
              <a href="/about-this/">\\
                <img src="/images/Polimorf-shapes-background.jpg" alt="About Morfless and more"  />\\
              </a></div><!-- end of .pm-post-image -->\\
              <div class="pm-blog-entry sticky">\\
                <h2><a href="/about-this/">About Morfless and more</a></h2>\\
              <div class="pm-author-category-meta">\\
                <span class="pm-meta-icon"><i class="fa fa-list" aria-hidden="true"></i></span>\\
                <a href="/categories/na/" alt="na">NA</a>\\
              </div><!-- end of .pm-author-category-meta -->\\
              <div class="pm-author-category-meta">\\
                <span class="pm-meta-icon"><i class="fa fa-user" aria-hidden="true"></i></span>\\
                <a href="/authors/jim-o-neill/" alt="jim-o-neill">Jim O&#39;Neill</a>\\
              </div><!-- end of .pm-author-category-meta -->\\
                <p>An about page - describe yourself in as much detail as you like!<br/>You can also add more to this extract.</p>\\
              </div><!-- end of .pm-blog_entry -->\\
            </div><!-- end of .pm-post-content -->',
      '\\
            <div class="pm-post-content clearfix-small">\\
              <div class="pm-post-image">\\
              <a href="/test1-the-first-post/">\\
                <img src="/images/Polimorf-shapes-background.jpg" alt="A new post"  />\\
              </a></div><!-- end of .pm-post-image -->\\
              <div class="pm-blog-entry sticky">\\
                <h2><a href="/test1-the-first-post/">A new post</a></h2>\\
              <div class="pm-author-category-meta">\\
                <span class="pm-meta-icon"><i class="fa fa-list" aria-hidden="true"></i></span>\\
                <a href="/categories/something/" alt="something">something</a>,&nbsp;\\
                <a href="/categories/another-category/" alt="another-category">another category</a>,&nbsp;\\
                <a href="/categories/things-to-write-about/" alt="things-to-write-about">things to write about</a>\\
              </div><!-- end of .pm-author-category-meta -->\\
              <div class="pm-author-category-meta">\\
                <span class="pm-meta-icon"><i class="fa fa-user" aria-hidden="true"></i></span>\\
                <a href="/authors/anon/" alt="anon">anon</a>\\
              </div><!-- end of .pm-author-category-meta -->\\
                <p>Something longer here to describe what is going on.<br/>Like we can see there are more lines to add.<br/>Then more again!</p>\\
              </div><!-- end of .pm-blog_entry -->\\
            </div><!-- end of .pm-post-content -->'
    ]
  }
  ]
};

        """
        }
    },
]

test_values_2 = [\
{   'remark': 'Test Case 1:pcom_create_sub_template_backlink - type tags = error',
    'type': 'tags',
    'settings': gb.DEFAULT_SETTINGS,
    'template_sub_header_back_link_text': {\
        'posts': 'Back to posts',
        'entries': 'Back to entries',
        'tags': ct.PCOM_JSON_LOAD_ERROR
    },
    'assertEqual': """

    """
    },

{   'remark': 'Test Case 2:pcom_create_sub_template_backlink - type posts',
    'type': 'posts',
    'settings': gb.DEFAULT_SETTINGS,
    'template_sub_header_back_link_text': {\
        'posts': 'Back to posts',
        'entries': 'Back to entries',
        'tags': ct.PCOM_JSON_LOAD_ERROR
    },
    'assertEqual': """

      \\
            <div class="pm-pagination-header-backlink pm-post-link-text">\\
              <i class="fa fa-arrow-left" aria-hidden="true"></i>\\
              <a href="/posts/">Back to posts</a>\\
            </div><!-- end of .pm-pagination-header-backlink -->
    """
    },

{   'remark': 'Test Case 3:pcom_create_sub_template_backlink - type entries',
    'type': 'entries',
    'settings': gb.DEFAULT_SETTINGS,
    'template_sub_header_back_link_text': {\
        'posts': 'Back to posts',
        'entries': 'Back to entries',
        'tags': ct.PCOM_JSON_LOAD_ERROR
    },
    'assertEqual': """

      \\
            <div class="pm-pagination-header-backlink pm-post-link-text">\\
              <i class="fa fa-arrow-left" aria-hidden="true"></i>\\
              <a href="/entries/">Back to entries</a>\\
            </div><!-- end of .pm-pagination-header-backlink -->
    """
    },

{   'remark': 'Test Case 4:pcom_create_sub_template_backlink - type entries - no backlink text',
    'type': 'entries',
    'settings': gb.DEFAULT_SETTINGS,
    'template_sub_header_back_link_text': {\
        'posts': 'Back to posts',
        'entries': '',
        'tags': ct.PCOM_JSON_LOAD_ERROR
    },
    'assertEqual': """

    """
    },
]

test_values_3 = [\
{   'remark': 'Test Case 1:pcom_create_sub_template_title - type tags = error',
    'type': 'tags',
    'settings': gb.DEFAULT_SETTINGS,
    'sub': 'This thing',
    'template_sub_header_back_link_text': {\
        'posts': 'Back to posts',
        'entries': 'Back to entries',
        'tags': ct.PCOM_JSON_LOAD_ERROR
    },
    'template_sub_header_text': {\
        'posts': 'Posts for categories',
        'entries': 'Posts for entries',
        'tags': ct.PCOM_JSON_LOAD_ERROR
    },
    'template_main_header_text': {\
        'posts': 'Posts',
        'entries': 'Entries',
        'tags': ct.PCOM_JSON_LOAD_ERROR
    },
    'assertEqual': {
        'sub_title': '',
        'back_link': ''
        }
    },

{   'remark': 'Test Case 2:pcom_create_sub_template_title - type entries',
    'type': 'entries',
    'settings': gb.DEFAULT_SETTINGS,
    'sub': 'This thing',
    'template_sub_header_back_link_text': {\
        'posts': 'Back to posts',
        'entries': 'Back to entries',
        'tags': ct.PCOM_JSON_LOAD_ERROR
    },
    'template_sub_header_text': {\
        'posts': 'Posts for categories',
        'entries': 'Posts for entries',
        'tags': ct.PCOM_JSON_LOAD_ERROR
    },
    'template_main_header_text': {\
        'posts': 'Posts',
        'entries': 'Entries',
        'tags': ct.PCOM_JSON_LOAD_ERROR
    },
    'assertEqual': {
        'sub_title': 'Posts for entries This thing',
        'back_link': """
      \\
            <div class="pm-pagination-header-backlink pm-post-link-text">\\
              <i class="fa fa-arrow-left" aria-hidden="true"></i>\\
              <a href="/entries/">Back to entries</a>\\
            </div><!-- end of .pm-pagination-header-backlink -->

        """
        }
    },

{   'remark': 'Test Case 3:pcom_create_sub_template_title - type posts',
    'type': 'posts',
    'settings': gb.DEFAULT_SETTINGS,
    'sub': 'This thing',
    'template_sub_header_back_link_text': {\
        'posts': 'Back to posts',
        'entries': 'Back to entries',
        'tags': ct.PCOM_JSON_LOAD_ERROR
    },
    'template_sub_header_text': {\
        'posts': 'Posts for categories',
        'entries': 'Posts for entries',
        'tags': ct.PCOM_JSON_LOAD_ERROR
    },
    'template_main_header_text': {\
        'posts': 'Posts',
        'entries': 'Entries',
        'tags': ct.PCOM_JSON_LOAD_ERROR
    },
    'assertEqual': {
        'sub_title': 'Posts',
        'back_link': """

        """
        }
    },

{   'remark': 'Test Case 4:pcom_create_sub_template_title - type posts with error',
    'type': 'posts',
    'settings': gb.DEFAULT_SETTINGS,
    'sub': 'This thing',
    'template_sub_header_back_link_text': {\
        'posts': 'Back to posts',
        'entries': 'Back to entries',
        'tags': ct.PCOM_JSON_LOAD_ERROR
    },
    'template_sub_header_text': {\
        'posts': 'Posts for categories',
        'entries': 'Posts for entries',
        'tags': ct.PCOM_JSON_LOAD_ERROR
    },
    'template_main_header_text': {\
        'posts': ct.PCOM_JSON_LOAD_ERROR,
        'entries': 'Entries',
        'tags': ct.PCOM_JSON_LOAD_ERROR
    },
    'assertEqual': {
        'sub_title': '',
        'back_link': """

        """
        }
    },
]

test_values_4 = [\
{   'remark': 'Test Case 1:pcom_determine_post_list_from_type - empty type',
    'postlist': [],
    'archive': [],
    'list_meta': {},
    'type': '',
    'sub': '',
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': []
    },
{   'remark': 'Test Case 2:pcom_determine_post_list_from_type - type posts',
    'postlist': POSTLIST_1,
    'archive': [],
    'list_meta': LIST_META_1,
    'type': ct.PCOM_SETTINGS_TYPE_POSTS,
    'sub': '',
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': [
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
    },

{   'remark': 'Test Case 3:pcom_determine_post_list_from_type - type categories - thing to write about',
    'postlist': POSTLIST_1,
    'archive': ARCHIVE_1,
    'list_meta': LIST_META_1,
    'type': ct.PCOM_SETTINGS_TYPE_CATEGORIES,
    'sub': 'things to write about',
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': [
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
        }
    ]
    },

{   'remark': "Test Case 4:pcom_determine_post_list_from_type - type authors - Jim O'Neill",
    'postlist': POSTLIST_1,
    'archive': ARCHIVE_1,
    'list_meta': LIST_META_1,
    'type': ct.PCOM_SETTINGS_TYPE_AUTHORS,
    'sub': "Jim O'Neill",
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': [
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
    },

{   'remark': "Test Case 5:pcom_determine_post_list_from_type - type archive - 10-2018",
    'postlist': POSTLIST_1,
    'archive': ARCHIVE_1,
    'list_meta': LIST_META_1,
    'type': ct.PCOM_SETTINGS_TYPE_ARCHIVE,
    'sub': "10-2018",
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': [
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
        }
    ]
    },
]
