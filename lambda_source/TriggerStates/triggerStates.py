import json
import logging, os
import boto3
import datetime

def handler(event, context):

    # set logs
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    outputLog = {'receivedEvents': [], 'triggerEvents': [],
    'stepfunction_starts': [], 'stepfunction_non_starts': [], 'error': []}

    step_function_name = os.environ['STEP_FUNCTION_NAME']
    s3client = boto3.client('stepfunctions')

    triggerEvent = { 'detail':
        { 'requestParameters':
            { 'bucketName': '', 'key': '' },
        'eventName': '' } }

    if 'Records' in event:

        if type(event['Records']) is list:

            for record in event['Records']:

                try:
                    # condition event
                    trigger_states = False
                    outputLog['receivedEvents'].append(record)

                    triggerEvent['detail']['requestParameters']['bucketName'] = record['s3']['bucket']['name']
                    triggerEvent['detail']['requestParameters']['key'] = record['s3']['object']['key']
                    triggerEvent['detail']['eventName'] = ''

                    if record['eventName'] == "ObjectCreated:Put":
                        triggerEvent['detail']['eventName'] = 'PutObject'
                        trigger_states = True

                    if record['eventName'] == "ObjectRemoved:Delete":
                        triggerEvent['detail']['eventName'] = 'DeleteObject'
                        trigger_states = True

                    outputLog['triggerEvents'].append(triggerEvent)

                    if trigger_states:
                        timemarker = datetime.datetime.now().strftime("%d %B %Y-%H:%M:%S")
                        trigger_event_json = json.dumps(triggerEvent)
                        try:
                            startresponse = s3client.start_execution(
                                stateMachineArn=step_function_name,
                                input=trigger_event_json
                            )
                            message = step_function_name + ' started on ' + timemarker
                            outputLog['stepfunction_starts'].append(message)
                        except:
                            message = step_function_name + ' not started on ' + timemarker
                            outputLog['stepfunction_non_starts'].append(message)

                except:
                    outputLog['error'].append('Record not correctly formatted')

        else: 
            outputLog['error'].append('Records not a list')
    else:
        outputLog['error'].append('No Records in event')


    # add data to log
    logger.info(outputLog)

    return {
        'statusCode': 200,
        'body': outputLog
    }
