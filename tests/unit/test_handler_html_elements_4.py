import unittest
import libraries.morflessLibs as libs

# import test values and expected outputs
# main includes sidebar data
import unit.html_elements_test_io.html_elements_4_functions_io as tv
from fixtures.decorators import testCall


class HtmlElements4HandlerCase(unittest.TestCase):

    def setUp(self):
        self.maxDiff= None
        self.settings = libs.string_processes.pcom_build_dictionary(libs.globals.DEFAULT_SETTINGS)

    def tearDown(self):
        self.settings = libs.string_processes.pcom_build_dictionary(libs.globals.DEFAULT_SETTINGS)

    @testCall
    def test_pcom_add_content_meta_command(self):

        for test in tv.test_values_1:

            print('\n' + test['remark'] + '\n')
            add_content_settings = test['settings']
            add_content_settings['current_file'] = test['current_file']

            result = libs.html_elements.pcom_add_content_meta_command(
                                            syntax=test['syntax'],
                                            custom_class=test['custom_class'],
                                            placement=test['placement'],
                                            type=test['type'],
                                            settings=add_content_settings)

            print(result)

            # check asserts in
            self.assertEqual(test['assertEqual'].strip(), result.strip())


    @testCall
    def test_pcom_find_content_meta_keywords(self):

        for test in tv.test_values_2:

            print('\n' + test['remark'] + '\n')

            result = libs.html_elements.pcom_find_content_meta_keywords(
                                            syntax=test['syntax'])

            print(result)

            # check asserts in
            self.assertEqual(test['assertEqual'], result)


    @testCall
    def test_pcom_find_content_meta_keywords(self):

        for test in tv.test_values_3:

            print('\n' + test['remark'] + '\n')

            result = libs.html_elements.pcom_insert_content_meta_data(
                                html_array=test['array'],
                                content_meta_info=test['meta_info'],
                                settings=test['settings'],
                                list_meta=test['list_meta'],
                                post=test['post'],
                                is_template=test['is_template'])

            print(result)

            # check asserts in
            self.assertEqual(test['assertEqual'], result)


    def test_pcom_insert_date_created(self):

        for test in tv.test_values_4:

            print('\n' + test['remark'] + '\n')

            result = libs.html_elements.pcom_insert_date_created(
                                post=test['post'],
                                settings=test['settings'],
                                show_time=test['show_time'])

            print(result)

            # check asserts in
            self.assertEqual(test['assertEqual'].strip(), result.strip())

    def test_pcom_insert_date_modified(self):

        for test in tv.test_values_5:

            print('\n' + test['remark'] + '\n')

            result = libs.html_elements.pcom_insert_date_modified(
                                post=test['post'],
                                settings=test['settings'],
                                show_time=test['show_time'])

            print(result)

            # check asserts in
            self.assertEqual(test['assertEqual'].strip(), result.strip())


if __name__ == '__main__':
    unittest.main()
