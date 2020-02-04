# layers file
import libraries.morflessLibs as libs
import boto3
import json
import logging, os

import createListPages_handlerLibrary as hl

cat_file = libs.constants.PCOM_REQ_FILE_CATEGORIES
authors_file = libs.constants.PCOM_REQ_FILE_AUTHORS
archive_file = libs.constants.PCOM_REQ_FILE_ARCHIVE
post_list_file = libs.constants.PCOM_REQ_FILE_POSTLIST
postlists_info_file = libs.constants.PCOM_REQ_FILE_POSTLISTS_INFO
pagination_file = libs.constants.PCOM_REQ_FILE_PAGINATION

targetbucket= os.environ['TARGET_BUCKET']
listbucket = os.environ["LIST_BUCKET"]


def handler(event, context):

    # set logs
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    outputLog = {"postlists_processed": [],
    "pagination_processed": [],
    "template_names": [],
    "outputs": []
    }

    if event['body']['files_processed'] == "Y":

        site_settings,outputLog = hl.get_site_settings(outputLog)
        categories,outputLog = hl.process_json_files(cat_file,listbucket,outputLog)
        authors,outputLog = hl.process_json_files(authors_file,listbucket,outputLog)
        archive,outputLog = hl.process_json_files(archive_file,listbucket,outputLog)
        postlist,outputLog = hl.process_json_files(post_list_file,listbucket,outputLog)
        postlists_info,outputLog = hl.process_json_files(postlists_info_file,listbucket,outputLog)
        pagination,outputLog = hl.process_json_files(pagination_file,listbucket,outputLog)

        list_meta = { 'authors': authors, 'categories': categories }

        cat_base = libs.constants.PCOM_SETTINGS_TYPE_CATEGORIES
        author_base = libs.constants.PCOM_SETTINGS_TYPE_AUTHORS
        archive_base = libs.constants.PCOM_SETTINGS_TYPE_ARCHIVE


        # create postlist constants
        outputLog = hl.process_postlists_info(postlists_info,postlist,site_settings,list_meta,outputLog)

        # create pagination constants
        outputLog = hl.process_pagination(pagination,postlist,outputLog)

        # create posts page
        outputLog = hl.process_posts_page(postlist,archive,site_settings,list_meta,outputLog)

        # create category pages and constants
        outputLog = hl.process_info_base_pages(categories[cat_base],postlist,archive,cat_base,site_settings,list_meta,outputLog)

        # create authors pages and constants
        outputLog = hl.process_info_base_pages(authors[author_base],postlist,archive,author_base,site_settings,list_meta,outputLog)

        # create archive pages and constants
        outputLog = hl.process_info_base_pages([],postlist,archive,archive_base,site_settings,list_meta,outputLog)

        # create search configuration
        outputLog = hl.process_search_config(site_settings,outputLog)

    # add data to log
    logger.info(outputLog)

    return {
        'statusCode': 200,
        'body': outputLog
    }
