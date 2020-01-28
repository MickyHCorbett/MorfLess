import unittest
import libraries.morflessLibs as libs

# import test values and expected outputs
# main includes sidebar data
import unit.lists_test_io.lists_1_functions_io as tv

# define settings element for test
settings = libs.globals.DEFAULT_SETTINGS

class ListsHandler1Case(unittest.TestCase):

    def test_pcom_update_authors_from_settings(self):

        for test in tv.test_values_1:

            print('\n' + test['remark'] + '\n')

            authors = test['inputs']['authors']
            settings_authors = test['inputs']['settings_authors']
            posts_per_page = test['inputs']['ppp']

            result = libs.lists.pcom_update_authors_from_settings(authors,settings_authors,posts_per_page)
            print(result)

            # check asserts in
            self.assertEqual(test['assertEqual'], result)
            self.assertNotEqual(test['assertNotEqual'], result)

        print('\n\n===== test_pcom_update_authors_from_settings - END \n\n')


if __name__ == '__main__':
    unittest.main()
