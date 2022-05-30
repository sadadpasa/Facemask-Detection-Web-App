import json
import logging
import uuid
from datetime import datetime

import azure.functions as func
from . import translate

FUNC_NAME = 'TRANSLATE_TEXT'
def main(req: func.HttpRequest, outputDocument: func.Out[func.Document]) -> func.HttpResponse:
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
        newdocs = func.DocumentList() 
        newproduct_dict = {
            "id": str(uuid.uuid4()),
            "method": FUNC_NAME,
            "req": req_body,
            "res": result,
            "createdAt": datetime.now().strftime('%m/%d/%Y, %H:%M:%S')
        }
        newdocs.append(func.Document.from_dict(newproduct_dict))
        outputDocument.set(newdocs)
        return func.HttpResponse(json.dumps(result, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a text, langFrom, langTo in the request body to get the result",
             status_code=200
        )
