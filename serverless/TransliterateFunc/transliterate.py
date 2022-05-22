import requests, uuid, os

# Add your key and endpoint
key = os.environ["TRANSLATOR_KEY"]
endpoint = "https://api.cognitive.microsofttranslator.com"

# Add your location, also known as region. The default is global.
# This is required if using a Cognitive Services resource.
location = os.environ["LOCATION"]

path = '/transliterate'
constructed_url = endpoint + path

headers = {
    'Ocp-Apim-Subscription-Key': key,
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

def transliterateText(text, lang, fromScript, toScript):
    params = {
        'api-version': '3.0',
        'language': lang,
        'fromScript': fromScript,
        'toScript': toScript
    }

    # You can pass more than one object in body.
    body = [{
        'text': text
    }]

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()
    return response