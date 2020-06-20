import unittest
import libraries.morflessLibs as libs

# import test values and expected outputs
# main includes sidebar data
import unit.html_elements_test_io.html_elements_6_functions_io as tv
from fixtures.decorators import testCall


class HtmlElements6HandlerCase(unittest.TestCase):

    def setUp(self):
        self.maxDiff= None
        self.settings = libs.string_processes.pcom_build_dictionary(libs.globals.DEFAULT_SETTINGS)

    def tearDown(self):
        self.settings = libs.string_processes.pcom_build_dictionary(libs.globals.DEFAULT_SETTINGS)

    @testCall
    def test_pcom_insert_quote_box_command(self):

        for test in tv.test_values_1:

            print('\n' + test['remark'] + '\n')

            result = libs.html_elements.pcom_insert_quote_box_command(
                                            syntax=test['syntax'],
                                            custom_class=test['custom_class'],
                                            placement=test['placement'],
                                            type=test['type'],
                                            settings=test['settings'])

            print(result)

            # check asserts in
            self.assertEqual(test['assertEqual'].strip(), result.strip())

    @testCall
    def test_pcom_add_header_content_to_head(self):

        for test in tv.test_values_2:

            print('\n' + test['remark'] + '\n')

            header_settings = test['settings']
            header_settings['header_additions'] = []

            result = libs.html_elements.pcom_add_header_content_to_head(
                                            syntax=test['syntax'],
                                            custom_class=test['custom_class'],
                                            placement=test['placement'],
                                            type=test['type'],
                                            settings=header_settings)

            print(result['header_additions'])

            # check asserts in
            self.assertEqual(test['assertEqual'], result['header_additions'])


    @testCall
    def test_pcom_add_footer_content_to_footer(self):

        for test in tv.test_values_3:

            print('\n' + test['remark'] + '\n')

            footer_settings = test['settings']
            footer_settings['footer_additions'] = []

            result = libs.html_elements.pcom_add_footer_content_to_footer(
                                            syntax=test['syntax'],
                                            custom_class=test['custom_class'],
                                            placement=test['placement'],
                                            type=test['type'],
                                            settings=footer_settings)

            print(result['footer_additions'])

            # check asserts in
            self.assertEqual(test['assertEqual'], result['footer_additions'])


    @testCall
    def test_pcom_process_section_command(self):

        for test in tv.test_values_4:

            print('\n' + test['remark'] + '\n')

            result,settings_out = libs.html_elements.pcom_process_section_command(
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
