# app.py
from flask import Flask, request, jsonify
import nltk
from nltk.stem import WordNetLemmatizer

app = Flask(__name__)
lemmatizer = WordNetLemmatizer()

# Basic intents for college management
intents = {
    "admissions": "For admissions, visit our website or contact admissions@college.edu.",
    "courses": "We offer courses in Engineering, Arts, and Sciences.",
    "contact": "You can contact us at +91-1234567890."
}

@app.route('/chat', methods=['POST'])
def chat():
    message = request.json['message'].lower()
    tokens = nltk.word_tokenize(message)
    for intent in intents:
        if intent in tokens:
            return jsonify({ "response": intents[intent] })
    return jsonify({ "response": "Sorry, I didn't understand that." })

if __name__ == '__main__':
    app.run(debug=True)
