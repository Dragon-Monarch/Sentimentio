from flask import Flask, render_template, request, jsonify
import joblib

app = Flask(__name__)

pipeline = joblib.load('sentiment_pipeline.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    review = request.json.get('review')
    result = pipeline(review)
    sentiment = result[0]['label']

    return jsonify(sentiment=sentiment)

if __name__ == '__main__':
    app.run(debug=True)