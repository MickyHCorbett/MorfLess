# secondary process functions - e.g. creating lists files
from libraries import constants as ct
from libraries import globals as gb
from libraries import schematics as sch
from libraries import html_elements as he
from libraries import string_processes as sp
from libraries import lists as ls

import json

def pcom_process_postlist(postlist_info,postlist,settings,list_meta,fileroot):

    postlist_constant = ct.PCOM_NO_ENTRY
    processed = False

    if postlist_info:
        postlist_constant = ''
        entry_end = '},'
        array_end = ']'

        for ind,info in enumerate(postlist_info):
            list_end = False

            if info['content'] == ct.PCOM_SETTINGS_TYPE_POSTS:
                # this section produces an array of post objects
                list_of_posts = ls.pcom_create_posts_pages_array(postlist['posts'],'post')
                # order most recent first
                list_of_posts = ls.pcom_order_postlist_posts(list_of_posts)
                # separate sticky posts from non sticky
                list_of_posts,list_of_stickies = ls.pcom_find_sticky_posts_by_meta(list_of_posts)
            else:
                # this section produces a list of postnames
                list_of_posts,list_of_stickies = ls.pcom_find_sticky_posts(info['content'],info['manual_sticky'])

            if ind == 0:
                postlist_constant += 'window._postlist_' + fileroot + ' = {' + ct.NL
                postlist_constant += ct.T1 + "identifier: '" + sch.PM_POST_LIST_IDENTIFIER + "'," + ct.NL
                postlist_constant += ct.T1 + "pagination_element: '" + sch.POSTLIST_PAGINATION + "'," + ct.NL
                postlist_constant += ct.T1 + "page_numbers_selected_class: '" + ct.PCOM_PAGE_NUMBERS_CURRENT_CLASS + "'," + ct.NL
                postlist_constant += ct.T1 + "pagination_class: '" + ct.PCOM_POSTLIST_PAGINATION_CLASS + "'," + ct.NL
                postlist_constant += ct.T1 + "pagination_selector_id: '" + sch.PM_POSTLIST_PAGINATION_SELECTOR_IDENT + "'," + ct.NL
                postlist_constant += ct.T1 + "pagination_number_sub: '" + sch.PM_POSTLIST_PAGINATION_NUMBER + "'," + ct.NL
                postlist_constant += ct.T1 + "pagination_number_ident: '" + sch.PM_POSTLIST_PAGINATION_IDENT + "'," + ct.NL
                postlist_constant += ct.T1 + 'entries: [' + ct.NL

            postlist_constant += ct.T1 + '{' + ct.NL
            postlist_constant += ct.T2 + 'posts_per_page: ' + info['ppp'] + ',' + ct.NL
            postlist_constant += ct.T2 + 'posts: ['+ ct.NL

            # add non sticky posts
            for ind2,entry in enumerate(list_of_posts):
                if info['content'] == ct.PCOM_SETTINGS_TYPE_POSTS:
                    post = entry
                else:
                    post = ls.pcom_find_post(postlist,entry)


                if ind2 == (len(list_of_posts)-1):
                    list_end = True

                if post['postname'] != ct.PCOM_NO_ENTRY:
                    if list_of_stickies:
                        entry_html =  he.pcom_create_post_list_entry(post,settings,list_meta,list_end,ignore_meta=True)
                    else:
                        entry_html =  he.pcom_create_post_list_entry(post,settings,list_meta,list_end)
                    postlist_constant += sp.pcom_add_3tabs_to_content_line(entry_html)

                if list_end:
                    postlist_constant += ct.T2 + '],' + ct.NL

            # add non sticky posts
            postlist_constant += ct.T2 + 'sticky: ['+ ct.NL

            if list_of_stickies:
                list_end = False

                for ind3,entry in enumerate(list_of_stickies):
                    if info['content'] == ct.PCOM_SETTINGS_TYPE_POSTS:
                        post = entry
                    else:
                        post = ls.pcom_find_post(postlist,entry)

                    if ind3 == (len(list_of_stickies)-1):
                        list_end = True

                    if post['postname'] != ct.PCOM_NO_ENTRY:
                        entry_html =  he.pcom_create_post_list_entry(post,settings,list_meta,list_end,manual_sticky=True)
                        postlist_constant += sp.pcom_add_3tabs_to_content_line(entry_html)

                    if list_end:
                        postlist_constant += ct.T2 + ']' + ct.NL

            else:
                postlist_constant += ct.T2 + ']' + ct.NL

            if ind == (len(postlist_info)-1):
                entry_end = '}'

            postlist_constant += ct.T1 + entry_end + ct.NL
            processed = True

        # close list
        postlist_constant += ct.T1 + ']' + ct.NL + '};'

    return postlist_constant,processed

# template postlist

def pcom_create_sub_template_backlink(type,settings):

    back_link_text = ''
    back_link = ''

    if settings['template_sub_header_back_link_text'][type] != ct.PCOM_JSON_LOAD_ERROR:
        back_link_text = settings['template_sub_header_back_link_text'][type].rstrip().lstrip()
        back_link_text = sp.pcom_replace_quotes(back_link_text)
        back_link_template = sch.PM_SUB_TEMPLATE_BACK_LINK
        back_link_url = "/" + sp.pcom_create_template_fileroot(type,settings) + "/"

        if back_link_text:
            back_link = '\\' +ct.NL
            back_link += back_link_template.replace(sch.PM_POSTLIST_TEMPLATE_BACKLINK_NAME,back_link_text)
            back_link = back_link.replace(sch.PM_POSTLIST_TEMPLATE_BACKLINK,back_link_url)

            back_link = sp.pcom_add_3tabs_to_content_line(back_link)

    return back_link

def pcom_create_sub_template_title(type,settings,sub):

    sub_title = ''
    back_link = ''

    if type != ct.PCOM_SETTINGS_TYPE_POSTS:
        if settings['template_sub_header_text'][type] != ct.PCOM_JSON_LOAD_ERROR:
            sub_title = settings['template_sub_header_text'][type] + ' ' + sub

        back_link = pcom_create_sub_template_backlink(type,settings)
    else:
        if settings['template_main_header_text'][type] != ct.PCOM_JSON_LOAD_ERROR:
            sub_title = settings['template_main_header_text'][type]

    return sub_title,back_link


def pcom_determine_post_list_from_type(postlist,archive,settings,list_meta,type,sub):

    list_of_posts = []

    if type == ct.PCOM_SETTINGS_TYPE_POSTS:
        list_of_posts = ls.pcom_create_posts_pages_array(postlist['posts'],'post')

    if type == ct.PCOM_SETTINGS_TYPE_CATEGORIES:
        list_of_posts = ls.pcom_find_sub_list(postlist['posts'],[],type,sub,'post')

    if type == ct.PCOM_SETTINGS_TYPE_AUTHORS:
        # get posts and pages
        list_of_posts = ls.pcom_find_sub_list(postlist['posts'],list_meta['authors']['authors'],type,sub,'',True)

    if type == ct.PCOM_SETTINGS_TYPE_ARCHIVE:
        list_of_posts = ls.pcom_find_sub_list_archive(archive,postlist,sub,'post')

    return list_of_posts

def pcom_process_template_postlist(postlist,archive,type,settings,list_meta,fileroot,sub=''):

    processed = False
    postlist_constant = ''
    sub_title = ''
    back_link = ''

    list_of_posts = pcom_determine_post_list_from_type(postlist,archive,settings,list_meta,type,sub)
    sub_title,back_link = pcom_create_sub_template_title(type,settings,sub)

    # order most recent first
    list_of_posts = ls.pcom_order_postlist_posts(list_of_posts)
    # separate sticky posts from non sticky
    list_of_posts,list_of_stickies = ls.pcom_find_sticky_posts_by_meta(list_of_posts)

    postlist_constant += 'window._postlist_' + fileroot + ' = {' + ct.NL
    postlist_constant += ct.T1 + "identifier: '" + sch.PM_POST_LIST_TEMPLATE_IDENTIFIER + "'," + ct.NL
    postlist_constant += ct.T1 + "pagination_element: '" + sch.POSTLIST_PAGINATION + "'," + ct.NL
    postlist_constant += ct.T1 + "page_numbers_selected_class: '" + ct.PCOM_PAGE_NUMBERS_CURRENT_CLASS + "'," + ct.NL
    postlist_constant += ct.T1 + "pagination_class: '" + ct.PCOM_POSTLIST_PAGINATION_CLASS + "'," + ct.NL
    postlist_constant += ct.T1 + "pagination_selector_id: '" + sch.PM_POSTLIST_PAGINATION_SELECTOR_IDENT + "'," + ct.NL
    postlist_constant += ct.T1 + "pagination_number_sub: '" + sch.PM_POSTLIST_PAGINATION_NUMBER + "'," + ct.NL
    postlist_constant += ct.T1 + "pagination_number_ident: '" + sch.PM_POSTLIST_PAGINATION_IDENT + "'," + ct.NL
    postlist_constant += ct.T1 + 'sub_title: "' + sub_title + '",' + ct.NL
    postlist_constant += ct.T1 + "back_link: '" + back_link + "'," + ct.NL
    postlist_constant += ct.T1 + "header: '" + sch.PM_TEMPLATE_HEADER_FORMAT + "'," + ct.NL
    postlist_constant += ct.T1 + 'entries: [' + ct.NL

    postlist_constant += ct.T1 + '{' + ct.NL
    postlist_constant += ct.T2 + 'posts_per_page: ' + str(settings['posts_per_page']) + ',' + ct.NL
    postlist_constant += ct.T2 + 'posts: ['+ ct.NL

    if list_of_posts:
        list_end = False
        for ind2,post in enumerate(list_of_posts):
            if ind2 == (len(list_of_posts)-1):
                list_end = True

            if post['postname'] != ct.PCOM_NO_ENTRY:
                entry_html =  he.pcom_create_post_list_entry(post,settings,list_meta,list_end)
                postlist_constant += sp.pcom_add_3tabs_to_content_line(entry_html)

    postlist_constant += ct.T2 + '],' + ct.NL

    # add non sticky posts
    postlist_constant += ct.T2 + 'sticky: ['+ ct.NL

    if list_of_stickies:
        list_end = False
        for ind3,post in enumerate(list_of_stickies):
            if ind3 == (len(list_of_stickies)-1):
                list_end = True

            if post['postname'] != ct.PCOM_NO_ENTRY:
                entry_html =  he.pcom_create_post_list_entry(post,settings,list_meta,list_end)
                postlist_constant += sp.pcom_add_3tabs_to_content_line(entry_html)

            if list_end:
                postlist_constant += ct.T2 + ']' + ct.NL

    else:
        postlist_constant += ct.T2 + ']' + ct.NL

    postlist_constant += ct.T1 + '}' + ct.NL
    processed = True

    # close list
    postlist_constant += ct.T1 + ']' + ct.NL + '};'

    return postlist_constant,processed

# create main list page of template categories, authors etc

def pcom_process_template_list_info(list,settings,base_url,fileroot):

    processed = False
    list_constant = ''
    sub_title = ''

    info = pcom_create_template_info_references(list,base_url,settings)

    if base_url == ct.PCOM_SETTINGS_TYPE_CATEGORIES:
        if settings['template_main_header_text'][base_url] != ct.PCOM_JSON_LOAD_ERROR:
            sub_title = settings['template_main_header_text'][base_url]

    if base_url == ct.PCOM_SETTINGS_TYPE_AUTHORS:
        if settings['template_main_header_text'][base_url] != ct.PCOM_JSON_LOAD_ERROR:
            sub_title = settings['template_main_header_text'][base_url]

    list_constant += 'window._postlist_' + fileroot + ' = {' + ct.NL
    list_constant += ct.T1 + "identifier: '" + sch.PM_POST_LIST_TEMPLATE_IDENTIFIER + "'," + ct.NL
    list_constant += ct.T1 + "pagination_element: '" + sch.POSTLIST_PAGINATION + "'," + ct.NL
    list_constant += ct.T1 + "page_numbers_selected_class: '" + ct.PCOM_PAGE_NUMBERS_CURRENT_CLASS + "'," + ct.NL
    list_constant += ct.T1 + "pagination_class: '" + ct.PCOM_POSTLIST_PAGINATION_CLASS + "'," + ct.NL
    list_constant += ct.T1 + "pagination_selector_id: '" + sch.PM_POSTLIST_PAGINATION_SELECTOR_IDENT + "'," + ct.NL
    list_constant += ct.T1 + "pagination_number_sub: '" + sch.PM_POSTLIST_PAGINATION_NUMBER + "'," + ct.NL
    list_constant += ct.T1 + "pagination_number_ident: '" + sch.PM_POSTLIST_PAGINATION_IDENT + "'," + ct.NL
    list_constant += ct.T1 + "sub_title: '" + sub_title + "'," + ct.NL
    list_constant += ct.T1 + "back_link: ''," + ct.NL
    list_constant += ct.T1 + "header: '" + sch.PM_TEMPLATE_HEADER_FORMAT + "'," + ct.NL
    list_constant += ct.T1 + 'entries: [' + ct.NL

    list_constant += ct.T1 + '{' + ct.NL
    list_constant += ct.T2 + 'posts_per_page: ' + str(settings['posts_per_page']) + ',' + ct.NL
    list_constant += ct.T2 + 'posts: ['+ ct.NL

    if list:
        list_end = False
        for ind2,entry in enumerate(list):
            if ind2 == (len(list)-1):
                list_end = True

            if entry['name'] != ct.PCOM_NO_ENTRY:
                entry_html =  he.pcom_create_info_list_entry(entry,info[ind2]['url'],settings,list_end)
                list_constant += sp.pcom_add_3tabs_to_content_line(entry_html)

    list_constant += ct.T2 + '],' + ct.NL
    list_constant += ct.T2 + 'sticky: []'+ ct.NL
    list_constant += ct.T1 + '}' + ct.NL
    processed = True

    # close list
    list_constant += ct.T1 + ']' + ct.NL + '};'

    return list_constant,info,processed


def pcom_process_archive_info(archive,settings,base_url,base_name,fileroot):

    processed = False
    list_constant = ''
    sub_title = ''

    list = archive['created']
    info = pcom_create_archive_info_references(list,base_url,settings)

    if settings['template_main_header_text'][base_url] != ct.PCOM_JSON_LOAD_ERROR:
        sub_title = settings['template_main_header_text'][base_url]

    list_constant += 'window._postlist_' + fileroot + ' = {' + ct.NL
    list_constant += ct.T1 + "identifier: '" + sch.PM_POST_LIST_TEMPLATE_IDENTIFIER + "'," + ct.NL
    list_constant += ct.T1 + "pagination_element: '" + sch.POSTLIST_PAGINATION + "'," + ct.NL
    list_constant += ct.T1 + "page_numbers_selected_class: '" + ct.PCOM_PAGE_NUMBERS_CURRENT_CLASS + "'," + ct.NL
    list_constant += ct.T1 + "pagination_class: '" + ct.PCOM_POSTLIST_PAGINATION_CLASS + "'," + ct.NL
    list_constant += ct.T1 + "pagination_selector_id: '" + sch.PM_POSTLIST_PAGINATION_SELECTOR_IDENT + "'," + ct.NL
    list_constant += ct.T1 + "pagination_number_sub: '" + sch.PM_POSTLIST_PAGINATION_NUMBER + "'," + ct.NL
    list_constant += ct.T1 + "pagination_number_ident: '" + sch.PM_POSTLIST_PAGINATION_IDENT + "'," + ct.NL
    list_constant += ct.T1 + "sub_title: '" + sub_title + "'," + ct.NL
    list_constant += ct.T1 + "back_link: ''," + ct.NL
    list_constant += ct.T1 + "header: '" + sch.PM_TEMPLATE_HEADER_FORMAT + "'," + ct.NL
    list_constant += ct.T1 + 'entries: [' + ct.NL

    list_constant += ct.T1 + '{' + ct.NL
    list_constant += ct.T2 + 'posts_per_page: 9999,' + ct.NL
    list_constant += ct.T2 + 'posts: ['+ ct.NL

    if list:
        list_constant += "'" + ct.JS_ESCAPE + ct.NL
        list_constant += ct.T3 + sch.PM_POST_OPEN_ONLY + ct.JS_ESCAPE + ct.NL

        for ind2,entry in enumerate(list):

            entry_html =  he.pcom_create_archive_entry(entry,base_name,settings)
            list_constant += sp.pcom_add_3tabs_to_content_line(entry_html)

        list_constant += ct.T3 + sch.PM_POST_CLOSE + "'" + ct.NL

    list_constant += ct.T2 + '],' + ct.NL
    list_constant += ct.T2 + 'sticky: []'+ ct.NL
    list_constant += ct.T1 + '}' + ct.NL
    processed = True

    # close list
    list_constant += ct.T1 + ']' + ct.NL + '};'

    return list_constant,info,processed

# create category, author refererence dictionary

def pcom_update_template_meta(template_content,info,no_meta=False):

    title_meta = ''
    desc_meta = ''
    js_meta = ''
    constant_meta = ''

    if template_content:
        if not no_meta:
            title_meta = ' - ' + info['title']
            if info['description']:
                desc_meta = ' - ' + info['description'].replace('"','').replace(ct.PCOM_META_IGNORE_QUOTES,'')
            js_meta = info['sub_js_root']
            constant_meta = info['sub_fileroot']

        template_content = template_content.replace(sch.PM_TEMPLATE_TITLE_REPLACEMENT,title_meta)
        template_content = template_content.replace(sch.PM_TEMPLATE_DESCRIPTION_REPLACEMENT,desc_meta)
        template_content = template_content.replace(sch.PM_TEMPLATE_JS_NAME,js_meta)
        template_content = template_content.replace(sch.PM_TEMPLATE_CONSTANT_NAME,constant_meta)

    return template_content

def pcom_create_template_info_references(list,base_string,settings):

    references = []

    for entry in list:
        sub_js_constant_root = entry['name'].lower().replace("'","-").replace(' ','-')
        full_js_root = base_string.lower() + '-' + sub_js_constant_root
        filename = ct.PCOM_POSTLIST_CONSTANT_NAME_BASE + full_js_root + '.js'

        sub_fileroot = '_' + entry['name'].lower().replace(' ','_').replace("'","_")
        fileroot = base_string.lower() + sub_fileroot
        base_name = sp.pcom_create_template_fileroot(base_string,settings)
        url = base_name + '/' +  sub_js_constant_root + "/"
        s3url = url + 'index.html'

        test_html = base_name + '-' + sub_js_constant_root + ".html"
        title = sp.pcom_replace_quotes(entry['name'])

        info = {'title': entry['name'],
        'description': entry['description'],
        'sub_js_root': ('-' + sub_js_constant_root),
        'full_js_root': full_js_root,
        'sub_fileroot': sub_fileroot,
        'fileroot': fileroot,
        'js_filename': filename,
        'test_html': test_html,
        'url': ("/" + url),
        's3url': s3url,
        'js_constant': '',
        'template_content':''}

        references.append(info)

    return references

def pcom_create_archive_info_references(list,base_string,settings):

    references = []

    for entry in list:
        sub_js_constant_root = entry['name']
        full_js_root = base_string.lower() + '-' + sub_js_constant_root
        filename = ct.PCOM_POSTLIST_CONSTANT_NAME_BASE + full_js_root + '.js'

        sub_fileroot = '_' + entry['fileroot']
        fileroot = base_string.lower() + sub_fileroot
        base_name = sp.pcom_create_template_fileroot(base_string,settings)
        url = base_name + '/' +  sub_js_constant_root + "/"
        s3url = url + 'index.html'

        test_html = base_name + '-' + sub_js_constant_root + ".html"
        title = entry['name']

        info = {'title': entry['name'],
        'description': '',
        'sub_js_root': ('-' + sub_js_constant_root),
        'full_js_root': full_js_root,
        'sub_fileroot': sub_fileroot,
        'fileroot': fileroot,
        'js_filename': filename,
        'test_html': test_html,
        'url': ("/" + url),
        's3url': s3url,
        'js_constant': '',
        'template_content':''}

        references.append(info)

    return references

# Pagination

def pcom_process_pagination(postlist,pg_name,fileroot,info):

    pagination_constant = ''
    processed = False
    if info:
        # manual refs
        if info['next_ref'] or info['prev_ref']:
            links,found = ls.pcom_find_manual_pagination(postlist,info['next_ref'],info['prev_ref'])
        else:
            links,found = ls.pcom_find_post_pagination(postlist,info['postname'],info['type'])

        pagination,links_created = he.pcom_create_pagination_link(links)

        if found:
            pagination_constant = 'window._pagination_' + fileroot + ' = {' + ct.NL
            pagination_constant += ct.T1 + 'pagination: ' + pagination
            pagination_constant += '};'
            processed = True

    return pagination_constant,processed

# --- PROCESS PAGES sesction

def pcom_process_posts_page(postlist,archive,settings,list_meta,log,template_content):

    info_out = {'template_content': '',
    's3url': '',
    'posts_name': '',
    'posts_js_name': '',
    'posts_js_constant': '',
    'processed': False}

    post_type = ct.PCOM_SETTINGS_TYPE_POSTS
    posts_js = ct.PCOM_POSTLIST_CONSTANT_NAME_BASE + post_type + '.js'
    posts_name = sp.pcom_create_template_fileroot(post_type,settings)
    log['template_names'].append("Posts template base name: " + posts_name)

    if template_content:
        template_content = pcom_update_template_meta(template_content,{},no_meta=True)

        # create postlist js
        fileroot = post_type
        posts_constant,processed = pcom_process_template_postlist(postlist,archive,post_type,settings,list_meta,fileroot)

        if processed:
            info_out['template_content'] = template_content
            info_out['posts_js_name'] = posts_js
            info_out['posts_js_constant'] = posts_constant
            info_out['posts_name'] = posts_name
            info_out['s3url'] = posts_name + "/index.html"
            info_out['processed'] = True


    return info_out,log

def pcom_process_info_base_pages(info_list,base_type,template_content,postlist,archive,settings,list_meta,log):

    info_out = {'template_content': '',
    's3url': '',
    'base_name': '',
    'js_name': '',
    'js_constant': '',
    'processed': False}

    base_sub_info = []

    js_name = ct.PCOM_POSTLIST_CONSTANT_NAME_BASE + base_type + '.js'
    base_name = sp.pcom_create_template_fileroot(base_type,settings)
    log['template_names'].append(base_type + " template base name: " + base_name)

    if template_content:
        main_content = pcom_update_template_meta(template_content,{},no_meta=True)

        # create base info js
        if base_type == ct.PCOM_SETTINGS_TYPE_ARCHIVE:
            js_constant,base_sub_info,processed = \
            pcom_process_archive_info(archive,settings,base_type,base_name,base_type)
        else:
            js_constant,base_sub_info,processed = \
            pcom_process_template_list_info(info_list,settings,base_type,base_type)

        if processed:
            info_out['template_content'] = main_content
            info_out['js_name'] = js_name
            info_out['js_constant'] = js_constant
            info_out['base_name'] = base_name
            info_out['s3url'] = base_name + "/index.html"
            info_out['processed'] = True

            for ind,info in enumerate(base_sub_info):
                sub_content = pcom_update_template_meta(template_content,info)
                sub_js_constant,processed = \
                pcom_process_template_postlist(postlist,archive,base_type,settings,list_meta,info['fileroot'],sub=info['title'])

                base_sub_info[ind]['template_content'] = sub_content
                base_sub_info[ind]['js_constant'] = sub_js_constant


    return info_out,base_sub_info,log

# search config

def pcom_process_search_config(settings):

    list_constant = ''
    sub_title = ''

    if settings['template_main_header_text'][ct.PCOM_SETTINGS_TYPE_SEARCH] != ct.PCOM_JSON_LOAD_ERROR:
        sub_title = settings['template_main_header_text'][ct.PCOM_SETTINGS_TYPE_SEARCH]

    list_constant += 'window._search_config = {' + ct.NL
    list_constant += ct.T1 + "api: '" + settings['search_api_url'] + "'," + ct.NL
    list_constant += ct.T1 + "content_ident: '" + sch.PM_SEARCH_CONTENT_IDENTIFIER + "'," + ct.NL
    list_constant += ct.T1 + "header_ident: '" + sch.PM_SEARCH_QUERY_IDENTIFIER + "'," + ct.NL
    list_constant += ct.T1 + "pagination_element: '" + sch.POSTLIST_PAGINATION + "'," + ct.NL
    list_constant += ct.T1 + "page_numbers_selected_class: '" + ct.PCOM_PAGE_NUMBERS_CURRENT_CLASS + "'," + ct.NL
    list_constant += ct.T1 + "pagination_ident: '" + sch.PM_SEARCH_PAGINATION_IDENTIFIER + "'," + ct.NL
    list_constant += ct.T1 + "pagination_selector_id: '" + sch.PM_POSTLIST_PAGINATION_SELECTOR_IDENT + "'," + ct.NL
    list_constant += ct.T1 + "pagination_number_sub: '" + sch.PM_POSTLIST_PAGINATION_NUMBER + "'," + ct.NL
    list_constant += ct.T1 + "pagination_number_ident: '" + sch.PM_POSTLIST_PAGINATION_IDENT + "'," + ct.NL
    list_constant += ct.T1 + "sub_title: '" + sub_title + "'," + ct.NL
    list_constant += ct.T1 + 'posts_per_page: ' + str(settings['posts_per_page']) + ct.NL
    list_constant += '};'

    return list_constant

def pcom_create_search_response(search_content,postlist,settings,list_meta):

    # json data with js formatting for elements

    list_data = {'entries': [], 'sticky': []}

    if search_content:

        for ind2,entry in enumerate(search_content):

            # check post list
            post = ls.pcom_find_post(postlist,entry['name'])
            if post['postname'] != ct.PCOM_NO_ENTRY:

                entry_html = he.pcom_create_search_post_list_entry(post,settings,list_meta,ignore_meta=True)
                entry_html = sp.pcom_add_3tabs_to_content_line(entry_html)
                # create json compliant data
                entry_html = json.dumps(entry_html,indent=4)
                list_data['entries'].append(entry_html)

            # check template search content
            post = ls.pcom_find_template_search_content(settings,entry['name'])
            print(json.dumps(post))

            if post['name'] != ct.PCOM_NO_ENTRY:

                url = sp.pcom_create_template_search_content_url(entry['name'],settings)
                entry_html = he.pcom_create_template_search_list_entry(post,url,settings)
                entry_html = sp.pcom_add_3tabs_to_content_line(entry_html)
                # create json compliant data
                entry_html = json.dumps(entry_html,indent=4)
                list_data['entries'].append(entry_html)

    return list_data

def pcom_search_content(search_content,search_term):

    results = []

    if search_term and search_content:

        for ind,entry in enumerate(search_content):
            search_term = search_term.lower().replace("'",ct.JS_APOS_REPLACE)
            search_content[ind]['count'] = entry['content'].lower().count(search_term)

        # order
        search_content_ordered = sorted(search_content, key=lambda entry: entry['count'],reverse=True)

        for entry in search_content_ordered:
            entry_name = entry['name'].replace('.content','')
            if entry['count'] > 0:
                searched = {'name': entry_name, 'count': entry['count']}
                results.append(searched)

    return results
