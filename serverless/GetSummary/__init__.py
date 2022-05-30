import logging

import azure.functions as func
import json


def main(req: func.HttpRequest, doc:func.DocumentList) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    translate_from_list = {}
    translate_to_list = {}
    translate_doc_filetype = {}
    translate_doc_lang = {}

    
    for log in doc:
        if log['method'] == 'TRANSLATE_TEXT':

            if log['req']['langFrom'] in translate_from_list:
                translate_from_list[log['req']['langFrom']] = translate_from_list[log['req']['langFrom']]+1
            else:
                translate_from_list[log['req']['langFrom']] = 1
            
            for langTo in log['req']['langTo']:
                if langTo in translate_to_list:
                    translate_to_list[langTo] = translate_to_list[langTo]+1
                else:
                    translate_to_list[langTo] = 1

        elif log['method'] == 'TRANSLATE_FILE':

            if log['req']['filetype'] in translate_doc_filetype:
                translate_doc_filetype[log['req']['filetype']] = translate_doc_filetype[log['req']['filetype']]+1
            else:
                translate_doc_filetype[log['req']['filetype']] = 1
            
            if log['req']['langTo'] in translate_doc_lang:
                translate_doc_lang[log['req']['langTo']] = translate_doc_lang[log['req']['langTo']]+1
            else:
                translate_doc_lang[log['req']['langTo']] = 1


    response = {
        "translateText": {
            "from": translate_from_list,
            "to": translate_to_list
        }, 
        "translateDoc": {
            "filetype": translate_doc_filetype,
            "langTo": translate_doc_lang
        }
    }

    return func.HttpResponse(
            json.dumps(response),
            status_code=200,
            mimetype="application/json"            
    )

    '''
    logs_json = []

    for log in doc:
        log_json = {
           "method": log['method'],
           "createdAt": log['createdAt']
        }
        logs_json.append(log_json)

    return func.HttpResponse(
            json.dumps(logs_json),
            status_code=200,
            mimetype="application/json"            
    )
    '''
