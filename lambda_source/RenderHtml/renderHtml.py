# layers file
import libraries.morflessLibs as libs
# local boto3 based file
import renderHtml_handlerLibrary as hl

import logging, os

# define project globals

dep_file = libs.constants.PCOM_REQ_FILE_DEPENDENCIES

sourcebucket= os.environ['SOURCE_BUCKET']
listbucket = os.environ["LIST_BUCKET"]

def handler(event, context):

    # set logs
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    outputLog = {'inserts_processed': [],
    'search_content': [],
    'files_processed': 'N',
    'default_header_additions': [],
    'default_footer_additions': [],
    'file_header_additions': [],
    'file_footer_additions': []}

    bucket_request = event["detail"]["requestParameters"]["bucketName"]

    if bucket_request == sourcebucket:

        fr = event["detail"]["requestParameters"]["key"]

        dependencies,outputLog = hl.process_json_files(dep_file,listbucket,outputLog)

        # if file is post or page - individual file is processed
        # if file is an insert or settings.txt dependencies are checked to get a list
        # of all files to be changed

        if fr.upper().find('.HTML') == -1 and fr.upper().find('.JSON') == -1:

            filelist,outputLog = hl.determine_upload_type(fr,dependencies,outputLog)

            # two types of trigger - put and delete

            if  event["detail"]["eventName"] == "PutObject":

                outputLog = hl.process_uploaded_files(filelist,dependencies,outputLog)

            if event["detail"]["eventName"] == "DeleteObject":

                outputLog = hl.delete_files(filelist,dependencies,outputLog)


    # add data to log
    logger.info(outputLog)


    return {
        'statusCode': 200,
        'body': outputLog
    }
