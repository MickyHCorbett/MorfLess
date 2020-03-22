import unittest
import libraries.morflessLibs as libs
import boto3
import os
import json
import time

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
POSTLISTS_INFO_FILE = 'postlists_info.json'
PAGINATION_FILE = 'pagination.json'
CATEGORIES_FILE = 'categories.json'
AUTHORS_FILE = 'authors.json'
ARCHIVE_FILE = 'archive.json'
DEFAULT_SOURCE_ROOT = "tests/mockAws/default_source/renderHtml_writes/"

POSTS_TEMPLATE = libs.constants.PCOM_REQ_FILE_TEMPLATES['posts']
CATEGORIES_TEMPLATE = libs.constants.PCOM_REQ_FILE_TEMPLATES['categories']

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
        file_source = os.path.join(class_dir,DEFAULT_SOURCE_ROOT,PAGINATION_FILE)
        self.pagination = json.loads(get_file_content(file_source))
        file_source = os.path.join(class_dir,DEFAULT_SOURCE_ROOT,POSTLISTS_INFO_FILE)
        self.postlists_info = json.loads(get_file_content(file_source))

        file_source = os.path.join(class_dir,DEFAULT_SOURCE_ROOT,CATEGORIES_FILE)
        categories = json.loads(get_file_content(file_source))
        file_source = os.path.join(class_dir,DEFAULT_SOURCE_ROOT,AUTHORS_FILE)
        authors = json.loads(get_file_content(file_source))
        self.list_meta = {'categories': categories, 'authors': authors}

        # create bucket and write json content to it
        self.s3resource = boto3.resource('s3', region_name=REGION)

        self.s3resource.create_bucket(Bucket=clp.sourcebucket)
        self.s3resource.create_bucket(Bucket=clp.listbucket)
        self.s3resource.create_bucket(Bucket=clp.targetbucket)

        self.s3client = boto3.client('s3', region_name=REGION)
        self.s3client.put_object(Bucket=clp.listbucket, Key=JSON_FILE, Body=JSON_TEXT)
        self.s3client.put_object(Bucket=clp.listbucket, Key=HTML_FILE, Body=HTML_TEXT)
        self.s3client.put_object(Bucket=clp.sourcebucket, Key=SETTINGS_FILE, Body=self.settings_content)

        # add templates
        file_source = os.path.join(class_dir,DEFAULT_SOURCE_ROOT,POSTS_TEMPLATE)
        self.posts_template_content = get_file_content(file_source)
        file_source = os.path.join(class_dir,DEFAULT_SOURCE_ROOT,CATEGORIES_TEMPLATE)
        self.categories_template_content = get_file_content(file_source)

        self.local_settings = libs.globals.DEFAULT_SETTINGS


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

        # ==============
        # process search config - write search configuration js to file
        # ==============

        print('\nTest 1 - process search config\n')
        config_key = "js/js-lists/" + libs.constants.PCOM_SEARCH_CONFIG_JS_NAME
        self.log = {'outputs': []}
        self.local_settings = libs.globals.DEFAULT_SETTINGS
        sub_title_text = 'This is a subtitle'
        self.local_settings['template_main_header_text'][libs.constants.PCOM_SETTINGS_TYPE_SEARCH] = sub_title_text
        self.log = clp.process_search_config(self.local_settings,self.log)

        print('Log: {}'.format(self.log))
        log_message = 'File: '+ libs.constants.PCOM_SEARCH_CONFIG_JS_NAME + ' processed and output as ' + config_key
        self.assertEqual(self.log['outputs'],[log_message])

        # check content
        self.log = {}
        processed,self.read_content,self.log = clp.get_content_from_s3(config_key, clp.targetbucket,self.log)
        print('Search config content: {}'.format(self.read_content))
        self.assertTrue(processed)
        self.assertIn(sub_title_text,self.read_content)

        # ==============
        # process pagination -
        # ==============

        print('\nTest 2 - process pagination\n')

        self.log = {'pagination_processed': [], 'outputs': []}
        self.log = clp.process_pagination(self.pagination,self.postlist_default,self.log)

        print('Log: {}'.format(self.log))

        # check the pagination files
        for entry in self.pagination:
            config_key = "js/js-lists/" + entry['name']
            self.log = {}
            processed,self.read_content,self.log = clp.get_content_from_s3(config_key, clp.targetbucket,self.log)
            self.assertTrue(processed)
            print('File {} found: {}'.format(entry['name'],processed))

        print('\nTest 3 - process pagination - no pagination file\n')

        self.log = {'pagination_processed': [], 'outputs': []}
        self.log = clp.process_pagination([],self.postlist_default,self.log)

        print('Log: {}'.format(self.log))
        self.assertEqual(self.log,{'pagination_processed': [], 'outputs': []})

        # ==============
        # process postlists info
        # ==============

        print('\nTest 4 - process postlists\n')

        self.log = {'pagination_processed': [], 'outputs': [], 'postlists_processed': []}
        self.log = clp.process_postlists_info(self.postlists_info,self.postlist_default,self.local_settings,self.list_meta,self.log)

        print('Log: {}'.format(self.log))

        # check the pagination files
        for entry in self.postlists_info:
            config_key = "js/js-lists/" + entry['name']
            self.log = {}
            processed,self.read_content,self.log = clp.get_content_from_s3(config_key, clp.targetbucket,self.log)
            self.assertTrue(processed)
            print('File {} found: {}'.format(entry['name'],processed))

        print('\nTest 5 - process postlists - no postlists info\n')

        self.log = {'pagination_processed': [], 'outputs': []}
        self.log = clp.process_postlists_info([],self.postlist_default,self.local_settings,self.list_meta,self.log)

        print('Log: {}'.format(self.log))
        self.assertEqual(self.log,{'pagination_processed': [], 'outputs': []})

        # ==============
        # process posts page
        # ==============

        print('\nTest 6 - process posts page - template = posts - no template file\n')
        # delete settings file from bucket
        self.log = {'pagination_processed': [], 'outputs': [], 'postlists_processed': [], 'template_names': []}
        self.local_settings = libs.globals.DEFAULT_SETTINGS
        self.log = clp.process_posts_page(self.postlist_default,self.archive_default,self.local_settings,self.list_meta,self.log)

        # check posts/index.html has been created
        config_key = "posts/index.html"
        self.log = {}
        self.read_content = ''
        processed,self.read_content,self.log = clp.get_content_from_s3(config_key, clp.targetbucket,self.log)
        print(self.read_content)
        self.assertFalse(processed)
        print("{} found: {}".format(config_key,processed))

        # check posts constant has been created
        config_key = "js/js-lists/postlist--posts.js"
        self.log = {}
        processed,self.read_content,self.log = clp.get_content_from_s3(config_key, clp.targetbucket,self.log)
        self.assertFalse(processed)
        print("{} found: {}".format(config_key,processed))

        # add posts template
        self.s3client.put_object(Bucket=clp.listbucket, Key=POSTS_TEMPLATE, Body=self.posts_template_content)

        print('\nTest 7 - process posts page - template = entries\n')

        self.log = {'pagination_processed': [], 'outputs': [], 'postlists_processed': [], 'template_names': []}
        self.local_settings = libs.globals.DEFAULT_SETTINGS
        self.local_settings['template_types']['posts'] = "entries"
        self.log = clp.process_posts_page(self.postlist_default,self.archive_default,self.local_settings,self.list_meta,self.log)

        # check posts/index.html has been created
        config_key = "entries/index.html"
        self.log = {}
        self.read_content = ''
        processed,self.read_content,self.log = clp.get_content_from_s3(config_key, clp.targetbucket,self.log)
        self.assertTrue(processed)
        print("{} found: {}".format(config_key,processed))

        # check posts constant has been created
        config_key = "js/js-lists/postlist--posts.js"
        self.log = {}
        self.read_content = ''
        processed,self.read_content,self.log = clp.get_content_from_s3(config_key, clp.targetbucket,self.log)
        self.assertTrue(processed)
        print("{} found: {}".format(config_key,processed))

        print('\nTest 8 - process posts page - template = posts\n')

        self.log = {'pagination_processed': [], 'outputs': [], 'postlists_processed': [], 'template_names': []}
        self.local_settings = libs.globals.DEFAULT_SETTINGS
        self.local_settings['template_types']['posts'] = "posts"
        self.log = clp.process_posts_page(self.postlist_default,self.archive_default,self.local_settings,self.list_meta,self.log)

        # check posts/index.html has been created
        config_key = "posts/index.html"
        self.log = {}
        self.read_content = ''
        processed,self.read_content,self.log = clp.get_content_from_s3(config_key, clp.targetbucket,self.log)
        self.assertTrue(processed)
        print("{} found: {}".format(config_key,processed))

        # check posts constant has been created
        config_key = "js/js-lists/postlist--posts.js"
        self.log = {}
        self.read_content = ''
        processed,self.read_content,self.log = clp.get_content_from_s3(config_key, clp.targetbucket,self.log)
        self.assertTrue(processed)
        print("{} found: {}".format(config_key,processed))

        # ==============
        # process info base pages
        # ==============
        print('\nTest 9 - process info base page - categories\n')

        # add categories template
        self.s3client.put_object(Bucket=clp.listbucket, Key=CATEGORIES_TEMPLATE, Body=self.categories_template_content)

        self.log = {'pagination_processed': [], 'outputs': [], 'postlists_processed': [], 'template_names': []}
        bt = 'categories' # base type
        st = libs.globals.DEFAULT_SETTINGS
        lm = self.list_meta
        postlist = self.postlist_default
        archive = self.archive_default
        info_list = self.list_meta['categories']['categories']
        test_names = []
        index_names = []
        for entry in info_list:
            name = 'postlist--categories-'+ entry['name'].replace(" ","-") + '.js'
            test_names.append(name)
            index = 'categories/' + entry['name'].replace(" ","-") + '/index.html'
            index_names.append(index)

        self.log = clp.process_info_base_pages(info_list,postlist,archive,bt,st,lm,self.log)
        print(self.log['outputs'])

        log_joined = ' '.join(self.log['outputs'])

        for entry in test_names:
            self.assertIn(entry,log_joined)

        for entry in index_names:
            self.assertIn(entry,log_joined)


        print('\nTest 9 - process info base page - empty list\n')

        self.log = {'pagination_processed': [], 'outputs': [], 'postlists_processed': [], 'template_names': []}
        info_list = []
        self.log = clp.process_info_base_pages(info_list,postlist,archive,bt,st,lm,self.log)
        print(self.log['outputs'])
        outputs = ['File: categories processed and output as categories/index.html',
        'File: postlist--categories.js processed and output as js/js-lists/postlist--categories.js']
        self.assertEqual(self.log['outputs'],outputs)

        

if __name__ == '__main__':
    unittest.main()
