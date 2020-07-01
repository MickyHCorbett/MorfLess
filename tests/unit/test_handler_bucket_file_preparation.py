import unittest
import libraries.morflessLibs as libs

import unit.bucket_file_preparation_test_io.bucket_file_preparation_1_functions_io as tv

from fixtures.decorators import testCall

class BucketFilePreparationHandler1Case(unittest.TestCase):

    # set up and tear down reset to default settings
    def setUp(self):
        self.maxDiff= None
        self.settings = libs.string_processes.pcom_build_dictionary(libs.globals.DEFAULT_SETTINGS)

    def tearDown(self):
        self.settings = dict()

    @testCall
    def test_classes_determine_bucket_and_key(self):

        for ind,test in enumerate(tv.test_values_1):

            print('\n' + test['remark'] + '\n')

            htmlOut = libs.classes.HtmlOut(
                                content=test['content'],
                                log=test['log'],
                                site_settings=test['site_settings'],
                                list_meta=test['list_meta'],
                                filename=test['filename'],
                                dependencies=test['dependencies'],
                                postlist=test['postlist'])

            htmlOut.meta = test['meta']

            key,bucket = libs.bucket_file_preparation.determine_bucket_and_key(
                    htmlOut=htmlOut,
                    target=test['target'],
                    list_bucket=test['list_bucket'])

            print(key)
            print(bucket)

            with self.subTest(i=ind+1):
                self.assertEqual(key,test['assertEqual']['key'])
                self.assertEqual(bucket,test['assertEqual']['bucket'])


if __name__ == '__main__':
    unittest.main()
