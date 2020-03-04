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
class CreateListPagesReadWrites(unittest.TestCase):

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
    def test_createListPages_read_writes(self):

        # process_json_files

        print('\nTest 1 - process json file\n')
        self.read_content,self.log = clp.process_json_files(JSON_FILE, clp.listbucket,self.log)
        print('read content: {}'.format(self.read_content))

        # check asserts
        self.assertEqual(JSON_ORDERED, self.read_content)
        self.assertEqual(self.log,{})

        print('\nTest 2 - process json file not present in bucket\n')
        self.read_content,self.log = clp.process_json_files(OTHER_JSON, clp.listbucket,self.log)
        print('read content: {}'.format(self.read_content))

        # check asserts
        self.assertEqual({}, self.read_content)
        log_message = 'File: {} not processed - does not exist'.format(OTHER_JSON)
        self.assertEqual(self.log[OTHER_JSON],log_message)

        # get_site_settings

        print('\nTest 3 - get settings - file does not contain usable data so default settings returned with empty section defaults\n')
        self.log = {}
        self.read_content,self.log = clp.get_site_settings(self.log)
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

        print('\nTest 4 - get settings - no settings file in bucket\n')
        # delete settings file from bucket
        self.s3client.delete_object(
            Bucket=clp.sourcebucket,
            Key='settings.txt')
        self.log = {}
        self.read_content,self.log = clp.get_site_settings(self.log)

        print('Log: {}'.format(self.log))
        print('Settings content {}:'.format(self.read_content))
        log_message = 'File: settings.txt not processed - does not exist'
        self.assertEqual(libs.constants.PCOM_NO_ENTRY, self.read_content)
        self.assertEqual(self.log['settings.txt'],log_message)


        # get template content

        print('\nTest 5 - get template content\n')
        self.log = {}
        self.read_content,self.log = clp.get_template_files(HTML_FILE,self.log)

        print('Log: {}'.format(self.log))
        print(self.read_content)
        self.assertEqual(HTML_TEXT, self.read_content)
        self.assertEqual(self.log,{})

        print('\nTest 6 - get template content - no file in bucket\n')
        self.log = {}
        self.read_content,self.log = clp.get_template_files(OTHERHTML_FILE,self.log)

        print('Log: {}'.format(self.log))
        print(self.read_content)
        log_message = 'File: ' + OTHERHTML_FILE + ' not processed - does not exist'
        self.assertEqual('', self.read_content)
        self.assertEqual(self.log[OTHERHTML_FILE],log_message)

        # write templates to buckets - can be any html

        print('\nTest 7 - write templates to buckets\n')
        outkey = 'categories/something/index.html'
        self.log = {'outputs': []}
        self.log = clp.write_templates_to_buckets(outkey,'categories-something',HTML_TEXT,self.log)
        print('Log: {}'.format(self.log))
        log_message = 'File: categories-something processed and output as categories/something/index.html'
        self.assertEqual(self.log['outputs'],[log_message])

        # check content
        self.log = {}
        processed,self.read_content,self.log = clp.get_content_from_s3(outkey, clp.targetbucket,self.log)
        self.assertTrue(processed)
        self.assertEqual(HTML_TEXT,self.read_content)

        # write js to target

        print('\nTest 8 - write templates to buckets\n')
        outkey = "js/js-lists/" + JS_NAME
        self.log = {'outputs': []}
        self.log = clp.write_js_to_buckets(JS_NAME,JS_CONSTANT,self.log)
        print('Log: {}'.format(self.log))
        log_message = 'File: '+ JS_NAME + ' processed and output as ' + outkey
        self.assertEqual(self.log['outputs'],[log_message])

        # check content
        self.log = {}
        processed,self.read_content,self.log = clp.get_content_from_s3(outkey, clp.targetbucket,self.log)
        self.assertTrue(processed)
        self.assertEqual(JS_CONSTANT,self.read_content)


if __name__ == '__main__':
    unittest.main()
