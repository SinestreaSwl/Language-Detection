import pandas as pd
import pickle
import re
import string
from model import model
from sklearn.feature_extraction.text import CountVectorizer

# Dataset
df = pd.read_csv('dataset/data_test.csv')

# Cleaned Text
def clean_text(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(r'\s+', '', text).strip()
    return text

df['clean_text'] = df['Text'].apply(clean_text)

# Feature
X = df['clean_text']

# Features Extracktion
vectorizer = CountVectorizer(ngram_range=(1, 2), analyzer='char')
X_train_vectorized = vectorizer.transform(X)
