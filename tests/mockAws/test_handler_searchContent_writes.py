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

import lambda_source.SearchContent.searchContent_handlerLibrary as sct

from fixtures.create_files_for_bucket import get_file_content
from fixtures.decorators import testCall
from collections import OrderedDict

# constants for test
SETTINGS_FILE = 'settings.txt'
POSTLIST_FILE = 'postlist.json'
ARCHIVE_FILE = 'archive.json'
DEFAULT_SOURCE_ROOT = "tests/mockAws/default_source/renderHtml_writes/"
CATEGORIES_FILE = 'categories.json'
AUTHORS_FILE = 'authors.json'

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

JSON_TEXT = """
{
    "variable1": "this",
    "variable2": "that"
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


@mock_s3
class SearchContentReadWrites(unittest.TestCase):

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

        file_source = os.path.join(class_dir,DEFAULT_SOURCE_ROOT,CATEGORIES_FILE)
        categories = get_file_content(file_source)
        file_source = os.path.join(class_dir,DEFAULT_SOURCE_ROOT,AUTHORS_FILE)
        authors = get_file_content(file_source)


        # create bucket and write json content to it
        self.s3resource = boto3.resource('s3', region_name=REGION)

        self.s3resource.create_bucket(Bucket=sct.sourcebucket)
        self.s3resource.create_bucket(Bucket=sct.listbucket)
        self.s3resource.create_bucket(Bucket=sct.searchbucket)

        self.s3client = boto3.client('s3', region_name=REGION)
        self.s3client.put_object(Bucket=sct.listbucket, Key=JSON_FILE, Body=JSON_TEXT)
        self.s3client.put_object(Bucket=sct.searchbucket, Key=HTML_FILE, Body=HTML_TEXT)
        self.s3client.put_object(Bucket=sct.sourcebucket, Key=SETTINGS_FILE, Body=self.settings_content)
        self.s3client.put_object(Bucket=sct.listbucket, Key=CATEGORIES_FILE, Body=categories)
        self.s3client.put_object(Bucket=sct.listbucket, Key=AUTHORS_FILE, Body=authors)

    def tearDown(self):
        self.log = {}
        self.source_content = ''
        self.read_content = ''
        self.settings_content = {}
        self.postlist_default = {}
        # delete content from s3 and delete buckets

        # source
        bucket = self.s3resource.Bucket(sct.sourcebucket)
        for key in bucket.objects.all():
            key.delete()
        bucket.delete()
        # list
        bucket = self.s3resource.Bucket(sct.listbucket)
        for key in bucket.objects.all():
            key.delete()
        bucket.delete()
        # target
        bucket = self.s3resource.Bucket(sct.searchbucket)
        for key in bucket.objects.all():
            key.delete()
        bucket.delete()


    @testCall
    def test_searchContent_read_writes(self):

        # ==============
        # process json files
        # ==============

        print('\nTest 1 - process json file\n')
        self.read_content,self.log = sct.process_json_files(JSON_FILE, sct.listbucket,self.log)
        print('read content: {}'.format(self.read_content))

        # check asserts
        self.assertEqual(JSON_ORDERED, self.read_content)
        self.assertEqual(self.log,{})

        print('\nTest 2 - process json file not present in bucket\n')
        self.read_content,self.log = sct.process_json_files(OTHER_JSON, sct.listbucket,self.log)
        print('read content: {}'.format(self.read_content))

        # check asserts
        self.assertEqual({}, self.read_content)
        log_message = 'File: {} not processed - does not exist'.format(OTHER_JSON)
        self.assertEqual(self.log[OTHER_JSON],log_message)

        # ==============
        # get site settings
        # ==============

        print('\nTest 3 - get settings - file does not contain usable data so default settings returned with empty section defaults\n')
        self.log = {}
        self.read_content,self.log = sct.get_site_settings(self.log)
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
            Bucket=sct.sourcebucket,
            Key='settings.txt')
        self.log = {}
        self.read_content,self.log = sct.get_site_settings(self.log)

        print('Log: {}'.format(self.log))
        print('Settings content {}:'.format(self.read_content))
        log_message = 'File: settings.txt not processed - does not exist'
        self.assertEqual(libs.constants.PCOM_NO_ENTRY, self.read_content)
        self.assertEqual(self.log['settings.txt'],log_message)


        # ==============
        # read file content
        # ==============

        print('\nTest 5 - read content\n')
        self.log = {}
        self.read_content,self.log = sct.read_content_file(HTML_FILE,sct.searchbucket,self.log)

        print('Log: {}'.format(self.log))
        print(self.read_content)
        self.assertEqual(HTML_TEXT, self.read_content)
        self.assertEqual(self.log,{})

        print('\nTest 6 - read content- no file in bucket\n')
        self.log = {}
        self.read_content,self.log = sct.read_content_file(OTHERHTML_FILE,sct.searchbucket,self.log)

        print('Log: {}'.format(self.log))
        print(self.read_content)
        log_message = 'File: ' + OTHERHTML_FILE + ' not processed - does not exist'
        self.assertEqual('', self.read_content)
        self.assertEqual(self.log[OTHERHTML_FILE],log_message)


        # ==============
        # build list meta
        # ==============


        print('\nTest 7 - build list meta\n')
        self.log = {}
        settings = libs.globals.DEFAULT_SETTINGS
        list_meta,self.log = sct.build_list_meta(settings,self.log)
        print('Log: {}'.format(self.log))

        # check categories content
        for ind,entry in enumerate(list_meta['categories']['categories']):
            if ind == 0:
                self.assertEqual(entry['name'],"something")
                self.assertEqual(entry['thumbnail'],"/images/Polimorf-shapes-background.jpg")
                self.assertEqual(entry['description'],"")
            if ind == 1:
                self.assertEqual(entry['name'],"another category")
                self.assertEqual(entry['thumbnail'],"/images/Polimorf-shapes-background.jpg")
                self.assertEqual(entry['description'],"")
            if ind == 2:
                self.assertEqual(entry['name'],"interesting")
                self.assertEqual(entry['thumbnail'],"/images/Polimorf-shapes-background-2.jpg")
                self.assertEqual(entry['description'],"")
            if ind == 3:
                self.assertEqual(entry['name'],"things to write about")
                self.assertEqual(entry['thumbnail'],"/images/Polimorf-shapes-background-2.jpg")
                self.assertEqual(entry['description'],"")

        # check some authors content
        for ind,entry in enumerate(list_meta['authors']['authors']):
            if ind == 0:
                self.assertEqual(entry['name'],"Corvos AE Team")
                self.assertEqual(entry['shortname'],"Team_CAE")
                self.assertEqual(entry['thumbnail'],"/images/CorvosTeam.jpg")
                self.assertEqual(entry['description'],"General information and content from the Corvos Astro Engineering site")
            if ind == 3:
                self.assertEqual(entry['name'],"Jim O'Neill")
                self.assertEqual(entry['shortname'],"Jim O'Neill")
                self.assertEqual(entry['thumbnail'],"/images/Polimorf-shapes-background-2.jpg")
                self.assertEqual(entry['description'],"")


if __name__ == '__main__':
    unittest.main()
