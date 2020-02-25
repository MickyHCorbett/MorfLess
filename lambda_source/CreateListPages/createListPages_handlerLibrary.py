import libraries.morflessLibs as libs
import boto3
import json
import logging, os

settings_file = libs.constants.PCOM_REQ_FILE_SETTINGS

sourcebucket= os.environ['SOURCE_BUCKET']
targetbucket= os.environ['TARGET_BUCKET']
listbucket = os.environ["LIST_BUCKET"]

s3resource = boto3.resource('s3')
s3client = boto3.client('s3')

# process and output postlist constants

def process_postlists_info(postlists_info,postlist,settings,list_meta,log):

    if postlists_info:

        for info in postlists_info:
            js_name = info['name']
            list_info = info['postlists']
            fileroot = info['fileroot']

            js_constant,processed = libs.second_processes.pcom_process_postlist(list_info,postlist,settings,list_meta,fileroot)
            if processed:
                log['postlists_processed'].append(js_name)

            log = write_js_to_buckets(js_name,js_constant,log)

    return log

# process and output postlist constants

def process_pagination(pagination,postlist,log):

    if pagination:

        for post_links in pagination:
            pg_name = post_links['name']
            info = post_links['pagination']
            fileroot = post_links['fileroot']

            pg_constant,processed = libs.second_processes.pcom_process_pagination(postlist,pg_name,fileroot,info)
            if processed:
                log['pagination_processed'].append(pg_name)

            log = write_js_to_buckets(pg_name,pg_constant,log)

    return log

# creates post list page

def process_posts_page(postlist,archive,settings,list_meta,log):

    posts_template = libs.constants.PCOM_REQ_FILE_TEMPLATES['posts']
    # get html template
    template_content,log = get_template_files(posts_template,log)

    posts_info,log = libs.second_processes.pcom_process_posts_page(postlist,archive,settings,list_meta,log,template_content)

    if posts_info['processed']:

        log = write_templates_to_buckets(posts_info['s3url'],posts_info['posts_name'],posts_info['template_content'],log)
        log = write_js_to_buckets(posts_info['posts_js_name'],posts_info['posts_js_constant'],log)

    return log


# creates the main category, authors or archive page

def process_info_base_pages(info_list,postlist,archive,base_type,settings,list_meta,log):

    base_template = libs.constants.PCOM_REQ_FILE_TEMPLATES[base_type]
    # get html template
    template_content,log = get_template_files(base_template,log)

    base_info,base_sub_info,log =\
    libs.second_processes.pcom_process_info_base_pages(info_list,base_type,template_content,postlist,archive,settings,list_meta,log)

    if base_info['processed']:

        log = write_templates_to_buckets(base_info['s3url'],base_info['base_name'],base_info['template_content'],log)
        log = write_js_to_buckets(base_info['js_name'],base_info['js_constant'],log)

        for info in base_sub_info:
            log = write_templates_to_buckets(info['s3url'],info['full_js_root'],info['template_content'],log)
            log = write_js_to_buckets(info['js_filename'],info['js_constant'],log)

    return log

def process_search_config(settings,log):

    search_config_content = libs.second_processes.pcom_process_search_config(settings)
    log = write_js_to_buckets(libs.constants.PCOM_SEARCH_CONFIG_JS_NAME,search_config_content,log)

    return log
# --------

# write js constants to js/js-lists folder on target

def write_js_to_buckets(js_name,js_constant,log):

    outkey = "js/js-lists/" + js_name

    # put file in target bucket
    write_content_to_s3(targetbucket,outkey,js_constant)

    # update output log
    log_detail = 'File: {} processed and output as {}'.format(js_name,outkey)
    log["outputs"].append(log_detail)

    return log

def write_templates_to_buckets(outkey,template_root,template_content,log):

    # put file in target bucket
    write_content_to_s3(targetbucket,outkey,template_content)

    # update output log
    log_detail = 'File: {} processed and output as {}'.format(template_root,outkey)
    log["outputs"].append(log_detail)

    return log

# gets json files using MorfLess library functions
# reads json as Ordered Dictionary

def process_json_files(filename,bucket,log):

    processed,content,log = get_content_from_s3(filename,bucket,log)

    if processed:
        content,error = libs.string_processes.pcom_process_json(content)
    else:
        content = {}

    return content,log

# get template file - html

def get_template_files(filename,log):

    processed,content,log = get_content_from_s3(filename,listbucket,log)

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


def write_content_to_s3(bucket,outkey,content):

    if outkey and bucket:

        s3client.put_object(
            Bucket=bucket,
            Key=outkey,
            Body=content,
            ContentDisposition='inline',
            ContentType="text/html; charset=utf-8")
