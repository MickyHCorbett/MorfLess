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
os.environ["SEARCH_BUCKET"] = "searchbucket"

import lambda_source.RenderHtml.renderHtml_handlerLibrary as rdl

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

DEPENDENCIES_DEFAULT = [\
    {
        "filename": "index.page",
        "dependencies": [
            "settings.txt"
        ]
    },
    {
        "filename": "404.page",
        "dependencies": [
            "settings.txt"
        ]
    }
]

@mock_s3
class RenderHtmlReadWrites(unittest.TestCase):

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

        self.s3resource.create_bucket(Bucket=rdl.sourcebucket)
        self.s3resource.create_bucket(Bucket=rdl.listbucket)
        self.s3resource.create_bucket(Bucket=rdl.searchbucket)
        self.s3resource.create_bucket(Bucket=rdl.targetbucket)

        self.s3client = boto3.client('s3', region_name=REGION)
        self.s3client.put_object(Bucket=rdl.listbucket, Key=JSON_FILE, Body=JSON_TEXT)
        self.s3client.put_object(Bucket=rdl.sourcebucket, Key=SETTINGS_FILE, Body=self.settings_content)


    def tearDown(self):
        self.log = {}
        self.source_content = ''
        self.read_content = ''
        self.settings_content = {}
        self.postlist_default = {}
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

        # process_json_files

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


        # write_source_json
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

        # update_list_json_info
        #  - any json can be used

        print('\nTest 4 - update list json info\n')
        self.log = {}
        info = JSON_TEXT
        filename = JSON_FILE
        self.log = rdl.update_list_json_info(info,filename,self.log)
        print(self.log)
        log_message = 'JSON File: {} processed and updated'.format(JSON_FILE)
        self.assertEqual(self.log[JSON_FILE],log_message)

        # get_site_settings

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


        print('\nTest 6 - get settings - no settings file in bucket\n')
        # delete settings file from bucket
        self.s3client.delete_object(
            Bucket=rdl.sourcebucket,
            Key='settings.txt')
        self.log = {}
        self.read_content,self.log = rdl.get_site_settings(self.log)

        print('Log: {}'.format(self.log))
        print('Settings content {}:'.format(self.read_content))
        log_message = 'File: settings.txt not processed - does not exist'
        self.assertEqual(libs.constants.PCOM_NO_ENTRY, self.read_content)
        self.assertEqual(self.log['settings.txt'],log_message)

        # update_dependencies

        print('\nTest 7 - update dependencies - check content\n')
        # create htmlOut class component
        postlist = {}
        file = 'test1.post'
        self.log = {}
        htmlOut = libs.classes.HtmlOut('', self.log, settings, LIST_META_DEFAULT, file, DEPENDENCIES_DEFAULT, postlist)
        htmlOut = rdl.update_dependencies(htmlOut)
        print(htmlOut.log)

        # check data
        # read file for confirmation - reset log
        processed,self.read_content,self.log = rdl.get_content_from_s3(rdl.dep_file, rdl.listbucket,self.log)
        # python library defined in json format
        self.assertEqual(DEPENDENCIES_DEFAULT, json.loads(self.read_content))

        # write to search - use htmlOut
        print('\nTest 8 - write to search - check content\n')

        self.log = {}
        htmlOut.raw_content = STANDARD_TEXT
        htmlOut.log = {'search_content': []}
        log_message = 'File test1.post raw content output as test1.post.content'
        htmlOut = rdl.write_to_search(htmlOut)
        print(htmlOut.log)

        # read file for confirmation - reset log
        processed,self.read_content,self.log = rdl.get_content_from_s3('test1.post.content', rdl.searchbucket,self.log)
        # raw text
        self.assertEqual(STANDARD_TEXT, self.read_content)
        self.assertEqual(htmlOut.log['search_content'],[log_message])


        print('\nTest 9 - write to search - no data\n')

        self.log = {}
        htmlOut.raw_content = ''
        htmlOut.filename = 'test2.post'
        htmlOut.log = {'search_content': []}
        htmlOut = rdl.write_to_search(htmlOut)
        print('Log message: {}'.format(htmlOut.log))

        # read file for confirmation - reset log
        processed,self.read_content,self.log = rdl.get_content_from_s3('test2.post.content', rdl.searchbucket,self.log)
        # raw text
        self.assertFalse(processed)
        self.assertEqual(htmlOut.log['search_content'],[])

        # update_list_meta_files - use htmlOut

        print('\nTest 10 - update list meta - check content\n')
        htmlOut.log = {}
        htmlOut = rdl.update_list_meta_files(htmlOut,LIST_META_DEFAULT)
        print(htmlOut.log)

        # check data
        # read category and author file for confirmation - reset log
        processed,self.read_content,self.log = rdl.get_content_from_s3(rdl.cat_file, rdl.listbucket,self.log)
        self.assertEqual(CATEGORIES_DEFAULT, json.loads(self.read_content))
        processed,self.read_content,self.log = rdl.get_content_from_s3(rdl.authors_file, rdl.listbucket,self.log)
        self.assertEqual(AUTHORS_DEFAULT, json.loads(self.read_content))

        # write to buckets - use htmlOut

        print('\nTest 11 - write_to_buckets - standard text\n')

        self.log = {}
        htmlOut.filename = 'test3.page'
        htmlOut.html = STANDARD_TEXT
        htmlOut.log = {}
        htmlOut.meta['url'] = '/test3/'

        htmlOut = rdl.write_to_buckets(htmlOut)
        print(htmlOut.log)

        log_message = 'File: test3.page processed and output as test3/index.html'
        self.assertEqual(htmlOut.log['test3.page'],log_message)
        # content in target bucket
        processed,self.read_content,self.log = rdl.get_content_from_s3('test3/index.html', rdl.targetbucket,self.log)
        self.assertEqual(STANDARD_TEXT, self.read_content)

        print('\n\ntest3/index.html : {}'.format(self.read_content))

        # update postlist - use htmlOut

        print('\nTest 12 - update postlist\n')

        self.log = {}
        htmlOut.log = {}
        htmlOut.postlist = self.postlist_default

        htmlOut = rdl.update_postlist(htmlOut)
        print(htmlOut.log)

        processed,self.read_content,self.log = rdl.get_content_from_s3(POSTLIST_FILE, rdl.listbucket,self.log)
        self.assertEqual(self.postlist_default, json.loads(self.read_content))

        # update archive - use htmlOut

        print('\nTest 13 - update archive\n')

        self.log = {}
        self.settings_content = libs.globals.DEFAULT_SETTINGS
        self.log = rdl.update_archive_info(self.archive_default,self.postlist_default,self.settings_content,ARCHIVE_FILE,self.log)
        print(self.log)

        processed,self.read_content,self.log = rdl.get_content_from_s3(ARCHIVE_FILE, rdl.listbucket,self.log)
        self.assertEqual(self.archive_default, json.loads(self.read_content))
        log_messsage = 'JSON File: archive.json processed and updated'
        self.assertEqual(self.log['archive.json'], log_messsage)



if __name__ == '__main__':
    unittest.main()
