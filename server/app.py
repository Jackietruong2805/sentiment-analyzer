import warnings
warnings.filterwarnings("ignore")
from flask import Flask, jsonify, request
from flask_cors import CORS
from gensim.models import FastText
from gensim.utils import simple_preprocess
import pandas as pd
import joblib
from utils import *
app = Flask(__name__)
CORS(app)

def vectorize_review(review):
    data = pd.read_csv("./review.csv", encoding='utf8')
    #simple preprocess
    sentences = [simple_preprocess(data) for data in data]
    #train model
    model = FastText(sentences, vector_size=100, window=5, min_count=1, workers=4, sg=1)
    words = simple_preprocess(review)
    #Calculate the average vector of the words in the review
    vectors = [model.wv[word] for word in words if word in model.wv]
    if vectors:
        #Returns the average of the word vectors
        return sum(vectors) / len(vectors)
    else:
        #In case no vector is found for any word in the review
        return [0] * model.vector_size

@app.route('/', methods=['POST'])

def analyze():
    # Get data from request body
    data = request.get_json()  # Nếu dữ liệu là JSON
    review = str(data['review'])
    review = process_data(review)
    
    # using model to predict
    model_type = data['type']
    predictions = ''
    if model_type == 'naivebayes' or model_type == 'maxent':
        # Load the vectorizer vocabulary and configuration
        vectorizer = joblib.load("./vectors/tfidf_vector.pkl")
        if model_type == 'naivebayes':
            # Load the pre-trained model
            model = joblib.load('./models/Naive_Bayes_model.pkl')
            # Vectorize your input text
            input_text = [review]
            tfidf_vectors = vectorizer.transform(input_text)
            # Make predictions using the loaded model
            predictions = model.predict(tfidf_vectors)[0]
        if model_type == 'maxent':
            # Load the pre-trained model
            model = joblib.load('./models/logistic_regression_model.pkl')
            # Vectorize your input text
            input_text = [review]
            tfidf_vectors = vectorizer.transform(input_text)
            # Make predictions using the loaded model
            predictions = model.predict(tfidf_vectors)[0]
    else:
        predictions = ''
    
    return jsonify({
        "review": predictions,
    })

if __name__ == '__main__':
    # Run the app in debug mode
    app.run(debug=True)

 