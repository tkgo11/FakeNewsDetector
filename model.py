import os
import numpy as np
import pandas as pd
import requests
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.preprocessing import MultiLabelBinarizer

# 한국어 불용어 다운로드
url = "https://raw.githubusercontent.com/stopwords-iso/stopwords-ko/master/stopwords-ko.txt"
response = requests.get(url)
stopwords = response.text.splitlines()

# 데이터 준비
data = []
labels = []

files = ['사실.txt', '대체로 사실.txt', '절반의 사실.txt', '대체로 사실 아님.txt', '전혀 사실 아님.txt']
for file_name in files:
    with open(file_name, "r", encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            text = line.strip()
            data.append(text)
            labels.append(file_name.replace('.txt', ''))  # Use the file name as the label

# 데이터프레임 생성
df = pd.DataFrame({'text': data, 'label': labels})

# 훈련용 데이터와 테스트용 데이터로 분할
X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.2, random_state=42)

# 모델 생성 및 훈련
vectorizer = CountVectorizer(stop_words=[word.strip() for word in stopwords])  # Tokenize stop words
model = make_pipeline(vectorizer, MultinomialNB())
model.fit(X_train, y_train)

# 테스트 데이터로 평가
predicted = model.predict(X_test)
print(classification_report(y_test, predicted, zero_division=0))  # Set zero_division to 0

# 사용자 입력 텍스트 분류
user_input = input("평가할 텍스트를 입력하세요: ")
predicted_label = model.predict([user_input])[0]
print(f"예측된 정도: {predicted_label}")
