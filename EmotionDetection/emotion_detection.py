"""Emotion Detector with the Watson NLP service."""

import requests

URL = ("https://sn-watson-emotion.labs.skills.network/v1/"
       "watson.runtime.nlp.v1/NlpService/EmotionPredict")
HEADERS = {
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
}
EMOTIONS = ("anger", "disgust", "fear", "joy", "sadness")


def emotion_detector(text_to_analyze):
    """Score a text for five emotions and name the strongest one.

    Returns a dict holding one score per emotion plus the key
    'dominant_emotion'. Every value is None when Watson rejects the
    input as blank.
    """
    response = requests.post(
        URL,
        headers=HEADERS,
        json={"raw_document": {"text": text_to_analyze}},
        timeout=30
    )

    if response.status_code == 400:
        return dict.fromkeys(EMOTIONS + ("dominant_emotion",))

    predictions = response.json()["emotionPredictions"][0]["emotion"]
    scores = {name: predictions[name] for name in EMOTIONS}
    scores["dominant_emotion"] = max(scores, key=scores.get)
    return scores
