from flask import Flask, render_template, request
from EmotionDetection import emotion_detector
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/emotionDetector')
def emotionDetector():
    textToAnalyze = request.args.get('textToAnalyze')

    if not textToAnalyze:
        return "Invalid input!", 400
    
    result = emotion_detector(textToAnalyze)

    response_sentence = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )
    return response_sentence, 200

if __name__ == "__main__":
    # localhost:5000 as required
    app.run(host="127.0.0.1", port=5000)