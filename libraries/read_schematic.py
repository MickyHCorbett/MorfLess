# read schematic functions
from libraries import constants as ct
from libraries import globals as gb
from libraries import schematics as sch
from libraries import meta_elements as me
from libraries import html_elements as he
from libraries import string_processes as sp
from libraries import header
from libraries import main
from libraries import before_after
from libraries import footer
from libraries import lists as ls

def get_settings(content):

    type_none = ct.PCOM_NO_ENTRY
    out = sp.pcom_build_dictionary(gb.DEFAULT_SETTINGS)
    settings = sp.pcom_build_dictionary(gb.DEFAULT_SETTINGS)
    args = sp.pcom_build_dictionary(gb.DEFAULT_GET_FIRST_COMMAND_ARGS)

    schematic_content = pcom_get_schematic_tags(content)

    out = me.pcom_process_settings_meta_syntax(schematic_content['meta'],out)

    default_header,settings = polimorf_process_settings_schematic(
                                schematic=schematic_content['header'],
                                args=args,
                                placement=ct.PCOM_SETTINGS_HEADER,
                                type=type_none,
                                settings=out)

    default_before,settings = polimorf_process_settings_schematic(
                                schematic=schematic_content['before'],
                                args=args,
                                placement=ct.PCOM_SETTINGS_BEFORE,
                                type=type_none,
                                settings=out)

    default_main,settings = polimorf_process_settings_schematic(
                                schematic=schematic_content['main'],
                                args=args,
                                placement=ct.PCOM_SETTINGS_MAIN,
                                type=type_none,
                                settings=out)

    default_after,settings = polimorf_process_settings_schematic(
                                schematic=schematic_content['after'],
                                args=args,
                                placement=ct.PCOM_SETTINGS_AFTER,
                                type=type_none,
                                settings=out)

    default_after,settings = polimorf_process_settings_schematic(
                                schematic=schematic_content['after'],
                                args=args,
                                placement=ct.PCOM_SETTINGS_AFTER,
                                type=type_none,
                                settings=out)

    default_sidebar,settings = polimorf_process_settings_schematic(
                                schematic=schematic_content['sidebar'],
                                args=args,
                                placement=ct.PCOM_SETTINGS_SIDEBAR,
                                type=type_none,
                                settings=out)

    default_footer,settings = polimorf_process_settings_schematic(
                                schematic=schematic_content['footer'],
                                args=args,
                                placement=ct.PCOM_SETTINGS_FOOTER,
                                type=type_none,
                                settings=out)

    default_header_additions = polimorf_process_additions_schematic(
                                    schematic=schematic_content['header'],
                                    args=args,
                                    placement=ct.PCOM_SETTINGS_HEADER,
                                    type=type_none)

    default_footer_additions = polimorf_process_additions_schematic(
                                    schematic=schematic_content['footer'],
                                    args=args,
                                    placement=ct.PCOM_SETTINGS_FOOTER,
                                    type=type_none)

    out['default_header'] = sp.pcom_create_html_from_array(default_header)
    out['default_before'] = sp.pcom_create_html_from_array(default_before)
    out['default_main'] = sp.pcom_create_html_from_array(default_main)
    out['default_after'] = sp.pcom_create_html_from_array(default_after)
    out['default_sidebar'] = sp.pcom_create_html_from_array(default_sidebar)
    out['default_footer'] = sp.pcom_create_html_from_array(default_footer)

    if default_header_additions and default_header_additions != ct.PCOM_NO_ENTRY:
        out['default_header_additions'] = sp.pcom_create_html_from_array(default_header_additions)
    if default_footer_additions and default_footer_additions != ct.PCOM_NO_ENTRY:
        out['default_footer_additions'] = sp.pcom_create_html_from_array(default_footer_additions)

    return out


def polimorf_determine_schematic_reference(content, settings):
    out = {}
    # get schematic content per tag
    schematic_content = pcom_get_schematic_tags(content)
    main_only = ct.PCOM_MAIN_PLACEMENT
    main_side = ct.PCOM_MAIN_WITH_SIDEBAR_PLACEMENT
    sidebar_side = ct.PCOM_SIDEBAR_PLACEMENT
    type_before = ct.PCOM_BEFORE_TYPE
    type_after = ct.PCOM_AFTER_TYPE
    type_none = ct.PCOM_NO_ENTRY

    # reset postlist present
    settings['postlist_present'] = False

    # if not meta data return meta tag only
    out['meta'] = schematic_content['meta']
    if schematic_content['meta'] != ct.PCOM_NO_ENTRY:
        # process header content
        args = sp.pcom_build_dictionary(gb.DEFAULT_GET_FIRST_COMMAND_ARGS)
        out['meta'] = me.pcom_process_meta_syntax(schematic_content['meta'])

        out['header'],settings = polimorf_process_schematic(
                                        schematic=schematic_content['header'],
                                        args=args,
                                        placement=ct.PCOM_HEADER_PLACEMENT,
                                        type=ct.PCOM_NO_ENTRY,
                                        settings=settings)

        out['before'],settings = polimorf_process_schematic(
                                        schematic=schematic_content['before'],
                                        args=args,
                                        placement=ct.PCOM_MAIN_PLACEMENT,
                                        type=ct.PCOM_BEFORE_TYPE,
                                        settings=settings)

        out['after'],settings = polimorf_process_schematic(
                                        schematic=schematic_content['after'],
                                        args=args,
                                        placement=ct.PCOM_MAIN_PLACEMENT,
                                        type=ct.PCOM_AFTER_TYPE,
                                        settings=settings)

        # main and sidebar

        if (schematic_content['sidebar'] != ct.PCOM_NO_ENTRY):

            out['main'],settings = polimorf_process_schematic(
                                            schematic=schematic_content['main'],
                                            args=args,
                                            placement=ct.PCOM_MAIN_WITH_SIDEBAR_PLACEMENT,
                                            type=ct.PCOM_NO_ENTRY,
                                            settings=settings)

            out['sidebar'],settings = polimorf_process_schematic(
                                            schematic=schematic_content['sidebar'],
                                            args=args,
                                            placement=ct.PCOM_SIDEBAR_PLACEMENT,
                                            type=ct.PCOM_NO_ENTRY,
                                            settings=settings)

        else:

            out['main'],settings = polimorf_process_schematic(
                                            schematic=schematic_content['main'],
                                            args=args,
                                            placement=ct.PCOM_MAIN_PLACEMENT,
                                            type=ct.PCOM_NO_ENTRY,
                                            settings=settings)

            out['sidebar'] = [ct.PCOM_NO_ENTRY]


        out['footer'],settings = polimorf_process_schematic(
                                        schematic=schematic_content['footer'],
                                        args=args,
                                        placement=ct.PCOM_FOOTER_PLACEMENT,
                                        type=ct.PCOM_NO_ENTRY,
                                        settings=settings)


    return {'processed': out, 'schematic_content': schematic_content, 'processed_settings': settings}


#
# Parse schematic using tags. Function returns schematic sections
# that are used to set globals for further schematic processing
#

def pcom_get_schematic_tags(format):
    # function returns header, main and schematic as an array of strings
    meta_tag = ct.PCOM_META_TAG
    header_tag = ct.PCOM_HEADER_SCHEMATIC_TAG
    main_tag = ct.PCOM_MAIN_SCHEMATIC_TAG
    footer_tag = ct.PCOM_FOOTER_SCHEMATIC_TAG
    sidebar_tag = ct.PCOM_SIDEBAR_SCHEMATIC_TAG
    before_tag = ct.PCOM_BEFORE_MAIN_SCHEMATIC_TAG
    after_tag = ct.PCOM_AFTER_MAIN_SCHEMATIC_TAG
    #
    meta_tag_offset = len(meta_tag)
    header_tag_offset = len(header_tag)
    main_tag_offset = len(main_tag)
    footer_tag_offset = len(footer_tag)
    # set up array for output - defaults are empty
    out_formats = sp.pcom_build_dictionary(gb.DEFAULT_SCHEMATICS)
    #
    # search for first #
    meta_tag_pos = format.find(meta_tag)
    header_tag_pos = format.find(header_tag)
    main_tag_pos = format.find(main_tag)
    footer_tag_pos = format.find(footer_tag)
    #
    # meta tag must be there
    if (meta_tag_pos) > -1:

        if ( ( footer_tag_pos > main_tag_pos) and
            ( main_tag_pos > header_tag_pos) and
            (header_tag_pos > meta_tag_pos) ):

            out_formats['meta'] = format[meta_tag_pos+meta_tag_offset : header_tag_pos]
            out_formats['header'] = format[header_tag_pos+header_tag_offset : main_tag_pos]
            out_formats['main'] = format[main_tag_pos+main_tag_offset : footer_tag_pos]
            out_formats['footer'] = format[footer_tag_pos+footer_tag_offset:]

        # ================
        # CONDITIONAL tags
        # ================
        # process header to see if there is a BEFORE tag
        before_search = sp.pcom_get_strings_syntax_separator(out_formats['header'],before_tag,True)
        if before_search['command_found']:
            out_formats['before_found'] = True
            out_formats['header'] = before_search['syntax_before']
            out_formats['before'] = before_search['syntax_after']

        # process main to see if there is a SIDEBAR tag
        sidebar_search = sp.pcom_get_strings_syntax_separator(out_formats['main'],sidebar_tag,True)
        #
        if sidebar_search['command_found']:
            out_formats['sidebar_found'] = True
            out_formats['main'] = sidebar_search['syntax_before']
            out_formats['sidebar'] = sidebar_search['syntax_after']

        # process SIDEBAR for AFTER tag
        after_search = sp.pcom_get_strings_syntax_separator(out_formats['sidebar'],after_tag,True)
        if after_search['command_found']:
            out_formats['after_found'] = True
            out_formats['sidebar'] = after_search['syntax_before']
            out_formats['after'] = after_search['syntax_after']

        else:
            # process for AFTER tag
            after_search = sp.pcom_get_strings_syntax_separator(out_formats['main'],after_tag,True)
            if after_search['command_found']:
                out_formats['after_found'] = True
                out_formats['main'] = after_search['syntax_before']
                out_formats['after'] = after_search['syntax_after']
    #
    return out_formats

#
# General schematic command loop
# Uses global list of commands for reference
#
#
def polimorf_process_schematic(schematic,args,placement,type,settings):
    # default output
    # copy for additions loop
    schematic_orig = schematic

    if schematic == ct.PCOM_NO_ENTRY:
        out = [ct.PCOM_NO_ENTRY]
    else:
        out = []
        # set command data array
        schematic_commands = sp.pcom_build_dictionary(gb.DEFAULT_GET_FIRST_COMMAND_OUTPUTS)
        schematic_commands['next_command'] = ""

        # loop over schematic data - command,syntax,placement,type,settings

        while schematic_commands['next_command'] != ct.PCOM_NO_ENTRY:
            schematic_commands = sp.pcom_get_first_command(schematic,args)
            syntax,settings = he.pcom_command_selection(
                                command=schematic_commands['command'],
                                syntax=schematic_commands['command_syntax'],
                                placement=placement,
                                type=type,
                                settings=settings)

            schematic = schematic_commands['next_command']
            # append to out data
            command = schematic_commands['command']
            out.append(syntax)

        # loop over additions
        # set command data array
        schematic = schematic_orig
        type = ct.PCOM_NO_ENTRY
        schematic_commands = sp.pcom_build_dictionary(gb.DEFAULT_GET_FIRST_COMMAND_OUTPUTS)
        schematic_commands['next_command'] = ""

        while schematic_commands['next_command'] != ct.PCOM_NO_ENTRY:
            schematic_commands = sp.pcom_get_first_command(schematic,args)
            settings = he.pcom_addition_selection(
                                command=schematic_commands['command'],
                                syntax=schematic_commands['command_syntax'],
                                placement=placement,
                                type=type,
                                settings=settings)

            schematic = schematic_commands['next_command']
            # append to out data
            command = schematic_commands['command']

    return out,settings

def polimorf_process_settings_schematic(schematic,args,placement,type,settings):
    # default output
    # convert placements to those used in parsing the html
    placement_for_html = pcom_determine_placement(placement)
    schematic_orig = schematic

    if schematic == ct.PCOM_NO_ENTRY:
        out = [ct.PCOM_NO_ENTRY]
    else:
        out = []
        # set command data array
        schematic_commands = sp.pcom_build_dictionary(gb.DEFAULT_GET_FIRST_COMMAND_OUTPUTS)
        schematic_commands['next_command'] = ""

        # loop over schematic data
        while schematic_commands['next_command'] != ct.PCOM_NO_ENTRY:
            schematic_commands = sp.pcom_get_first_command(schematic,args)

            # if command is default replace content with default schematic and reprocess
            if schematic_commands['command'] == ct.PCOM_DEFAULT_COMMAND:

                schematic = he.pcom_use_settings_defaults(placement, settings)
                schematic += schematic_commands['next_command']
                schematic_commands = sp.pcom_get_first_command(schematic,args)

            syntax,settings = he.pcom_command_selection(
                                command=schematic_commands['command'],
                                syntax=schematic_commands['command_syntax'],
                                placement=placement_for_html,
                                type=type,
                                settings=settings)

            schematic = schematic_commands['next_command']
            # append to out data
            command = schematic_commands['command']
            out.append(syntax)

    return out,settings


def polimorf_process_additions_schematic(schematic,args,placement,type):
    # default output
    # convert placements to those used in parsing the html
    placement_for_html = pcom_determine_placement(placement)

    local_settings = {'header_additions': [],
    'footer_additions': []}

    if schematic == ct.PCOM_NO_ENTRY:
        out = ct.PCOM_NO_ENTRY
    else:
        out = ''
        # loop over additions
        # set command data array
        type = ct.PCOM_NO_ENTRY
        schematic_commands = sp.pcom_build_dictionary(gb.DEFAULT_GET_FIRST_COMMAND_OUTPUTS)
        schematic_commands['next_command'] = ""

        while schematic_commands['next_command'] != ct.PCOM_NO_ENTRY:
            schematic_commands = sp.pcom_get_first_command(schematic,args)
            local_settings = he.pcom_addition_selection(
                        command=schematic_commands['command'],
                        syntax=schematic_commands['command_syntax'],
                        placement=placement_for_html,
                        type=type,
                        settings=local_settings)

            schematic = schematic_commands['next_command']
            # append to out data
            command = schematic_commands['command']

        if placement == ct.PCOM_SETTINGS_HEADER:
            out = local_settings['header_additions']
        if placement == ct.PCOM_SETTINGS_FOOTER:
            out = local_settings['footer_additions']

    return out

def pcom_determine_placement(placement):
    # converts from settings placement
    if placement == ct.PCOM_SETTINGS_HEADER:
        placement_out = ct.PCOM_HEADER_PLACEMENT
    if placement == ct.PCOM_SETTINGS_BEFORE:
        placement_out = ct.PCOM_MAIN_PLACEMENT
    if placement == ct.PCOM_SETTINGS_MAIN:
        placement_out = ct.PCOM_MAIN_PLACEMENT
    if placement == ct.PCOM_SETTINGS_AFTER:
        placement_out = ct.PCOM_MAIN_PLACEMENT
    if placement == ct.PCOM_SETTINGS_SIDEBAR:
        placement_out = ct.PCOM_SIDEBAR_PLACEMENT
    if placement == ct.PCOM_SETTINGS_FOOTER:
        placement_out = ct.PCOM_FOOTER_PLACEMENT

    return placement_out

# output html from processed schematic
def polimorf_process_schematic_sections(data, settings,filename,fileroot):
    # data is a dictionary with the different sections
    # if no meta data return no entry
    meta_present = False
    out_html = ct.PCOM_NO_ENTRY
    add_main_wrap = False
    add_after_wrap = False
    no_before = False
    no_main = False
    is_template,is_search = sp.pcom_filter_template(fileroot,settings)

    if data['meta'] != ct.PCOM_NO_ENTRY:
        meta_present = True
        out_html = ''
        out_html = header.polimorf_head_and_title(meta_present,settings,data['meta'],filename,fileroot)

        if data['header'] != [ct.PCOM_NO_ENTRY]:
            out_html += header.polimorf_add_header(data['header'],meta_present) + ct.NL

        if data['before'] != [ct.PCOM_NO_ENTRY]:
            out_html += before_after.polimorf_add_before(data['before'],data['sidebar'],meta_present)
        else:
            add_main_wrap = True
            no_before = True

        if data['main'] != [ct.PCOM_NO_ENTRY] or is_template:
            out_html += main.polimorf_add_main(
                            main_data=data['main'],
                            sidebar_data=data['sidebar'],
                            meta_present=meta_present,
                            wrap=add_main_wrap,
                            fileroot=fileroot,
                            settings=settings,
                            is_template=is_template,
                            is_search=is_search)
        else:
            add_after_wrap = True
            no_main = True

        if data['after'] != [ct.PCOM_NO_ENTRY]:
            out_html += (before_after.polimorf_add_after(
                            after_data=data['after'],
                            sidebar_data=data['sidebar'],
                            meta_present=meta_present,
                            wrap=add_after_wrap) + ct.NL)
        else:
            if no_before and no_main:
                out_html += sch.PM_MAIN_WRAP_OPEN + ct.NL + sch.PM_MAIN_WRAP_CLOSE + ct.NL
            else:
                out_html += sch.PM_MAIN_WRAP_CLOSE + ct.NL

        if data['footer'] != [ct.PCOM_NO_ENTRY]:
            out_html += footer.polimorf_add_footer(data['footer'],meta_present)

        # close body and html tags
        out_html += sch.DEFAULT_FOOTER_SCRIPTS
        out_html += sch.PM_CLOSE_BODY_TAG
        out_html += sch.PM_CLOSE_HTML_TAG


    return out_html

def pcom_process_inserts(html_array,insert_info,outlog,site_settings,filename,dependencies):

    args = sp.pcom_build_dictionary(gb.DEFAULT_GET_FIRST_COMMAND_ARGS)

    # create local list of inserts from dependencies
    local_deps = ls.pcom_get_dependency(dependencies,filename)
    valid_inserts = []

    for insert in insert_info:

        key_ref = insert['filename']

        if insert['valid_entry'] == ct.PCOM_VALID_ENTRY:
            # process insert
            type_none = ct.PCOM_NO_ENTRY
            insert_out_data,site_settings = polimorf_process_schematic(
                                                schematic=insert['content'],
                                                args=args,
                                                placement=insert['placement'],
                                                type=type_none,
                                                settings=site_settings)
            insert_out = sp.pcom_create_html_from_array(insert_out_data)

            # put back in content
            html_array[insert['index']] = insert_out
            # update dependencies - no change if insert file is already listed
            dependencies = ls.pcom_update_dependencies(dependencies,filename,key_ref)
            # update local record of inserts processed
            valid_inserts.append(key_ref)
        else:
            # delete line from html array
            key_ref += ':No such file'
            # put empty string
            html_array[insert['index']] = ''

        # add log entry
        inserts_processed_string = filename + '--' + key_ref + '-PLACEMENT=' + insert['placement']
        outlog['inserts_processed'].append(inserts_processed_string)

    # once inserts are processed - check if all dependencies where used.
    dependencies = ls.pcom_post_process_dependencies(dependencies,filename,valid_inserts)

    # if settings.txt is set from default commands then update dependencies
    if ct.PCOM_REQ_FILE_SETTINGS in site_settings['add_settings_to_dependencies']:
        # update dependencies - no change if insert file is already listed
        key_ref = ct.PCOM_REQ_FILE_SETTINGS
        dependencies = ls.pcom_update_dependencies(dependencies,filename,key_ref)

    #log_detail = 'Inserts for {} found: {}'.format(filename,valid_inserts)
    #outlog['valid_inserts'] = log_detail

    return html_array,outlog,site_settings,dependencies
