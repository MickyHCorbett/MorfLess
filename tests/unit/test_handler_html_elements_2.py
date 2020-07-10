import unittest
import libraries.morflessLibs as libs

# import test values and expected outputs
# main includes sidebar data
import unit.html_elements_test_io.html_elements_2_functions_io as tv
from fixtures.decorators import testCall


class HtmlElements2HandlerCase(unittest.TestCase):

    def setUp(self):
        self.maxDiff= None
        self.settings = libs.string_processes.pcom_build_dictionary(libs.globals.DEFAULT_SETTINGS)

    def tearDown(self):
        self.settings = dict()

    @testCall
    def test_pcom_add_content_command(self):

        for test in tv.test_values_1:

            print('\n' + test['remark'] + '\n')

            result = libs.html_elements.pcom_add_content_command(
                                            syntax=test['syntax'],
                                            custom_class=test['custom_class'],
                                            placement=test['placement'],
                                            type=test['type'],
                                            settings=test['settings'])

            print(result)

            # check asserts in
            self.assertEqual(test['assertEqual'].strip(), result.strip())

    @testCall
    def test_pcom_insert_searchbar_command(self):

        for test in tv.test_values_2:

            print('\n' + test['remark'] + '\n')

            result = libs.html_elements.pcom_insert_searchbar_command(
                                            syntax=test['syntax'],
                                            custom_class=test['custom_class'],
                                            placement=test['placement'],
                                            type=test['type'],
                                            settings=test['settings'])

            print(result)

            # check asserts in
            self.assertEqual(test['assertEqual'].strip(), result.strip())

    @testCall
    def test_pcom_process_insert_command(self):

        for test in tv.test_values_3:

            print('\n' + test['remark'] + '\n')

            result = libs.html_elements.pcom_process_insert_command(
                                            syntax=test['syntax'],
                                            custom_class=test['custom_class'],
                                            placement=test['placement'],
                                            type=test['type'],
                                            settings=test['settings'])

            print(result)

            # check asserts in
            self.assertEqual(test['assertEqual'].strip(), result.strip())

    # @testCall
    # def test_pcom_process_insert_additions_command(self):
    #
    #     for test in tv.test_values_4:
    #
    #         print('\n' + test['remark'] + '\n')
    #
    #         result = libs.html_elements.pcom_process_insert_additions_command(
    #                                         syntax=test['syntax'],
    #                                         custom_class=test['custom_class'],
    #                                         placement=test['placement'],
    #                                         type=test['type'],
    #                                         settings=test['settings'])
    #
    #         print(result)
    #
    #         # check asserts in
    #         self.assertEqual(test['assertEqual'].strip(), result.strip())

    @testCall
    def test_pcom_insert_pagination_command(self):

        for test in tv.test_values_5:

            print('\n' + test['remark'] + '\n')

            result = libs.html_elements.pcom_insert_pagination_command(
                                            syntax=test['syntax'],
                                            custom_class=test['custom_class'],
                                            placement=test['placement'],
                                            type=test['type'],
                                            settings=test['settings'])
            print(result)

            # check asserts in
            self.assertEqual(test['assertEqual'].strip(), result.strip())

    @testCall
    def test_pcom_create_pagination_link(self):

        for test in tv.test_values_6:

            print('\n' + test['remark'] + '\n')

            result,pagination = libs.html_elements.pcom_create_pagination_link(test['links'])

            print(result)

            # check asserts in
            self.assertEqual(test['assertEqual']['pagination'], pagination)
            for item in test['assertIn']:
                self.assertIn(item,result)


if __name__ == '__main__':
    unittest.main()
