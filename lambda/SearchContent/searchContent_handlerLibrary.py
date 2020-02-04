# Handler Library
#
# s3 boto based python functions called by handler programs

# determines if file is schematic (page/post) or insert
# and returns a list of files to update

import libraries.morflessLibs as libs
import boto3
import json
import os

settings_file = libs.constants.PCOM_REQ_FILE_SETTINGS
post_list_file = libs.constants.PCOM_REQ_FILE_POSTLIST
cat_file = libs.constants.PCOM_REQ_FILE_CATEGORIES
authors_file = libs.constants.PCOM_REQ_FILE_AUTHORS

sourcebucket = os.environ["SOURCE_BUCKET"]
searchbucket = os.environ["SEARCH_BUCKET"]
listbucket = os.environ["LIST_BUCKET"]

s3resource = boto3.resource('s3')
s3client = boto3.client('s3')

def process_search_request(search_term,log):

    search_content = []
    filelist = []
    results = []

    search_response = ''

    if search_term:

        site_settings,log = get_site_settings(log)
        postlist,log = process_json_files(post_list_file,listbucket,log)
        list_meta,log = build_list_meta(site_settings,log)

        for object in s3client.list_objects(Bucket=searchbucket)['Contents']:
            if object['Key'].upper().find('.CONTENT') > -1:
                filelist.append(object['Key'])

        log['raw_content_files'] = filelist

        # scan raw content into dictionary
        for filename in filelist:

            content,log = read_content_file(filename,searchbucket,log)

            search_detail = {'name': filename, 'content': content, 'count': 0}
            search_content.append(search_detail)


        # search
        results = libs.second_processes.pcom_search_content(search_content,search_term)


        log['search_content_info'] = results

        search_response = libs.second_processes.pcom_create_search_response(results,postlist,site_settings,list_meta)

    return search_response,log

# --

# gets categories and authors lists and updates if settings includes more

def build_list_meta(site_settings,log):

    categories,log = process_json_files(cat_file,listbucket,log)
    authors,log = process_json_files(authors_file,listbucket,log)

    # update categories and authors from settings
    categories = libs.lists.pcom_update_categories_from_settings(categories,site_settings['category_info'],site_settings['posts_per_page'])
    authors = libs.lists.pcom_update_authors_from_settings(authors,site_settings['author_info'],site_settings['posts_per_page'])

    list_meta = {'categories': categories, 'authors': authors }

    return  list_meta,log

# gets json files using MorfLess library functions

def process_json_files(filename,bucket,log):

    processed,content,log = get_content_from_s3(filename,bucket,log)

    if processed:
        content,error = libs.string_processes.pcom_process_json(content)
    else:
        content = {}

    return content,log


def read_content_file(filename,bucket,log):

    processed,content,log = get_content_from_s3(filename,bucket,log)
    if not processed:
        content = ''

    return content,log


# gets settings file
# this is a schematic hence the unique MorfLess library function call

def get_site_settings(log):

    # settings.txt is in source bucket by default
    processed,content,log = get_content_from_s3(settings_file,sourcebucket,log)

    if processed:
        content = libs.read_schematic.get_settings(content)

    return content,log

# ==============
#
#
# ==============
#
#
# ==============

# bucket interaction

def get_content_from_s3(file,bucket,log):

    content = libs.constants.PCOM_NO_ENTRY
    processed = False

    if file and bucket:
        try:
            f = s3resource.Object(bucket,file)
            content = f.get()['Body'].read().decode('utf-8')
            processed = True
        except:
            log_detail = 'File: {} not processed - does not exist'.format(file)
            log[file] = log_detail

    return processed,content,log
