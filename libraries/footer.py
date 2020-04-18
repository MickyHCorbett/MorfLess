# header html
from libraries.string_processes import pcom_create_html_from_array

from libraries import constants as ct
from libraries import schematics as sch

# adds footer

def polimorf_add_footer(footer_data,meta_present):

    out_html = ct.PCOM_NO_ENTRY

    if meta_present:

        add_footer = pcom_create_html_from_array(footer_data)
        if (add_footer):
            out_html = (sch.PM_FOOTER_WRAP_OPEN + ct.NL
            + sch.PM_FOOTER_OUTER_OPEN + ct.NL
            + sch.PM_FOOTER_INNER_OPEN + ct.NL
            + add_footer
            + sch.PM_FOOTER_INNER_CLOSE + ct.NL
            + sch.PM_FOOTER_OUTER_CLOSE + ct.NL
            + sch.PM_FOOTER_WRAP_CLOSE)

    return out_html
