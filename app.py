from flask import Flask, request, jsonify, render_template
from model import clean_text, multi_output_model
import numpy as np
import pickle


with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('vectorizer.pkl', 'rb')  as vec_file:
    vectorizer = pickle.load(vec_file)

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    response = {}
    try:
        # Take input from form
        data = request.get_json()
        text = data['Text']

        # Clean datatest
        text_clean = clean_text(text)

        # Vectorizing datatest
        text_vectorized = vectorizer.transform([text_clean])

        # Predict
        prediction = multi_output_model.predict(text_vectorized)
        language_prediction = prediction[0][0]
        emotion_prediction = prediction[0][1]

        # Show the result
        response['language_prediction'] = language_prediction
        response['emotion_prediction'] = emotion_prediction
        return jsonify(response)
    except KeyError as e:
        response['error'] = f'KeyError: {str(e)}'
        return jsonify(response), 400
    except Exception as e:
        response['error'] = str(e)
        return jsonify(response), 500

if __name__ == "__main__":
    app.run(debug=True)
        