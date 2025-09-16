import requests
import json

def empty_dictionary():
    return {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None,
    }

def emotion_detector(text_to_analyse):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/' \
            'watson.runtime.nlp.v1/NlpService/EmotionPredict'

    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(URL, json = myobj, headers=headers)

    if response.status_code == 400:
        return empty_dictionary()

    formatted_response = json.loads(response.text)

    response_as_dict = formatted_response['emotionPredictions'][0]['emotion']
    response_as_dict['dominant_emotion'] = max(response_as_dict, key=response_as_dict.get)

    return response_as_dict