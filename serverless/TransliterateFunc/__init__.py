import json
import logging

import azure.functions as func
from . import transliterate


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        req_body = req.get_json()
    except ValueError:
        pass
    else:
        text = req_body.get('text')
        fromScript = req_body.get('fromScript')
        toScript = req_body.get('toScript')
        lang = req_body.get('lang')

    if text and fromScript and toScript and lang :
        result = transliterate.transliterateText(text, lang, fromScript, toScript)
        return func.HttpResponse(json.dumps(result, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a text, lang, fromScript, toScript in the request body to get the result",
             status_code=200
        )
