import logging
from . import translateFile
import azure.functions as func
from azure.storage.blob import BlobServiceClient, BlobClient
from datetime import datetime
import uuid
import os

FUNC_NAME = 'TRANSLATE_FILE'
def main(req: func.HttpRequest, outputDocument: func.Out[func.Document]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    connectionString = os.environ["CONTAINER_CONNECTION_STRING"]
    containerName = os.environ["CONTAINER_NAME"]
    try:
        file = req.files.get('file')
        langTo = req.params.get('langTo')
        filename = datetime.now().strftime('%m-%d-%Y %H:%M:%S') + file.filename
        filetype = file.filename.split('.')[-1]
        logging.info(filename)

        blob_service_client = BlobServiceClient.from_connection_string(conn_str = connectionString)
        blob_client = blob_service_client.get_blob_client(container = containerName, blob = filename)
        blob_client.upload_blob(file)

        translateFile.translateFileFunc(langTo)

        resultUrl = 'https://seniorprojectstorage.blob.core.windows.net/targetfile/' + filename

        newdocs = func.DocumentList() 
        newproduct_dict = {
            "id": str(uuid.uuid4()),
            "method": FUNC_NAME,
            "req": {
                "filename": filename,
                "filetype": filetype,
                "langTo": langTo
            },
            "res": {
                "result": resultUrl
            },
            "createdAt": datetime.now().strftime('%m/%d/%Y, %H:%M:%S')
        }

        newdocs.append(func.Document.from_dict(newproduct_dict))
        outputDocument.set(newdocs)
        return func.HttpResponse(
            resultUrl,
            status_code=200
        )

    except:
        pass

    