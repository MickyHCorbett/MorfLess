import unittest
import libraries.morflessLibs as libs

# import test values and expected outputs
# main includes sidebar data
import unit.classes_test_io.classes_1_functions_io as tv

from fixtures.decorators import testCall

class ClassesHandler1Case(unittest.TestCase):

    # set up and tear down reset to default settings
    def setUp(self):
        self.maxDiff= None
        self.settings = libs.string_processes.pcom_build_dictionary(libs.globals.DEFAULT_SETTINGS)

    def tearDown(self):
        self.settings = dict()

    @testCall
    def test_classes_init(self):

        for ind,test in enumerate(tv.test_values_1):

            print('\n' + test['remark'] + '\n')

            result = libs.classes.HtmlOut(
                                content=test['content'],
                                log=test['log'],
                                site_settings=test['site_settings'],
                                list_meta=test['list_meta'],
                                filename=test['filename'],
                                dependencies=test['dependencies'],
                                postlist=test['postlist'])

            for k,v in test['assertEqual'].items():
                test_point = eval('result.' + k)
                print(f"{k}: {test_point}")
                self.assertEqual(v,test_point)

    @testCall
    def test_classes_process_pagination(self):

        for ind,test in enumerate(tv.test_values_2):

            print('\n' + test['remark'] + '\n')

            result = libs.classes.HtmlOut(
                                content=test['content'],
                                log=test['log'],
                                site_settings=test['site_settings'],
                                list_meta=test['list_meta'],
                                filename=test['filename'],
                                dependencies=test['dependencies'],
                                postlist=test['postlist'])

            result.meta['unlisted'] = test['meta']['unlisted']
            result.html_array = test['html_array']
            result.process_pagination()

            print(result.pagination_info)

            self.assertEqual(test['assertEqual'],result.pagination_info)


    def test_classes_insert_additions_into_html(self):

        for ind,test in enumerate(tv.test_values_3):

            print('\n' + test['remark'] + '\n')

            result = libs.classes.HtmlOut(
                                content=test['content'],
                                log=test['log'],
                                site_settings=test['site_settings'],
                                list_meta=test['list_meta'],
                                filename=test['filename'],
                                dependencies=test['dependencies'],
                                postlist=test['postlist'])

            result.all_data = {'processed_settings': test['site_settings']}
            result.all_data['processed_settings']['default_header_additions'] = \
            test['default_header_additions']
            result.all_data['processed_settings']['add_default_header_additions'] = \
            test['add_default_header_additions']

            result.all_data['processed_settings']['default_footer_additions'] = \
            test['default_footer_additions']
            result.all_data['processed_settings']['add_default_footer_additions'] = \
            test['add_default_footer_additions']

            result.insert_additions_into_html(test['placement'])

            print(result.site_settings['header_additions'])
            print(result.site_settings['footer_additions'])

            self.assertEqual(test['assertEqual']['header_additions'],result.site_settings['header_additions'])
            self.assertEqual(test['assertEqual']['footer_additions'],result.site_settings['footer_additions'])

            # reset
            result.site_settings['header_additions'] = []
            result.site_settings['default_header_additions'] = ''
            result.site_settings['footer_additions'] = []
            result.site_settings['default_footer_additions'] = ''
            result.site_settings['add_default_header_additions'] = False
            result.site_settings['add_default_footer_additions'] = False

    @testCall
    def test_classes_get_raw_content(self):

        for ind,test in enumerate(tv.test_values_4):

            print('\n' + test['remark'] + '\n')

            result = libs.classes.HtmlOut(
                                content=test['content'],
                                log=test['log'],
                                site_settings=test['site_settings'],
                                list_meta=test['list_meta'],
                                filename=test['filename'],
                                dependencies=test['dependencies'],
                                postlist=test['postlist'])

            result.meta = test['meta']
            result.html = test['html_content']

            result.get_raw_content()

            print(result.raw_content)

            self.assertEqual(test['assertEqual'].strip(),result.raw_content.strip())


    @testCall
    def test_classes_update_postlist(self):

        for ind,test in enumerate(tv.test_values_5):

            print('\n' + test['remark'] + '\n')

            result = libs.classes.HtmlOut(
                                content=test['content'],
                                log=test['log'],
                                site_settings=test['site_settings'],
                                list_meta=test['list_meta'],
                                filename=test['filename'],
                                dependencies=test['dependencies'],
                                postlist=test['postlist'])

            result.meta = test['meta']

            result.update_postlist()

            # find post
            test_post = libs.lists.pcom_find_post(result.postlist,test['filename'])

            self.assertEqual(test['assertEqual'],test_post['postname'])
            print(f"Postname: {test_post['postname']}")


    @testCall
    def test_classes_update_categories(self):

        for ind,test in enumerate(tv.test_values_6):

            print('\n' + test['remark'] + '\n')

            result = libs.classes.HtmlOut(
                                content=test['content'],
                                log=test['log'],
                                site_settings=test['site_settings'],
                                list_meta=test['list_meta'],
                                filename=test['filename'],
                                dependencies=test['dependencies'],
                                postlist=test['postlist'])

            result.meta = test['meta']
            result.update_categories()

            print(f"Categories: {result.list_meta['categories']}")

            self.assertEqual(test['assertEqual'],result.list_meta['categories'])


    @testCall
    def test_classes_update_authors(self):

        for ind,test in enumerate(tv.test_values_7):

            print('\n' + test['remark'] + '\n')

            result = libs.classes.HtmlOut(
                                content=test['content'],
                                log=test['log'],
                                site_settings=test['site_settings'],
                                list_meta=test['list_meta'],
                                filename=test['filename'],
                                dependencies=test['dependencies'],
                                postlist=test['postlist'])

            result.meta = test['meta']
            result.update_authors()

            print(f"Authors: {result.list_meta['authors']}")

            self.assertEqual(test['assertEqual'],result.list_meta['authors'])

if __name__ == '__main__':
    unittest.main()
