import unittest
import libraries.morflessLibs as libs
import datetime

# import test values and expected outputs
# main includes sidebar data
import unit.lists_test_io.lists_5_functions_io as tv

from collections import OrderedDict

from fixtures.decorators import testCall

class ListsHandler5Case(unittest.TestCase):

    # set up and tear down reset to default settings
    def setUp(self):
        self.maxDiff= None
        self.settings = libs.string_processes.pcom_build_dictionary(libs.globals.DEFAULT_SETTINGS)

    def tearDown(self):
        self.settings = dict()

    @testCall
    def test_pcom_update_postlists_info(self):

        for ind,test in enumerate(tv.test_values_1):

            print('\n' + test['remark'] + '\n')

            inputs = test['inputs']
            result = libs.lists.pcom_update_postlists_info(
                                    postlist_info=inputs['postlist_info'],
                                    local_info=inputs['local_info'],
                                    js_name=inputs['js_name'],
                                    fileroot=inputs['fileroot'],
                                    is_template=inputs['is_template'],
                                    is_search=inputs['is_search'])


            print(result)

            with self.subTest(i=ind+1):
                self.assertEqual(result,test['assertEqual'])

    @testCall
    def test_pcom_update_pagination_info(self):

        for ind,test in enumerate(tv.test_values_2):

            print('\n' + test['remark'] + '\n')

            inputs = test['inputs']
            result = libs.lists.pcom_update_pagination_info(
                                    pagination_info=inputs['pagination_info'],
                                    local_info=inputs['local_info'],
                                    pagination_name=inputs['pagination_name'],
                                    fileroot=inputs['fileroot'])

            print(result)

            with self.subTest(i=ind+1):
                self.assertEqual(result,test['assertEqual'])

    @testCall
    def test_pcom_get_archive_date_info(self):

        print('\nTest 1: pcom_get_archive_date_info - US date format\n')

        archive_settings = libs.globals.DEFAULT_SETTINGS
        archive_settings['date_format'] = libs.constants.PCOM_US_DATE_FORMAT
        result = libs.lists.pcom_get_archive_date_info(
                            date_string='34/67/78',
                            settings=archive_settings)

        print(result)

        out = {'month': '34',
        'year': '78',
        'date_fileroot': '34_78',
        'date_url_name': '34-78'
        }
        self.assertEqual(result,out)

        print('\nTest 2: pcom_get_archive_date_info - UK date format\n')

        archive_settings = libs.globals.DEFAULT_SETTINGS
        archive_settings['date_format'] = libs.constants.PCOM_UK_DATE_FORMAT
        result = libs.lists.pcom_get_archive_date_info(
                            date_string='34/67/80003',
                            settings=archive_settings)

        print(result)

        out = {'month': '67',
        'year': '80003',
        'date_fileroot': '67_80003',
        'date_url_name': '67-80003'
        }
        self.assertEqual(result,out)


    @testCall
    def test_pcom_create_archive_entry(self):

        print('\nTest 1: pcom_create_archive_entry - post type = post\n')
        test_post = {\
        'type': 'post',
        'postname': 'test1'
        }
        test_dates = {\
        'date_url_name': '3456',
        'date_fileroot': '546'
        }
        result = libs.lists.pcom_create_archive_entry(
                                list=[],
                                post=test_post,
                                dates=test_dates)


        print(result)

        out = [OrderedDict([ ('name', '3456'),
            ('fileroot', '546'),
            ('posts', [ 'test1' ]),
            ('pages', [])   ])]
        self.assertEqual(result,out)

        print('\nTest 2: pcom_create_archive_entry - post type = something\n')
        test_post = {\
        'type': 'something',
        'postname': 'test1'
        }
        test_dates = {\
        'date_url_name': '3756',
        'date_fileroot': '548'
        }
        result = libs.lists.pcom_create_archive_entry(
                                list=[],
                                post=test_post,
                                dates=test_dates)


        print(result)

        out = [OrderedDict([ ('name', '3756'),
            ('fileroot', '548'),
            ('posts', []),
            ('pages', [ 'test1'])   ])]
        self.assertEqual(result,out)


    def test_pcom_update_archive(self):

        for ind,test in enumerate(tv.test_values_3):

            print('\n' + test['remark'] + '\n')

            inputs = test['inputs']
            result = libs.lists.pcom_update_archive(
                            archive=inputs['archive'],
                            postlist=inputs['postlist'],
                            settings=inputs['settings'])

            print(result)

            with self.subTest(i=ind+1):
                self.assertEqual(result,test['assertEqual'])


if __name__ == '__main__':
    unittest.main()
