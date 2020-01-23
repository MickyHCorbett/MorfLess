#
from libraries import string_processes as sp
from libraries import constants as ct
from libraries import schematics as sch

# determines write bucket and key format

def determine_bucket_and_key(htmlOut,target,list_bucket):

    # default is target
    bucket = target
    outkey = ''

    # check for index (index.page) or 404 (404.page) or template
    if htmlOut.filename == "index.page":
        outkey = "index.html"
    elif htmlOut.filename == "404.page":
        outkey = "404.html"
    elif htmlOut.is_template and not htmlOut.is_search:
        outkey = sp.pcom_get_template_key(htmlOut.fileroot,htmlOut.site_settings) + ".template"
        bucket = list_bucket
    elif htmlOut.is_search:
        url = sp.pcom_create_template_fileroot(ct.PCOM_SETTINGS_TYPE_SEARCH,htmlOut.site_settings)
        outkey = url + "/index.html"
    else:
        if htmlOut.meta['url']:
            string_end = len(htmlOut.meta['url'])-1
            # strip any initial and end slashes
            start_char = htmlOut.meta['url'][0].replace('/','')
            bulk = htmlOut.meta['url'][1:string_end]
            end_char = htmlOut.meta['url'][string_end].replace('/','')

            url = start_char + bulk + end_char

            outkey = url + "/index.html"
        else:
            outkey = htmlOut.fileroot + "/index.html"

    return outkey,bucket
