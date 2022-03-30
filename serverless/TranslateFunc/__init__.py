import json
import logging

import azure.functions as func
from . import translate


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        req_body = req.get_json()
    except ValueError:
        pass
    else:
        text = req_body.get('text')
        langFrom = req_body.get('langFrom')
        langTo = req_body.get('langTo')

    if text and langFrom and langTo :
        result = translate.translateText(text, langFrom, langTo)
        return func.HttpResponse(json.dumps(result, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a text, langFrom, langTo in the request body to get the result",
             status_code=200
        )
