# MorfLess v1.0
#
# classes
#

from libraries import globals as gb
from libraries import constants as ct
from libraries import schematics as sch
from libraries import string_processes as sp
from libraries import html_elements as he
from libraries import read_schematic as rs
from libraries import lists as ls

class HtmlOut:
    def __init__(self, content, log, site_settings, list_meta, filename, dependencies, postlist):
        self.log = log
        self.site_settings = site_settings
        self.list_meta = list_meta

        self.filename = filename
        self.fileroot = filename.lower().replace('.post','').replace('.page','')
        # check type of file
        self.is_root = sp.pcom_check_root(self.fileroot)
        self.is_template,self.is_search = sp.pcom_filter_template(self.fileroot,self.site_settings)
        # adjust fileroot for search
        if self.is_search:
            self.fileroot = sp.pcom_create_template_fileroot(self.fileroot,self.site_settings)

        # variable for adding template to page
        self.add_template = {}
        # reset some settings
        self.site_settings['current_file'] = filename
        self.site_settings['add_settings_to_dependencies'] = []
        self.site_settings['header_additions'] = []
        self.site_settings['footer_additions'] = []
        self.site_settings['add_default_header_additions'] = False
        self.site_settings['add_default_header_additions'] = False

        self.dependencies = dependencies
        self.all_data = {}
        self.html = ''
        self.html_array = []
        self.content = content
        self.insert_info = []
        self.postlist = postlist
        self.postlists_info = []
        self.content_meta_info = []
        self.pagination_info = {}
        self.pagination_name = ''
        self.raw_content = ''
        self.meta = {}

        # set postlist constant - check for search
        if not self.is_search:
            self.postlist_constant_name = 'postlist--' + sp.pcom_get_template_key(self.fileroot,self.site_settings) + '.js'
            self.pagination_name = ('pagination--'
                + sp.pcom_get_template_key(self.fileroot,self.site_settings)
                + '.js')
        else:
            self.postlist_constant_name = 'postlist--' + self.fileroot + '.js'
            self.pagination_name = 'pagination--' + self.fileroot + '.js'

    def convert_to_array(self):
        self.html_array = self.html.splitlines(True)

    def combine_array(self):
        self.html = ''.join(self.html_array)

    def process_schematic_sections(self):
        # get sections
        self.all_data = rs.polimorf_determine_schematic_reference(self.content, self.site_settings)
        self.meta = self.all_data['processed']['meta']
        self.update_postlist()
        self.update_categories()
        self.update_authors()
        # parse file html
        self.html = rs.polimorf_process_schematic_sections(
                            data=self.all_data['processed'],
                            settings=self.all_data['processed_settings'],
                            filename=self.filename,
                            fileroot=self.fileroot)

    def get_insert_info(self):
        self.convert_to_array()
        self.insert_info = sp.pcom_get_insert_info(self.html_array)

    def process_inserts(self):

        (self.html_array,
        self.log,
        self.site_settings,
        self.dependencies) = rs.pcom_process_inserts(
                                html_array=self.html_array,
                                insert_info=self.insert_info,
                                outlog=self.log,
                                site_settings=self.site_settings,
                                filename=self.filename,
                                dependencies=self.dependencies)
        self.combine_array()

    # process postlist, pagination and post meta html elements
    def process_second_stage(self):
        self.convert_to_array()
        self.process_postlists()
        self.process_pagination()
        self.process_content_meta()
        self.combine_array()
        self.insert_additions_into_html(ct.PCOM_HEADER_PLACEMENT)
        self.insert_additions_into_html(ct.PCOM_FOOTER_PLACEMENT)
        self.html = sp.pcom_remove_empty_lines(self.html)

    def process_postlists(self):
        self.postlists_info = sp.pcom_get_postlists_info(self.html_array,self.fileroot)

        (self.html_array,
        self.log) = sp.pcom_insert_postlist_wrapper(
                    html_array=self.html_array,
                    postlist_info=self.postlists_info,
                    outlog=self.log)

    def process_pagination(self):
        if (not self.is_template and not self.is_root
        and self.meta != ct.PCOM_NO_ENTRY and not self.meta[ct.PCOM_META_UNLISTED]):

            (self.html_array,
            self.pagination_info) = ls.pcom_get_pagination_info(
                                        html_array=self.html_array,
                                        postlist=self.postlist,
                                        postname=self.filename,
                                        fileroot=self.fileroot)

    def process_content_meta(self):
        self.content_meta_info = sp.pcom_get_content_meta_info(self.html_array)
        post = ls.pcom_find_post(self.postlist,self.filename)
        self.html_array = he.pcom_insert_content_meta_data(
                                    html_array=self.html_array,
                                    content_meta_info=self.content_meta_info,
                                    settings=self.site_settings,
                                    list_meta=self.list_meta,
                                    post=post,
                                    is_template=self.is_template)

    def insert_additions_into_html(self, placement):

        args = {'html': self.html,
        'settings': self.all_data['processed_settings'],
        'placement': placement,
        'js_name': self.postlist_constant_name,
        'fileroot': self.fileroot,
        'pagination_name': self.pagination_name,
        'pagination': self.pagination_info,
        'is_template': self.is_template,
        'is_search': self.is_search}

        default_additions = ''

        self.html = sp.pcom_insert_additions_into_html(args)

        (self.html,
        default_additions) = sp.pcom_insert_default_additions_into_html(args['settings'],self.html,placement)

        if placement == ct.PCOM_HEADER_PLACEMENT:
            self.site_settings['header_additions'].append(default_additions)

        if placement == ct.PCOM_FOOTER_PLACEMENT:
            self.site_settings['footer_additions'].append(default_additions)


    def get_raw_content(self):
        if (not self.is_search and self.meta != ct.PCOM_NO_ENTRY
        and not self.meta[ct.PCOM_META_UNLISTED]):
            self.raw_content = sp.pcom_create_raw_content(self.html, self.meta)

    # updates

    def update_postlist(self):
        # get type and url from file name
        # only update is meta not NONE
        if (self.meta != ct.PCOM_NO_ENTRY and not self.is_template
        and not self.is_root and not self.meta[ct.PCOM_META_UNLISTED]):

            url,type = sp.pcom_create_url(self.filename,self.meta)

            self.postlist = ls.pcom_update_postlist(
                                postlist=self.postlist,
                                postname=self.filename,
                                url=url,
                                meta=self.meta,
                                date_format=self.site_settings['date_format'],
                                type=type,
                                settings=self.site_settings)

    def update_categories(self):
        if (self.meta != ct.PCOM_NO_ENTRY and not self.is_template
        and not self.is_root and not self.meta[ct.PCOM_META_UNLISTED]):

            post = ls.pcom_find_post(self.postlist,self.filename)

            self.list_meta['categories'] = ls.pcom_update_categories_from_postlist_data(
                                                    categories=self.list_meta['categories'],
                                                    cat_list=post['categories'],
                                                    settings=self.site_settings,
                                                    type=post['type'])

    def update_authors(self):
        if (self.meta != ct.PCOM_NO_ENTRY and not self.is_template 
        and not self.is_root and not self.meta[ct.PCOM_META_UNLISTED]):

            post = ls.pcom_find_post(self.postlist,self.filename)

            self.list_meta['authors'] = ls.pcom_update_authors_from_postlist_data(
                                                    authors=self.list_meta['authors'],
                                                    author_list=post['authors'],
                                                    settings=self.site_settings)
