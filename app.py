from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

app.route("/emotionDetector")
def detect_emotion():
    text = request.args.get("textToAnalyze")
    result = emotion_detector(text)
    return str(result)

if __name__ == "__main__":
    app.run(debug=True)