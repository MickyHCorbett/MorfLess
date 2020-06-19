import unittest
import libraries.morflessLibs as libs

# import test values and expected outputs
# main includes sidebar data
import unit.html_elements_test_io.html_elements_5_functions_io as tv
from fixtures.decorators import testCall


class HtmlElements5HandlerCase(unittest.TestCase):

    def setUp(self):
        self.maxDiff= None
        self.settings = libs.string_processes.pcom_build_dictionary(libs.globals.DEFAULT_SETTINGS)

    def tearDown(self):
        self.settings = libs.string_processes.pcom_build_dictionary(libs.globals.DEFAULT_SETTINGS)

    @testCall
    def test_pcom_add_post_list_command(self):

        for test in tv.test_values_1:

            print('\n' + test['remark'] + '\n')

            result = libs.html_elements.pcom_add_post_list_command(
                                            syntax=test['syntax'],
                                            custom_class=test['custom_class'],
                                            placement=test['placement'],
                                            type=test['type'],
                                            settings=test['settings'])

            print(result)

            # check asserts in
            self.assertEqual(test['assertEqual'].strip(), result.strip())


    @testCall
    def test_pcom_process_postlist_keywords(self):

        for test in tv.test_values_2:

            print('\n' + test['remark'] + '\n')

            result = libs.html_elements.pcom_process_postlist_keywords(
                                            syntax=test['syntax'])

            print(result)

            # check asserts in
            self.assertEqual(test['assertEqual'], result)


    @testCall
    def test_pcom_create_post_list_entry(self):

        for test in tv.test_values_3:

            print('\n' + test['remark'] + '\n')

            result = libs.html_elements.pcom_create_post_list_entry(
                                            post=test['post'],
                                            settings=test['settings'],
                                            list_meta=test['list_meta'],
                                            list_end=test['list_end'],
                                            manual_sticky=test['manual_sticky'],
                                            ignore_meta=test['ignore_meta'],
                                            no_js=test['no_js'])

            print(result)

            # check asserts in
            for item in test['assertIn']:
                self.assertIn(item.strip(), result.strip())

            if test['test_assertNotIn']:
                for item in test['assertNotIn']:
                    self.assertNotIn(item.strip(), result.strip())


    @testCall
    def test_pcom_create_search_post_list_entry(self):

        for test in tv.test_values_4:

            print('\n' + test['remark'] + '\n')

            result = libs.html_elements.pcom_create_search_post_list_entry(
                                            post=test['post_search'],
                                            settings=test['settings'],
                                            list_meta=test['list_meta'],
                                            ignore_meta=test['ignore_meta'])

            print(result)

            # check asserts in
            for item in test['assertIn']:
                self.assertIn(item.strip(), result.strip())

            if test['test_assertNotIn']:
                for item in test['assertNotIn']:
                    self.assertNotIn(item.strip(), result.strip())


    @testCall
    def test_pcom_create_info_list_entry(self):

        for test in tv.test_values_5:

            print('\n' + test['remark'] + '\n')

            result = libs.html_elements.pcom_create_info_list_entry(
                                            entry=test['entry'],
                                            url=test['url'],
                                            settings=test['settings'],
                                            list_end=test['list_end'],
                                            no_js=test['no_js'])

            print(result)

            # check asserts in
            for item in test['assertIn']:
                self.assertIn(item.strip(), result.strip())

            if test['test_assertNotIn']:
                for item in test['assertNotIn']:
                    self.assertNotIn(item.strip(), result.strip())


    @testCall
    def test_pcom_create_template_search_list_entry(self):

        for test in tv.test_values_6:

            print('\n' + test['remark'] + '\n')

            result = libs.html_elements.pcom_create_template_search_list_entry(
                                            entry=test['entry'],
                                            url=test['url'],
                                            settings=test['settings'])

            print(result)

            # check asserts in
            for item in test['assertIn']:
                self.assertIn(item.strip(), result.strip())


    @testCall
    def test_pcom_create_archive_entry(self):

        for test in tv.test_values_7:

            print('\n' + test['remark'] + '\n')

            result = libs.html_elements.pcom_create_archive_entry(
                                            entry=test['entry'],
                                            base_name=test['base_name'],
                                            settings=test['settings'])

            print(result)

            # check asserts in
            for item in test['assertIn']:
                self.assertIn(item.strip(), result.strip())


    @testCall
    def test_pcom_insert_author_category_in_post_list(self):

        for test in tv.test_values_8:

            print('\n' + test['remark'] + '\n')

            result = libs.html_elements.pcom_insert_author_category_in_post_list(
                                                post=test['post'],
                                                settings=test['settings'],
                                                list_meta_array=test['list_meta_array'],
                                                type=test['type'],
                                                add_escape=test['add_escape'],
                                                no_js=test['no_js'])

            print(result)

            # check asserts in
            self.assertEqual(test['assertEqual'].strip(), result.strip())


if __name__ == '__main__':
    unittest.main()
