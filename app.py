import requests
import re
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from keybert import KeyBERT
from transformers import BertModel
from kiwipiepy import Kiwi
from flask import Flask, request, jsonify
from flask_cors import CORS

def noun_extractor(text):
    results = []
    kiwi = Kiwi()
    result = kiwi.analyze(text)
    for token, pos, _, _ in result[0][0]:
        if len(token) != 1 and pos.startswith('N') or pos.startswith('SL'):
            results.append(token)
    return results

def preprocess(text):
    nouns = noun_extractor(text)
    return ' '.join(nouns)

def get_keywords(kw_model, text):
    preprocessed_text = preprocess(text)
    keywords = kw_model.extract_keywords(preprocessed_text, keyphrase_ngram_range=(1, 2), stop_words=None, top_n=3)
    keywords = [item[0] for item in keywords]
    return keywords

client_id = "iRRD0P6q5HghHv94n8K3"
client_secret = "GBfTG8vmuU"

url = "https://openapi.naver.com/v1/search/news.json"

model = BertModel.from_pretrained('skt/kobert-base-v1')
kw_model = KeyBERT(model)

stopwords_url = "https://raw.githubusercontent.com/stopwords-iso/stopwords-ko/master/stopwords-ko.txt"
response = requests.get(stopwords_url)
stopwords = response.text.splitlines()

app = Flask(__name__)
CORS(app)

@app.route('/generate_selector', methods=['POST'])
def generate_selector():
    extracted_text = request.get_json().get("text", "")
    print(extracted_text)
    
    keywords = get_keywords(kw_model, extracted_text)
    print("추출된 단어:", keywords)
    
    all_descriptions = []
    
    for token in keywords:
        if token not in stopwords:
            params = {
                'query': token,
                'display': 100,
                'sort': 'sim'
            }
            headers = {
                'X-Naver-Client-Id': client_id,
                'X-Naver-Client-Secret': client_secret
            }
            response = requests.get(url, headers=headers, params=params)
            data = response.json()
            #Idk what item to use(title or description)
            descriptions = [item['description'] for item in data['items']]
            descriptions = [re.sub('<b>', '', description) for description in descriptions]
            descriptions = [re.sub('</b>', '', description) for description in descriptions]
            all_descriptions.extend(descriptions)
    
    #removing useless words
    all_descriptions_combined = ' '.join(all_descriptions)
    all_descriptions_combined = all_descriptions_combined.replace('[사진]', '')
    all_descriptions_combined = all_descriptions_combined.replace('&quot;', '')
    documents = [all_descriptions_combined, extracted_text]
    
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(documents)
    
    cos_similar = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    print("코사인 유사도:", cos_similar[0][0])
    
    if cos_similar[0][0] > 0.1:
        result = "해당 뉴스는 사실입니다."
    elif cos_similar[0][0] > 0.05:
        result = "해당 뉴스는 대체로 사실입니다."
    elif cos_similar[0][0] > 0.01:
        result = "해당 뉴스는 절반의 사실입니다."
    elif cos_similar[0][0] > 0.005:
        result = "해당 뉴스는 대체로 사실이 아닙니다."
    else:
        result = "해당 뉴스는 전혀 사실이 아닙니다."
    
    return result

app.run(port=5050)
