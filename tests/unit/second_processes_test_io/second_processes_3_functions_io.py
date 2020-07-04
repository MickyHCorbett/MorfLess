#
import libraries.constants as ct
import libraries.globals as gb
import libraries.schematics as sch

from unit.second_processes_test_io.second_processes_supplemental import LIST_META_1
from unit.second_processes_test_io.second_processes_supplemental import POSTLIST_1
from unit.second_processes_test_io.second_processes_supplemental import ARCHIVE_1
from unit.second_processes_test_io.second_processes_supplemental import ARCHIVE_2
from unit.second_processes_test_io.second_processes_supplemental import ARCHIVE_3
from unit.second_processes_test_io.second_processes_supplemental import TEMP_CONTENT_1
from unit.second_processes_test_io.second_processes_supplemental import TEMP_CONTENT_2

from collections import OrderedDict
#

test_values_1 = [\
{   'remark': 'Test Case 1:pcom_process_pagination - empty info',
    'postlist': POSTLIST_1,
    'pg_name': 'pagination__list1.js',
    'fileroot': 'test5',
    'info': {},
    'assertEqual': {\
        'result': """

        """,
        'processed': False
        }
    },

{   'remark': 'Test Case 2:pcom_process_pagination - info',
    'postlist': POSTLIST_1,
    'pg_name': 'pagination__list2.js',
    'fileroot': 'test6-at-all',
    'info': {\
        'type': 'post',
        'postname': 'test3.post',
        'next_ref': '',
        'prev_ref': ''
    },
    'assertEqual': {\
        'result': """

window._pagination_test6_at_all = {
  pagination: '\\
      <div id="pm-single-post-link">\\
        <span class="pm-post-link-text"><i class="fa fa-arrow-left" aria-hidden="true"></i>\\
        <a href="/test2/">A new post - second coming - redux</a>\\
      </span></div><!-- post link -->'
};
        """,
        'processed': True
        }
    },

{   'remark': 'Test Case 3:pcom_process_pagination - info',
    'postlist': POSTLIST_1,
    'pg_name': 'pagination__list2.js',
    'fileroot': 'test7',
    'info': {\
        'type': 'post',
        'postname': 'test2.post',
        'next_ref': '',
        'prev_ref': ''
    },
    'assertEqual': {\
        'result': """

window._pagination_test7 = {
  pagination: '\\
      <div id="pm-next-post-link">\\
        <span class="pm-post-link-text"><i class="fa fa-arrow-right" aria-hidden="true"></i>\\
        <a href="/test3-post-something-new/">A new post</a>\\
      </span></div><!-- post link -->\\
      <div id="pm-prev-post-link">\\
        <span class="pm-post-link-text"><i class="fa fa-arrow-left" aria-hidden="true"></i>\\
        <a href="/test1-the-first-post/">A new post</a>\\
      </span></div><!-- post link -->'
};

        """,
        'processed': True
        }
    },

{   'remark': 'Test Case 4:pcom_process_pagination - info - next ref',
    'postlist': POSTLIST_1,
    'pg_name': 'pagination__list2.js',
    'fileroot': 'test7',
    'info': {\
        'type': 'post',
        'postname': 'test2.post',
        'next_ref': 'test3.post',
        'prev_ref': ''
    },
    'assertEqual': {\
        'result': """

window._pagination_test7 = {
  pagination: '\\
      <div id="pm-single-post-link">\\
        <span class="pm-post-link-text"><i class="fa fa-arrow-right" aria-hidden="true"></i>\\
        <a href="/test3-post-something-new/">A new post</a>\\
      </span></div><!-- post link -->'
};

        """,
        'processed': True
        }
    },

{   'remark': 'Test Case 5:pcom_process_pagination - info - prev ref',
    'postlist': POSTLIST_1,
    'pg_name': 'pagination__list2.js',
    'fileroot': 'test7',
    'info': {\
        'type': 'post',
        'postname': 'test2.post',
        'next_ref': '',
        'prev_ref': 'test1.post'
    },
    'assertEqual': {\
        'result': """

window._pagination_test7 = {
  pagination: '\\
      <div id="pm-single-post-link">\\
        <span class="pm-post-link-text"><i class="fa fa-arrow-left" aria-hidden="true"></i>\\
        <a href="/test1-the-first-post/">A new post</a>\\
      </span></div><!-- post link -->'
};

        """,
        'processed': True
        }
    },
]

test_values_2 = [\
{   'remark': 'Test Case 1:pcom_process_posts_page - empty info',
    'postlist': POSTLIST_1,
    'archive': ARCHIVE_1,
    'settings': gb.DEFAULT_SETTINGS,
    'list_meta': LIST_META_1,
    'log': {'template_names': []},
    'template_content': '',
    'assertEqual': {\
            'info': {\
                'template_content': '',
                's3url': '',
                'posts_name': '',
                'posts_js_name': '',
                'posts_js_constant': '',
                'processed': False
            },
            'log': {\
                'template_names': ['Posts template base name: posts']
            }
        }
    },

{   'remark': 'Test Case 2:pcom_process_posts_page - empty info',
    'postlist': POSTLIST_1,
    'archive': ARCHIVE_1,
    'settings': gb.DEFAULT_SETTINGS,
    'list_meta': LIST_META_1,
    'log': {'template_names': []},
    'template_content': 'Something to add',
    'assertEqual': {\
            'info': {\
                'template_content': 'Something to add',
                's3url': 'posts/index.html',
                'posts_name': 'posts',
                'posts_js_name': 'postlist--posts.js',
                'posts_js_constant': """

window._postlist_posts = {
  identifier: 'postlist-template',
  pagination_element: '        <span class="pm-page-numbers %%$_NUMBERIDENT_$%%">%%$_NUMBER_$%%</span>',
  page_numbers_selected_class: 'current',
  pagination_class: 'pm-postlist-pagination',
  pagination_selector_id: '-pm-page-numbers',
  pagination_number_sub: '%%$_NUMBER_$%%',
  pagination_number_ident: '%%$_NUMBERIDENT_$%%',
  sub_title: "Posts",
  back_link: '',
  header: '      <h1 class="pm-template-header"></h1>',
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

                """,
                'processed': True
            },
            'log': {\
                'template_names': ['Posts template base name: posts']
            }
        }
    },
]

test_values_3 = [\
{   'remark': 'Test Case 1:pcom_process_info_base_pages - empty info',
    'info_list': [],
    'base_type': ct.PCOM_SETTINGS_TYPE_CATEGORIES,
    'postlist': POSTLIST_1,
    'archive': ARCHIVE_1,
    'settings': gb.DEFAULT_SETTINGS,
    'list_meta': LIST_META_1,
    'log': {'template_names': []},
    'template_content': '',
    'assertEqual': {\
            'info': {\
                'template_content': '',
                's3url': '',
                'base_name': '',
                'js_name': '',
                'js_constant': '',
                'processed': False
            },
            'log': {\
                'template_names': ['categories template base name: categories']
            },
            'base_sub_info': []
        }
    },

{   'remark': 'Test Case 2:pcom_process_info_base_pages - empty info',
    'info_list': [],
    'base_type': ct.PCOM_SETTINGS_TYPE_CATEGORIES,
    'postlist': POSTLIST_1,
    'archive': ARCHIVE_1,
    'settings': gb.DEFAULT_SETTINGS,
    'list_meta': LIST_META_1,
    'log': {'template_names': []},
    'template_content': 'Something here again',
    'assertEqual': {\
            'info': {\
                'template_content': 'Something here again',
                's3url': 'categories/index.html',
                'base_name': 'categories',
                'js_name': 'postlist--categories.js',
                'js_constant': """

window._postlist_categories = {
  identifier: 'postlist-template',
  pagination_element: '        <span class="pm-page-numbers %%$_NUMBERIDENT_$%%">%%$_NUMBER_$%%</span>',
  page_numbers_selected_class: 'current',
  pagination_class: 'pm-postlist-pagination',
  pagination_selector_id: '-pm-page-numbers',
  pagination_number_sub: '%%$_NUMBER_$%%',
  pagination_number_ident: '%%$_NUMBERIDENT_$%%',
  sub_title: 'Categories',
  back_link: '',
  header: '      <h1 class="pm-template-header"></h1>',
  entries: [
  {
    posts_per_page: 5,
    posts: [
    ],
    sticky: []
  }
  ]
};


                """,
                'processed': True
            },
            'log': {\
                'template_names': ['categories template base name: categories']
            },
            'base_sub_info': []

        }
    },

{   'remark': 'Test Case 2:pcom_process_info_base_pages - categories info',
    'info_list': LIST_META_1['categories']['categories'],
    'base_type': ct.PCOM_SETTINGS_TYPE_CATEGORIES,
    'postlist': POSTLIST_1,
    'archive': ARCHIVE_1,
    'settings': gb.DEFAULT_SETTINGS,
    'list_meta': LIST_META_1,
    'log': {'template_names': []},
    'template_content': 'Something here again',
    'assertEqual': {\
            'info': {\
                'template_content': 'Something here again',
                's3url': 'categories/index.html',
                'base_name': 'categories',
                'js_name': 'postlist--categories.js',
                'js_constant': """

window._postlist_categories = {
  identifier: 'postlist-template',
  pagination_element: '        <span class="pm-page-numbers %%$_NUMBERIDENT_$%%">%%$_NUMBER_$%%</span>',
  page_numbers_selected_class: 'current',
  pagination_class: 'pm-postlist-pagination',
  pagination_selector_id: '-pm-page-numbers',
  pagination_number_sub: '%%$_NUMBER_$%%',
  pagination_number_ident: '%%$_NUMBERIDENT_$%%',
  sub_title: 'Categories',
  back_link: '',
  header: '      <h1 class="pm-template-header"></h1>',
  entries: [
  {
    posts_per_page: 5,
    posts: [
      '\\
            <div class="pm-post-content clearfix-small">\\
              <div class="pm-post-image">\\
              <a href="/categories/something/">\\
                <img src="/images/Polimorf-shapes-background.jpg" alt="something"  />\\
              </a></div><!-- end of .pm-post-image -->\\
              <div class="pm-blog-entry">\\
                <h2><a href="/categories/something/">something</a></h2>\\
                <p></p>\\
              </div><!-- end of .pm-blog_entry -->\\
            </div><!-- end of .pm-post-content -->',
      '\\
            <div class="pm-post-content clearfix-small">\\
              <div class="pm-post-image">\\
              <a href="/categories/another-category/">\\
                <img src="/images/Polimorf-shapes-background.jpg" alt="another-category"  />\\
              </a></div><!-- end of .pm-post-image -->\\
              <div class="pm-blog-entry">\\
                <h2><a href="/categories/another-category/">another category</a></h2>\\
                <p></p>\\
              </div><!-- end of .pm-blog_entry -->\\
            </div><!-- end of .pm-post-content -->',
      '\\
            <div class="pm-post-content clearfix-small">\\
              <div class="pm-post-image">\\
              <a href="/categories/interesting/">\\
                <img src="/images/Polimorf-shapes-background-2.jpg" alt="interesting"  />\\
              </a></div><!-- end of .pm-post-image -->\\
              <div class="pm-blog-entry">\\
                <h2><a href="/categories/interesting/">interesting</a></h2>\\
                <p></p>\\
              </div><!-- end of .pm-blog_entry -->\\
            </div><!-- end of .pm-post-content -->',
      '\\
            <div class="pm-post-content clearfix-small">\\
              <div class="pm-post-image">\\
              <a href="/categories/things-to-write-about/">\\
                <img src="/images/Polimorf-shapes-background-2.jpg" alt="things-to-write-about"  />\\
              </a></div><!-- end of .pm-post-image -->\\
              <div class="pm-blog-entry">\\
                <h2><a href="/categories/things-to-write-about/">things to write about</a></h2>\\
                <p></p>\\
              </div><!-- end of .pm-blog_entry -->\\
            </div><!-- end of .pm-post-content -->'
    ],
    sticky: []
  }
  ]
};

                """,
                'processed': True
            },
            'log': {\
                'template_names': ['categories template base name: categories']
            },
            'base_sub_info': [\
                {\
                    'title': 'something',
                    'description': '',
                    'sub_js_root': '-something',
                    'full_js_root': 'categories-something',
                    'sub_fileroot': '_something',
                    'fileroot': 'categories_something',
                    'js_filename': 'postlist--categories-something.js',
                    'test_html': 'categories-something.html',
                    'url': '/categories/something/',
                    's3url': 'categories/something/index.html',
                    'js_constant': """

window._postlist_categories_something = {
  identifier: 'postlist-template',
  pagination_element: '        <span class="pm-page-numbers %%$_NUMBERIDENT_$%%">%%$_NUMBER_$%%</span>',
  page_numbers_selected_class: 'current',
  pagination_class: 'pm-postlist-pagination',
  pagination_selector_id: '-pm-page-numbers',
  pagination_number_sub: '%%$_NUMBER_$%%',
  pagination_number_ident: '%%$_NUMBERIDENT_$%%',
  sub_title: "Posts for category:  something",
  back_link: '      \\
            <div class="pm-pagination-header-backlink pm-post-link-text">\\
              <i class="fa fa-arrow-left" aria-hidden="true"></i>\\
              <a href="/categories/">Back to Categories</a>\\
            </div><!-- end of .pm-pagination-header-backlink -->',
  header: '      <h1 class="pm-template-header"></h1>',
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

                    """,
                    'template_content': 'Something here again'
                },
                {\
                    'title': 'another category',
                    'description': '',
                    'sub_js_root': '-another-category',
                    'full_js_root': 'categories-another-category',
                    'sub_fileroot': '_another_category',
                    'fileroot': 'categories_another_category',
                    'js_filename':
                    'postlist--categories-another-category.js',
                    'test_html': 'categories-another-category.html',
                    'url': '/categories/another-category/',
                    's3url': 'categories/another-category/index.html',
                    'js_constant': """

window._postlist_categories_another_category = {
  identifier: 'postlist-template',
  pagination_element: '        <span class="pm-page-numbers %%$_NUMBERIDENT_$%%">%%$_NUMBER_$%%</span>',
  page_numbers_selected_class: 'current',
  pagination_class: 'pm-postlist-pagination',
  pagination_selector_id: '-pm-page-numbers',
  pagination_number_sub: '%%$_NUMBER_$%%',
  pagination_number_ident: '%%$_NUMBERIDENT_$%%',
  sub_title: "Posts for category:  another category",
  back_link: '      \\
            <div class="pm-pagination-header-backlink pm-post-link-text">\\
              <i class="fa fa-arrow-left" aria-hidden="true"></i>\\
              <a href="/categories/">Back to Categories</a>\\
            </div><!-- end of .pm-pagination-header-backlink -->',
  header: '      <h1 class="pm-template-header"></h1>',
  entries: [
  {
    posts_per_page: 5,
    posts: [
    ],
    sticky: [
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

                    """,
                    'template_content': 'Something here again'
                }
            ]
        }
    },

{   'remark': 'Test Case 3:pcom_process_info_base_pages - archive info',
    'info_list': LIST_META_1['categories']['categories'],
    'base_type': ct.PCOM_SETTINGS_TYPE_ARCHIVE,
    'postlist': POSTLIST_1,
    'archive': ARCHIVE_3,
    'settings': gb.DEFAULT_SETTINGS,
    'list_meta': LIST_META_1,
    'log': {'template_names': []},
    'template_content': 'Something here again',
    'assertEqual': {\
            'info': {\
                'template_content': 'Something here again',
                's3url': 'archive/index.html',
                'base_name': 'archive',
                'js_name': 'postlist--archive.js',
                'js_constant': """

window._postlist_archive = {
  identifier: 'postlist-template',
  pagination_element: '        <span class="pm-page-numbers %%$_NUMBERIDENT_$%%">%%$_NUMBER_$%%</span>',
  page_numbers_selected_class: 'current',
  pagination_class: 'pm-postlist-pagination',
  pagination_selector_id: '-pm-page-numbers',
  pagination_number_sub: '%%$_NUMBER_$%%',
  pagination_number_ident: '%%$_NUMBERIDENT_$%%',
  sub_title: 'Monthly Archives',
  back_link: '',
  header: '      <h1 class="pm-template-header"></h1>',
  entries: [
  {
    posts_per_page: 9999,
    posts: [
'\\
          <div class="post">\\
            <p class="pm-archive-links"><a href="/archive/09-2018">09-2018</a></p>\\
            <p class="pm-archive-links"><a href="/archive/10-2018">10-2018</a></p>\\
            <p class="pm-archive-links"><a href="/archive/09-2019">09-2019</a></p>\\
            <p class="pm-archive-links"><a href="/archive/10-2019">10-2019</a></p>\\
          </div><!-- end of .post -->'
    ],
    sticky: []
  }
  ]
};

                """,
                'processed': True
            },
            'log': {\
                'template_names': ['archive template base name: archive']
            },
            'base_sub_info': [\
                {\
                    'title': '09-2018',
                    'description': '',
                    'sub_js_root': '-09-2018',
                    'full_js_root': 'archive-09-2018',
                    'sub_fileroot': '_09_2018',
                    'fileroot': 'archive_09_2018',
                    'js_filename': 'postlist--archive-09-2018.js',
                    'test_html': 'archive-09-2018.html',
                    'url': '/archive/09-2018/',
                    's3url': 'archive/09-2018/index.html',
                    'js_constant': """

window._postlist_archive_09_2018 = {
  identifier: 'postlist-template',
  pagination_element: '        <span class="pm-page-numbers %%$_NUMBERIDENT_$%%">%%$_NUMBER_$%%</span>',
  page_numbers_selected_class: 'current',
  pagination_class: 'pm-postlist-pagination',
  pagination_selector_id: '-pm-page-numbers',
  pagination_number_sub: '%%$_NUMBER_$%%',
  pagination_number_ident: '%%$_NUMBERIDENT_$%%',
  sub_title: "Posts updated on:  09-2018",
  back_link: '      \\
            <div class="pm-pagination-header-backlink pm-post-link-text">\\
              <i class="fa fa-arrow-left" aria-hidden="true"></i>\\
              <a href="/archive/">Back to Archives</a>\\
            </div><!-- end of .pm-pagination-header-backlink -->',
  header: '      <h1 class="pm-template-header"></h1>',
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

                    """,
                    'template_content': 'Something here again'
                },
                {\
                    'title': '10-2018',
                    'description': '',
                    'sub_js_root': '-10-2018',
                    'full_js_root': 'archive-10-2018',
                    'sub_fileroot': '_10_2018',
                    'fileroot': 'archive_10_2018',
                    'js_filename': 'postlist--archive-10-2018.js',
                    'test_html': 'archive-10-2018.html',
                    'url': '/archive/10-2018/',
                    's3url': 'archive/10-2018/index.html',
                    'js_constant': """

window._postlist_archive_10_2018 = {
  identifier: 'postlist-template',
  pagination_element: '        <span class="pm-page-numbers %%$_NUMBERIDENT_$%%">%%$_NUMBER_$%%</span>',
  page_numbers_selected_class: 'current',
  pagination_class: 'pm-postlist-pagination',
  pagination_selector_id: '-pm-page-numbers',
  pagination_number_sub: '%%$_NUMBER_$%%',
  pagination_number_ident: '%%$_NUMBERIDENT_$%%',
  sub_title: "Posts updated on:  10-2018",
  back_link: '      \\
            <div class="pm-pagination-header-backlink pm-post-link-text">\\
              <i class="fa fa-arrow-left" aria-hidden="true"></i>\\
              <a href="/archive/">Back to Archives</a>\\
            </div><!-- end of .pm-pagination-header-backlink -->',
  header: '      <h1 class="pm-template-header"></h1>',
  entries: [
  {
    posts_per_page: 5,
    posts: [
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
    ]
  }
  ]
};

                    """,
                    'template_content': 'Something here again'
                },
            ]
        }
    },
]

test_values_4 = [\
{   'remark': 'Test Case 1:pcom_process_search_config - search config',
    'template_main_header_text': { ct.PCOM_SETTINGS_TYPE_SEARCH: "Results for: ",
    ct.PCOM_SETTINGS_TYPE_CATEGORIES: "Categories",
    ct.PCOM_SETTINGS_TYPE_AUTHORS: "Authors",
    ct.PCOM_SETTINGS_TYPE_ARCHIVE: "Monthly Archives",
    ct.PCOM_SETTINGS_TYPE_POSTS: "Posts"
    },
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': """

window._search_config = {
  api: '',
  content_ident: 'pm-search-content',
  header_ident: 'pm-search-query',
  pagination_element: '        <span class="pm-page-numbers %%$_NUMBERIDENT_$%%">%%$_NUMBER_$%%</span>',
  page_numbers_selected_class: 'current',
  pagination_ident: 'pm-search-pagination',
  pagination_selector_id: '-pm-page-numbers',
  pagination_number_sub: '%%$_NUMBER_$%%',
  pagination_number_ident: '%%$_NUMBERIDENT_$%%',
  sub_title: 'Results for: ',
  posts_per_page: 5
};

    """
    },

{   'remark': 'Test Case 2:pcom_process_search_config - search config -JSON title error',
    'template_main_header_text': { ct.PCOM_SETTINGS_TYPE_SEARCH: ct.PCOM_JSON_LOAD_ERROR,
    ct.PCOM_SETTINGS_TYPE_CATEGORIES: "Categories",
    ct.PCOM_SETTINGS_TYPE_AUTHORS: "Authors",
    ct.PCOM_SETTINGS_TYPE_ARCHIVE: "Monthly Archives",
    ct.PCOM_SETTINGS_TYPE_POSTS: "Posts"
    },
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': """

window._search_config = {
  api: '',
  content_ident: 'pm-search-content',
  header_ident: 'pm-search-query',
  pagination_element: '        <span class="pm-page-numbers %%$_NUMBERIDENT_$%%">%%$_NUMBER_$%%</span>',
  page_numbers_selected_class: 'current',
  pagination_ident: 'pm-search-pagination',
  pagination_selector_id: '-pm-page-numbers',
  pagination_number_sub: '%%$_NUMBER_$%%',
  pagination_number_ident: '%%$_NUMBERIDENT_$%%',
  sub_title: '',
  posts_per_page: 5
};

    """
    },
]

test_values_5 = [\
{   'remark': 'Test Case 1:pcom_create_search_response - no search content',
    'search_content': [],
    'postlist': POSTLIST_1,
    'list_meta': LIST_META_1,
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': {\
        'entries': [],
        'sticky': []
        }
    },

{   'remark': 'Test Case 2:pcom_create_search_response - search content - posts and templates',
    'search_content': [\
        { 'name': 'posts', 'count': 5 },
        { 'name': 'authors', 'count': 4 },
        { 'name': 'test1.post', 'count': 3 },
        { 'name': 'about.page', 'count': 0 },
    ],
    'postlist': POSTLIST_1,
    'list_meta': LIST_META_1,
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': {\
        'entries': ['"            <div class=\\"pm-post-content '
             'clearfix-small\\">\\n              <div '
             'class=\\"pm-post-image\\">\\n              <a '
             'href=\\"/test1-the-first-post/\\">\\n                <img '
             'src=\\"/images/Polimorf-shapes-background.jpg\\" alt=\\"A new '
             'post\\"  />\\n              </a></div><!-- end of .pm-post-image '
             '-->\\n              <div '
             'class=\\"pm-blog-entry\\">\\n                <h2><a '
             'href=\\"/test1-the-first-post/\\">A new '
             'post</a></h2>\\n              <div '
             'class=\\"pm-author-category-meta\\">\\n                <span '
             'class=\\"pm-meta-icon\\"><i class=\\"fa fa-list\\" '
             'aria-hidden=\\"true\\"></i></span>\\n                <a '
             'href=\\"/categories/something/\\" '
             'alt=\\"something\\">something</a>,&nbsp;\\n                <a '
             'href=\\"/categories/another-category/\\" '
             'alt=\\"another-category\\">another '
             'category</a>,&nbsp;\\n                <a '
             'href=\\"/categories/things-to-write-about/\\" '
             'alt=\\"things-to-write-about\\">things to write '
             'about</a>\\n              </div><!-- end of '
             '.pm-author-category-meta -->\\n              <div '
             'class=\\"pm-author-category-meta\\">\\n                <span '
             'class=\\"pm-meta-icon\\"><i class=\\"fa fa-user\\" '
             'aria-hidden=\\"true\\"></i></span>\\n                <a '
             'href=\\"/authors/anon/\\" '
             'alt=\\"anon\\">anon</a>\\n              </div><!-- end of '
             '.pm-author-category-meta -->\\n                <p>Something '
             'longer here to describe what is going on.<br/>Like we can see '
             'there are more lines to add.<br/>Then more '
             'again!</p>\\n              </div><!-- end of .pm-blog_entry '
             '-->\\n            </div><!-- end of .pm-post-content -->"',
             '"            <div class=\\"pm-post-content '
             'clearfix-small\\">\\n              <div '
             'class=\\"pm-post-image\\">\\n              <a '
             'href=\\"/about/\\">\\n                <img '
             'src=\\"/images/Polimorf-shapes-background.jpg\\" alt=\\"About '
             'Morfless\\"  />\\n              </a></div><!-- end of '
             '.pm-post-image -->\\n              <div '
             'class=\\"pm-blog-entry\\">\\n                <h2><a '
             'href=\\"/about/\\">About Morfless</a></h2>\\n              <div '
             'class=\\"pm-author-category-meta\\">\\n                <span '
             'class=\\"pm-meta-icon\\"><i class=\\"fa fa-user\\" '
             'aria-hidden=\\"true\\"></i></span>\\n                <a '
             'href=\\"/authors/jim-o-neill/\\" alt=\\"jim-o-neill\\">Jim '
             'O&#39;Neill</a>\\n              </div><!-- end of '
             '.pm-author-category-meta -->\\n                <p>An about page '
             '- describe yourself in as much detail as you like!<br/>You can '
             'also add more to this extract.</p>\\n              </div><!-- '
             'end of .pm-blog_entry -->\\n            </div><!-- end of '
             '.pm-post-content -->"'],
        'sticky': []
        }
    },

{   'remark': 'Test Case 3:pcom_create_search_response - search content - unknown posts and templates',
    'search_content': [\
        { 'name': 'things', 'count': 5 },
        { 'name': 'tags', 'count': 4 },
        { 'name': 'test10.post', 'count': 3 },
        { 'name': 'about-nothing.page', 'count': 0 },
    ],
    'postlist': POSTLIST_1,
    'list_meta': LIST_META_1,
    'settings': gb.DEFAULT_SETTINGS,
    'assertEqual': {\
        'entries': [],
        'sticky': []
        }
    },
]

test_values_6 = [\
{   'remark': 'Test Case 1:pcom_search_content - no search content - search term',
    'search_content': [],
    'search_term': 'this thing',
    'assertEqual': []
    },

{   'remark': 'Test Case 2:pcom_search_content - search content - no search term',
    'search_content': [\
        {\
            'name': 'entry1',
            'content': """

            this thing here and that thing there

            """
        },
        {\
            'name': 'entry2',
            'content': """

            this thing here and that thing there
            this thing here and that thing there

            """
        },
        {\
            'name': 'entry3',
            'content': """

            this thing here and that thing there
            this thing here and that thing there
            this thing here and that thing there

            """
        },
    ],
    'search_term': '',
    'assertEqual': []
    },

{   'remark': 'Test Case 3:pcom_search_content - search content - search term',
    'search_content': [\
        {\
            'name': 'entry1.content',
            'content': """

            this thing here and that thing there

            """
        },
        {\
            'name': 'entry2.content',
            'content': """

            this thing here and that thing there
            this thing here and that thing there

            """
        },
        {\
            'name': 'entry3.content',
            'content': """

            this thing here and that thing there
            this thing here and that thing there
            this thing here and that thing there

            """
        },
    ],
    'search_term': 'this thing',
    'assertEqual': [\
        {'name': 'entry3', 'count': 3},
        {'name': 'entry2', 'count': 2},
        {'name': 'entry1', 'count': 1}
    ]
    },
]
