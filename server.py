"""
A simple Flask application for emotion detection.
"""

from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    """
    Renders the index.html template.
    Returns:
        str: Rendered HTML content.
    """
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def analyze_emotion():
    """
    Analyzes the input text for emotions and returns the dominant emotion detected.
    Args:
        textToAnalyze (str): Text to analyze for emotions.
    Returns:
        dict: Dictionary containing the dominant emotion and other detected emotions.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)
    if result['dominant_emotion'] is None:
        return jsonify({'error': 'Invalid text! Please try again.'}), 400
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
