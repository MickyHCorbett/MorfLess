import unittest
import libraries.morflessLibs as libs
import boto3
import os
import json

"""
set environment to allow
renderHtml handler library module to be called
"""

from moto import mock_s3

os.environ['SOURCE_BUCKET'] = "sourcebucket"
os.environ['TARGET_BUCKET'] = "targetbucket"
os.environ["LIST_BUCKET"] = "listbucket"
os.environ["SEARCH_BUCKET"] = "searchbucket"

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

TEST1_POST_CONTENT = 'test1.post.content'
TEST2_POST_CONTENT = 'test2.post.content'
ABOUT_PAGE_CONTENT = 'about.page.content'

REGION = "us-east-1"

@mock_s3
class SearchContentProcess(unittest.TestCase):

    # set up bucket
    def setUp(self):
        self.log = {}
        self.read_content = ''
        self.maxDiff = None
        self.search_result = ''

        class_dir = os.getcwd()
        file_source = os.path.join(class_dir,DEFAULT_SOURCE_ROOT,SETTINGS_FILE)
        self.settings_content = get_file_content(file_source)
        file_source = os.path.join(class_dir,DEFAULT_SOURCE_ROOT,POSTLIST_FILE)
        postlist = get_file_content(file_source)

        file_source = os.path.join(class_dir,DEFAULT_SOURCE_ROOT,CATEGORIES_FILE)
        categories = get_file_content(file_source)
        file_source = os.path.join(class_dir,DEFAULT_SOURCE_ROOT,AUTHORS_FILE)
        authors = get_file_content(file_source)

        file_source = os.path.join(class_dir,DEFAULT_SOURCE_ROOT,TEST1_POST_CONTENT)
        test1_post_content = get_file_content(file_source)
        file_source = os.path.join(class_dir,DEFAULT_SOURCE_ROOT,TEST2_POST_CONTENT)
        test2_post_content = get_file_content(file_source)
        file_source = os.path.join(class_dir,DEFAULT_SOURCE_ROOT,ABOUT_PAGE_CONTENT)
        about_page_content = get_file_content(file_source)

        # create bucket and write json content to it
        self.s3resource = boto3.resource('s3', region_name=REGION)

        self.s3resource.create_bucket(Bucket=sct.sourcebucket)
        self.s3resource.create_bucket(Bucket=sct.listbucket)
        self.s3resource.create_bucket(Bucket=sct.searchbucket)

        self.s3client = boto3.client('s3', region_name=REGION)
        self.s3client.put_object(Bucket=sct.sourcebucket, Key=SETTINGS_FILE, Body=self.settings_content)
        self.s3client.put_object(Bucket=sct.listbucket, Key=CATEGORIES_FILE, Body=categories)
        self.s3client.put_object(Bucket=sct.listbucket, Key=AUTHORS_FILE, Body=authors)
        self.s3client.put_object(Bucket=sct.listbucket, Key=POSTLIST_FILE, Body=postlist)

        self.s3client.put_object(Bucket=sct.searchbucket, Key=TEST1_POST_CONTENT, Body=test1_post_content)
        self.s3client.put_object(Bucket=sct.searchbucket, Key=TEST2_POST_CONTENT, Body=test2_post_content)
        self.s3client.put_object(Bucket=sct.searchbucket, Key=ABOUT_PAGE_CONTENT, Body=about_page_content)

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
    def test_searchContent_process(self):

        # ==============
        # process search request
        # ==============

        print('\nTest 1 - process search term - something\n')
        self.search_result,self.log
        self.search_result,self.log = sct.process_search_request('something',self.log)
        print(self.log)
        # check log
        self.assertEqual(self.log['raw_content_files'], ['about.page.content', 'test1.post.content', 'test2.post.content'])
        self.assertEqual(self.log['search_content_info'], [{'name': 'test1.post', 'count': 8}, {'name': 'test2.post', 'count': 4}])

        result1 = \
        {'entries': ['"            <div class=\\"pm-post-content clearfix-small\\">\\n              <div class=\\"pm-post-image\\">\\n              <a href=\\"/test1-the-first-post/\\">\\n                <img src=\\"/images/Polimorf-shapes-background.jpg\\" alt=\\"A new post\\"  />\\n              </a></div><!-- end of .pm-post-image -->\\n              <div class=\\"pm-blog-entry\\">\\n                <h2><a href=\\"/test1-the-first-post/\\">A new post</a></h2>\\n              <div class=\\"pm-author-category-meta\\">\\n                <span class=\\"pm-meta-icon\\"><i class=\\"fa fa-list\\" aria-hidden=\\"true\\"></i></span>\\n                <a href=\\"/categories/something/\\" alt=\\"something\\">something</a>,&nbsp;\\n                <a href=\\"/categories/another-category/\\" alt=\\"another-category\\">another category</a>,&nbsp;\\n                <a href=\\"/categories/things-to-write-about/\\" alt=\\"things-to-write-about\\">things to write about</a>\\n              </div><!-- end of .pm-author-category-meta -->\\n              <div class=\\"pm-author-category-meta\\">\\n                <span class=\\"pm-meta-icon\\"><i class=\\"fa fa-user\\" aria-hidden=\\"true\\"></i></span>\\n                <a href=\\"/authors/anon/\\" alt=\\"anon\\">anon</a>\\n              </div><!-- end of .pm-author-category-meta -->\\n                <p>Something longer here to describe what is going on.<br/>Like we can see there are more lines to add.<br/>Then more again!</p>\\n              </div><!-- end of .pm-blog_entry -->\\n            </div><!-- end of .pm-post-content -->"', '"            <div class=\\"pm-post-content clearfix-small\\">\\n              <div class=\\"pm-post-image\\">\\n              <a href=\\"/test2/\\">\\n                <img src=\\"/images/Polimorf-shapes-background.jpg\\" alt=\\"A new post - second coming - redux\\"  />\\n              </a></div><!-- end of .pm-post-image -->\\n              <div class=\\"pm-blog-entry\\">\\n                <h2><a href=\\"/test2/\\">A new post - second coming - redux</a></h2>\\n              <div class=\\"pm-author-category-meta\\">\\n                <span class=\\"pm-meta-icon\\"><i class=\\"fa fa-list\\" aria-hidden=\\"true\\"></i></span>\\n                <a href=\\"/categories/something/\\" alt=\\"something\\">something</a>,&nbsp;\\n                <a href=\\"/categories/interesting/\\" alt=\\"interesting\\">interesting</a>\\n              </div><!-- end of .pm-author-category-meta -->\\n              <div class=\\"pm-author-category-meta\\">\\n                <span class=\\"pm-meta-icon\\"><i class=\\"fa fa-user\\" aria-hidden=\\"true\\"></i></span>\\n                <a href=\\"/authors/micky-h-corbett/\\" alt=\\"micky-h-corbett\\">Micky H Corbett</a>,&nbsp;\\n                <a href=\\"/authors/albert/\\" alt=\\"albert\\">Albert</a>\\n              </div><!-- end of .pm-author-category-meta -->\\n                <p>Something longer here to describe what is going on</p>\\n              </div><!-- end of .pm-blog_entry -->\\n            </div><!-- end of .pm-post-content -->"'], 'sticky': []}

        self.assertEqual(result1,self.search_result)

        print('\nTest 2 - process search term  - simplified syntax\n')
        self.search_result,self.log
        self.search_result,self.log = sct.process_search_request('simplified syntax',self.log)
        print(self.log)
        # check log
        self.assertEqual(self.log['raw_content_files'], ['about.page.content', 'test1.post.content', 'test2.post.content'])
        self.assertEqual(self.log['search_content_info'], [{'name': 'about.page', 'count': 1}])

        result2 = \
        {'entries': ['"            <div class=\\"pm-post-content clearfix-small\\">\\n              <div class=\\"pm-post-image\\">\\n              <a href=\\"/about/\\">\\n                <img src=\\"/images/Polimorf-shapes-background.jpg\\" alt=\\"About Morfless\\"  />\\n              </a></div><!-- end of .pm-post-image -->\\n              <div class=\\"pm-blog-entry\\">\\n                <h2><a href=\\"/about/\\">About Morfless</a></h2>\\n              <div class=\\"pm-author-category-meta\\">\\n                <span class=\\"pm-meta-icon\\"><i class=\\"fa fa-user\\" aria-hidden=\\"true\\"></i></span>\\n                <a href=\\"/authors/jim-o-neill/\\" alt=\\"jim-o-neill\\">Jim O&#39;Neill</a>\\n              </div><!-- end of .pm-author-category-meta -->\\n                <p>An about page - describe yourself in as much detail as you like!<br/>You can also add more to this extract.</p>\\n              </div><!-- end of .pm-blog_entry -->\\n            </div><!-- end of .pm-post-content -->"'], 'sticky': []}

        self.assertEqual(result2,self.search_result)

if __name__ == '__main__':
    unittest.main()
