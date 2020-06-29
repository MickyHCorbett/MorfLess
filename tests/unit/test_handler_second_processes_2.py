import unittest
import libraries.morflessLibs as libs

# import test values and expected outputs
# main includes sidebar data
import unit.second_processes_test_io.second_processes_2_functions_io as tv

from fixtures.decorators import testCall

class SecondProcessesHandler2Case(unittest.TestCase):

    # set up and tear down reset to default settings
    def setUp(self):
        self.maxDiff= None
        self.settings = libs.string_processes.pcom_build_dictionary(libs.globals.DEFAULT_SETTINGS)

    def tearDown(self):
        self.settings = dict()

    @testCall
    def test_pcom_process_template_postlist(self):

        for ind,test in enumerate(tv.test_values_1):

            print('\n' + test['remark'] + '\n')

            result,processed = libs.second_processes.pcom_process_template_postlist(
                postlist=test['postlist'],
                archive=test['archive'],
                type=test['type'],
                settings=test['settings'],
                list_meta=test['list_meta'],
                fileroot=test['fileroot'],
                sub=test['sub'])

            print(result)

            # check asserts in
            with self.subTest(i=ind+1):
                self.assertEqual(test['assertEqual']['result'].strip(), result.strip())
                self.assertEqual(test['assertEqual']['processed'], processed)

    @testCall
    def test_pcom_process_template_list_info(self):

        for ind,test in enumerate(tv.test_values_2):

            print('\n' + test['remark'] + '\n')

            settings=test['settings']
            settings['template_main_header_text'] = test['template_main_header_text']

            result,info,processed = libs.second_processes.pcom_process_template_list_info(
                list=test['list'],
                settings=settings,
                base_url=test['base_url'],
                fileroot=test['fileroot'])


            print(result)
            print(info)
            print(processed)

            # check asserts in
            with self.subTest(i=ind+1):
                self.assertEqual(test['assertEqual']['result'].strip(), result.strip())
                self.assertEqual(test['assertEqual']['processed'], processed)

        settings['template_main_header_text'] = \
        libs.globals.DEFAULT_TEMPLATE_MAIN_HEADER_TEXT


    @testCall
    def test_pcom_process_archive_info(self):

        for ind,test in enumerate(tv.test_values_3):

            print('\n' + test['remark'] + '\n')

            settings=test['settings']
            settings['template_main_header_text'] = test['template_main_header_text']

            result,info,processed = libs.second_processes.pcom_process_archive_info(
                archive=test['archive'],
                settings=settings,
                base_url=test['base_url'],
                base_name=test['base_name'],
                fileroot=test['fileroot'])

            print(result)
            print(info)
            print(processed)

            # check asserts in
            with self.subTest(i=ind+1):
                self.assertEqual(test['assertEqual']['result'].strip(), result.strip())
                self.assertEqual(test['assertEqual']['processed'], processed)

        settings['template_main_header_text'] = \
        libs.globals.DEFAULT_TEMPLATE_MAIN_HEADER_TEXT

    @testCall
    def test_pcom_update_template_meta(self):

        for ind,test in enumerate(tv.test_values_4):

            print('\n' + test['remark'] + '\n')

            result = libs.second_processes.pcom_update_template_meta(
                template_content=test['template_content'],
                info=test['info'],
                no_meta=test['no_meta'])

            print(result)

            # check asserts in
            with self.subTest(i=ind+1):
                self.assertEqual(test['assertEqual'].strip(), result.strip())


    @testCall
    def test_pcom_create_template_info_references(self):

        for ind,test in enumerate(tv.test_values_5):

            print('\n' + test['remark'] + '\n')

            result = libs.second_processes.pcom_create_template_info_references(
                list=test['list'],
                base_string=test['base_string'],
                settings=test['settings'])

            print(result)

            # check asserts in
            with self.subTest(i=ind+1):
                self.assertEqual(test['assertEqual'], result)


    @testCall
    def test_pcom_create_archive_info_references(self):

        for ind,test in enumerate(tv.test_values_6):

            print('\n' + test['remark'] + '\n')

            result = libs.second_processes.pcom_create_archive_info_references(
                list=test['list'],
                base_string=test['base_string'],
                settings=test['settings'])

            print(result)

            # check asserts in
            with self.subTest(i=ind+1):
                self.assertEqual(test['assertEqual'], result)

if __name__ == '__main__':
    unittest.main()
