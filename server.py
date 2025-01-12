"""Executing this function initiates the application of emotion
   detection to be executed over the Flask channel and deployed on
   localhost:5000.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    """Handles the /emotionDetector route. 
    Receives text from user and returns a formatted response with emotion analysis.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if not response['dominant_emotion']:
        return "Invalid text! Please try again!"

    return (f"For the given statement, the system response is 'anger': {response['anger']}, "
    f"'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']} and "
    f"'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}.")

@app.route("/")
def render_index_page():
    """Renders the main HTML page of the application. 
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
