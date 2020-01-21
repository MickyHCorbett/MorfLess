# header html

from libraries.string_processes import pcom_create_html_from_array
from libraries.string_processes import pcom_filter_template
from libraries.string_processes import pcom_create_template_fileroot

from libraries import constants as ct
from libraries import globals as gb
from libraries import meta_defaults as md
from libraries import schematics as sch

#
# Sets up head
#
def polimorf_head_and_title(meta_present,settings,meta,filename,fileroot):
    # from settings and other processes
    add_page_title = settings['site_title']
    is_template,is_search = pcom_filter_template(fileroot,settings)
    template_name = pcom_create_template_fileroot(fileroot,settings)

    if meta['page_title'] != md.DEFAULT_PAGE_TITLE:
        if is_template and not is_search:
            add_page_title = template_name.capitalize() + sch.PM_TEMPLATE_TITLE_REPLACEMENT
        elif is_search:
            add_page_title = template_name.capitalize()
        else:
            add_page_title = meta['page_title']

    description = settings['site_description']
    if meta['page_description'] != md.DEFAULT_PAGE_DESCRIPTION:
        if is_template and not is_search:
            description = template_name.capitalize() + sch.PM_TEMPLATE_DESCRIPTION_REPLACEMENT
        elif is_search:
            description = template_name.capitalize()
        else:
            description = meta['page_description'].replace('"','')

    add_description = '"' + description + '"'

    out_html = ct.PCOM_NO_ENTRY

    if meta_present:
        out_html = (sch.PM_HTML_OPEN_DECLARATION
        + ct.T1 + """<title>""" + add_page_title + """</title>""" + ct.NL
        + ct.T1 + """<link rel="shortcut icon" type"image/x-icon" href="/images/favicon.ico" />""" + ct.NL
        + ct.T1 + """<meta name="viewport" content="width=device-width, initial-scale=1">""" + ct.NL
        + ct.T1 + """<meta name="description" content=""" + add_description + """>""" + ct.NL
        + ct.T1 + """<link rel="stylesheet" href="/extras/font-awesome-4.7.0/css/font-awesome.min.css" type="text/css" media="screen">""" + ct.NL
        + ct.T1 + """<link rel="stylesheet" href="/fonts/Faustina-FontFace.css" type="text/css" media="screen">""" + ct.NL
        + ct.T1 + """<link rel="stylesheet" href="/css/normalize.css" type="text/css" media="screen">""" + ct.NL
        + ct.T1 + """<link rel="stylesheet" href="/css/style-core.css" type="text/css" media="screen">""" + ct.NL
        + ct.T1 + """<link rel="stylesheet" href="/css/style-responsive.css" type="text/css" media="screen">""" + ct.NL
        + ct.T1 + sch.HEADER_ADDITIONS_START + ct.NL
        + ct.T1 + sch.HEADER_ADDITIONS_END + ct.NL +
        """</head>""" + ct.NL)

    return out_html

def polimorf_add_header(header_data,meta_present):

    out_html = ct.PCOM_NO_ENTRY

    if meta_present:

        add_header = pcom_create_html_from_array(header_data)

        if (add_header):
            out_html = (sch.PM_HEADER_WRAP_OPEN + ct.NL
            + sch.PM_HEADER_OUTER_OPEN + ct.NL
            + sch.PM_HEADER_INNER_OPEN + ct.NL
            + add_header
            + sch.PM_HEADER_INNER_CLOSE + ct.NL
            + sch.PM_HEADER_OUTER_CLOSE + ct.NL
            + sch.PM_HEADER_WRAP_CLOSE)

    return out_html
