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
POSTLISTS_INFO_FILE = 'postlists_info.json'
PAGINATION_FILE = 'pagination.json'
CATEGORIES_FILE = 'categories.json'
AUTHORS_FILE = 'authors.json'
ARCHIVE_FILE = 'archive.json'
DEFAULT_SOURCE_ROOT = "tests/mockAws/default_source/renderHtml_writes/"

REGION = "us-east-1"

DEPENDENCIES_DEFAULT = [\
    {
        "filename": "index.page",
        "dependencies": [
            "settings.txt"
        ]
    },
    {
        "filename": "this.post",
        "dependencies": [
            "another_file.txt"
        ]
    },
    {
        "filename": "that.post",
        "dependencies": [
            "another_file.txt"
        ]
    }
]

@mock_s3
class RenderHtmlProcess(unittest.TestCase):

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

        self.s3resource.create_bucket(Bucket=rdl.sourcebucket)
        self.s3resource.create_bucket(Bucket=rdl.listbucket)
        self.s3resource.create_bucket(Bucket=rdl.searchbucket)
        self.s3resource.create_bucket(Bucket=rdl.targetbucket)

        self.s3client = boto3.client('s3', region_name=REGION)
        self.s3client.put_object(Bucket=rdl.sourcebucket, Key=SETTINGS_FILE, Body=self.settings_content)
        self.s3client.put_object(Bucket=rdl.listbucket, Key=CATEGORIES_FILE, Body=categories)
        self.s3client.put_object(Bucket=rdl.listbucket, Key=AUTHORS_FILE, Body=authors)

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
    def test_renderHtml_process(self):

        # ==============
        # build list meta
        # ==============


        print('\nTest 1- build list meta\n')
        self.log = {}
        settings = libs.globals.DEFAULT_SETTINGS
        list_meta,self.log = rdl.build_list_meta(settings,self.log)
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

        # ===========
        # determine upload type
        # ===========

        print('\nTest 2 - determine upload type - page example\n')
        self.log = {}
        upload_list,self.log = rdl.determine_upload_type('index.page',DEPENDENCIES_DEFAULT,self.log)
        print('Log: {}'.format(self.log))
        print('Filelist: {}'.format(upload_list))
        self.assertEqual(["index.page"],upload_list)
        self.assertEqual({},self.log)

        print('\nTest 3 - determine upload type - post example\n')
        self.log = {}
        upload_list,self.log = rdl.determine_upload_type('test1.post',DEPENDENCIES_DEFAULT,self.log)
        print('Log: {}'.format(self.log))
        print('Filelist: {}'.format(upload_list))
        self.assertEqual(["test1.post"],upload_list)
        self.assertEqual({},self.log)

        print('\nTest 4 - determine upload type - non post or page\n')
        self.log = {}
        upload_list,self.log = rdl.determine_upload_type('test1.txt',DEPENDENCIES_DEFAULT,self.log)
        print('Log: {}'.format(self.log))
        print('Filelist: {}'.format(upload_list))
        self.assertEqual([],upload_list)
        self.assertEqual({'filelist':'Dependencies for test1.txt found: []'},self.log)

        print('\nTest 5 - determine upload type - non post or page in dependencies\n')
        self.log = {}
        upload_list,self.log = rdl.determine_upload_type('another_file.txt',DEPENDENCIES_DEFAULT,self.log)
        print('Log: {}'.format(self.log))
        print('Filelist: {}'.format(upload_list))
        self.assertEqual(['this.post','that.post'],upload_list)
        self.assertEqual({'filelist': "Dependencies for another_file.txt found: ['this.post', 'that.post']"},self.log)

        # ===========
        # process schematic
        # ===========

if __name__ == '__main__':
    unittest.main()
