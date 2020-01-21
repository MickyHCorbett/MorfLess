# main html
from libraries.string_processes import pcom_create_html_from_array

from libraries import constants as ct
from libraries import schematics as sch

# adds before and after data

def polimorf_add_before(before_data,meta_present):

    out_html = ct.PCOM_NO_ENTRY

    if meta_present:

        add_data = pcom_create_html_from_array(before_data)

        if add_data != '':
            out_html = sch.PM_MAIN_WRAP_OPEN + add_data + ct.NL

    return out_html.rstrip()


def polimorf_add_after(after_data,meta_present,wrap):

    out_html = ct.PCOM_NO_ENTRY

    if meta_present:

        add_data = pcom_create_html_from_array(after_data)

        if add_data != '':
            if wrap:
                out_html = (sch.PM_MAIN_WRAP_OPEN
                + add_data
                + sch.PM_MAIN_WRAP_CLOSE)
            else:
                out_html = add_data + sch.PM_MAIN_WRAP_CLOSE

    return out_html.lstrip()
