import unittest
import libraries.morflessLibs as libs

# import test values and expected outputs
# main includes sidebar data
import unit.html_elements_test_io.html_elements_1_functions_io as tv
from fixtures.decorators import testCall


class HtmlElements1HandlerCase(unittest.TestCase):

    def setUp(self):
        self.maxDiff= None
        self.settings = libs.string_processes.pcom_build_dictionary(libs.globals.DEFAULT_SETTINGS)

    def tearDown(self):
        self.settings = dict()

    @testCall
    def test_pcom_process_custom_command(self):

        for test in tv.test_values_1:

            print('\n' + test['remark'] + '\n')

            result = libs.html_elements.pcom_process_custom_command(
                command=test['command'])

            print(result)

            # check asserts in
            self.assertEqual(test['assertEqual'], result)

    @testCall
    def test_pcom_use_defaults(self):

        for test in tv.test_values_2:

            print('\n' + test['remark'] + '\n')

            settings = test['settings']
            settings[test['default_type']] = test['default_entry']

            result = libs.html_elements.pcom_use_defaults(
                                            command=test['command'],
                                            syntax=test['syntax'],
                                            placement=test['placement'],
                                            type=test['type'],
                                            settings=settings)

            print(result)

            # check asserts in
            self.assertEqual(test['assertEqual']['syntax'], result)

    def test_pcom_use_settings_defaults(self):

        for test in tv.test_values_3:

            print('\n' + test['remark'] + '\n')

            settings = test['settings']
            settings[test['default_type']] = test['default_entry']

            result = libs.html_elements.pcom_use_settings_defaults(
                                            placement=test['placement'],
                                            settings=settings)

            print(result)

            # check asserts in
            self.assertEqual(test['assertEqual'], result)

    def test_pcom_process_nav_command(self):

        for test in tv.test_values_4:

            print('\n' + test['remark'] + '\n')

            result = libs.html_elements.pcom_process_nav_command(
                                            syntax=test['syntax'],
                                            custom_class=test['custom_class'],
                                            placement=test['placement'],
                                            type=test['type'],
                                            settings=test['settings'])

            print(result)

            # check asserts in
            self.assertEqual(test['assertEqual'].strip(), result.strip())

    def test_pcom_process_menu_command(self):

        for test in tv.test_values_5:

            print('\n' + test['remark'] + '\n')

            result = libs.html_elements.pcom_process_menu_command(
                                            syntax=test['syntax'],
                                            custom_class=test['custom_class'],
                                            placement=test['placement'],
                                            type=test['type'],
                                            settings=test['settings'])

            print(result)

            # check asserts in
            self.assertEqual(test['assertEqual'].strip(), result.strip())

    def test_pcom_process_menu_command_syntax(self):

        for test in tv.test_values_6:

            print('\n' + test['remark'] + '\n')

            result = libs.html_elements.pcom_process_menu_command_syntax(
                                            syntax=test['syntax'],
                                            custom_class=test['custom_class'],
                                            placement=test['placement'],
                                            type=test['type'],
                                            settings=test['settings'])

            print(result)

            # check asserts in
            self.assertEqual(test['assertEqual'].strip(), result.strip())


if __name__ == '__main__':
    unittest.main()
