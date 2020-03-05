import unittest
import libraries.morflessLibs as libs
import boto3
import os, json

"""
set environment to allow
renderHtml handler library module to be called
"""

from moto import mock_s3

os.environ['SOURCE_BUCKET'] = "sourcebucket"
os.environ['TARGET_BUCKET'] = "targetbucket"
os.environ["LIST_BUCKET"] = "listbucket"

import lambda_source.CreateListPages.createListPages_handlerLibrary as clp

from fixtures.create_files_for_bucket import get_file_content
from fixtures.decorators import testCall
from collections import OrderedDict

# constants for test
SETTINGS_FILE = 'settings.txt'
POSTLIST_FILE = 'postlist.json'
ARCHIVE_FILE = 'archive.json'
DEFAULT_SOURCE_ROOT = "tests/mockAws/default_source/renderHtml_writes/"

FILENAME = "test_file.txt"
OTHERFILE = "test_file_other.txt"
REGION = "us-east-1"
FILE_SOURCE = "tests/mockAws/default_source/settings.txt"

JSON_FILE = 'test_json_file.json'
JSON_FILE_2 = 'test_json_file_2.json'
OTHER_JSON = 'test_other.json'
HTML_FILE = 'test_html_file.html'
OTHERHTML_FILE = 'test_other_html_file.html'
STANDARD_FILE = 'test_standard_file.txt'
JS_NAME = 'js_constant.js'

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

JS_CONSTANT = """
window._js_constant_name = {
    something: 'a list of things',
    something_else: 'another thing'
};
"""
CONTENT_DISPOSITION = 'ContentDisposition'

CATEGORIES_DEFAULT = {
    "no_of_category_pages": 1,
    "categories": [
    ]
}
AUTHORS_DEFAULT = {
    "no_of_author_pages": 1,
    "authors": [
    ]
}
LIST_META_DEFAULT = { \
'categories': CATEGORIES_DEFAULT,
'authors': AUTHORS_DEFAULT
}

@mock_s3
class CreateListPagesProcess(unittest.TestCase):

    # set up bucket
    def setUp(self):
        self.log = {}
        self.read_content = ''
        self.maxDiff = None

        class_dir = os.getcwd()
        file_source = os.path.join(class_dir,DEFAULT_SOURCE_ROOT,SETTINGS_FILE)
        self.settings_content = get_file_content(file_source)
        file_source = os.path.join(class_dir,DEFAULT_SOURCE_ROOT,POSTLIST_FILE)
        self.postlist_default = json.loads(get_file_content(file_source))
        file_source = os.path.join(class_dir,DEFAULT_SOURCE_ROOT,ARCHIVE_FILE)
        self.archive_default = json.loads(get_file_content(file_source))

        # create bucket and write json content to it
        self.s3resource = boto3.resource('s3', region_name=REGION)

        self.s3resource.create_bucket(Bucket=clp.sourcebucket)
        self.s3resource.create_bucket(Bucket=clp.listbucket)
        self.s3resource.create_bucket(Bucket=clp.targetbucket)

        self.s3client = boto3.client('s3', region_name=REGION)
        self.s3client.put_object(Bucket=clp.listbucket, Key=JSON_FILE, Body=JSON_TEXT)
        self.s3client.put_object(Bucket=clp.listbucket, Key=HTML_FILE, Body=HTML_TEXT)
        self.s3client.put_object(Bucket=clp.sourcebucket, Key=SETTINGS_FILE, Body=self.settings_content)


    def tearDown(self):
        self.log = {}
        self.source_content = ''
        self.read_content = ''
        self.settings_content = {}
        self.postlist_default = {}
        # delete content from s3 and delete buckets

        # source
        bucket = self.s3resource.Bucket(clp.sourcebucket)
        for key in bucket.objects.all():
            key.delete()
        bucket.delete()
        # list
        bucket = self.s3resource.Bucket(clp.listbucket)
        for key in bucket.objects.all():
            key.delete()
        bucket.delete()
        # target
        bucket = self.s3resource.Bucket(clp.targetbucket)
        for key in bucket.objects.all():
            key.delete()
        bucket.delete()


    @testCall
    def test_createListPages_process(self):

        # process search config - write search configuration js to file

        print('\nTest 1 - process search config\n')
        config_key = "js/js-lists/" + libs.constants.PCOM_SEARCH_CONFIG_JS_NAME
        self.log = {'outputs': []}
        settings = libs.globals.DEFAULT_SETTINGS
        sub_title_text = 'This is a subtitle'
        settings['template_main_header_text'][libs.constants.PCOM_SETTINGS_TYPE_SEARCH] = sub_title_text
        self.log = clp.process_search_config(settings,self.log)

        print('Log: {}'.format(self.log))
        log_message = 'File: '+ libs.constants.PCOM_SEARCH_CONFIG_JS_NAME + ' processed and output as ' + config_key
        self.assertEqual(self.log['outputs'],[log_message])

        # check content
        self.log = {}
        processed,self.read_content,self.log = clp.get_content_from_s3(config_key, clp.targetbucket,self.log)
        print('Search config content: {}'.format(self.read_content))
        self.assertTrue(processed)
        self.assertIn(sub_title_text,self.read_content)


if __name__ == '__main__':
    unittest.main()
