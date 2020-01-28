import unittest
import libraries.morflessLibs as libs

# import test values and expected outputs
# main includes sidebar data
import unit.string_processes_test_io.string_processes_2_functions_io as tv

# define settings element for test
settings = libs.globals.DEFAULT_SETTINGS

class StringProcesses2HandlerCase(unittest.TestCase):

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

        print('\n\n===== test_pcom_process_json - END \n\n')


if __name__ == '__main__':
    unittest.main()
