# layers file
import libraries.morflessLibs as libs
# local boto3 based file
import searchContent_handlerLibrary as hl

import logging, os
import json
import urllib.parse

def handler(event, context):

    # set logs
    #logger = logging.getLogger()
    #logger.setLevel(logging.INFO)

    outputLog = {'search_term': '', 'search_content_info': []}
    response = {'search_term': '', 'content': ''}

    try:
        search_term = urllib.parse.unquote_plus(event['pathParameters']['search'])

        response['search_term'] = search_term
        outputLog['search_term'] = search_term
        response['content'],outputLog = hl.process_search_request(search_term,outputLog)
    except:
        outputLog['error'] = 'Path parameters search term incorrect'

    # add data to log
    #logger.info(outputLog)

    print('Log: {}'.format(json.dumps(outputLog)))

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps(response)
    }
