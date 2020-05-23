import unittest
import libraries.morflessLibs as libs
import datetime

# import test values and expected outputs
# main includes sidebar data
import unit.lists_test_io.lists_4_functions_io as tv

from unit.lists_test_io.lists_supplemental import POSTLIST_2,POSTLIST_3


from fixtures.decorators import testCall

class ListsHandler4Case(unittest.TestCase):

    # set up and tear down reset to default settings
    def setUp(self):
        self.maxDiff= None
        self.settings = libs.string_processes.pcom_build_dictionary(libs.globals.DEFAULT_SETTINGS)

    def tearDown(self):
        self.settings = dict()

    @testCall
    def test_pcom_update_postlist_empty(self):

        for ind,test in enumerate(tv.test_values_1):

            print('\n' + test['remark'] + '\n')

            inputs = test['inputs']
            result = libs.lists.pcom_update_postlist(
                                    postlist=inputs['postlist'],
                                    postname=inputs['postname'],
                                    url=inputs['url'],
                                    meta=inputs['meta'],
                                    date_format=inputs['date_format'],
                                    type=inputs['type'],
                                    settings=inputs['settings'])


            print(result)

            with self.subTest(i=ind+1):
                self.assertEqual(result,test['assertEqual'])

    @testCall
    def test_pcom_update_postlist(self):

        for ind,test in enumerate(tv.test_values_2):

            print('\n' + test['remark'] + '\n')

            inputs = test['inputs']
            entry = test['entry']

            result = libs.lists.pcom_update_postlist(
                                    postlist=inputs['postlist'],
                                    postname=inputs['postname'],
                                    url=inputs['url'],
                                    meta=inputs['meta'],
                                    date_format=inputs['date_format'],
                                    type=inputs['type'],
                                    settings=inputs['settings'])

            # get post and check data (don't check time)
            test_post = libs.lists.pcom_find_post(result,entry)
            print(test_post)

            with self.subTest(i=ind+1):
                for test_point,val in test['assertEqual'].items():
                    self.assertEqual(test_post[test_point],val)

            local_date = libs.lists.pcom_get_date(inputs['date_format'])
            self.assertEqual(test_post['date_modified'],local_date)

            # check post indices
            self.assertEqual(result['post_index'],test['post_index'])
            self.assertEqual(result['no_posts'],test['no_posts'])

    @testCall
    def test_pcom_update_postlist_entry(self):

        for ind,test in enumerate(tv.test_values_3):

            print('\n' + test['remark'] + '\n')

            inputs = test['inputs']
            entry = test['entry']

            result = libs.lists.pcom_update_postlist_entry(
                    post=inputs['post'],
                    url=inputs['url'],
                    name=inputs['postname'],
                    meta=inputs['meta'],
                    date=inputs['date'],
                    time=inputs['time'],
                    new=inputs['new'],
                    index=inputs['index'],
                    type=inputs['type'],
                    settings=inputs['settings'])

            print(result)

            with self.subTest(i=ind+1):
                for test_point,val in test['assertEqual'].items():
                    self.assertEqual(result[test_point],val)

    @testCall
    def test_pcom_delete_from_postlist(self):

        print('\nTest 1: pcom_delete_from_postlist - no list\n')
        result = libs.lists.pcom_delete_from_postlist([],'contact.page')
        print(result)
        self.assertEqual(result,[])

        print('\nTest 2: pcom_delete_from_postlist - delete test5.post\n')
        result = libs.lists.pcom_delete_from_postlist(POSTLIST_2,'test5.post')
        print(result)
        self.assertEqual(result,POSTLIST_3)
        self.assertEqual(result['no_posts'],1)

        print('\nTest 3: pcom_delete_from_postlist - delete other post not present - no change\n')
        result = libs.lists.pcom_delete_from_postlist(POSTLIST_2,'other.post')
        print(result)
        self.assertEqual(result,POSTLIST_2)
        self.assertEqual(result['no_posts'],1)

    @testCall
    def test_pcom_find_post_pagination(self):

        for ind,test in enumerate(tv.test_values_4):

            print('\n' + test['remark'] + '\n')

            inputs = test['inputs']

            result,found = libs.lists.pcom_find_post_pagination(
                    postlist=inputs['postlist'],
                    postname=inputs['postname'],
                    type=inputs['type'])

            print(result)

            with self.subTest(i=ind+1):
                self.assertEqual(result,test['assertEqual']['out'])
                self.assertEqual(found,test['assertEqual']['found'])

    @testCall
    def test_pcom_find_manual_pagination(self):

        for ind,test in enumerate(tv.test_values_5):

            print('\n' + test['remark'] + '\n')

            inputs = test['inputs']

            result,found = libs.lists.pcom_find_manual_pagination(
                    postlist=inputs['postlist'],
                    next=inputs['next'],
                    prev=inputs['prev'])

            print(result)

            with self.subTest(i=ind+1):
                self.assertEqual(result,test['assertEqual']['out'])
                self.assertEqual(found,test['assertEqual']['found'])

    @testCall
    def test_pcom_get_pagination_info(self):

        for ind,test in enumerate(tv.test_values_6):

            print('\n' + test['remark'] + '\n')

            inputs = test['inputs']
            html_array = inputs['html'].splitlines(True)
            array,pag_info = libs.lists.pcom_get_pagination_info(
                    html_array=html_array,
                    postlist=inputs['postlist'],
                    postname=inputs['postname'],
                    fileroot=inputs['fileroot'])

            print(array)
            print(pag_info)

            with self.subTest(i=ind+1):
                self.assertEqual(array,test['assertEqual']['array'])
                self.assertEqual(pag_info,test['assertEqual']['info'])


if __name__ == '__main__':
    unittest.main()
