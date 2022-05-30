import requests, os

def translateFileFunc(lang):
    endpoint = os.environ["DOCUMENT_TRANSLATION_ENDPOINT"]
    key = os.environ["DOCUMENT_TRANSLATION_KEY"]
    path = '/batches'
    constructed_url = endpoint + path

    payload= {
        "inputs": [
            {
                "source": {
                    "sourceUrl": os.environ["DOCUMENT_SOURCE_URL"],
                    "storageSource": "AzureBlob",
                },
                "targets": [
                    {
                        "targetUrl": os.environ["DOCUMENT_TARGET_URL"],
                        "storageSource": "AzureBlob",
                        "category": "general",
                        "language": lang
                    }
                ]
            }
        ]
    }

    headers = {
        'Ocp-Apim-Subscription-Key': key,
        'Content-Type': 'application/json'
    }

    response = requests.post(constructed_url, headers=headers, json=payload)

    return(f'response status code: {response.status_code}\nresponse status: {response.reason}\nresponse headers: {response.headers}')