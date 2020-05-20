import unittest
import libraries.morflessLibs as libs

# import test values and expected outputs
# main includes sidebar data
import unit.lists_test_io.lists_1_functions_io as tv

from unit.lists_test_io.lists_supplemental import POSTLIST_1, CONTACT_PAGE_POST
from unit.lists_test_io.lists_supplemental import TEMPLATE_SEARCH_CONTENT
from unit.lists_test_io.lists_supplemental import TEMPLATE_POSTS, TEMPLATE_INDEX
from unit.lists_test_io.lists_supplemental import AUTHORS_1, ARCHIVE_1

from fixtures.decorators import testCall

class ListsHandler2Case(unittest.TestCase):

    # set up and tear down reset to default settings
    def setUp(self):
        self.maxDiff= None
        self.settings = libs.string_processes.pcom_build_dictionary(libs.globals.DEFAULT_SETTINGS)

    def tearDown(self):
        self.settings = dict()

    @testCall
    def test_pcom_order_postlist_posts(self):


        print('\nTest 1: pcom_order_postlist_posts - highest first\n')
        posts = POSTLIST_1['posts']
        result = libs.lists.pcom_order_postlist_posts(posts,up_down=True)
        print(result)

        # check index
        for ind,post in enumerate(result):
            with self.subTest(msg='Highest first = '+str(ind+1)):
                post_index = len(result) - ind
                self.assertEqual(post['index'],post_index)
                print(f"Post {post['postname']} index {post['index']}")

        print('\nTest 2: pcom_order_postlist_posts - lowest first\n')
        posts = POSTLIST_1['posts']
        result = libs.lists.pcom_order_postlist_posts(posts,up_down=False)
        print(result)

        # check index
        for ind,post in enumerate(result):
            with self.subTest(msg='Lowest first = '+str(ind+1)):
                post_index = ind + 1
                self.assertEqual(post['index'],post_index)
                print(f"Post {post['postname']} index {post['index']}")

    @testCall
    def test_pcom_find_post(self):

        print('\nTest 1: pcom_find_post - contact.page\n')
        result = libs.lists.pcom_find_post(POSTLIST_1,'contact.page')
        print(result)

        # check description
        self.assertEqual(result['description'],'Morfless Contact page')
        self.assertNotEqual(result['description'],'A new post about something again')
        self.assertEqual(result,CONTACT_PAGE_POST)

        print('\nTest 2: pcom_find_post - test3.post\n')
        result = libs.lists.pcom_find_post(POSTLIST_1,'test3.post')
        print(result)

        # check description
        self.assertEqual(result['description'],'A new post about something again')
        self.assertNotEqual(result['description'],'Morfless Contact page')

    @testCall
    def test_pcom_find_template_search_content(self):

        print('\nTest 1: pcom_find_template_search_content - posts.page\n')
        test_settings = self.settings
        test_settings['template_search_content'] = TEMPLATE_SEARCH_CONTENT
        result = libs.lists.pcom_find_template_search_content(test_settings,'posts.page')
        print(result)

        # check content
        self.assertEqual(result,TEMPLATE_POSTS)

        print('\nTest 2: pcom_find_template_search_content - index.page\n')
        test_settings = self.settings
        test_settings['template_search_content'] = TEMPLATE_SEARCH_CONTENT
        result = libs.lists.pcom_find_template_search_content(test_settings,'index.page')
        print(result)

        # check content
        self.assertEqual(result,TEMPLATE_INDEX)

        print('\nTest 3: pcom_find_template_search_content - template.page - not in list\n')
        test_settings = self.settings
        test_settings['template_search_content'] = TEMPLATE_SEARCH_CONTENT
        result = libs.lists.pcom_find_template_search_content(test_settings,'template.page')
        print(result)

        # check content
        self.assertEqual(result,{'name': libs.constants.PCOM_NO_ENTRY })

    @testCall
    def test_pcom_find_sub_list(self):

        print('\nTest 1: test_pcom_find_sub_list - no posts\n')
        result = libs.lists.pcom_find_sub_list([],[],'categories','something',type='post',get_all=False)
        print(f"Sub list: {result}")

        # check content
        self.assertEqual(result,[])

        print('\nTest 2: test_pcom_find_sub_list - all posts for "things to write about"\n')
        sub_type = "things to write about"
        result = libs.lists.pcom_find_sub_list(POSTLIST_1['posts'],AUTHORS_1,'categories',sub_type,'post',False)

        # check content
        check_list = ['test1.post']
        for ind,post in enumerate(result):
            with self.subTest(msg='Post in list: '+str(ind+1)):
                self.assertEqual(post['postname'],check_list[ind])
                print(f"Post {post['postname']}")

        print('\nTest 3: test_pcom_find_sub_list - all posts for "things to write about" but type = txt\n')
        sub_type = "things to write about"
        result = libs.lists.pcom_find_sub_list(POSTLIST_1['posts'],AUTHORS_1,'categories',sub_type,'txt',False)
        print(f"Sub list: {result}")

        # check content
        self.assertEqual(result,[])

        print("\nTest 4: test_pcom_find_sub_list - all posts for author Jim O'Neill\n")
        sub_type = "Jim O'Neill"
        result = libs.lists.pcom_find_sub_list(POSTLIST_1['posts'],AUTHORS_1,'authors',sub_type,'post',False)

        # check content
        check_list = ['about-this.post']
        for ind,post in enumerate(result):
            with self.subTest(msg='Post in list: '+str(ind+1)):
                self.assertEqual(post['postname'],check_list[ind])
                print(f"Post {post['postname']}")

        print("\nTest 5: test_pcom_find_sub_list - all entries for author Jim O'Neill\n")
        sub_type = "Jim O'Neill"
        result = libs.lists.pcom_find_sub_list(POSTLIST_1['posts'],AUTHORS_1,'authors',sub_type,'post',True)

        # check content
        check_list = ['about.page','about-this.post']
        for ind,post in enumerate(result):
            with self.subTest(msg='Post in list: '+str(ind+1)):
                self.assertEqual(post['postname'],check_list[ind])
                print(f"Post {post['postname']}")

        print("\nTest 6: test_pcom_find_sub_list - all entries for author Jim O'Neill but using shortname\n")
        sub_type = "Jimbo"
        result = libs.lists.pcom_find_sub_list(POSTLIST_1['posts'],AUTHORS_1,'authors',sub_type,'post',True)

        # check content
        check_list = ['about.page','about-this.post']
        for ind,post in enumerate(result):
            with self.subTest(msg='Post in list: '+str(ind+1)):
                self.assertEqual(post['postname'],check_list[ind])
                print(f"Post {post['postname']}")

        print("\nTest 7: test_pcom_find_sub_list - all pages for author Micky H Corbett but using shortname\n")
        sub_type = "Micky"
        result = libs.lists.pcom_find_sub_list(POSTLIST_1['posts'],AUTHORS_1,'authors',sub_type,'page',False)

        # check content
        check_list = ['contact.page']
        for ind,post in enumerate(result):
            with self.subTest(msg='Post in list: '+str(ind+1)):
                self.assertEqual(post['postname'],check_list[ind])
                print(f"Post {post['postname']}")

    @testCall
    def test_pcom_find_sub_list_archive(self):

        print('\nTest 1: test_pcom_find_sub_list archive - no posts\n')
        no_archive = {'created': []}
        type = ''
        result = libs.lists.pcom_find_sub_list_archive(no_archive,POSTLIST_1,'10-2018',type)
        self.assertEqual(result,[])
        print(f"Sub list: {result}")

        print('\nTest 2: test_pcom_find_sub_list archive - 10-2018\n')
        result = libs.lists.pcom_find_sub_list_archive(ARCHIVE_1,POSTLIST_1,'10-2018',type)

        # check content
        check_list = ['test3.post']
        no_check_list = ['about.page']

        for ind,post in enumerate(result):
            with self.subTest(msg='Post in list: '+str(ind+1)):
                self.assertEqual(post['postname'],check_list[ind])
                print(f"Post {post['postname']}")

        for ind,post in enumerate(result):
            with self.subTest(msg='Post not in list: '+str(ind+1)):
                self.assertNotEqual(post['postname'],no_check_list[ind])
                print(f"Entry {no_check_list[ind]} not in list")

        print(f"Sub list: {result}")

        print('\nTest 3: test_pcom_find_sub_list archive - no posts for entry name\n')
        type = 'page'
        result = libs.lists.pcom_find_sub_list_archive(ARCHIVE_1,POSTLIST_1,'67-000',type)
        self.assertEqual(result,[])
        print(f"Sub list: {result}")

    @testCall
    def test_pcom_create_posts_pages_array(self):

        print('\nTest 1: pcom_create_posts_pages_array - no posts\n')
        posts = []
        type = True
        result = libs.lists.pcom_create_posts_pages_array(posts,type)
        self.assertEqual(result,[])
        print(f"Sub list: {result}")

        print('\nTest 2: pcom_create_posts_pages_array - posts array\n')
        type = True
        result = libs.lists.pcom_create_posts_pages_array(POSTLIST_1['posts'],type)
        print(f"Sub list: {result}")

        # check content
        check_list = ['test3.post', 'test2.post', 'test1.post', 'about-this.post']
        no_check_list = ['contact.page','about.page']

        for ind,post in enumerate(result):
            with self.subTest(msg='Post in list: '+str(ind+1)):
                self.assertEqual(post['postname'],check_list[ind])
                print(f"Post {post['postname']}")

        for ind,post in enumerate(no_check_list):
            with self.subTest(msg='Post not in list: '+str(ind+1)):
                self.assertNotIn(no_check_list[ind],result)
                print(f"Entry {no_check_list[ind]} not in list")

        print('\nTest 3: pcom_create_posts_pages_array - pages array\n')
        type = False
        result = libs.lists.pcom_create_posts_pages_array(POSTLIST_1['posts'],type)
        print(f"Sub list: {result}")

        # check content
        no_check_list = ['test3.post', 'test2.post', 'test1.post', 'about-this.post']
        check_list = ['contact.page','about.page']

        for ind,post in enumerate(result):
            with self.subTest(msg='Post in list: '+str(ind+1)):
                self.assertEqual(post['postname'],check_list[ind])
                print(f"Post {post['postname']}")

        for ind,post in enumerate(no_check_list):
            with self.subTest(msg='Post not in list: '+str(ind+1)):
                self.assertNotIn(no_check_list[ind],result)
                print(f"Entry {no_check_list[ind]} not in list")

    @testCall
    def test_pcom_calculate_posts_per_page(self):

        print('\nTest 1: pcom_calculate_posts_per_page - no_posts=9, posts_per_page=0, no_of_pages=1\n')
        no_posts = 0
        posts_per_page = 0
        no_of_pages = 1
        result = libs.lists.pcom_calculate_posts_per_page(no_posts,posts_per_page)
        print(f"No of pages: {result}")
        self.assertEqual(result,no_of_pages)

        print('\nTest 2: pcom_calculate_posts_per_page - no_posts=7, posts_per_page=1, no_of_pages=7\n')
        no_posts = 7
        posts_per_page = 1
        no_of_pages = 7
        result = libs.lists.pcom_calculate_posts_per_page(no_posts,posts_per_page)
        print(f"No of pages: {result}")
        self.assertEqual(result,no_of_pages)

        print('\nTest 3: pcom_calculate_posts_per_page - no_posts=9, posts_per_page=2, no_of_pages=5\n')
        no_posts = 9
        posts_per_page = 2
        no_of_pages = 5
        result = libs.lists.pcom_calculate_posts_per_page(no_posts,posts_per_page)
        print(f"No of pages: {result}")
        self.assertEqual(result,no_of_pages)

        print('\nTest 4: pcom_calculate_posts_per_page - no_posts=4, posts_per_page=2, no_of_pages=2\n')
        no_posts = 4
        posts_per_page = 2
        no_of_pages = 2
        result = libs.lists.pcom_calculate_posts_per_page(no_posts,posts_per_page)
        print(f"No of pages: {result}")
        self.assertEqual(result,no_of_pages)

    @testCall
    def test_pcom_find_sticky_posts(self):

        sticky_ind = libs.constants.PCOM_POST_LIST_STICKY_INDICATOR

        print('\nTest 1: pcom_find_sticky_posts - no sticky marker - no manual sticky\n')
        content_list = "test1.post, test2.post, test3.post"
        test_posts_out = ['test1.post', 'test2.post', 'test3.post']
        test_sticky_out = []
        posts_out,sticky_out = libs.lists.pcom_find_sticky_posts(content_list,manual_sticky=False)

        print(f"Posts list: {posts_out}")
        print(f"Sticky list: {sticky_out}")
        self.assertEqual(posts_out,test_posts_out)
        self.assertEqual(sticky_out,test_sticky_out)

        print('\nTest 2: pcom_find_sticky_posts - sticky marker - no manual sticky\n')
        content_list = f"{sticky_ind}test1.post, test2.post, test3.post"
        test_posts_out = [f"{sticky_ind}test1.post", 'test2.post', 'test3.post']
        test_sticky_out = []
        posts_out,sticky_out = libs.lists.pcom_find_sticky_posts(content_list,manual_sticky=False)

        print(f"Posts list: {posts_out}")
        print(f"Sticky list: {sticky_out}")
        self.assertEqual(posts_out,test_posts_out)
        self.assertEqual(sticky_out,test_sticky_out)

        print('\nTest 3: pcom_find_sticky_posts - sticky marker - manual sticky\n')
        content_list = f"{sticky_ind}test1.post, test2.post, test3.post"
        test_posts_out = ['test2.post', 'test3.post']
        test_sticky_out = ["test1.post"]
        posts_out,sticky_out = libs.lists.pcom_find_sticky_posts(content_list,manual_sticky='True')

        print(f"Posts list: {posts_out}")
        print(f"Sticky list: {sticky_out}")
        self.assertEqual(posts_out,test_posts_out)
        self.assertEqual(sticky_out,test_sticky_out)

        print('\nTest 4: pcom_find_sticky_posts - no posts - manual sticky\n')
        content_list = ''
        test_posts_out = ['']
        test_sticky_out = []
        posts_out,sticky_out = libs.lists.pcom_find_sticky_posts(content_list,manual_sticky='True')

        print(f"Posts list: {posts_out}")
        print(f"Sticky list: {sticky_out}")
        self.assertEqual(posts_out,test_posts_out)
        self.assertEqual(sticky_out,test_sticky_out)

    @testCall
    def test_pcom_find_sticky_posts_by_meta(self):

        print('\nTest 1: pcom_find_sticky_posts_by_meta - no posts\n')
        posts = []
        test_posts_out = []
        test_sticky_out = []
        posts_out,sticky_out = libs.lists.pcom_find_sticky_posts_by_meta(posts)
        print(f"Posts list: {posts_out}")
        print(f"Sticky list: {sticky_out}")
        self.assertEqual(posts_out,test_posts_out)
        self.assertEqual(sticky_out,test_sticky_out)

        print('\nTest 2: pcom_find_sticky_posts_by_meta - posts\n')
        test_posts_out = ['contact.page','test3.post','about.page', 'test2.post']
        test_sticky_out = ['test1.post', 'about-this.post']
        posts_out,sticky_out = libs.lists.pcom_find_sticky_posts_by_meta(POSTLIST_1['posts'])

        for ind,post in enumerate(posts_out):
            with self.subTest(msg='Post in posts list: '+str(ind+1)):
                self.assertEqual(post['postname'],test_posts_out[ind])
                print(f"Post in posts list: {post['postname']}")

        for ind,post in enumerate(sticky_out):
            with self.subTest(msg='Post in sticky list: '+str(ind+1)):
                self.assertEqual(post['postname'],test_sticky_out[ind])
                print(f"Post in sticky list: {post['postname']}")

if __name__ == '__main__':
    unittest.main()
