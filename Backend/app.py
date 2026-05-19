from flask import Flask, request, jsonify
from flask_cors import CORS
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import pandas as pd
import joblib 

nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)


class EmailPreprocessor:
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))

    def clean_text(self, text):
        if pd.isna(text):
            return ''
        text = str(text).lower()
        text = re.sub(r'http\S+|www\S+|https\S+', '', text)
        text = re.sub(r'\S+@\S+', '', text)
        text = re.sub(r'<[^>]+>', '', text)
        text = re.sub(r'[^\w\s]', ' ', text)
        text = re.sub(r'\d+', '', text)
        text = re.sub(r'\s+', ' ', text)
        tokens = word_tokenize(text)
        tokens = [self.lemmatizer.lemmatize(token) for token in tokens
        if token not in self.stop_words and len(token) > 2]
        return ' '.join(tokens).strip()


app = Flask(__name__)
CORS(app)


try:
    model = joblib.load('phishing_model.pkl')
    vectorizer = joblib.load('tfidf_vectorizer.pkl')
except FileNotFoundError:
    print("Error: Model or Vectorizer file not found. Ensure 'phishing_model.pkl' and 'tfidf_vectorizer.pkl' are in the same directory.")
    model = None
    vectorizer = None
except Exception as e:
    print(f"Error loading model/vectorizer: {e}")
    model = None
    vectorizer = None


# Initialize preprocessor
preprocessor = EmailPreprocessor()

@app.route('/')
def home():
    return 'API is working! Visit /predict with POST request.'

@app.route('/predict', methods=['POST'])
def predict():
    if model is None or vectorizer is None:
        return jsonify({"error": "Model or Vectorizer not loaded. Check server logs."}), 500

    data = request.get_json()
    email_text = data.get('email_text', '')

    if not email_text:
        return jsonify({"error": "No 'email_text' provided in the request."}), 400

    clean_text = preprocessor.clean_text(email_text)
    X_new = vectorizer.transform([clean_text])
    prediction = model.predict(X_new)[0]
    result = "Phishing" if prediction == 1 else "Legitimate"
    return jsonify({'prediction': result})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True) 