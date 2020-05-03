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
cat_file = libs.constants.PCOM_REQ_FILE_CATEGORIES
authors_file = libs.constants.PCOM_REQ_FILE_AUTHORS
archive_file = libs.constants.PCOM_REQ_FILE_ARCHIVE
post_list_file = libs.constants.PCOM_REQ_FILE_POSTLIST
postlists_info_file = libs.constants.PCOM_REQ_FILE_POSTLISTS_INFO
pagination_file = libs.constants.PCOM_REQ_FILE_PAGINATION
dep_file = libs.constants.PCOM_REQ_FILE_DEPENDENCIES

sourcebucket= os.environ['SOURCE_BUCKET']
targetbucket= os.environ['TARGET_BUCKET']
listbucket = os.environ["LIST_BUCKET"]
searchbucket = os.environ["SEARCH_BUCKET"]

s3resource = boto3.resource('s3')
s3client = boto3.client('s3')

def determine_upload_type(fr,dependencies,outputLog):

    filelist = []

    if fr.upper().find('.POST') > -1  or fr.upper().find('.PAGE') > -1 :

        # single post or page to change
        filelist.append(fr)

    elif fr.upper().find('.POST') == -1  and fr.upper().find('.PAGE') == -1:

        # check dependencies and create file list of things to change.
        filelist = libs.lists.pcom_find_dependencies(dependencies,fr)
        # update output log
        log_detail = 'Dependencies for {} found: {}'.format(fr,filelist)
        outputLog['filelist'] = log_detail

    return filelist,outputLog


# gets categories and authors lists and updates if settings includes more

def build_list_meta(site_settings,log):

    categories,log = process_json_files(cat_file,listbucket,log)
    authors,log = process_json_files(authors_file,listbucket,log)

    # update categories and authors from settings
    categories = libs.lists.pcom_update_categories_from_settings(categories,site_settings['category_info'],site_settings)
    authors = libs.lists.pcom_update_authors_from_settings(authors,site_settings['author_info'],site_settings)

    list_meta = {'categories': categories, 'authors': authors }

    return  list_meta,log

# ---

# ---
# processes files uploaded to sourcebucket
# creates html files for target and updates
# postlist, dependencies and search content
#

def process_uploaded_files(filelist,dependencies,outputLog):

    site_settings,outputLog = get_site_settings(outputLog)

    postlist,outputLog = process_json_files(post_list_file,listbucket,outputLog)
    archive,outputLog = process_json_files(archive_file,listbucket,outputLog)
    postlists_info,outputLog = process_json_files(postlists_info_file,listbucket,outputLog)
    pagination_info,outputLog = process_json_files(pagination_file,listbucket,outputLog)

    list_meta,outputLog = build_list_meta(site_settings,outputLog)

    if filelist:

        outputLog['files_processed'] = 'Y'
        outputLog['default_header_additions'] = site_settings['default_header_additions']
        outputLog['default_footer_additions'] = site_settings['default_footer_additions']

        for file in filelist:

            process_file,content,outputLog = get_content_from_s3(file,sourcebucket,outputLog)

            if process_file:

                # create HtmlOut object
                htmlOut = libs.classes.HtmlOut(content, outputLog, site_settings, list_meta, file, dependencies, postlist)

                # process schematic
                htmlOut = process_schematic(htmlOut)

                # write to target and list buckets (for templates)
                htmlOut = write_to_buckets(htmlOut)

                 # write raw content
                htmlOut = write_to_search(htmlOut)

                # update lists
                list_meta['categories'] = htmlOut.list_meta['categories']
                list_meta['authors'] = htmlOut.list_meta['authors']
                dependencies = htmlOut.dependencies
                postlist = htmlOut.postlist

                postlists_info =  libs.lists.pcom_update_postlists_info(
                                postlist_info=postlists_info,
                                local_info=htmlOut.postlists_info,
                                js_name=htmlOut.postlist_constant_name,
                                fileroot=htmlOut.fileroot,
                                is_template=htmlOut.is_template,
                                is_search=htmlOut.is_search)

                pagination_info = libs.lists.pcom_update_pagination_info(
                                pagination_info=pagination_info,
                                local_info=htmlOut.pagination_info,
                                pagination_name=htmlOut.pagination_name,
                                fileroot=htmlOut.fileroot)

                # add addition info
                htmlOut.log['file_header_additions'].append({file: htmlOut.site_settings['header_additions'] })
                htmlOut.log['file_footer_additions'].append({file: htmlOut.site_settings['footer_additions'] })

        # update dependencies file after processing files
        htmlOut = update_dependencies(htmlOut)

        # update catgories and authors files after processing files
        htmlOut = update_list_meta_files(htmlOut,list_meta)

        # update postlist file after processing files
        htmlOut = update_postlist(htmlOut)


        # set log
        outputLog = htmlOut.log

        # update postlists_info file after processing files
        outputLog = update_list_json_info(postlists_info,postlists_info_file,outputLog)

        # update pagination_info file after processing files
        outputLog = update_list_json_info(pagination_info,pagination_file,outputLog)

        # update archive list
        outputLog = update_archive_info(archive,postlist,site_settings,archive_file,outputLog)

    return outputLog

# deletes target html file/dir, search content files
# and updates postlist

def delete_files(filelist,dependencies,outputLog):

    postlist,outputLog = process_json_files(post_list_file,listbucket,outputLog)

    # process files in list
    for file in filelist:

        # condition filename
        fileroot = file.lower().replace(".post","").replace(".page","")
        outkey = fileroot + "/index.html"
        template_key = fileroot + ".template"
        raw_key = file + ".content"

        file_deleted = False

        # check if template
        if fileroot in libs.globals.DEFAULT_TEMPLATE_TYPES:
            # delete from list
            template_deleted,outputLog = delete_content_from_s3(file,template_key,listbucket,outputLog)
        else:
            # delete from target
            file_deleted,outputLog = delete_content_from_s3(file,outkey,targetbucket,outputLog)

        # delete from search
        raw_deleted,outputLog = delete_content_from_s3(file,raw_key,searchbucket,outputLog)

        # update postlist
        if file_deleted:
            postlist = libs.lists.pcom_delete_from_postlist(postlist,file)

    # update postlist file
    postlist_content = libs.string_processes.pcom_write_json(postlist)
    outputLog = write_source_json(listbucket,post_list_file,postlist_content,outputLog)

    return outputLog



# processes uploaded schematic using MorfLess libraries
# and htmlOut class methods

def process_schematic(htmlOut):

    htmlOut.process_schematic_sections()
    htmlOut.get_insert_info()

    # get insert file content from s3
    htmlOut = get_insert_content(htmlOut)
    htmlOut.process_inserts()

    # process postlists, pagination and meta html elements
    htmlOut.process_second_stage()

    # create raw content for search
    htmlOut.get_raw_content()

    return htmlOut

# update archive list

def update_archive_info(archive,postlist,settings,archive_file,log):

    archive = libs.lists.pcom_update_archive(archive,postlist,settings)
    log = update_list_json_info(archive,archive_file,log)

    return log

# update the postlist json using the htmlOut properties
# and write to sourcebucket

def update_postlist(htmlOut):

    postlist_content = libs.string_processes.pcom_write_json(htmlOut.postlist)
    htmlOut.log = write_source_json(listbucket,post_list_file,postlist_content,htmlOut.log)

    return htmlOut


# update the info json (e.g. pagination)
# and write to list bucket

def update_list_json_info(info,filename,log):

    content = libs.string_processes.pcom_write_json(info)
    log = write_source_json(listbucket,filename,content,log)

    return log

# update the dependencies using the htmlOut properties
# and write to sourcebucket

def update_dependencies(htmlOut):

    dep_content = libs.string_processes.pcom_write_json(htmlOut.dependencies)
    htmlOut.log = write_source_json(listbucket,dep_file,dep_content,htmlOut.log)

    return htmlOut

# update categories and authors file using the list meta
# and write to listbucket

def update_list_meta_files(htmlOut,list_meta):

    content = libs.string_processes.pcom_write_json(list_meta['categories'])
    htmlOut.log = write_source_json(listbucket,cat_file,content,htmlOut.log)

    content = libs.string_processes.pcom_write_json(list_meta['authors'])
    htmlOut.log = write_source_json(listbucket,authors_file,content,htmlOut.log)

    return htmlOut


# retrieves the content of the insert files stated in the INSERT command
# and places them in the htmlOut insert_info property

def get_insert_content(htmlOut):


    for ind,insert in enumerate(htmlOut.insert_info):

        processed,content,htmlOut.log = get_content_from_s3(insert['filename'],sourcebucket,htmlOut.log)

        if processed:
            htmlOut.insert_info[ind]['content'] = content
            htmlOut.insert_info[ind]['valid_entry'] = libs.constants.PCOM_VALID_ENTRY
        else:
            htmlOut.insert_info[ind]['valid_entry'] = libs.constants.PCOM_NOT_VALID_ENTRY

    return htmlOut

# writes sources files as name (without post/page) / index.html
# except for index, 404 and certain key template pages

def write_to_buckets(htmlOut):

    outkey,bucket = libs.bucket_file_preparation.determine_bucket_and_key(htmlOut,targetbucket,listbucket)

    # put html file in target bucket
    write_content_to_s3(bucket,outkey,htmlOut.html,'html')

    # update output log
    log_detail = 'File: {} processed and output as {}'.format(htmlOut.filename,outkey)
    htmlOut.log[htmlOut.filename] = log_detail

    return htmlOut


# writes raw content files to search folder

def write_to_search(htmlOut):

    if htmlOut.raw_content:
        outkey = htmlOut.filename + ".content"

        write_content_to_s3(searchbucket,outkey,htmlOut.raw_content,'search')

        # update output log
        log_detail = 'File {} raw content output as {}'.format(htmlOut.filename,outkey)
        htmlOut.log['search_content'].append(log_detail)

    return htmlOut

# gets json files using MorfLess library functions
# reads json as Ordered Dictionary

def process_json_files(filename,bucket,log):

    processed,content,log = get_content_from_s3(filename,bucket,log)

    if processed:
        content,error = libs.string_processes.pcom_process_json(content)
    else:
        content = {}

    return content,log


# writes json files using Boto syntax

def write_source_json(bucket,filename,content,outlog):
    # writes to bucket

    # put html file in bucket
    write_content_to_s3(bucket,filename,content,'json')

    # update output log
    log_detail = 'JSON File: {} processed and updated'.format(filename)
    outlog[filename] = log_detail

    return outlog


# gets settings file
# this is a schematic hence the unique MorfLess library function call

def get_site_settings(log):

    # settings.txt is in source bucket by default
    processed,content,log = get_content_from_s3(settings_file,sourcebucket,log)

    if processed:
        content = libs.read_schematic.get_settings(content)

    return content,log
#
#
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


def write_content_to_s3(bucket,outkey,content,type):

    if outkey and bucket:

        if type == 'search':
            # put html file in search bucket
            s3client.put_object(
                Bucket=bucket,
                Key=outkey,
                Body=content,
                ContentType="text; charset=utf-8")

        if type == 'html':
            # can be list or target bucket
            s3client.put_object(
                Bucket=bucket,
                Key=outkey,
                Body=content,
                ContentDisposition='inline',
                ContentType="text/html; charset=utf-8")

        if type == 'json':
            # put html file in bucket
            s3client.put_object(
                Bucket=bucket,
                Key=outkey,
                Body=content,
                ContentType="json")


def delete_content_from_s3(file,outkey,bucket,log):

    file_deleted = False

    s3client.delete_object(
        Bucket=bucket,
        Key=outkey)

    file_deleted = True
    log['files_processed'] = 'Y'
    log_detail = 'File: {} deleted from bucket {}, File {} deleted from site'.format(file,bucket,outkey)

    # update output log
    log[file] = log_detail

    return file_deleted,log
