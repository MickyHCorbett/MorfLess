"""
read file content into string
file is in fixtures bucket
"""
import os, sys

def get_file_content(filename):

    content = ''
    curr_dir = os.getcwd()
    fullfile = os.path.join(curr_dir,filename)

    try:
        with open(fullfile) as file:
            for line in file:
                content += line
    except:
        print("Can't read {}".format(filename))

    return content
