import unittest
import libraries.morflessLibs as libs

# import test values and expected outputs
# main includes sidebar data
import unit.string_processes_test_io.string_processes_3_functions_io as tv
from fixtures.decorators import testCall
# define settings element for test
settings = libs.globals.DEFAULT_SETTINGS

class StringProcesses3HandlerCase(unittest.TestCase):

    def setUp(self):
        self.settings = libs.string_processes.pcom_build_dictionary(libs.globals.DEFAULT_SETTINGS)

    def tearDown(self):
        self.settings = dict()

    @testCall
    def test_pcom_get_strings_syntax_separator(self):

        for test in tv.test_values_1:

            print('\n' + test['remark'] + '\n')

            result = libs.string_processes.pcom_get_strings_syntax_separator(
                syntax=test['text'],
                separator=test['separator'],
                trim=test['trim'])

            print(result)

            # check asserts in
            self.assertEqual(test['assertEqual'], result)

    @testCall
    def test_pcom_get_first_command(self):

        for test in tv.test_values_2:

            print('\n' + test['remark'] + '\n')

            result = libs.string_processes.pcom_get_first_command(
                format=test['text'],
                args=test['args'])

            print(result)

            # check asserts in
            self.assertEqual(test['assertEqual'], result)

    @testCall
    def test_pcom_process_command_open_close_syntax(self):

        for test in tv.test_values_3:

            print('\n' + test['remark'] + '\n')

            result = libs.string_processes.pcom_process_command_open_close_syntax(
                syntax=test['syntax'],
                args=test['args'])

            print(result)

            # check asserts in
            self.assertEqual(test['assertEqual'], result)

    @testCall
    def test_pcom_create_html_from_array(self):

        for test in tv.test_values_4:

            print('\n' + test['remark'] + '\n')

            result = libs.string_processes.pcom_create_html_from_array(test['array'])

            print(result)

            # check asserts in
            self.assertEqual(test['assertEqual'], result)

    @testCall
    def test_pcom_remove_empty_lines(self):

        for test in tv.test_values_5:

            print('\n' + test['remark'] + '\n')

            result = libs.string_processes.pcom_remove_empty_lines(test['content'])

            print(result)

            # check asserts in
            self.assertEqual(test['assertEqual'], result)

    @testCall
    def test_pcom_build_dictionary(self):

        for test in tv.test_values_6:

            print('\n' + test['remark'] + '\n')

            result = libs.string_processes.pcom_build_dictionary(test['dict'])

            print(result)

            # check asserts in
            self.assertEqual(test['assertEqual'], result)

    @testCall
    def test_pcom_add_tab_to_content_line(self):

        for test in tv.test_values_7:

            print('\n' + test['remark'] + '\n')

            result = libs.string_processes.pcom_add_tab_to_content_line(test['content'])

            print(result)

            # check asserts in
            self.assertEqual(test['assertEqual'], result)

    @testCall
    def test_pcom_add_2tabs_to_content_line(self):

        for test in tv.test_values_8:

            print('\n' + test['remark'] + '\n')

            result = libs.string_processes.pcom_add_2tabs_to_content_line(test['content'])

            print(result)

            # check asserts in
            self.assertEqual(test['assertEqual'], result)

    @testCall
    def test_pcom_add_3tabs_to_content_line(self):

        for test in tv.test_values_9:

            print('\n' + test['remark'] + '\n')

            result = libs.string_processes.pcom_add_3tabs_to_content_line(test['content'])

            print(result)

            # check asserts in
            self.assertEqual(test['assertEqual'], result)



if __name__ == '__main__':
    unittest.main()
