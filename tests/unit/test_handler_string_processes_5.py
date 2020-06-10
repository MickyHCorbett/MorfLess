import unittest
import libraries.morflessLibs as libs

# import test values and expected outputs
# main includes sidebar data
import unit.string_processes_test_io.string_processes_5_functions_io as tv
from fixtures.decorators import testCall


class StringProcesses5HandlerCase(unittest.TestCase):

    def setUp(self):
        self.maxDiff= None
        self.settings = libs.string_processes.pcom_build_dictionary(libs.globals.DEFAULT_SETTINGS)

    def tearDown(self):
        self.settings = dict()

    @testCall
    def test_pcom_insert_default_additions_into_html(self):

        for test in tv.test_values_1:

            print('\n' + test['remark'] + '\n')
            additions = test['additions']
            additions[test['add_addition_placement']] = test['add_default']
            additions[test['addition_placement']] = test['default_additions']

            result,list = libs.string_processes.pcom_insert_default_additions_into_html(
                additions=additions,
                content=test['content'],
                placement=test['placement'])

            print(result)

            # check asserts in
            self.assertEqual(test['assertEqual'].strip(), result.strip())

    @testCall
    def test_pcom_insert_additions_into_html(self):

        for test in tv.test_values_2:

            print('\n' + test['remark'] + '\n')
            args = test['args']
            args['settings']['postlist_present'] = test['postlist_present']
            args['settings'][test['addition_placement']] = test['additions']

            result = libs.string_processes.pcom_insert_additions_into_html(
                args=test['args'])

            print(result)

            # check asserts in
            self.assertEqual(test['assertEqual'].strip(), result.strip())

    @testCall
    def test_pcom_get_insert_info(self):

        for test in tv.test_values_3:

            print('\n' + test['remark'] + '\n')

            result = libs.string_processes.pcom_get_insert_info(
                html_array=test['html_array'])

            print(result)

            # check asserts in
            self.assertEqual(test['assertEqual'], result)

    @testCall
    def test_pcom_get_postlists_info(self):

        for test in tv.test_values_4:

            print('\n' + test['remark'] + '\n')

            result = libs.string_processes.pcom_get_postlists_info(
                html_array=test['html_array'],
                fileroot=test['fileroot'])

            print(result)

            # check asserts in
            self.assertEqual(test['assertEqual'], result)


    @testCall
    def test_pcom_insert_postlist_wrapper(self):

        for test in tv.test_values_5:

            print('\n' + test['remark'] + '\n')

            result,log = libs.string_processes.pcom_insert_postlist_wrapper(
                html_array=test['html_array'],
                postlist_info=test['postlist_info'],
                outlog=test['outlog'])

            print(result)

            # check asserts in
            self.assertEqual(test['assertEqual']['array'], result)
            self.assertEqual(test['assertEqual']['log'], log)

    @testCall
    def test_pcom_get_content_meta_info(self):

        for test in tv.test_values_6:

            print('\n' + test['remark'] + '\n')

            result = libs.string_processes.pcom_get_content_meta_info(
                html_array=test['html_array'])

            print(result)

            # check asserts in
            self.assertEqual(test['assertEqual'], result)

    @testCall
    def test_pcom_get_comma_list(self):

        for test in tv.test_values_7:

            print('\n' + test['remark'] + '\n')

            result = libs.string_processes.pcom_get_comma_list(
                list=test['list'])

            print(result)

            # check asserts in
            self.assertEqual(test['assertEqual'], result)

    @testCall
    def test_pcom_get_comma_list(self):

        for test in tv.test_values_8:

            print('\n' + test['remark'] + '\n')

            result = libs.string_processes.pcom_assign_content_meta(
                content_meta_list=test['list'])

            print(result)

            # check asserts in
            self.assertEqual(test['assertEqual'], result)

    @testCall
    def test_pcom_strip_string(self):

        for test in tv.test_values_9:

            print('\n' + test['remark'] + '\n')

            result = libs.string_processes.pcom_strip_string(
                content=test['content'])

            print(result)

            # check asserts in
            self.assertEqual(test['assertEqual'], result)

    @testCall
    def test_pcom_create_raw_content(self):

        for test in tv.test_values_10:

            print('\n' + test['remark'] + '\n')

            result = libs.string_processes.pcom_create_raw_content(
                content=test['content'],
                meta=test['meta'])

            print(result)

            # check asserts in
            self.assertEqual(test['assertEqual'].strip(), result.strip())


if __name__ == '__main__':
    unittest.main()
