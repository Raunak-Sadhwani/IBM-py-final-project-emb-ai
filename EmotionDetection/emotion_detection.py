import requests
import json

def emotion_detector(text_to_analyse):
    if not text_to_analyse:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": {"text": text_to_analyse}}
    response = requests.post(url, json=myobj, headers=header)
    response_dict = response.json()
    
    emotions = response_dict.get('emotionPredictions', [])[0].get('emotion', {})
    scores = {key: val for key, val in emotions.items() if key != 'target'}
    
    dominant_emotion_name = max(scores, key=scores.get)
    dominant_emotion_score = scores[dominant_emotion_name]
    
    output = {
        'anger': emotions.get('anger', 0),
        'disgust': emotions.get('disgust', 0),
        'fear': emotions.get('fear', 0),
        'joy': emotions.get('joy', 0),
        'sadness': emotions.get('sadness', 0),
        'dominant_emotion': dominant_emotion_name,
    }
    
    return output