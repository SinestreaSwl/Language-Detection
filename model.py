import pandas as pd
import re
import string
import pickle
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, recall_score, f1_score, precision_score
from sklearn.multioutput import MultiOutputClassifier

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
 
# TRAINING I

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

# Evaluate score
# print(f'Model Accuracy: {accuracy_score(y_test, y_pred)}')

"""
Result : Training Model
Model Accuracy: 0.9166666666666666
"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - # 

# TEST I

# Dataset
df_1 = pd.read_csv('dataset/data_test.csv')

# Cleaned Text
df_1['clean_text'] = df_1['Text'].apply(clean_text)

# Feature
X_1 = df_1['clean_text']

# Features Extraction
X_test_vectorized_1 = vectorizer.transform(X_1)

# Predict
y_pred_1 = model.predict(X_test_vectorized_1)
df_1['Language Prediction'] = y_pred_1

# Evaluate score
actual_label = df_1['Language']
# print("Accurasy:", accuracy_score(actual_label, y_pred_1))
# print("Precision:", precision_score(actual_label, y_pred_1, average='weighted'))
# print("Recall:", recall_score(actual_label, y_pred_1, average='weighted'))
# print("F1-Score:", f1_score(actual_label, y_pred_1,average='weighted'))

"""
Result : TEST I
Model Accuracy: 0.9166666666666666
Accurasy: 0.9416666666666667
Precision: 0.9477611940298508
Recall: 0.9416666666666667
F1-Score: 0.9414674935544561
"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - # 

# TEST II

df_2 = pd.read_csv('dataset/data_test_2.csv')

"""
The text in dataset are randomized,maybe it doesn't produce a clear sentence
In this dataset i want to know how usseful the model perform in randomized text in dataset
"""

# Clean the text
df_2['Clean_text'] = df_2['Text'].apply(clean_text)

# Feature
X_2 = df_2['Clean_text']

# Feature Extraction
X_test_vectorized_2 = vectorizer.transform(X_2)

# Predict
y_pred_2 = model.predict(X_test_vectorized_2)
df_2['Language Prediction'] = y_pred_2

# Evaluate score
actual_label_2 = df_2['Language']
# print("Accurasy:", accuracy_score(actual_label_2, y_pred_2))
# print("Precision:", precision_score(actual_label_2, y_pred_2, average='weighted'))
# print("Recall:", recall_score(actual_label_2, y_pred_2, average='weighted'))
# print("F1-Score:", f1_score(actual_label_2, y_pred_2,average='weighted'))

"""
Result : TEST II
Model Accurasy: 0.988
Precision: 0.988
Recall: 0.988
F1-Score: 0.988
"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - # 

# TEST III

df_3 = pd.read_csv('dataset/data_test_3.csv')

"""
Because in previous test the result are bad,so in this datatest 
the text produce a complete sentence not randomize sentence as previously
"""

# Cleaned text
df_3['Clean_text'] = df_3['Text'].apply(clean_text)

# Feature
X_3 = df_3['Clean_text']

# Feature extraction
X_test_vectorized_3 = vectorizer.transform(X_3)

# Predict
y_pred_3 = model.predict(X_test_vectorized_3)
df_3['Predict Language'] = y_pred_3

# Evaluate
actual_label_3 = df_3['Language']
# print("Accurasy:", accuracy_score(actual_label_3, y_pred_3))
# print("Precision:", precision_score(actual_label_3, y_pred_3, average='weighted'))
# print("Recall:", recall_score(actual_label_3, y_pred_3, average='weighted'))
# print("F1-Score:", f1_score(actual_label_3, y_pred_3, average='weighted'))

"""
Result : TEST III
Accurasy: 0.95
Precision: 0.9511278195488722
Recall: 0.95
F1-Score: 0.9499687304565352
"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - # 

# TEST IV

"""
In previous result the model perform are great,but it just for a complete text,in the single text
the model can't spesificly to predict a correct language text,so in this test i train again the
model with dataset single text
"""

# Dataset
df_4 = pd.read_csv('dataset/data_test_4.csv')
df = pd.concat([df, df_4], ignore_index=True)

# Clean new dataset
df['clean_text'] = df['Text'].apply(clean_text)

# Split the new dataset
X_train, X_test, y_train, y_test = train_test_split(df['clean_text'], df['Language'], test_size=0.2, random_state=42)

# Refit the model with new dataset
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

model.fit(X_train_vectorized, y_train)

y_pred = model.predict(X_test_vectorized)

# Test performa model

# Read csv 
df_4_1 = pd.read_csv('dataset/data_test_4.csv')

# Clean text
df_4_1['clean_text'] = df_4_1['Text'].apply(clean_text)

# Feature and vectorized
X_4 = df_4_1['clean_text']
X_test_vectorized_4 = vectorizer.transform(X_4)

# Prediction
y_pred_4 = model.predict(X_test_vectorized_4)
df_4_1['Language Predicted'] = y_pred_4

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - # 

# TRAINING II

"""
because in the previously testing,model can more effective to predicted input data,so i want to
make the model can predict more language,besides indonesian,and english
"""

# Datatrain
df_train_2 = pd.read_csv('dataset/data_train_2.csv')

# Clean the text
df_train_2['clean_text'] = df_train_2['Text'].apply(clean_text)

# Split dataset
X_train_2, X_test_2, y_train_2, y_test_2 = train_test_split(df_train_2['clean_text'], df_train_2[['Language', 'Emotion']], test_size=0.2, random_state=42)

# Feature Extraction
X_train_2_vectorizer_2 = vectorizer.fit_transform(X_train_2)
X_test_2_vectorizer_2 = vectorizer.transform(X_test_2)

# Model building
multi_output_model = MultiOutputClassifier(model, n_jobs=1)
multi_output_model.fit(X_train_2_vectorizer_2, y_train_2)

# Predict
y_pred_model_2 = multi_output_model.predict(X_test_2_vectorizer_2)

# Evaluate score
accuracy_lang = accuracy_score(y_test_2['Language'], y_pred_model_2[:, 0])
accuracy_emotion = accuracy_score(y_test_2['Emotion'], y_pred_model_2[:, 1])

print(f'Language Prediction Accuracy: {accuracy_lang}')
print(f'Emotion Prediction Accuracy: {accuracy_emotion}')

"""
Result : Training II
Language Prediction Accuracy: 1.0
Emotion Prediction Accuracy: 0.75
"""

# Save model
# with open('model.pkl', 'wb') as f:
#     pickle.dump(model, f)

# # Save vectorizer
# with open('vectorizer.pkl', 'wb') as f:
#     pickle.dump(vectorizer, f)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - # 

# TEST V

# Dataset
df_5 = pd.read_csv('dataset/data_test_5.csv')

# Text cleaning
df_5['clean_text'] = df_5['Text'].apply(clean_text)

# Feature and vectorized
X_5 = df_5['clean_text']
X_test_vectorized_5 = vectorizer.transform(X_5)

# Prediction
y_pred_5 = multi_output_model.predict(X_test_vectorized_5)
df_5[['Prediction_lang', 'Prediction_emotion']] = y_pred_5

# Evaluate score
accuracy_lang_2 = accuracy_score(df_5['Language'], y_pred_5[:, 0])
accuracy_emotion_2 = accuracy_score(df_5['Emotion'], y_pred_5[:, 1])

# print(f'Language Prediction Accuracy: {accuracy_lang_2}')
# print(f'Emotion Prediction Accuracy: {accuracy_emotion_2}')

"""
Result : TEST V
Language Prediction Accuracy: 0.95
Emotion Prediction Accuracy: 0.65
"""
