#
import libraries.constants as ct
import libraries.globals as gb
import libraries.schematics as sch

from unit.second_processes_test_io.second_processes_supplemental import LIST_META_1
from unit.second_processes_test_io.second_processes_supplemental import POSTLIST_1
from unit.second_processes_test_io.second_processes_supplemental import ARCHIVE_1, ARCHIVE_2
from unit.second_processes_test_io.second_processes_supplemental import TEMP_CONTENT_1, TEMP_CONTENT_2

from collections import OrderedDict
#

test_values_1 = [\
{   'remark': 'Test Case 1:pcom_process_template_postlist - category - something',
    'postlist': POSTLIST_1,
    'archive': ARCHIVE_1,
    'type': ct.PCOM_SETTINGS_TYPE_CATEGORIES,
    'settings': gb.DEFAULT_SETTINGS,
    'list_meta': LIST_META_1,
    'fileroot': 'test5',
    'sub': 'something',
    'assertEqual': {\
        'result': """

window._postlist_test5 = {
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
        'processed': True
        }
    },

{   'remark': 'Test Case 2:pcom_process_template_postlist - category - this thing',
    'postlist': POSTLIST_1,
    'archive': ARCHIVE_1,
    'type': ct.PCOM_SETTINGS_TYPE_CATEGORIES,
    'settings': gb.DEFAULT_SETTINGS,
    'list_meta': LIST_META_1,
    'fileroot': 'test5',
    'sub': 'this thing',
    'assertEqual': {\
        'result': """

window._postlist_test5 = {
  identifier: 'postlist-template',
  pagination_element: '        <span class="pm-page-numbers %%$_NUMBERIDENT_$%%">%%$_NUMBER_$%%</span>',
  page_numbers_selected_class: 'current',
  pagination_class: 'pm-postlist-pagination',
  pagination_selector_id: '-pm-page-numbers',
  pagination_number_sub: '%%$_NUMBER_$%%',
  pagination_number_ident: '%%$_NUMBERIDENT_$%%',
  sub_title: "Posts for category:  this thing",
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
    ]
  }
  ]
};

        """,
        'processed': True
        }
    },
]

test_values_2 = [\
{   'remark': 'Test Case 1:pcom_process_template_list_info - categories',
    'list': LIST_META_1['categories']['categories'],
    'base_url': ct.PCOM_SETTINGS_TYPE_CATEGORIES,
    'settings': gb.DEFAULT_SETTINGS,
    'template_main_header_text': { ct.PCOM_SETTINGS_TYPE_SEARCH: "Results for: ",
    ct.PCOM_SETTINGS_TYPE_CATEGORIES: "Categories",
    ct.PCOM_SETTINGS_TYPE_AUTHORS: "Authors",
    ct.PCOM_SETTINGS_TYPE_ARCHIVE: "Monthly Archives",
    ct.PCOM_SETTINGS_TYPE_POSTS: "Posts"
    },
    'fileroot': 'test3',
    'assertEqual': {\
        'result': """

window._postlist_test3 = {
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
        }
    },

{   'remark': 'Test Case 2:pcom_process_template_list_info - authors',
    'list': LIST_META_1['authors']['authors'],
    'base_url': ct.PCOM_SETTINGS_TYPE_AUTHORS,
    'settings': gb.DEFAULT_SETTINGS,
    'template_main_header_text': { ct.PCOM_SETTINGS_TYPE_SEARCH: "Results for: ",
    ct.PCOM_SETTINGS_TYPE_CATEGORIES: "Categories",
    ct.PCOM_SETTINGS_TYPE_AUTHORS: "Authors",
    ct.PCOM_SETTINGS_TYPE_ARCHIVE: "Monthly Archives",
    ct.PCOM_SETTINGS_TYPE_POSTS: "Posts"
    },
    'fileroot': 'test1',
    'assertEqual': {\
        'result': """

window._postlist_test1 = {
  identifier: 'postlist-template',
  pagination_element: '        <span class="pm-page-numbers %%$_NUMBERIDENT_$%%">%%$_NUMBER_$%%</span>',
  page_numbers_selected_class: 'current',
  pagination_class: 'pm-postlist-pagination',
  pagination_selector_id: '-pm-page-numbers',
  pagination_number_sub: '%%$_NUMBER_$%%',
  pagination_number_ident: '%%$_NUMBERIDENT_$%%',
  sub_title: 'Authors',
  back_link: '',
  header: '      <h1 class="pm-template-header"></h1>',
  entries: [
  {
    posts_per_page: 5,
    posts: [
      '\\
            <div class="pm-post-content clearfix-small">\\
              <div class="pm-post-image">\\
              <a href="/authors/corvos-ae-team/">\\
                <img src="/images/CorvosTeam.jpg" alt="Corvos-AE-Team"  />\\
              </a></div><!-- end of .pm-post-image -->\\
              <div class="pm-blog-entry">\\
                <h2><a href="/authors/corvos-ae-team/">Corvos AE Team</a></h2>\\
                <p>General information and content from the Corvos Astro Engineering site</p>\\
              </div><!-- end of .pm-blog_entry -->\\
            </div><!-- end of .pm-post-content -->',
      '\\
            <div class="pm-post-content clearfix-small">\\
              <div class="pm-post-image">\\
              <a href="/authors/micky-h-corbett/">\\
                <img src="/images/CorvosDefaultImage.jpg" alt="Micky-H-Corbett"  />\\
              </a></div><!-- end of .pm-post-image -->\\
              <div class="pm-blog-entry">\\
                <h2><a href="/authors/micky-h-corbett/">Micky H Corbett</a></h2>\\
                <p>Aerospace and Space engineer with over 20 years experience in various fields including ion propulsion, aerospace systems, flight control, thruster control, prototype development. <br/>Other skills include cloud application development coding in multiple languages and enjoying the creative process!</p>\\
              </div><!-- end of .pm-blog_entry -->\\
            </div><!-- end of .pm-post-content -->',
      '\\
            <div class="pm-post-content clearfix-small">\\
              <div class="pm-post-image">\\
              <a href="/authors/albert/">\\
                <img src="/images/Polimorf-shapes-background-2.jpg" alt="Albert"  />\\
              </a></div><!-- end of .pm-post-image -->\\
              <div class="pm-blog-entry">\\
                <h2><a href="/authors/albert/">Albert</a></h2>\\
                <p></p>\\
              </div><!-- end of .pm-blog_entry -->\\
            </div><!-- end of .pm-post-content -->',
      '\\
            <div class="pm-post-content clearfix-small">\\
              <div class="pm-post-image">\\
              <a href="/authors/jim-o-neill/">\\
                <img src="/images/Polimorf-shapes-background-2.jpg" alt="Jim-O-Neill"  />\\
              </a></div><!-- end of .pm-post-image -->\\
              <div class="pm-blog-entry">\\
                <h2><a href="/authors/jim-o-neill/">Jim O&#39;Neill</a></h2>\\
                <p></p>\\
              </div><!-- end of .pm-blog_entry -->\\
            </div><!-- end of .pm-post-content -->',
      '\\
            <div class="pm-post-content clearfix-small">\\
              <div class="pm-post-image">\\
              <a href="/authors/contact/">\\
                <img src="/images/Polimorf-shapes-background-2.jpg" alt="Contact"  />\\
              </a></div><!-- end of .pm-post-image -->\\
              <div class="pm-blog-entry">\\
                <h2><a href="/authors/contact/">Contact</a></h2>\\
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
        }
    },

{   'remark': 'Test Case 3:pcom_process_template_list_info - categories - JSON error',
    'list': LIST_META_1['categories']['categories'],
    'base_url': ct.PCOM_SETTINGS_TYPE_CATEGORIES,
    'settings': gb.DEFAULT_SETTINGS,
    'template_main_header_text': { ct.PCOM_SETTINGS_TYPE_SEARCH: "Results for: ",
    ct.PCOM_SETTINGS_TYPE_CATEGORIES: ct.PCOM_JSON_LOAD_ERROR,
    ct.PCOM_SETTINGS_TYPE_AUTHORS: "Authors",
    ct.PCOM_SETTINGS_TYPE_ARCHIVE: "Monthly Archives",
    ct.PCOM_SETTINGS_TYPE_POSTS: "Posts"
    },
    'fileroot': 'test3',
    'assertEqual': {\
        'result': """

window._postlist_test3 = {
  identifier: 'postlist-template',
  pagination_element: '        <span class="pm-page-numbers %%$_NUMBERIDENT_$%%">%%$_NUMBER_$%%</span>',
  page_numbers_selected_class: 'current',
  pagination_class: 'pm-postlist-pagination',
  pagination_selector_id: '-pm-page-numbers',
  pagination_number_sub: '%%$_NUMBER_$%%',
  pagination_number_ident: '%%$_NUMBERIDENT_$%%',
  sub_title: '',
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
        }
    },

{   'remark': 'Test Case 4:pcom_process_template_list_info - authors - JSON error',
    'list': LIST_META_1['authors']['authors'],
    'base_url': ct.PCOM_SETTINGS_TYPE_AUTHORS,
    'settings': gb.DEFAULT_SETTINGS,
    'template_main_header_text': { ct.PCOM_SETTINGS_TYPE_SEARCH: "Results for: ",
    ct.PCOM_SETTINGS_TYPE_CATEGORIES: "Categories",
    ct.PCOM_SETTINGS_TYPE_AUTHORS: ct.PCOM_JSON_LOAD_ERROR,
    ct.PCOM_SETTINGS_TYPE_ARCHIVE: "Monthly Archives",
    ct.PCOM_SETTINGS_TYPE_POSTS: "Posts"
    },
    'fileroot': 'test1',
    'assertEqual': {\
        'result': """

window._postlist_test1 = {
  identifier: 'postlist-template',
  pagination_element: '        <span class="pm-page-numbers %%$_NUMBERIDENT_$%%">%%$_NUMBER_$%%</span>',
  page_numbers_selected_class: 'current',
  pagination_class: 'pm-postlist-pagination',
  pagination_selector_id: '-pm-page-numbers',
  pagination_number_sub: '%%$_NUMBER_$%%',
  pagination_number_ident: '%%$_NUMBERIDENT_$%%',
  sub_title: '',
  back_link: '',
  header: '      <h1 class="pm-template-header"></h1>',
  entries: [
  {
    posts_per_page: 5,
    posts: [
      '\\
            <div class="pm-post-content clearfix-small">\\
              <div class="pm-post-image">\\
              <a href="/authors/corvos-ae-team/">\\
                <img src="/images/CorvosTeam.jpg" alt="Corvos-AE-Team"  />\\
              </a></div><!-- end of .pm-post-image -->\\
              <div class="pm-blog-entry">\\
                <h2><a href="/authors/corvos-ae-team/">Corvos AE Team</a></h2>\\
                <p>General information and content from the Corvos Astro Engineering site</p>\\
              </div><!-- end of .pm-blog_entry -->\\
            </div><!-- end of .pm-post-content -->',
      '\\
            <div class="pm-post-content clearfix-small">\\
              <div class="pm-post-image">\\
              <a href="/authors/micky-h-corbett/">\\
                <img src="/images/CorvosDefaultImage.jpg" alt="Micky-H-Corbett"  />\\
              </a></div><!-- end of .pm-post-image -->\\
              <div class="pm-blog-entry">\\
                <h2><a href="/authors/micky-h-corbett/">Micky H Corbett</a></h2>\\
                <p>Aerospace and Space engineer with over 20 years experience in various fields including ion propulsion, aerospace systems, flight control, thruster control, prototype development. <br/>Other skills include cloud application development coding in multiple languages and enjoying the creative process!</p>\\
              </div><!-- end of .pm-blog_entry -->\\
            </div><!-- end of .pm-post-content -->',
      '\\
            <div class="pm-post-content clearfix-small">\\
              <div class="pm-post-image">\\
              <a href="/authors/albert/">\\
                <img src="/images/Polimorf-shapes-background-2.jpg" alt="Albert"  />\\
              </a></div><!-- end of .pm-post-image -->\\
              <div class="pm-blog-entry">\\
                <h2><a href="/authors/albert/">Albert</a></h2>\\
                <p></p>\\
              </div><!-- end of .pm-blog_entry -->\\
            </div><!-- end of .pm-post-content -->',
      '\\
            <div class="pm-post-content clearfix-small">\\
              <div class="pm-post-image">\\
              <a href="/authors/jim-o-neill/">\\
                <img src="/images/Polimorf-shapes-background-2.jpg" alt="Jim-O-Neill"  />\\
              </a></div><!-- end of .pm-post-image -->\\
              <div class="pm-blog-entry">\\
                <h2><a href="/authors/jim-o-neill/">Jim O&#39;Neill</a></h2>\\
                <p></p>\\
              </div><!-- end of .pm-blog_entry -->\\
            </div><!-- end of .pm-post-content -->',
      '\\
            <div class="pm-post-content clearfix-small">\\
              <div class="pm-post-image">\\
              <a href="/authors/contact/">\\
                <img src="/images/Polimorf-shapes-background-2.jpg" alt="Contact"  />\\
              </a></div><!-- end of .pm-post-image -->\\
              <div class="pm-blog-entry">\\
                <h2><a href="/authors/contact/">Contact</a></h2>\\
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
        }
    },
]


test_values_3 = [\
{   'remark': 'Test Case 1:pcom_process_archive_info - archive',
    'archive': ARCHIVE_1,
    'base_url': ct.PCOM_SETTINGS_TYPE_ARCHIVE,
    'base_name': '10-2018',
    'settings': gb.DEFAULT_SETTINGS,
    'template_main_header_text': { ct.PCOM_SETTINGS_TYPE_SEARCH: "Results for: ",
    ct.PCOM_SETTINGS_TYPE_CATEGORIES: ct.PCOM_JSON_LOAD_ERROR,
    ct.PCOM_SETTINGS_TYPE_AUTHORS: "Authors",
    ct.PCOM_SETTINGS_TYPE_ARCHIVE: "Monthly Archives",
    ct.PCOM_SETTINGS_TYPE_POSTS: "Posts"
    },
    'fileroot': 'test9',
    'assertEqual': {\
        'result': """

window._postlist_test9 = {
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
            <p class="pm-archive-links"><a href="/10-2018/09-2018">09-2018</a></p>\\
            <p class="pm-archive-links"><a href="/10-2018/10-2018">10-2018</a></p>\\
            <p class="pm-archive-links"><a href="/10-2018/09-2019">09-2019</a></p>\\
            <p class="pm-archive-links"><a href="/10-2018/10-2019">10-2019</a></p>\\
            <p class="pm-archive-links"><a href="/10-2018/06-2020">06-2020</a></p>\\
          </div><!-- end of .post -->'
    ],
    sticky: []
  }
  ]
};

        """,
        'processed': True
        }
    },

{   'remark': 'Test Case 2:pcom_process_archive_info - archive - load error',
    'archive': ARCHIVE_1,
    'base_url': ct.PCOM_SETTINGS_TYPE_ARCHIVE,
    'base_name': '10-2018',
    'settings': gb.DEFAULT_SETTINGS,
    'template_main_header_text': { ct.PCOM_SETTINGS_TYPE_SEARCH: "Results for: ",
    ct.PCOM_SETTINGS_TYPE_CATEGORIES: ct.PCOM_JSON_LOAD_ERROR,
    ct.PCOM_SETTINGS_TYPE_AUTHORS: "Authors",
    ct.PCOM_SETTINGS_TYPE_ARCHIVE: ct.PCOM_JSON_LOAD_ERROR,
    ct.PCOM_SETTINGS_TYPE_POSTS: "Posts"
    },
    'fileroot': 'test9',
    'assertEqual': {\
        'result': """

window._postlist_test9 = {
  identifier: 'postlist-template',
  pagination_element: '        <span class="pm-page-numbers %%$_NUMBERIDENT_$%%">%%$_NUMBER_$%%</span>',
  page_numbers_selected_class: 'current',
  pagination_class: 'pm-postlist-pagination',
  pagination_selector_id: '-pm-page-numbers',
  pagination_number_sub: '%%$_NUMBER_$%%',
  pagination_number_ident: '%%$_NUMBERIDENT_$%%',
  sub_title: '',
  back_link: '',
  header: '      <h1 class="pm-template-header"></h1>',
  entries: [
  {
    posts_per_page: 9999,
    posts: [
'\\
          <div class="post">\\
            <p class="pm-archive-links"><a href="/10-2018/09-2018">09-2018</a></p>\\
            <p class="pm-archive-links"><a href="/10-2018/10-2018">10-2018</a></p>\\
            <p class="pm-archive-links"><a href="/10-2018/09-2019">09-2019</a></p>\\
            <p class="pm-archive-links"><a href="/10-2018/10-2019">10-2019</a></p>\\
            <p class="pm-archive-links"><a href="/10-2018/06-2020">06-2020</a></p>\\
          </div><!-- end of .post -->'
    ],
    sticky: []
  }
  ]
};

        """,
        'processed': True
        }
    },

{   'remark': 'Test Case 3:pcom_process_archive_info - archive - load error - empty created archive',
    'archive': ARCHIVE_2,
    'base_url': ct.PCOM_SETTINGS_TYPE_ARCHIVE,
    'base_name': '10-2018',
    'settings': gb.DEFAULT_SETTINGS,
    'template_main_header_text': { ct.PCOM_SETTINGS_TYPE_SEARCH: "Results for: ",
    ct.PCOM_SETTINGS_TYPE_CATEGORIES: ct.PCOM_JSON_LOAD_ERROR,
    ct.PCOM_SETTINGS_TYPE_AUTHORS: "Authors",
    ct.PCOM_SETTINGS_TYPE_ARCHIVE: ct.PCOM_JSON_LOAD_ERROR,
    ct.PCOM_SETTINGS_TYPE_POSTS: "Posts"
    },
    'fileroot': 'test7',
    'assertEqual': {\
        'result': """

window._postlist_test7 = {
  identifier: 'postlist-template',
  pagination_element: '        <span class="pm-page-numbers %%$_NUMBERIDENT_$%%">%%$_NUMBER_$%%</span>',
  page_numbers_selected_class: 'current',
  pagination_class: 'pm-postlist-pagination',
  pagination_selector_id: '-pm-page-numbers',
  pagination_number_sub: '%%$_NUMBER_$%%',
  pagination_number_ident: '%%$_NUMBERIDENT_$%%',
  sub_title: '',
  back_link: '',
  header: '      <h1 class="pm-template-header"></h1>',
  entries: [
  {
    posts_per_page: 9999,
    posts: [
    ],
    sticky: []
  }
  ]
};

        """,
        'processed': True
        }
    },
]

test_values_4 = [\
{   'remark': 'Test Case 1:pcom_update_template_meta - no template content',
    'template_content': '',
    'info': {},
    'no_meta': False,
    'assertEqual': ''
    },

{   'remark': 'Test Case 2:pcom_update_template_meta - template content - no info data',
    'template_content': TEMP_CONTENT_1,
    'info': {\
        'title': '',
        'description': '',
        'sub_js_root': '',
        'sub_fileroot': ''
    },
    'no_meta': False,
    'assertEqual': """

<!doctype html>
<html class="" lang="en">
<head>
  <title>Archive - </title>
  <meta name="description" content="Archive">
</head>
<body class="body-archive">
<script src="/js/js-lists/postlist--archive.js" data-template-constant-name="_postlist_archive"></script>
</body>
</html>

    """
    },

{   'remark': 'Test Case 3:pcom_update_template_meta - template content - info data',
    'template_content': TEMP_CONTENT_1,
    'info': {\
        'title': 'This page',
        'description': "About this page 'Otherwise'",
        'sub_js_root': '_06_1020',
        'sub_fileroot': 'Something'
    },
    'no_meta': False,
    'assertEqual': """

<!doctype html>
<html class="" lang="en">
<head>
  <title>Archive - This page</title>
  <meta name="description" content="Archive - About this page 'Otherwise'">
</head>
<body class="body-archive_06_1020">
<script src="/js/js-lists/postlist--archive_06_1020.js" data-template-constant-name="_postlist_archiveSomething"></script>
</body>
</html>

    """
    },
]

test_values_5 = [\
{   'remark': 'Test Case 1:pcom_create_template_info_references - empty list',
    'list': [\
    ],
    'settings': gb.DEFAULT_SETTINGS,
    'base_string': 'something_here',
    'assertEqual': []
    },

{   'remark': 'Test Case 2:pcom_create_template_info_references - list - one entry',
    'list': [\
        {
            'name': 'Name1',
            'description': 'A brief description'
        }
    ],
    'settings': gb.DEFAULT_SETTINGS,
    'base_string': 'something_here_again',
    'assertEqual': [
          {\
            'title': 'Name1',
            'description': 'A brief description',
            'sub_js_root': '-name1',
            'full_js_root': 'something_here_again-name1',
            'sub_fileroot': '_name1',
            'fileroot': 'something_here_again_name1',
            'js_filename': 'postlist--something_here_again-name1.js',
            'test_html': 'something_here_again-name1.html',
            'url': '/something_here_again/name1/',
            's3url': 'something_here_again/name1/index.html',
            'js_constant': '',
            'template_content': ''
          }
        ]
    },
{   'remark': 'Test Case 3:pcom_create_template_info_references - list - two entries',
    'list': [\
        {
            'name': 'Name1',
            'description': 'A brief description'
        },
        {
            'name': 'Name2',
            'description': 'Another brief description'
        }
    ],
    'settings': gb.DEFAULT_SETTINGS,
    'base_string': 'something_here_again',
    'assertEqual': [
          {
            'title': 'Name1',
            'description': 'A brief description',
            'sub_js_root': '-name1',
            'full_js_root': 'something_here_again-name1',
            'sub_fileroot': '_name1',
            'fileroot': 'something_here_again_name1',
            'js_filename': 'postlist--something_here_again-name1.js',
            'test_html': 'something_here_again-name1.html',
            'url': '/something_here_again/name1/',
            's3url': 'something_here_again/name1/index.html',
            'js_constant': '',
            'template_content': ''
          },
          {
            'title': 'Name2',
            'description': 'Another brief description',
            'sub_js_root': '-name2',
            'full_js_root': 'something_here_again-name2',
            'sub_fileroot': '_name2',
            'fileroot': 'something_here_again_name2',
            'js_filename': 'postlist--something_here_again-name2.js',
            'test_html': 'something_here_again-name2.html',
            'url': '/something_here_again/name2/',
            's3url': 'something_here_again/name2/index.html',
            'js_constant': '',
            'template_content': ''
          }
        ]
    },
]

test_values_6 = [\
{   'remark': 'Test Case 1:pcom_create_archive_info_references - empty list',
    'list': [\
    ],
    'settings': gb.DEFAULT_SETTINGS,
    'base_string': 'something_here',
    'assertEqual': []
    },

{   'remark': 'Test Case 2:pcom_create_archive_info_references - list - one entry',
    'list': [\
        {
            'name': 'Name1',
            'fileroot': 'name1'
        }
    ],
    'settings': gb.DEFAULT_SETTINGS,
    'base_string': 'something_here_again',
    'assertEqual': [
          {\
            'title': 'Name1',
            'description': '',
            'sub_js_root': '-Name1',
            'full_js_root': 'something_here_again-Name1',
            'sub_fileroot': '_name1',
            'fileroot': 'something_here_again_name1',
            'js_filename': 'postlist--something_here_again-Name1.js',
            'test_html': 'something_here_again-Name1.html',
            'url': '/something_here_again/Name1/',
            's3url': 'something_here_again/Name1/index.html',
            'js_constant': '',
            'template_content': ''
          }
        ]
    },
{   'remark': 'Test Case 3:pcom_create_archive_info_references - list - two entries',
    'list': [\
        {
            'name': 'Name1',
            'fileroot': 'name1'
        },
        {
            'name': 'Name2',
            'fileroot': 'name2'
        }
    ],
    'settings': gb.DEFAULT_SETTINGS,
    'base_string': 'something_here_again',
    'assertEqual': [
          {
            'title': 'Name1',
            'description': '',
            'sub_js_root': '-Name1',
            'full_js_root': 'something_here_again-Name1',
            'sub_fileroot': '_name1',
            'fileroot': 'something_here_again_name1',
            'js_filename': 'postlist--something_here_again-Name1.js',
            'test_html': 'something_here_again-Name1.html',
            'url': '/something_here_again/Name1/',
            's3url': 'something_here_again/Name1/index.html',
            'js_constant': '',
            'template_content': ''
          },
          {
            'title': 'Name2',
            'description': '',
            'sub_js_root': '-Name2',
            'full_js_root': 'something_here_again-Name2',
            'sub_fileroot': '_name2',
            'fileroot': 'something_here_again_name2',
            'js_filename': 'postlist--something_here_again-Name2.js',
            'test_html': 'something_here_again-Name2.html',
            'url': '/something_here_again/Name2/',
            's3url': 'something_here_again/Name2/index.html',
            'js_constant': '',
            'template_content': ''
          }
        ]
    },
]
