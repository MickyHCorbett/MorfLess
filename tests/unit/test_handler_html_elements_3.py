import unittest
import libraries.morflessLibs as libs

# import test values and expected outputs
# main includes sidebar data
import unit.html_elements_test_io.html_elements_3_functions_io as tv
from fixtures.decorators import testCall


class HtmlElements3HandlerCase(unittest.TestCase):

    def setUp(self):
        self.maxDiff= None
        self.settings = libs.string_processes.pcom_build_dictionary(libs.globals.DEFAULT_SETTINGS)

    def tearDown(self):
        self.settings = dict()

    @testCall
    def test_pcom_process_n_box_command(self):

        for test in tv.test_values_1:

            print('\n' + test['remark'] + '\n')

            result = libs.html_elements.pcom_process_n_box_command(
                                            syntax=test['syntax'],
                                            custom_class=test['custom_class'],
                                            placement=test['placement'],
                                            no_boxes=test['no_boxes'],
                                            settings=test['settings'])

            print(result)

            # check asserts in
            self.assertEqual(test['assertEqual'].strip(), result.strip())

    @testCall
    def test_pcom_parse_box_arguments(self):

        for test in tv.test_values_2:

            print('\n' + test['remark'] + '\n')

            result = libs.html_elements.pcom_parse_box_arguments(
                                            syntax=test['syntax'],
                                            no_boxes=test['no_boxes'],
                                            placement=test['placement'],
                                            ppp=test['ppp'])

            print(result)

            # check asserts in
            self.assertEqual(test['assertEqual'].strip(), result.strip())


    @testCall
    def test_pcom_add_box_for_n_box(self):

        for test in tv.test_values_3:

            print('\n' + test['remark'] + '\n')

            result = libs.html_elements.pcom_add_box_for_n_box(
                                            syntax=test['syntax'],
                                            type=test['type'],
                                            no_boxes=test['no_boxes'],
                                            placement=test['placement'],
                                            ppp=test['ppp'])

            print(result)

            # check asserts in
            self.assertEqual(test['assertEqual'].strip(), result.strip())


    @testCall
    def test_pcom_process_n_box_subcommands(self):

        for test in tv.test_values_4:

            print('\n' + test['remark'] + '\n')

            result = libs.html_elements.pcom_process_n_box_subcommands(
                                            command=test['command'],
                                            syntax=test['syntax'],
                                            ppp=test['ppp'])

            print(result)

            # check asserts in
            self.assertEqual(test['assertEqual'].strip(), result.strip())

    @testCall
    def test_pcom_process_n_box_menu_command(self):

        for test in tv.test_values_5:

            print('\n' + test['remark'] + '\n')

            result = libs.html_elements.pcom_process_n_box_menu_command(
                                            syntax=test['syntax'])

            print(result)

            # check asserts in
            self.assertEqual(test['assertEqual'].strip(), result.strip())


    @testCall
    def test_pcom_process_n_box_text_command(self):

        for test in tv.test_values_6:

            print('\n' + test['remark'] + '\n')

            result = libs.html_elements.pcom_process_n_box_text_command(
                                            syntax=test['syntax'])

            print(result)

            # check asserts in
            for item in test['assertIn']:
                self.assertIn(item, result)


if __name__ == '__main__':
    unittest.main()
