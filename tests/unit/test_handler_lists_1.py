import unittest
import libraries.morflessLibs as libs

# import test values and expected outputs
# main includes sidebar data
import unit.lists_test_io.lists_1_functions_io as tv
from fixtures.decorators import testCall

class ListsHandler1Case(unittest.TestCase):

    # set up and tear down reset to default settings
    def setUp(self):
        self.settings = libs.globals.DEFAULT_SETTINGS
        self.maxDiff = None

    def tearDown(self):
        self.settings = libs.globals.DEFAULT_SETTINGS

    @testCall
    def test_pcom_update_authors_from_settings(self):

        for ind,test in enumerate(tv.test_values_1):

            print('\n' + test['remark'] + '\n')

            authors = test['inputs']['authors']
            settings_authors = test['inputs']['settings_authors']
            self.settings['posts_per_page'] = test['inputs']['ppp']
            self.settings['default_thumbnail'] = test['inputs']['default_thumb_link']
            self.settings['default_author'] = test['inputs']['default_author']

            print(settings_authors)

            result = libs.lists.pcom_update_authors_from_settings(authors,settings_authors,self.settings)
            print(result)

            # check asserts in
            with self.subTest(i=ind+1):
                self.assertEqual(test['assertEqual'], result)
                self.assertNotEqual(test['assertNotEqual'], result)



if __name__ == '__main__':
    unittest.main()
