import unittest
import libraries.morflessLibs as libs
import boto3
import os

"""
set environment to allow
renderHtml handler library module to be called
"""

from moto import mock_s3

os.environ['SOURCE_BUCKET'] = "sourcebucket"
os.environ['TARGET_BUCKET'] = "targetbucket"
os.environ["LIST_BUCKET"] = "listbucket"
os.environ["SEARCH_BUCKET"] = "searchbucket"

import lambda_source.RenderHtml.renderHtml_handlerLibrary as rdl

from fixtures.create_files_for_bucket import get_file_content
from fixtures.decorators import testCall
from collections import OrderedDict

# constants for test
SETTINGS_NAME = 'settings.txt'
SETTINGS_FILE = "tests/mockAws/default_source/settings.txt"

FILENAME = "test_file.txt"
OTHERFILE = "test_file_other.txt"
REGION = "us-east-1"
FILE_SOURCE = "tests/mockAws/default_source/settings.txt"

JSON_FILE = 'test_json_file.json'
JSON_FILE_2 = 'test_json_file_2.json'
OTHER_JSON = 'test_other.json'
HTML_FILE = 'test_html_file.html'
STANDARD_FILE = 'test_standard_file.txt'

JSON_TEXT = """
{
    "variable1": "this",
    "variable2": "that"
}
"""
JSON_TEXT_2 = """
{
    "variable3": "this",
    "variable4": {
        "variable5" : [
            "that",
            "that again"
        ]
    }
}
"""

JSON_ORDERED = OrderedDict([('variable1', 'this'), ('variable2', 'that')])

HTML_TEXT = """
<html>
<head>Something here</head>
<body>Somethinf else here</body>
</html>
"""

STANDARD_TEXT = """
Something here
"""

CONTENT_DISPOSITION = 'ContentDisposition'

@mock_s3
class RenderHtmlReadWrites(unittest.TestCase):

    # set up bucket
    def setUp(self):
        self.log = {}
        self.read_content = ''
        self.maxDiff = None

        class_dir = os.getcwd()
        file_source = os.path.join(class_dir,SETTINGS_FILE)
        self.settings_content = get_file_content(file_source)

        # create bucket and write json content to it
        self.s3resource = boto3.resource('s3', region_name=REGION)

        self.s3resource.create_bucket(Bucket=rdl.sourcebucket)
        self.s3resource.create_bucket(Bucket=rdl.listbucket)
        self.s3resource.create_bucket(Bucket=rdl.searchbucket)
        self.s3resource.create_bucket(Bucket=rdl.targetbucket)

        self.s3client = boto3.client('s3', region_name=REGION)
        self.s3client.put_object(Bucket=rdl.listbucket, Key=JSON_FILE, Body=JSON_TEXT)
        self.s3client.put_object(Bucket=rdl.sourcebucket, Key=SETTINGS_NAME, Body=self.settings_content)


    def tearDown(self):
        self.log = {}
        self.source_content = ''
        self.read_content = ''
        self.settings_content = {}
        # delete content from s3 and delete buckets

        # source
        bucket = self.s3resource.Bucket(rdl.sourcebucket)
        for key in bucket.objects.all():
            key.delete()
        bucket.delete()
        # list
        bucket = self.s3resource.Bucket(rdl.listbucket)
        for key in bucket.objects.all():
            key.delete()
        bucket.delete()
        # search
        bucket = self.s3resource.Bucket(rdl.searchbucket)
        for key in bucket.objects.all():
            key.delete()
        bucket.delete()
        # target
        bucket = self.s3resource.Bucket(rdl.targetbucket)
        for key in bucket.objects.all():
            key.delete()
        bucket.delete()


    @testCall
    def test_renderHtml_read_writes(self):

        # read json content

        print('\nTest 1 - process json file\n')
        self.read_content,self.log = rdl.process_json_files(JSON_FILE, rdl.listbucket,self.log)
        print('read content: {}'.format(self.read_content))

        # check asserts
        self.assertEqual(JSON_ORDERED, self.read_content)
        self.assertEqual(self.log,{})

        print('\nTest 2 - process json file not present in bucket\n')
        self.read_content,self.log = rdl.process_json_files(OTHER_JSON, rdl.listbucket,self.log)
        print('read content: {}'.format(self.read_content))

        # check asserts
        self.assertEqual({}, self.read_content)
        log_message = 'File: {} not processed - does not exist'.format(OTHER_JSON)
        self.assertEqual(self.log[OTHER_JSON],log_message)


        # write json content
        self.log = {}

        print('\nTest 3 - write_source_json\n')
        self.log = rdl.write_source_json(rdl.listbucket,JSON_FILE_2,JSON_TEXT_2,self.log)
        # save local copy of log
        write_log = self.log
        print(write_log)

        # read file for confirmation - reset log
        self.log = {}
        processed,self.read_content,self.log = rdl.get_content_from_s3(JSON_FILE_2, rdl.listbucket,self.log)
        # check asserts
        self.assertEqual(processed,True)
        self.assertEqual(JSON_TEXT_2, self.read_content)
        self.assertEqual(self.log,{})
        log_message = 'JSON File: {} processed and updated'.format(JSON_FILE_2)
        self.assertEqual(write_log[JSON_FILE_2],log_message)

        # update info json  - any json can be used
        print('\nTest 4 - update list json info\n')
        self.log = {}
        info = JSON_TEXT
        filename = JSON_FILE
        self.log = rdl.update_list_json_info(info,filename,self.log)
        print(self.log)
        log_message = 'JSON File: {} processed and updated'.format(JSON_FILE)
        self.assertEqual(self.log[JSON_FILE],log_message)

        # read settings
        print('\nTest 5 - get settings - file does not contain usable data so default settings returned with empty section defaults\n')
        self.log = {}
        self.read_content,self.log = rdl.get_site_settings(self.log)
        settings = libs.globals.DEFAULT_SETTINGS
        # set section html to empty
        settings['default_header'] = ''
        settings['default_before'] = ''
        settings['default_main'] = ''
        settings['default_after'] = ''
        settings['default_sidebar'] = ''
        settings['default_footer'] = ''

        print('Log: {}'.format(self.log))
        print('Settings content {}:'.format(self.read_content))
        self.assertEqual(settings, self.read_content)
        self.assertEqual(self.log,{})



if __name__ == '__main__':
    unittest.main()
