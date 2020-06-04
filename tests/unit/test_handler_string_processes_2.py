import unittest
import libraries.morflessLibs as libs

# import test values and expected outputs
# main includes sidebar data
import unit.string_processes_test_io.string_processes_2_functions_io as tv
from fixtures.decorators import testCall
# define settings element for test
settings = libs.globals.DEFAULT_SETTINGS

class StringProcesses2HandlerCase(unittest.TestCase):

    def setUp(self):
        self.settings = libs.string_processes.pcom_build_dictionary(libs.globals.DEFAULT_SETTINGS)

    def tearDown(self):
        self.settings = dict()

    @testCall
    def test_pcom_create_template_fileroot(self):

        for test in tv.test_values_1:

            print('\n' + test['remark'] + '\n')

            self.settings['template_types'] = test['template_types']

            result = libs.string_processes.pcom_create_template_fileroot(test['fileroot'],self.settings)
            print(result)

            # check asserts in
            self.assertEqual(test['assertEqual'], result)

        # reset settings
        self.settings = libs.string_processes.pcom_build_dictionary(libs.globals.DEFAULT_SETTINGS)


    @testCall
    def test_pcom_get_template_key(self):

        for test in tv.test_values_2:

            print('\n' + test['remark'] + '\n')

            self.settings['template_types'] = test['template_types']

            result = libs.string_processes.pcom_get_template_key(test['fileroot'],self.settings)
            print(result)

            # check asserts in
            self.assertEqual(test['assertEqual'], result)

        # reset settings
        self.settings = libs.string_processes.pcom_build_dictionary(libs.globals.DEFAULT_SETTINGS)


    @testCall
    def test_pcom_replace_quotes(self):

        for test in tv.test_values_3:

            print('\n' + test['remark'] + '\n')

            result = libs.string_processes.pcom_replace_quotes(test['text'])
            print(result)

            # check asserts in
            self.assertEqual(test['assertEqual'], result)

    @testCall
    def test_pcom_find_author_full_name(self):

        for test in tv.test_values_4:

            print('\n' + test['remark'] + '\n')

            result = libs.string_processes.pcom_find_author_full_name(
                    name=test['name'],
                    authors=test['authors'])

            print(result)

            # check asserts in
            self.assertEqual(test['assertEqual'], result)



if __name__ == '__main__':
    unittest.main()
