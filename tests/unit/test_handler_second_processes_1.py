import unittest
import libraries.morflessLibs as libs

# import test values and expected outputs
# main includes sidebar data
import unit.second_processes_test_io.second_processes_1_functions_io as tv

from fixtures.decorators import testCall

class SecondProcessesHandler1Case(unittest.TestCase):

    # set up and tear down reset to default settings
    def setUp(self):
        self.maxDiff= None
        self.settings = libs.string_processes.pcom_build_dictionary(libs.globals.DEFAULT_SETTINGS)

    def tearDown(self):
        self.settings = dict()

    @testCall
    def test_pcom_process_postlist(self):

        for ind,test in enumerate(tv.test_values_1):

            print('\n' + test['remark'] + '\n')

            result,processed = libs.second_processes.pcom_process_postlist(
                postlist_info=test['postlist_info'],
                postlist=test['postlist'],
                settings=test['settings'],
                list_meta=test['list_meta'],
                fileroot=test['fileroot'])

            print(result)

            # check asserts in
            with self.subTest(i=ind+1):
                self.assertEqual(test['assertEqual']['result'].strip(), result.strip())
                self.assertEqual(test['assertEqual']['processed'], processed)

    @testCall
    def test_pcom_create_sub_template_backlink(self):

        for ind,test in enumerate(tv.test_values_2):

            print('\n' + test['remark'] + '\n')

            settings = test['settings']
            settings['template_sub_header_back_link_text'] = test['template_sub_header_back_link_text']

            result = libs.second_processes.pcom_create_sub_template_backlink(
                                                type=test['type'],
                                                settings=settings)

            print(result)

            # check asserts in
            with self.subTest(i=ind+1):
                self.assertEqual(test['assertEqual'].strip(), result.strip())

        # reset settings
        settings['template_sub_header_back_link_text'] = \
        libs.globals.DEFAULT_TEMPLATE_SUB_HEADER_BACK_LINK_TEXT


    @testCall
    def test_pcom_create_sub_template_title(self):

        for ind,test in enumerate(tv.test_values_3):

            print('\n' + test['remark'] + '\n')

            settings = test['settings']
            settings['template_sub_header_text'] = test['template_sub_header_text']
            settings['template_main_header_text'] = test['template_main_header_text']
            settings['template_sub_header_back_link_text'] = test['template_sub_header_back_link_text']

            sub_title,back_link = libs.second_processes.pcom_create_sub_template_title(
                                                type=test['type'],
                                                settings=settings,
                                                sub=test['sub'])

            print(sub_title)
            print(back_link)

            # check asserts in
            with self.subTest(i=ind+1):
                self.assertEqual(test['assertEqual']['sub_title'].strip(), sub_title.strip())
                self.assertEqual(test['assertEqual']['back_link'].strip(), back_link.strip())

        # reset settings
        settings['template_sub_header_text'] = \
        libs.globals.DEFAULT_TEMPLATE_SUB_HEADER_TEXT
        settings['template_main_header_text'] = \
        libs.globals.DEFAULT_TEMPLATE_MAIN_HEADER_TEXT
        settings['template_sub_header_back_link_text'] = \
        libs.globals.DEFAULT_TEMPLATE_SUB_HEADER_BACK_LINK_TEXT


    @testCall
    def test_pcom_determine_post_list_from_type(self):

        for ind,test in enumerate(tv.test_values_4):

            print('\n' + test['remark'] + '\n')

            result = libs.second_processes.pcom_determine_post_list_from_type(
                                            postlist=test['postlist'],
                                            archive=test['archive'],
                                            settings=test['settings'],
                                            list_meta=test['list_meta'],
                                            type=test['type'],
                                            sub=test['sub'])

            print(result)

            # check asserts in
            with self.subTest(i=ind+1):
                self.assertEqual(test['assertEqual'], result)



if __name__ == '__main__':
    unittest.main()
