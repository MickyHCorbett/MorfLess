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

from lambda_source.RenderHtml.renderHtml_handlerLibrary import delete_content_from_s3 as rd_delete
from lambda_source.RenderHtml.renderHtml_handlerLibrary import get_content_from_s3 as rd_get
from lambda_source.RenderHtml.renderHtml_handlerLibrary import write_content_to_s3 as rd_write

from lambda_source.CreateListPages.createListPages_handlerLibrary import get_content_from_s3 as clp_get
from lambda_source.CreateListPages.createListPages_handlerLibrary import write_content_to_s3 as clp_write

from lambda_source.SearchContent.searchContent_handlerLibrary import get_content_from_s3 as sc_get

from fixtures.create_files_for_bucket import get_file_content
from fixtures.decorators import testCall


# constants for test

BUCKETNAME = "test_bucket"
FILENAME = "test_file.txt"
OTHERFILE = "test_file_other.txt"
REGION = "us-east-1"
FILE_SOURCE = "tests/mockAws/default_source/settings.txt"

JSON_FILE = 'test_json_file.json'
HTML_FILE = 'test_html_file.html'
STANDARD_FILE = 'test_standard_file.txt'

JSON_TEXT = """
{
    "variable1": "this",
    "variable2": "that"
}
"""

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
class RenderHtmlBucketOperations(unittest.TestCase):

    # set up bucket
    def setUp(self):
        class_dir = os.getcwd()
        file_source = os.path.join(class_dir,FILE_SOURCE)

        self.source_content = get_file_content(file_source)
        self.log = {}
        self.read_content = ''

        # create bucket and write content to it
        self.s3resource = boto3.resource('s3', region_name=REGION)
        self.s3resource.create_bucket(Bucket=BUCKETNAME)

        self.s3client = boto3.client('s3', region_name=REGION)
        self.s3client.put_object(Bucket=BUCKETNAME, Key=FILENAME, Body=self.source_content)


    def tearDown(self):
        self.log = {}
        self.source_content = ''
        self.read_content = ''
        # delete content from s3 and delete bucket
        bucket = self.s3resource.Bucket(BUCKETNAME)
        for key in bucket.objects.all():
            key.delete()
        bucket.delete()


    @testCall
    def test_renderHtml_get_write_delete_content_from_s3(self):

        # read content

        print('\nTest 1 - read content from file in bucket\n')
        processed,self.read_content,self.log = rd_get(FILENAME, BUCKETNAME,self.log)
        print('read content: {}'.format(self.read_content))

        # check asserts
        self.assertEqual(self.source_content, self.read_content)
        self.assertEqual(self.log,{})
        self.assertTrue(processed)

        print('\nTest 2 - read content from file not in bucket\n')
        processed,self.read_content,self.log = rd_get(OTHERFILE, BUCKETNAME,self.log)
        print('read content: {}'.format(self.read_content))

        # check asserts
        self.assertEqual(libs.constants.PCOM_NO_ENTRY, self.read_content)
        self.assertNotEqual(self.source_content,self.read_content)
        self.assertFalse(processed)
        log_message = 'File: {} not processed - does not exist'.format(OTHERFILE)
        self.assertEqual(self.log[OTHERFILE],log_message)

        # write

        print('\nTest 3 - write content as json\n')
        rd_write(BUCKETNAME,JSON_FILE,JSON_TEXT,'json')

        # get object properties
        obj = self.s3client.get_object(Bucket=BUCKETNAME, Key=JSON_FILE)
        print(obj)
        self.assertEqual(obj['ContentType'],'json')
        self.assertTrue(CONTENT_DISPOSITION not in obj)

        print('\nTest 4 - write content as html\n')
        rd_write(BUCKETNAME,HTML_FILE,HTML_TEXT,'html')

        # get object properties
        obj = self.s3client.get_object(Bucket=BUCKETNAME, Key=HTML_FILE)
        print(obj)
        self.assertEqual(obj['ContentType'],'text/html; charset=utf-8')
        self.assertTrue(CONTENT_DISPOSITION in obj)
        self.assertEqual(obj[CONTENT_DISPOSITION],'inline')

        print('\nTest 5 - write content as general(search)\n')
        rd_write(BUCKETNAME,STANDARD_FILE,STANDARD_TEXT,'search')

        # get object properties
        obj = self.s3client.get_object(Bucket=BUCKETNAME, Key=STANDARD_FILE)
        print(obj)
        self.assertEqual(obj['ContentType'],'text; charset=utf-8')
        self.assertTrue(CONTENT_DISPOSITION not in obj)


        # delete
        print('\nTest 6 - delete JSON FILE from bucket\n')
        self.log = {'files_processed': 'N'}

        file_deleted,self.log = rd_delete(JSON_FILE,JSON_FILE,BUCKETNAME,self.log)
        print(self.log)

        log_message = 'File: {0} deleted from bucket {1}, File {0} deleted from site'.format(JSON_FILE,BUCKETNAME)
        self.assertEqual(self.log[JSON_FILE],log_message)
        self.assertEqual(self.log['files_processed'],'Y')


        print('\nTest 7 - delete OTHERFILE from bucket - does not exist\n')

        self.log = {'files_processed': 'N'}
        file_deleted,self.log = rd_delete(OTHERFILE,OTHERFILE,BUCKETNAME,self.log)
        print(self.log)

        log_message = 'File: {0} deleted from bucket {1}, File {0} deleted from site'.format(OTHERFILE,BUCKETNAME)
        self.assertEqual(self.log[OTHERFILE],log_message)
        self.assertEqual(self.log['files_processed'],'Y')


@mock_s3
class CreateListPagesBucketOperations(unittest.TestCase):

    # set up bucket
    def setUp(self):
        class_dir = os.getcwd()
        file_source = os.path.join(class_dir,FILE_SOURCE)

        self.source_content = get_file_content(file_source)
        self.log = {}
        self.read_content = ''

        # create bucket and write content to it
        self.s3resource = boto3.resource('s3', region_name=REGION)
        self.s3resource.create_bucket(Bucket=BUCKETNAME)

        self.s3client = boto3.client('s3', region_name=REGION)
        self.s3client.put_object(Bucket=BUCKETNAME, Key=FILENAME, Body=self.source_content)


    def tearDown(self):
        self.log = {}
        self.source_content = ''
        self.read_content = ''
        # delete content from s3 and delete bucket
        bucket = self.s3resource.Bucket(BUCKETNAME)
        for key in bucket.objects.all():
            key.delete()
        bucket.delete()

    @testCall
    def test_createListPages_get_write_content_from_s3(self):

        # read content

        print('\nTest 1 - read content from file in bucket\n')
        processed,self.read_content,self.log = clp_get(FILENAME, BUCKETNAME,self.log)
        print('read content: {}'.format(self.read_content))

        # check asserts
        self.assertEqual(self.source_content, self.read_content)
        self.assertEqual(self.log,{})
        self.assertTrue(processed)

        print('\nTest 2 - read content from file not in bucket\n')
        processed,self.read_content,self.log = clp_get(OTHERFILE, BUCKETNAME,self.log)
        print('read content: {}'.format(self.read_content))

        # check asserts
        self.assertEqual(libs.constants.PCOM_NO_ENTRY, self.read_content)
        self.assertNotEqual(self.source_content,self.read_content)
        self.assertFalse(processed)
        log_message = 'File: {} not processed - does not exist'.format(OTHERFILE)
        self.assertEqual(self.log[OTHERFILE],log_message)

        print('\nTest 3 - write content\n')
        clp_write(BUCKETNAME,HTML_FILE,HTML_TEXT)

        # get object properties
        obj = self.s3client.get_object(Bucket=BUCKETNAME, Key=HTML_FILE)
        print(obj)
        self.assertEqual(obj['ContentType'],'text/html; charset=utf-8')
        self.assertTrue(CONTENT_DISPOSITION in obj)
        self.assertEqual(obj[CONTENT_DISPOSITION],'inline')

@mock_s3
class SearchContentBucketOperations(unittest.TestCase):

    # set up bucket
    def setUp(self):
        class_dir = os.getcwd()
        file_source = os.path.join(class_dir,FILE_SOURCE)

        self.source_content = get_file_content(file_source)
        self.log = {}
        self.read_content = ''

        # create bucket and write content to it
        self.s3resource = boto3.resource('s3', region_name=REGION)
        self.s3resource.create_bucket(Bucket=BUCKETNAME)

        self.s3client = boto3.client('s3', region_name=REGION)
        self.s3client.put_object(Bucket=BUCKETNAME, Key=FILENAME, Body=self.source_content)


    def tearDown(self):
        self.log = {}
        self.source_content = ''
        self.read_content = ''
        # delete content from s3 and delete bucket
        bucket = self.s3resource.Bucket(BUCKETNAME)
        for key in bucket.objects.all():
            key.delete()
        bucket.delete()


    @testCall
    def test_searchContent_get_content_from_s3(self):

        # read content

        print('\nTest 1 - read content from file in bucket\n')
        processed,self.read_content,self.log = sc_get(FILENAME, BUCKETNAME,self.log)
        print('read content: {}'.format(self.read_content))

        # check asserts
        self.assertEqual(self.source_content, self.read_content)
        self.assertEqual(self.log,{})
        self.assertTrue(processed)

        print('\nTest 2 - read content from file not in bucket\n')
        processed,self.read_content,self.log = sc_get(OTHERFILE, BUCKETNAME,self.log)
        print('read content: {}'.format(self.read_content))

        # check asserts
        self.assertEqual(libs.constants.PCOM_NO_ENTRY, self.read_content)
        self.assertNotEqual(self.source_content,self.read_content)
        self.assertFalse(processed)
        log_message = 'File: {} not processed - does not exist'.format(OTHERFILE)
        self.assertEqual(self.log[OTHERFILE],log_message)


if __name__ == '__main__':
    unittest.main()
