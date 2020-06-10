import unittest
import libraries.morflessLibs as libs

# import test values and expected outputs
# main includes sidebar data
import unit.string_processes_test_io.string_processes_4_functions_io as tv
from fixtures.decorators import testCall


class StringProcesses4HandlerCase(unittest.TestCase):

    def setUp(self):
        self.settings = libs.string_processes.pcom_build_dictionary(libs.globals.DEFAULT_SETTINGS)

    def tearDown(self):
        self.settings = dict()

    @testCall
    def test_pcom_process_menu_command_mlk_keyword(self):

        for test in tv.test_values_1:

            print('\n' + test['remark'] + '\n')

            result = libs.string_processes.pcom_process_menu_command_mlk_keyword(
                command_string=test['command_string'])

            print(result)

            # check asserts in
            self.assertEqual(test['assertEqual'], result)


    @testCall
    def test_pcom_process_logo_for_nav(self):

        for test in tv.test_values_2:

            print('\n' + test['remark'] + '\n')

            result = libs.string_processes.pcom_process_logo_for_nav(
                syntax=test['syntax'],
                site_title=test['site_title'])

            print(result)

            # check asserts in
            self.assertEqual(test['assertEqual'].strip(), result.strip())


    @testCall
    def test_pcom_add_title(self):

        for test in tv.test_values_3:

            print('\n' + test['remark'] + '\n')

            result = libs.string_processes.pcom_add_title(
                syntax=test['syntax'])

            print(result)

            # check asserts in
            self.assertEqual(test['assertEqual'].strip(), result.strip())

    @testCall
    def test_pcom_replace_custom_attributes(self):

        for test in tv.test_values_4:

            print('\n' + test['remark'] + '\n')

            result = libs.string_processes.pcom_replace_custom_attributes(
                syntax=test['syntax'],
                custom_keys=test['custom_keys'])

            print(result)

            # check asserts in
            self.assertEqual(test['assertEqual'], result)

    @testCall
    def test_pcom_open_custom_class_div(self):

        for test in tv.test_values_5:

            print('\n' + test['remark'] + '\n')

            result = libs.string_processes.pcom_open_custom_class_div(
                custom_class=test['custom_class'],
                opening_html=test['html'])

            print(result)

            # check asserts in
            self.assertEqual(test['assertEqual'], result)

    @testCall
    def test_pcom_open_placement_class(self):

        for test in tv.test_values_6:

            print('\n' + test['remark'] + '\n')

            result = libs.string_processes.pcom_open_placement_class(
                custom_class=test['custom_class'],
                placement=test['placement'])

            print(result)

            # check asserts in
            self.assertEqual(test['assertEqual'], result)

    @testCall
    def test_pcom_close_placement_class(self):

        for test in tv.test_values_7:

            print('\n' + test['remark'] + '\n')

            result = libs.string_processes.pcom_close_placement_class(
                placement=test['placement'])

            print(result)

            # check asserts in
            self.assertEqual(test['assertEqual'].strip(), result.strip())

    @testCall
    def test_pcom_process_keyword_args(self):

        for test in tv.test_values_8:

            print('\n' + test['remark'] + '\n')

            result = libs.string_processes.pcom_process_keyword_args(
                command_string=test['command_string'],
                defaults=test['defaults'])

            print(result)

            # check asserts in
            self.assertEqual(test['assertEqual'], result)

    @testCall
    def test_pcom_site_constants_replacement(self):

        for test in tv.test_values_9:

            print('\n' + test['remark'] + '\n')

            result = libs.string_processes.pcom_site_constants_replacement(
                content=test['content'])

            print(result)

            # check asserts in
            self.assertEqual(test['assertEqual'], result)


if __name__ == '__main__':
    unittest.main()
