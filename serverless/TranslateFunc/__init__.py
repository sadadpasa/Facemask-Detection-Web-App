import logging

import azure.functions as func


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
        return func.HttpResponse(f"this is the result")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a text, langFrom, langTo in the request body to get the result",
             status_code=200
        )
