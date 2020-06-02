import unittest
import libraries.morflessLibs as libs

# import test values and expected outputs
# main includes sidebar data
import unit.meta_elements_test_io.meta_elements_io as tv

from fixtures.decorators import testCall


class SetMetaElementsCase(unittest.TestCase):

    def setUp(self):
        self.settings = libs.string_processes.pcom_build_dictionary(libs.globals.DEFAULT_SETTINGS)

    def tearDown(self):
        self.settings = dict()

    @testCall
    def test_pcom_process_meta_syntax_none(self):

        for ind,test in enumerate(tv.test_values_1):

            print('\n' + test['remark'] + '\n')

            syntax = test['input']
            print(syntax)

            result = libs.meta_elements.pcom_process_settings_meta_syntax(syntax,self.settings)
            print(result)

            # check asserts in
            with self.subTest(msg='test - 1.'+str(ind+1)):
                self.assertEqual(test['assertEqual'], result)
                self.assertNotEqual(test['assertNotEqual'], result)


    @testCall
    def test_pcom_process_meta_syntax_single_entries(self):

        for ind,test in enumerate(tv.test_values_2):

            print('\n' + test['remark'] + '\n')

            syntax = test['input']
            test_element = test['element']
            print(syntax)

            result = libs.meta_elements.pcom_process_settings_meta_syntax(syntax,self.settings)
            print(test_element + ': ' + str(result[test_element]))

            with self.subTest(msg='test - 2.'+str(ind+1)):
                # check asserts in
                self.assertEqual(test['assertEqual'], result[test_element])
                self.assertNotEqual(test['assertNotEqual'], result[test_element])


    @testCall
    def test_pcom_process_meta_syntax_multi_entries(self):

        for ind,test in enumerate(tv.test_values_3):

            print('\n' + test['remark'] + '\n')

            syntax = test['input']
            test_element = test['element']
            print(syntax)


            result = libs.meta_elements.pcom_process_settings_meta_syntax(syntax,self.settings)
            print(test_element + ': ' + str(result[test_element]))

            # check asserts in
            with self.subTest(msg='test - 3.'+str(ind+1)):
                self.assertEqual(test['assertEqual'], result[test_element])
                self.assertNotEqual(test['assertNotEqual'], result[test_element])


    @testCall
    def test_pcom_process_meta_syntax(self):

        for ind,test in enumerate(tv.test_values_4):

            print('\n' + test['remark'] + '\n')

            syntax = test['input']
            print(syntax)

            result = libs.meta_elements.pcom_process_meta_syntax(syntax)
            print(result)

            # check asserts in
            with self.subTest(msg='test - 4.'+str(ind+1)):
                self.assertEqual(test['assertEqual'], result)
                self.assertNotEqual(test['assertNotEqual'], result)


    @testCall
    def test_pcom_update_json_based_settings(self):

        for ind,test in enumerate(tv.test_values_5):

            print('\n' + test['remark'] + '\n')

            settings_element = test['settings_element']
            updates = test['input']
            json_type = test['json_type']
            print('Input :{}'.format(updates))

            result = libs.meta_elements.pcom_update_json_based_settings(settings_element,updates,json_type)
            print('Output :{}'.format(result))

            # check asserts in
            with self.subTest(msg='test - 5.'+str(ind+1)):
                self.assertEqual(test['assertEqual'], result)
                self.assertNotEqual(test['assertNotEqual'], result)


if __name__ == '__main__':
    unittest.main()
