import unittest
import libraries.morflessLibs as libs

# import test values and expected outputs
# main includes sidebar data
import unit.string_processes_test_io.string_processes_1_functions_io as tv
from fixtures.decorators import testCall

# define settings element for test
settings = libs.globals.DEFAULT_SETTINGS

class StringProcesses1HandlerCase(unittest.TestCase):

    @testCall
    def test_pcom_process_json(self):

        for test in tv.test_values_1:

            print('\n' + test['remark'] + '\n')

            json_data = test['input']
            print(json_data)

            result = libs.string_processes.pcom_process_json(json_data)
            print(result)

            # check asserts in
            self.assertEqual(test['assertEqual'], result)
            self.assertNotEqual(test['assertNotEqual'], result)

    @testCall
    def test_pcom_write_json(self):

        for test in tv.test_values_2:

            print('\n' + test['remark'] + '\n')

            json_data = test['input']
            print(json_data)

            result = libs.string_processes.pcom_write_json(json_data)
            print(result)

            # check asserts in
            self.assertEqual(test['assertEqual'].rstrip().lstrip(), result.rstrip().lstrip())

    @testCall
    def test_pcom_create_url(self):

        for test in tv.test_values_3:

            print('\n' + test['remark'] + '\n')

            file = test['inputs']['name']
            meta = { 'url': test['inputs']['meta_url']}

            outkey,type = libs.string_processes.pcom_create_url(file,meta)
            print(outkey)
            print(type)

            # check asserts in
            self.assertEqual(test['assertEqual']['outkey'],outkey)
            self.assertEqual(test['assertEqual']['type'],type)


    @testCall
    def test_pcom_filter_template(self):

        for test in tv.test_values_4:

            print('\n' + test['remark'] + '\n')

            fileroot = test['input']

            is_template,is_search = libs.string_processes.pcom_filter_template(fileroot,settings)
            print('Template: {}, Search: {}'.format(is_template,is_search))

            # check asserts in
            self.assertEqual(test['assertEqual']['is_template'],is_template)
            self.assertEqual(test['assertEqual']['is_search'],is_search)

    @testCall
    def test_pcom_check_root(self):

        print('\n' + 'Test case 1:pcom_check_root - fileroot = index,is_root TRUE' + '\n')

        fileroot = 'index'
        print(fileroot)

        is_root = libs.string_processes.pcom_check_root(fileroot)
        print(is_root)
        self.assertTrue(is_root)

        # --

        print('\n' + 'Test case 2:pcom_check_root - fileroot = 404,is_root TRUE' + '\n')

        fileroot = '404'
        print(fileroot)

        is_root = libs.string_processes.pcom_check_root(fileroot)
        print(is_root)
        self.assertTrue(is_root)

        # --

        print('\n' + 'Test case 3:pcom_check_root - fileroot = post,is_root False' + '\n')

        fileroot = 'post'
        print(fileroot)

        is_root = libs.string_processes.pcom_check_root(fileroot)
        print(is_root)
        self.assertFalse(is_root)


if __name__ == '__main__':
    unittest.main()
