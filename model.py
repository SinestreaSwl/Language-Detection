import pandas as pd
import re
import string
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Dataset
df = pd.read_csv('dataset/data_train.csv')

# Cleaned text
def clean_text(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(r'\s+', '', text).strip()
    return text

df['clean_text'] = df['Text'].apply(clean_text)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(df['clean_text'], df['Language'], test_size=0.2, random_state=42)


# Features Extracktion
vectorizer = CountVectorizer(ngram_range=(1, 2), analyzer='char')
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)


# Model Building
model = LogisticRegression(max_iter=1000)
model.fit(X_train_vectorized, y_train)

# Predict
y_pred = model.predict(X_test_vectorized)

# Evaluate
print(f'Accuracy {accuracy_score(y_test, y_pred)}')
print(classification_report(y_test, y_pred))