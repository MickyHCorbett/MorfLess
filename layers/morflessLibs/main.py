# main html
from libraries.string_processes import pcom_create_html_from_array
from libraries.string_processes import pcom_open_custom_class_div
from libraries.string_processes import pcom_filter_template
from libraries.string_processes import pcom_create_template_fileroot
from libraries.string_processes import pcom_get_template_key

from libraries.html_elements import pcom_insert_searchbar_for_search_page

from libraries import constants as ct
from libraries import schematics as sch
from libraries import globals as gb

# adds main and sidebar data

def polimorf_add_main(main_data,sidebar_data,meta_present,wrap,fileroot,settings,is_template,is_search):

    out_html = ct.PCOM_NO_ENTRY
    add_sidebar = ''
    template_tag = ''
    add_main = ''

    template_name = pcom_create_template_fileroot(fileroot,settings)

    if is_template and not is_search:

        template_tag = (ct.NL
        + pcom_open_custom_class_div("",sch.PM_MAIN_OUTER_OPEN) + ct.NL
        + pcom_open_custom_class_div("",sch.PM_MAIN_INNER_OPEN) + ct.NL
        + sch.PM_TEMPLATE_POSTLIST_INSERT + ct.NL
        + sch.PM_MAIN_INNER_CLOSE + ct.NL + sch.PM_MAIN_OUTER_CLOSE + ct.NL)

    if meta_present or is_template:

        if is_search:
            first_data = [pcom_insert_searchbar_for_search_page()]
            first_data.extend(main_data)
            main_data = first_data

        if main_data != ct.PCOM_NO_ENTRY:
            add_main = pcom_create_html_from_array(main_data) + template_tag
        elif:
            add_main = template_tag

        if sidebar_data != [ct.PCOM_NO_ENTRY]:
            # add outer and inner wrappers to start
            add_main = (ct.NL
            + pcom_open_custom_class_div("",sch.PM_MAIN_OUTER_OPEN) + ct.NL
            + pcom_open_custom_class_div("",sch.PM_MAIN_INNER_OPEN) + ct.NL
            + sch.PM_MAIN_WITH_SIDEBAR_MAIN_OPEN + ct.NL
            + add_main
            + sch.PM_MAIN_WITH_SIDEBAR_MAIN_CLOSE + ct.NL)

            # add outer and inner wrappers to end
            add_sidebar = (sch.PM_MAIN_WITH_SIDEBAR_SIDEBAR_OPEN + ct.NL
            + pcom_create_html_from_array(sidebar_data)
            + sch.PM_MAIN_WITH_SIDEBAR_SIDEBAR_CLOSE + ct.NL
            + sch.PM_MAIN_INNER_CLOSE + ct.NL + sch.PM_MAIN_OUTER_CLOSE + ct.NL)

        if add_main != '':
            if wrap:
                out_html = (sch.PM_MAIN_WRAP_OPEN
                + add_main
                + add_sidebar)
            else:
                out_html = add_main + add_sidebar

        # finalise section html tabs
        if sidebar_data != [ct.PCOM_NO_ENTRY]:
            out_html = out_html.replace(ct.PCOM_SECTION_SIDEBAR_TAB,ct.T2)
        else:
            out_html = out_html.replace(ct.PCOM_SECTION_SIDEBAR_TAB,'')



    return out_html
