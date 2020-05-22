import unittest
import libraries.morflessLibs as libs
import datetime

# import test values and expected outputs
# main includes sidebar data

from unit.lists_test_io.lists_supplemental import DEPENDENCIES_1
from unit.lists_test_io.lists_supplemental import DEPENDENCIES_2
from unit.lists_test_io.lists_supplemental import DEPENDENCIES_3
from unit.lists_test_io.lists_supplemental import DEPENDENCIES_4

from fixtures.decorators import testCall

class ListsHandler3Case(unittest.TestCase):

    # set up and tear down reset to default settings
    def setUp(self):
        self.maxDiff= None
        self.settings = libs.string_processes.pcom_build_dictionary(libs.globals.DEFAULT_SETTINGS)

    def tearDown(self):
        self.settings = dict()

    @testCall
    def test_pcom_get_dependency(self):

        print('\nTest 1: pcom_get_dependency - empty list\n')
        result = libs.lists.pcom_get_dependency([],'test1.post')
        print(result)
        self.assertEqual(result,{})

        print('\nTest 2: pcom_get_dependency - puppies_2.txt - no result\n')
        result = libs.lists.pcom_get_dependency(DEPENDENCIES_1,'puppies_2.txt')
        print(result)
        self.assertEqual(result,{})

        print('\nTest 3: pcom_get_dependency - test3.post\n')
        result = libs.lists.pcom_get_dependency(DEPENDENCIES_1,'test3.post')
        print(result)
        out = { "filename": "test3.post",
                    "dependencies": [
                        "puppies_2.txt"
                    ]
            }
        self.assertEqual(result,out)

    @testCall
    def test_pcom_update_dependencies(self):

        print('\nTest 1: pcom_update_dependencies - empty list\n')
        result = libs.lists.pcom_update_dependencies([],'test1.post','insert2.txt')
        print(result)
        self.assertEqual(result,[])

        print('\nTest 2: pcom_update_dependencies - insert2.txt in test1.post\n')
        result = libs.lists.pcom_update_dependencies(DEPENDENCIES_1,'test1.post','insert2.txt')

        # get test1.post entry
        test_out = {}
        for entry in result:
            if entry['filename'] == 'test1.post':
                test_out = entry

        print(test_out)

        out = { "filename": "test1.post",
                    "dependencies": [
                        "puppies.txt",
                        "settings.txt",
                        "insert2.txt"
                    ]
            }
        self.assertEqual(out,test_out)

        print('\nTest 3: pcom_update_dependencies - puppies.txt in about.page - no change\n')
        result = libs.lists.pcom_update_dependencies(DEPENDENCIES_1,'about.page','puppies.txt')

        # get test1.post entry
        test_out = {}
        for entry in result:
            if entry['filename'] == 'about.page':
                test_out = entry

        print(test_out)

        out = { "filename": "about.page",
                    "dependencies": [
                        "puppies.txt"
                    ]
            }
        self.assertEqual(out,test_out)

        print('\nTest 4: pcom_update_dependencies - insert3.txt in new file new_page.page\n')

        print('\nCheck new_page.page is not in dependencies\n')
        result1 = libs.lists.pcom_get_dependency(DEPENDENCIES_1,'new_page.page')
        print(f"Entry for new_page.page: {result1}")
        self.assertEqual(result1,{})

        print('\nAdd insert3.txt to new_page.page\n')

        result = libs.lists.pcom_update_dependencies(DEPENDENCIES_1,'new_page.page','insert3.txt')

        # get test1.post entry
        test_out = {}
        for entry in result:
            if entry['filename'] == 'new_page.page':
                test_out = entry

        print(test_out)

        out = { "filename": "new_page.page",
                    "dependencies": [
                        "insert3.txt"
                    ]
            }
        self.assertEqual(out,test_out)

    @testCall
    def test_pcom_find_dependencies(self):

        print('\nTest 1: pcom_update_dependencies - empty list\n')
        result = libs.lists.pcom_find_dependencies([],'test1.post')
        print(result)
        self.assertEqual(result,[])


        print('\nTest 2: pcom_update_dependencies - search_insert.dat\n')
        result = libs.lists.pcom_find_dependencies(DEPENDENCIES_1,'search_insert.dat')
        print(result)
        self.assertEqual(result,['search.page'])

        print('\nTest 3: pcom_update_dependencies - extra.txt\n')
        result = libs.lists.pcom_find_dependencies(DEPENDENCIES_1,'extra.txt')
        print(result)
        self.assertEqual(result,['index.page','404.page'])


    @testCall
    def test_pcom_delete_dependencies_file(self):

        print('\nTest 1: pcom_delete_dependencies_file - empty list\n')
        result = libs.lists.pcom_delete_dependencies_file([],'index.page')
        print(result)
        self.assertEqual(result,[])

        print('\nTest 2: pcom_delete_dependencies_file - index.page\n')
        result = libs.lists.pcom_delete_dependencies_file(DEPENDENCIES_2,'index.page')
        print(result)
        self.assertEqual(result,DEPENDENCIES_3)

    @testCall
    def test_pcom_delete_dependencies_insert(self):

        print('\nTest 1: pcom_delete_dependencies_insert - empty list\n')
        result = libs.lists.pcom_delete_dependencies_insert([],'index.page','insert2.txt')
        print(result)
        self.assertEqual(result,[])

        print('\nTest 2: pcom_delete_dependencies_insert - extra1.txt from index.page\n')
        result = libs.lists.pcom_delete_dependencies_insert(DEPENDENCIES_4,'index.page','extra1.txt')

        result1 = libs.lists.pcom_get_dependency(DEPENDENCIES_4,'index.page')
        print(result1)
        out = { "filename": "index.page",
                    "dependencies": [
                        "settings.txt",
                        "something.else"
                    ]
            }
        self.assertEqual(result1,out)

    @testCall
    def test_pcom_post_process_dependencies(self):

        print('\nTest 1: pcom_post_process_dependencies - empty list no filename or valid inserts\n')
        result = libs.lists.pcom_post_process_dependencies([],'',[])
        print(result)
        self.assertEqual(result,[])

        print('\nTest 2: pcom_post_process_dependencies - delete 2 files - settings.txt included\n')
        # set input
        input = \
        [
            {
                "filename": "404.page",
                "dependencies": [
                    "settings.txt",
                    "extra2.txt",
                    "something.else"
                ]
            }
        ]
        output = \
        [
            {
                "filename": "404.page",
                "dependencies": [
                    "settings.txt"
                ]
            }
        ]
        valid_inserts = ["settings.txt"]

        result = libs.lists.pcom_post_process_dependencies(input,'404.page',valid_inserts)
        print(result)
        self.assertEqual(result,output)

        print('\nTest 3: pcom_post_process_dependencies - no valid inserts- no settings.txt - will delete file\n')
        # set input
        input = \
        [
            {
                "filename": "404.page",
                "dependencies": [
                    "extra2.txt",
                    "something.else"
                ]
            }
        ]
        output = []
        valid_inserts = []

        result = libs.lists.pcom_post_process_dependencies(input,'404.page',valid_inserts)
        print(result)
        self.assertEqual(result,output)

        print('\nTest 4: pcom_post_process_dependencies - all files valid - settings.txt included\n')
        # set input
        input = \
        [
            {
                "filename": "404.page",
                "dependencies": [
                    "settings.txt",
                    "extra2.txt",
                    "something.else"
                ]
            }
        ]
        output = \
        [
            {
                "filename": "404.page",
                "dependencies": [
                    "extra2.txt",
                    "something.else"
                ]
            }
        ]
        valid_inserts = ["extra2.txt","something.else"]

        result = libs.lists.pcom_post_process_dependencies(input,'404.page',valid_inserts)
        print(result)
        self.assertEqual(result,output)

    @testCall
    def test_pcom_get_date(self):

        print('\nTest 1: pcom_get_date - UK format\n')
        local_date = datetime.datetime.now().strftime("%d/%m/%Y")
        local_date_parts = local_date.split("/")

        result = libs.lists.pcom_get_date(libs.constants.PCOM_UK_DATE_FORMAT)
        print(result)
        result_parts = result.split("/")

        for ind,part in enumerate(local_date_parts):
            self.assertEqual(part,result_parts[ind])


        print('\nTest 2: pcom_get_date - US format\n')
        local_date = datetime.datetime.now().strftime("%m/%d/%Y")
        local_date_parts = local_date.split("/")

        result = libs.lists.pcom_get_date(libs.constants.PCOM_US_DATE_FORMAT)
        print(result)
        result_parts = result.split("/")

        for ind,part in enumerate(local_date_parts):
            self.assertEqual(part,result_parts[ind])


        print('\nTest 3: pcom_get_date - any other format - default UK\n')
        local_date = datetime.datetime.now().strftime("%d/%m/%Y")
        local_date_parts = local_date.split("/")

        result = libs.lists.pcom_get_date('something')
        print(result)
        result_parts = result.split("/")

        for ind,part in enumerate(local_date_parts):
            self.assertEqual(part,result_parts[ind])

    @testCall
    def test_pcom_get_comma_list(self):

        print('\nTest 1: pcom_get_comma_list - empty list')
        list = ''
        result = libs.lists.pcom_get_comma_list(list)
        print(result)
        self.assertEqual(result,[''])

        print('\nTest 2: pcom_get_comma_list - non-empty list')
        list = 'this.one, that.one'
        result = libs.lists.pcom_get_comma_list(list)
        print(result)
        self.assertEqual(result,['this.one','that.one'])

    @testCall
    def test_pcom_create_comma_list_from_array(self):

        print('\nTest 1: pcom_create_comma_list_from_array - empty list')
        list = []
        result = libs.lists.pcom_create_comma_list_from_array(list)
        print(result)
        self.assertEqual(result,'')

        print('\nTest 2: pcom_create_comma_list_from_array - non-empty list')
        list = ['this.one', 'that.one']
        result = libs.lists.pcom_create_comma_list_from_array(list)
        print(result)
        self.assertEqual(result,'this.one,that.one')

    @testCall
    def test_pcom_create_comma_list_from_dict(self):

        print('\nTest 1: pcom_create_comma_list_from_array - empty dictionary')
        dict = {}
        result = libs.lists.pcom_create_comma_list_from_dict(dict)
        print(result)
        self.assertEqual(result,'')

        print('\nTest 2: pcom_create_comma_list_from_array - non-empty dictionary')
        dict = {'this.one': 'one', 'that.one': 'that'}
        result = libs.lists.pcom_create_comma_list_from_dict(dict)
        print(result)
        self.assertEqual(result,'this.one,that.one')


if __name__ == '__main__':
    unittest.main()
