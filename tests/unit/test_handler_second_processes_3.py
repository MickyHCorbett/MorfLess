import unittest
import libraries.morflessLibs as libs

# import test values and expected outputs
# main includes sidebar data
import unit.second_processes_test_io.second_processes_3_functions_io as tv

from fixtures.decorators import testCall

class SecondProcessesHandler3Case(unittest.TestCase):

    # set up and tear down reset to default settings
    def setUp(self):
        self.maxDiff= None
        self.settings = libs.string_processes.pcom_build_dictionary(libs.globals.DEFAULT_SETTINGS)

    def tearDown(self):
        self.settings = dict()

    @testCall
    def test_pcom_process_pagination(self):

        for ind,test in enumerate(tv.test_values_1):

            print('\n' + test['remark'] + '\n')

            result,processed = libs.second_processes.pcom_process_pagination(
                postlist=test['postlist'],
                pg_name=test['pg_name'],
                fileroot=test['fileroot'],
                info=test['info'])

            print(result)
            print(processed)

            # check asserts in
            with self.subTest(i=ind+1):
                self.assertEqual(test['assertEqual']['result'].strip(), result.strip())
                self.assertEqual(test['assertEqual']['processed'], processed)

    @testCall
    def test_pcom_process_posts_page(self):

        for ind,test in enumerate(tv.test_values_2):

            print('\n' + test['remark'] + '\n')

            info,log = libs.second_processes.pcom_process_posts_page(
                                postlist=test['postlist'],
                                archive=test['archive'],
                                settings=test['settings'],
                                list_meta=test['list_meta'],
                                log=test['log'],
                                template_content=test['template_content'])

            print(info)
            print(log)

            # check asserts in
            with self.subTest(i=ind+1):
                for k,v in test['assertEqual']['info'].items():
                    if k == 'processed':
                        self.assertEqual(v, info[k])
                    else:
                        self.assertEqual(v.strip(), info[k].strip())

                self.assertEqual(test['assertEqual']['log'], log)


    @testCall
    def test_pcom_process_info_base_pages(self):

        for ind,test in enumerate(tv.test_values_3):

            print('\n' + test['remark'] + '\n')

            settings=test['settings']

            settings['template_sub_header_text'] = \
            libs.globals.DEFAULT_TEMPLATE_SUB_HEADER_TEXT

            info,base_sub_info,log = libs.second_processes.pcom_process_info_base_pages(
                info_list=test['info_list'],
                base_type=test['base_type'],
                template_content=test['template_content'],
                postlist=test['postlist'],
                archive=test['archive'],
                settings=settings,
                list_meta=test['list_meta'],
                log=test['log'])

            print(info)
            print(base_sub_info)
            print(log)

            # check asserts in
            with self.subTest(i=ind+1):
                for k,v in test['assertEqual']['info'].items():
                    if k == 'processed':
                        self.assertEqual(v, info[k])
                    else:
                        self.assertEqual(v.strip(), info[k].strip())

                self.assertEqual(test['assertEqual']['log'], log)

                for ind,item in enumerate(test['assertEqual']['base_sub_info']):
                    for k,v in item.items():
                        self.assertEqual(v.strip(), base_sub_info[ind][k].strip())


    @testCall
    def test_pcom_process_search_config(self):

        for ind,test in enumerate(tv.test_values_4):

            print('\n' + test['remark'] + '\n')

            settings = test['settings']
            settings['template_main_header_text'] = test['template_main_header_text']
            result = libs.second_processes.pcom_process_search_config(
                                                settings=settings)

            print(result)

            # check asserts in
            with self.subTest(i=ind+1):
                self.assertEqual(test['assertEqual'].strip(), result.strip())

        # reset settings
        settings['template_main_header_text'] = \
        libs.globals.DEFAULT_TEMPLATE_MAIN_HEADER_TEXT


    def test_pcom_create_search_response(self):

        for ind,test in enumerate(tv.test_values_5):

            print('\n' + test['remark'] + '\n')

            result = libs.second_processes.pcom_create_search_response(
                                            search_content=test['search_content'],
                                            postlist=test['postlist'],
                                            settings=test['settings'],
                                            list_meta=test['list_meta'])

            print(result)

            # check asserts in
            with self.subTest(i=ind+1):
                self.assertEqual(test['assertEqual'], result)


    def test_pcom_search_content(self):

        for ind,test in enumerate(tv.test_values_6):

            print('\n' + test['remark'] + '\n')

            result = libs.second_processes.pcom_search_content(
                                            search_content=test['search_content'],
                                            search_term=test['search_term'])

            print(result)

            # check asserts in
            with self.subTest(i=ind+1):
                self.assertEqual(test['assertEqual'], result)



if __name__ == '__main__':
    unittest.main()
