# MorfLess v1.0
#
# list functions
#

from libraries import globals as gb
from libraries import constants as ct
from libraries import schematics as sch
from libraries import string_processes as sp
from libraries import meta_defaults as md

from collections import OrderedDict

import os, json, datetime, math

def pcom_order_postlist_posts(posts,up_down=True):
    # most recent post first
    return sorted(posts, key=lambda post: post['index'],reverse=up_down)

def pcom_find_post(postlist,postname):

    post_found = False
    for ind,post in enumerate(postlist['posts']):
        if post['postname'] == postname:
            post_found = True
            post = postlist['posts'][ind]
            break

    if not post_found:
        post = {'postname': ct.PCOM_NO_ENTRY}

    return post

def pcom_find_template_search_content(settings,file):

    fileroot = ''
    if file.lower().find('.page') > -1:
        fileroot = file.replace('.page','')

    print(fileroot)
    post = {'name': ct.PCOM_NO_ENTRY }
    if fileroot:
        if fileroot in settings['template_search_content']:
            post = settings['template_search_content'][fileroot]

    return post


def pcom_find_post_index(post):
    index = 0
    if index in post:
        index = post['index']

    return index

# sub type is an array of categories, authors etc.
def pcom_find_sub_list(posts,authors,sub_type,sub_name,type,get_all=False):

    posts_out = []
    for post in posts:
        if get_all:
            for sub in post[sub_type]:
                sub = sp.pcom_find_author_full_name(sub,authors)
                if sub == sub_name:
                    posts_out.append(post)
        else:
            if post['type'] == type:
                for sub in post[sub_type]:
                    sub = sp.pcom_find_author_full_name(sub,authors)
                    if sub == sub_name:
                        posts_out.append(post)

    return posts_out

# sub type is an array of categories, authors etc.
def pcom_find_sub_list_archive(archive,postlist,sub_name,type):

    posts_out = []
    for info in archive['created']:
        if info['name'] == sub_name:
            for item in info['posts']:
                post = pcom_find_post(postlist,item)
                posts_out.append(post)

    return posts_out

def pcom_create_posts_pages_array(posts,type):

    out = []
    for post in posts:
        if type:
            if post['type'] == 'post':
                out.append(post)
        else:
            if post['type'] == 'page':
                out.append(post)

    return out

def pcom_calculate_posts_per_page(no_posts,posts_per_page):

    # limit posts per page and calculate pages needed to display all posts
    if posts_per_page < 1:
        no_of_pages = 1
    else:
        no_of_pages = int(math.floor((no_posts-1)/posts_per_page) + 1)

    return no_of_pages

def pcom_find_sticky_posts(content_list,manual_sticky):

    sticky_out = []
    posts_out = pcom_get_comma_list(content_list)

    if manual_sticky == 'True':
        non_sticky = []
        for postname in posts_out:
            if postname.find(ct.PCOM_POST_LIST_STICKY_INDICATOR) > -1:
                # remove indicator and any additional spaces
                name_out = postname.replace(ct.PCOM_POST_LIST_STICKY_INDICATOR,'')
                name_out = name_out.rstrip().lstrip()
                sticky_out.append(name_out)
            else:
                non_sticky.append(postname)

        posts_out = non_sticky

    return posts_out,sticky_out

def pcom_find_sticky_posts_by_meta(posts):

    sticky_out = []
    non_sticky = []

    for post in posts:
        if post['sticky'] == ct.PCOM_META_STICKY:
            sticky_out.append(post)
        else:
            non_sticky.append(post)

    return non_sticky,sticky_out

# DEPENDENCIES

def pcom_get_dependency(dependency_list,filename):
    out = {}
    if dependency_list:
        for dependency in dependency_list:
            if dependency[ct.PCOM_DEPENDENCY_LIST_FILENAME] == filename:
                out = dependency

    return out

# update dependency list for file.
# if page or post - add to list
def pcom_update_dependencies(dependency_list,filename,insert_name):
    no_file = True
    # if dependency exists add insert if not present
    # if dependency does not exist create its
    if dependency_list:
        for dependency in dependency_list:
            if dependency[ct.PCOM_DEPENDENCY_LIST_FILENAME] == filename:
                no_file = False
                if insert_name not in dependency[ct.PCOM_DEPENDENCY_LIST_DEPS]:
                    dependency[ct.PCOM_DEPENDENCY_LIST_DEPS].append(insert_name)

        if no_file:
            dependency = OrderedDict([ (ct.PCOM_DEPENDENCY_LIST_FILENAME, filename),
                (ct.PCOM_DEPENDENCY_LIST_DEPS, [insert_name]) ])
            dependency_list.append(dependency)

    return dependency_list

#

# finds all filenames that have a dependency on the insert file
def pcom_find_dependencies(dependency_list,insert_file):

    out = []
    # construct array of dictionaries that does not include the
    # entry for filename
    if dependency_list:
        for dependency in dependency_list:
            if insert_file in dependency[ct.PCOM_DEPENDENCY_LIST_DEPS]:
                out.append(dependency[ct.PCOM_DEPENDENCY_LIST_FILENAME])

    return out

# removes file from dependencies when deleted from source
def pcom_delete_dependencies_file(dependency_list,filename):

    out = []
    # construct array of dictionaries that does not include the
    # entry for filename
    if dependency_list:
        for dependency in dependency_list:
            if dependency[ct.PCOM_DEPENDENCY_LIST_FILENAME] != filename:
                out.append(dependency)

    return out

# removes file from dependencies when deleted from source
def pcom_delete_dependencies_insert(dependency_list,filename,insert_file):

    # construct array of dictionaries that does not include the
    # entry for filename
    list = []
    if dependency_list:
        for dependency in dependency_list:
            if dependency[ct.PCOM_DEPENDENCY_LIST_FILENAME] == filename:
                for insert in dependency[ct.PCOM_DEPENDENCY_LIST_DEPS]:
                    if insert != insert_file:
                        list.append(insert)

                # set dependency to new list
                dependency[ct.PCOM_DEPENDENCY_LIST_DEPS] = list
                break

    return dependency_list

# update dependency list with list of valid inserts that were processed
# delete file if list is empty and there is no dependency on settings.txt
def pcom_post_process_dependencies(dependency_list,filename,valid_inserts):

    delete_file =  False
    delete_inserts = False
    inserts_to_delete = []

    if dependency_list:
        for dependency in dependency_list:

            if dependency[ct.PCOM_DEPENDENCY_LIST_FILENAME] == filename:
                if valid_inserts:
                    # scan dependencies and check if they are processed
                    # if not add to deletion list
                    for insert in dependency[ct.PCOM_DEPENDENCY_LIST_DEPS]:
                        if insert not in valid_inserts:
                            delete_inserts = True
                            inserts_to_delete.append(insert)

                else:
                    # if no settings text - set file to be deleted
                    if ct.PCOM_REQ_FILE_SETTINGS not in dependency[ct.PCOM_DEPENDENCY_LIST_DEPS]:
                        delete_file = True

                break

        if delete_file:
            dependency_list = pcom_delete_dependencies_file(dependency_list,filename)

        if delete_inserts:
            for insert in inserts_to_delete:
                dependency_list = pcom_delete_dependencies_insert(dependency_list,filename,insert)

    return dependency_list

# POSTLIST

def pcom_update_postlist(postlist,postname,url,meta,date_format,type,settings):
    # check if postname in post
    posts_per_page = settings['posts_per_page']
    def_author = settings['default_author']
    post_exists = False
    post_entry = {}
    date = pcom_get_date(date_format)
    time = pcom_get_time()

    if postlist:
        for ind,post in enumerate(postlist['posts']):
            if post['postname'] == postname:
                post_exists = True
                # update meta and update time
                postlist['posts'][ind] = \
                pcom_update_postlist_entry(post, url, postname, meta, date, time, False, post['index'], post['type'], settings)

        if not post_exists:
            # add post
            postlist['post_index'] += 1
            postlist['no_posts'] += 1
            post_entry = \
            pcom_update_postlist_entry(post_entry,url,postname,meta,date,time,True,postlist['post_index'],type,settings)
            postlist['posts'].append(post_entry)

        postlist['no_of_post_pages'] = pcom_calculate_posts_per_page(postlist['no_posts'],posts_per_page)

    return postlist

def pcom_update_postlist_entry(post, url, name, meta, date, time, new, index, type, settings):

    cats = pcom_get_comma_list(meta['categories'])
    authors = pcom_get_comma_list(meta['authors'])

    # check against default author if author is default
    if authors == [md.DEFAULT_AUTHOR]:
        if settings['default_author']['name'] != md.DEFAULT_AUTHOR:
            authors = [ settings['default_author']['name'] ]

    # check for defined default thumbnail
    if meta['thumb_link'] == sch.PM_DEFAULT_THUMBNAIL_IMAGE_LINK:
        if settings['default_thumb_link'] != sch.PM_DEFAULT_THUMBNAIL_IMAGE_LINK:
            meta['thumb_link'] = settings['default_thumb_link']

    # update post meta - if new add creation date and time
    if new:

        post = OrderedDict([ ('index', index),
            ('type', type),
            ('url', url),
            ('title', meta['page_title']),
            ('postname', name),
            ('description', meta['page_description']),
            ('categories', cats),
            ('authors', authors),
            ('extract',meta['page_extract']),
            ('thumbnail',meta['thumb_link']),
            ('creation_date', date),
            ('creation_time', time),
            ('date_modified', date),
            ('time_modified', time),
            ('sticky', meta['sticky']) ])
    else:
        # update other attributes in current post
        post['title'] = meta['page_title']
        post['description'] = meta['page_description']
        post['extract'] = meta['page_extract']
        post['thumbnail'] = meta['thumb_link']
        post['date_modified'] = date
        post['time_modified'] = time
        post['categories'] = cats
        post['authors'] = authors
        post['sticky'] = meta['sticky']
        post['url'] = meta['url']

    return post

def pcom_delete_from_postlist(postlist,postname):
    # returns postlist after deletion
    if postlist:
        re_posts = []
        for post in postlist['posts']:
            if post['postname'] != postname:
                re_posts.append(post)

        # set posts array to re_posts
        postlist['posts'] = re_posts

        # adjust number of posts down by one
        postlist['no_posts'] -= 1

    return postlist


def pcom_find_post_pagination(postlist,postname,type):

    out = {'next_url': ct.PCOM_NO_ENTRY,
    'prev_url': ct.PCOM_NO_ENTRY,
    'next_title': ct.PCOM_NO_ENTRY,
    'prev_title': ct.PCOM_NO_ENTRY}

    selected_ind = 0
    found = False

    if postlist:
        posts = pcom_order_postlist_posts(postlist['posts'])
        posts = pcom_create_posts_pages_array(posts,type)

        # find post
        for ind,post in enumerate(posts):
            if postname == post['postname']:
                selected_index = ind

                if selected_index == 0:
                    if len(posts) > 1:
                        found = True
                        out['next_url'] = posts[ind+1]['url']
                        out['next_title'] = posts[ind+1]['title']
                elif selected_index == len(posts)-1:
                    if len(posts) > 1:
                        found = True
                        out['prev_url'] = posts[ind-1]['url']
                        out['prev_title'] = posts[ind-1]['title']
                else:
                    if len(posts) > 2:
                        found = True
                        out['next_url'] = posts[ind+1]['url']
                        out['next_title'] = posts[ind+1]['title']
                        out['prev_url'] = posts[ind-1]['url']
                        out['prev_title'] = posts[ind-1]['title']

    return out,found

def pcom_find_manual_pagination(postlist,next,prev):

    out = {'next_url': ct.PCOM_NO_ENTRY,
    'prev_url': ct.PCOM_NO_ENTRY,
    'next_title': ct.PCOM_NO_ENTRY,
    'prev_title': ct.PCOM_NO_ENTRY}
    found = False

    if next or prev:
        if next:
            found = True
            next_post = pcom_find_post(postlist,next)
            if next_post['postname'] != ct.PCOM_NO_ENTRY:
                out['next_url'] = next_post['url']
                out['next_title'] = next_post['title']

        if prev:
            found = True
            prev_post = pcom_find_post(postlist,prev)
            if prev_post['postname'] != ct.PCOM_NO_ENTRY:
                out['prev_url'] = prev_post['url']
                out['prev_title'] = prev_post['title']

    return out,found


# PAGINATION

def pcom_get_pagination_info(html_array,postlist,postname,fileroot):

    args = {'open': ct.PCOM_INSERT_PAGINATION_TAG_OPEN,'close': ct.PCOM_INSERT_PAGINATION_TAG_CLOSE}
    links_html = ''
    pagination_info = {}
    next_ref = ''
    prev_ref = ''

    selected_post = pcom_find_post(postlist,postname)

    type = False
    if selected_post['type'] == 'post':
        type = True

    for ind,line in enumerate(html_array):
        if line.find(ct.PCOM_INSERT_PAGINATION_TAG_OPEN) > -1:

            syntax = sp.pcom_process_command_open_close_syntax(line,args)
            # placement : custom class
            elements = syntax['command_syntax'].split(':')
            placement = elements[0].rstrip().lstrip()
            custom_class = elements[1].rstrip().lstrip()
            manual_refs = elements[2].rstrip().lstrip()
            links,found = pcom_find_post_pagination(postlist,postname,type)

            if manual_refs:
                refs = manual_refs.split(',')
                next_ref = refs[0]
                prev_ref = refs[1]

            pagination_info = {'index': ind,
            'fileroot': fileroot.replace("/","_"),
            'next_ref': next_ref,
            'prev_ref': prev_ref,
            'postname': postname,
            'type': type}

            if found:
                out_html = (sp.pcom_open_placement_class(custom_class,placement)
                        + sp.pcom_open_custom_class_div(custom_class,sch.PM_POST_PAGINATION_OPEN) + ct.NL
                        + sch.PM_POST_PAGINATION_CLOSE + ct.NL
                        + sp.pcom_close_placement_class(placement))

                html_array[ind] = out_html
            else:
                html_array[ind] = ''

    return html_array,pagination_info

# ---


def pcom_update_categories_from_settings(categories,settings_categories,settings):

    posts_per_page = settings['posts_per_page']

    if 'name' not in settings_categories:

        for settings_category in settings_categories:
            # check to see if already there
            cat_present = False

            for ind, category in enumerate(categories['categories']):

                if 'name' in settings_category:

                    if settings_category['name'] == category['name']:
                        cat_present = True
                        # update data
                        category['thumbnail'] = settings_category['thumbnail']
                        category['description'] = settings_category['description']

                        categories['categories'][ind] = category

            if not cat_present:
                if 'name' in settings_category:

                    thumbnail = sch.PM_DEFAULT_THUMBNAIL_IMAGE_LINK
                    if settings['default_thumb_link'] != sch.PM_DEFAULT_THUMBNAIL_IMAGE_LINK:
                        thumbnail = settings['default_thumb_link']

                    if 'thumbnail' in settings_category:
                        if settings_category['thumbnail']:
                            thumbnail = settings_category['thumbnail']

                    description = ''
                    if 'description' in settings_category:
                        description = settings_category['description']

                    new_category = OrderedDict([ ('name', settings_category['name']),
                        ('thumbnail', thumbnail),
                        ('description', description) ])
                    categories['categories'].append(new_category)

        # update no of pages
        categories['no_of_category_pages'] = pcom_calculate_posts_per_page(len(categories['categories']),posts_per_page)

    return categories

def pcom_update_authors_from_settings(authors,settings_authors,settings):

    posts_per_page = settings['posts_per_page']

    # initial filter - error will have name and error
    if 'name' not in settings_authors:

        if settings_authors == ct.PCOM_NO_ENTRY or settings['default_author']:

            thumbnail = settings['default_author']['thumbnail']

            if thumbnail == sch.PM_DEFAULT_THUMBNAIL_IMAGE_LINK:
                if thumbnail != settings['default_thumb_link']:
                    thumbnail = settings['default_thumb_link']

            new_author = OrderedDict([ ('name', settings['default_author']['name']),
                ('shortname', settings['default_author']['shortname']),
                ('thumbnail', thumbnail),
                ('description', settings['default_author']['description']) ])
            authors['authors'].append(new_author)

        for settings_author in settings_authors:
            # check to see if already there
            author_present =  False

            for ind,author in enumerate(authors['authors']):

                if 'name' in settings_author and 'shortname' in settings_author:

                    if settings_author['name'] == author['name'] or settings_author['shortname'] == author['shortname']:
                        author_present = True
                        # update data
                        if 'name' in settings_author:
                            author['name'] = settings_author['name']
                        if 'shortname' in settings_author:
                            author['shortname'] = settings_author['shortname']
                        if 'thumbnail' in settings_author:
                            author['thumbnail'] = settings_author['thumbnail']
                        if 'description' in settings_author:
                            author['description'] = settings_author['description']

                        authors['authors'][ind] = author

            if not author_present:
                if 'name' in settings_author and 'shortname' in settings_author:

                    thumbnail = sch.PM_DEFAULT_THUMBNAIL_IMAGE_LINK
                    if settings['default_thumb_link'] != sch.PM_DEFAULT_THUMBNAIL_IMAGE_LINK:
                        thumbnail = settings['default_thumb_link']

                    if 'thumbnail' in settings_author:
                        if settings_author['thumbnail']:
                            thumbnail = settings_author['thumbnail']

                    description = ''
                    if 'description' in settings_author:
                        description = settings_author['description']

                    new_author = OrderedDict([ ('name', settings_author['name']),
                        ('shortname', settings_author['shortname']),
                        ('thumbnail', thumbnail),
                        ('description', description) ])
                    authors['authors'].append(new_author)

        # update no of pages
        authors['no_of_author_pages'] = pcom_calculate_posts_per_page(len(authors['authors']),posts_per_page)

        # update default author in settings
        for ind,author in enumerate(authors['authors']):

            if author['name'] == settings['default_author']['name'] or \
            author['shortname'] == settings['default_author']['shortname']:

                author['name'] = settings['default_author']['name']
                author['shortname'] = settings['default_author']['shortname']
                author['thumbnail'] = settings['default_author']['thumbnail']
                author['description'] = settings['default_author']['description']

                authors['authors'][ind] = author

    return authors

def pcom_update_categories_from_postlist_data(categories,cat_list,settings,type):

    posts_per_page = settings['posts_per_page']

    if categories:
        if type == 'post':
            for request_cat in cat_list:
                # check to see if already there
                cat_present = False
                for category in categories['categories']:
                    if request_cat == category['name']:
                        cat_present = True

                if not cat_present:
                    thumbnail = sch.PM_DEFAULT_THUMBNAIL_IMAGE_LINK
                    if settings['default_thumb_link'] != sch.PM_DEFAULT_THUMBNAIL_IMAGE_LINK:
                        thumbnail = settings['default_thumb_link']

                    new_category = OrderedDict([ ('name', request_cat),
                        ('thumbnail',thumbnail),
                        ('description', '') ])
                    categories['categories'].append(new_category)

            # update no of pages
            categories['no_of_category_pages'] = pcom_calculate_posts_per_page(len(categories['categories']),posts_per_page)

    return categories

def pcom_update_authors_from_postlist_data(authors,author_list,settings):

    posts_per_page = settings['posts_per_page']

    if authors:
        for request_author in author_list:
            # check to see if already there
            author_present =  False
            for author in authors['authors']:
                if request_author == author['name'] or request_author == author['shortname']:
                    author_present = True

            if not author_present:

                thumbnail = sch.PM_DEFAULT_THUMBNAIL_IMAGE_LINK
                if settings['default_thumb_link'] != sch.PM_DEFAULT_THUMBNAIL_IMAGE_LINK:
                    thumbnail = settings['default_thumb_link']

                new_author = OrderedDict([ ('name', request_author),
                    ('shortname', request_author),
                    ('thumbnail', thumbnail),
                    ('description', '') ])
                authors['authors'].append(new_author)

        # update no of pages
        authors['no_of_author_pages'] = pcom_calculate_posts_per_page(len(authors['authors']),posts_per_page)

    return authors

# ---

def pcom_update_postlists_info(postlist_info,local_info,js_name,fileroot,is_template,is_search):

    file_present = False
    delete_info = False
    fileroot = fileroot.replace("/","_")

    # check for current information and update accordingly
    if postlist_info:
        for ind,info in enumerate(postlist_info):
            if js_name == info['name']:
                file_present = True
                if local_info:
                    postlist_info[ind]['postlists'] = local_info
                else:
                    delete_info = True

    if (not file_present and not is_template) or not postlist_info or is_search:
        if local_info:
            new_info = OrderedDict([ ('name', js_name),
                ('fileroot', fileroot),
                ('postlists', local_info) ])
            postlist_info.append(new_info)

    # remove empty postlists
    if delete_info:
        temp = []
        for info in postlist_info:
            if js_name != info['name']:
                temp.append(info)

        postlist_info = temp

    return postlist_info


# pagination

def pcom_update_pagination_info(pagination_info,local_info,pagination_name,fileroot):

    file_present = False
    delete_info = False
    fileroot = fileroot.replace("/","_")

    # check for current information and update accordingly
    if pagination_info:
        for ind,info in enumerate(pagination_info):
            if pagination_name == info['name']:
                file_present = True
                if local_info:
                    pagination_info[ind]['pagination'] = local_info
                else:
                    delete_info = True

    if not file_present or not pagination_info:
        if local_info:
            new_info = OrderedDict([ ('name', pagination_name),
                ('fileroot', fileroot),
                ('pagination', local_info) ])
            pagination_info.append(new_info)

    # remove empty postlists
    if delete_info:
        temp = []
        for info in pagination_info:
            if pagination_name != info['name']:
                temp.append(info)

        pagination_info = temp

    return pagination_info

# check or add new js_constant file
def pcom_update_js_constants(js_constants,js_file):

    if js_file not in js_constants:
        js_constants.append(js_file)

    return js_constants

def pcom_delete_from_js_constants(js_constants,js_file):
    out = []
    for js in js_constants:
        if js != js_file:
            out.append(js)

    return out

# archive

def pcom_get_archive_date_info(date_string,settings):

    dates = {'month': '',
    'year': '',
    'date_fileroot': '',
    'date_url_name': ''
    }

    date_info = date_string.split('/')

    if settings['date_format'] == ct.PCOM_UK_DATE_FORMAT:
        dates['month'] = date_info[1]
    else:
        dates['month'] = date_info[0]
    dates['year'] = date_info[2]

    dates['date_fileroot'] = dates['month'] + "_" + dates['year']
    dates['date_url_name'] = dates['month'] + "-" + dates['year']

    return dates

def pcom_create_archive_entry(list,post,dates):

    if post['type'] == 'post':
        new_info = OrderedDict([ ('name', dates['date_url_name']),
            ('fileroot', dates['date_fileroot']),
            ('posts', [ post['postname'] ]),
            ('pages', [])   ])
    else:
        new_info = OrderedDict([ ('name', dates['date_url_name']),
            ('fileroot', dates['date_fileroot']),
            ('posts', []),
            ('pages', [ post['postname'] ] )   ])
    list.append(new_info)

    return list


def pcom_update_archive(archive,postlist,settings):

    for post in postlist['posts']:

        dates = pcom_get_archive_date_info(post['creation_date'],settings)
        date_match = False

        if archive['created']:
            for info in archive['created']:
                if info['name'] == dates['date_url_name']:
                    date_match = True
                    if post['type'] == 'post':
                        if post['postname'] not in info['posts']:
                            info['posts'].append(post['postname'])
                    else:
                        if post['postname'] not in info['pages']:
                            info['pages'].append(post['postname'])

            if not date_match:
                archive['created'] = pcom_create_archive_entry(archive['created'],post,dates)

        else:
            archive['created'] = pcom_create_archive_entry(archive['created'],post,dates)

        dates = pcom_get_archive_date_info(post['date_modified'],settings)
        date_match = False

        if archive['modified']:
            for info in archive['modified']:
                if info['name'] == dates['date_url_name']:
                    date_match = True
                    if post['type'] == 'post':
                        if post['postname'] not in info['posts']:
                            info['posts'].append(post['postname'])
                    else:
                        if post['postname'] not in info['pages']:
                            info['pages'].append(post['postname'])

            if not date_match:
                archive['modified'] = pcom_create_archive_entry(archive['modified'],post,dates)

        else:
            archive['modified'] = pcom_create_archive_entry(archive['modified'],post,dates)

    return archive
# ==========

def pcom_get_date(date_format):

    x = datetime.datetime.now()
    if date_format == ct.PCOM_US_DATE_FORMAT:
        date = x.strftime("%m/%d/%Y")
    else:
        date = x.strftime("%d/%m/%Y")

    return date

def pcom_get_time():

    x = datetime.datetime.now()
    time = x.strftime("%X")
    return time

def pcom_get_comma_list(list):

    comma_list = []
    # split list at commas
    split_strings = list.split(",")
    for string in split_strings:
        comma_list.append(string.rstrip().lstrip())

    return comma_list

def pcom_create_comma_list_from_array(array):

    comma_list = []
    for k in array:
        comma_list.append(k.rstrip().lstrip())

    return (",").join(comma_list)

def pcom_create_comma_list_from_dict(dict):

    comma_list = []
    for k in dict:
        comma_list.append(k.rstrip().lstrip())

    return (",").join(comma_list)
