import requests
import re
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from keybert import KeyBERT
from transformers import BertModel
from kiwipiepy import Kiwi
from tqdm import tqdm
import threading
import time

def request_to_naver(url, headers, params, client_id, client_secret):
    headers['X-Naver-Client-Id'] = client_id
    headers['X-Naver-Client-Secret'] = client_secret
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 429:
        if 'Retry-After' not in response.headers:
            wait_time = 1
        else:
            wait_time = response.headers.get('Retry-After', 1)
        print(f"Rate limit exceeded. Waiting for {wait_time} seconds.")
        time.sleep(wait_time)
        return request_to_naver(url, headers, params, client_id, client_secret)
    return response

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

data = ["data/사실.txt", "data/대체로 사실.txt", "data/절반의 사실.txt", "data/대체로 사실 아님.txt", "data/전혀 사실 아님.txt"]

#I don't think this algorithm is best for this task, because it takes 13 lines
non_existent_files = []
empty_files = []
for file in data:
    if not os.path.exists(file):
        non_existent_files.append(file)
    elif os.path.getsize(file) == 0:
        empty_files.append(file)
if non_existent_files:
    for file in non_existent_files:
        print(f"{file} does not exist.")
if empty_files:
    for file in empty_files:
        print(f"{file} is empty.")

client_ids = ["iRRD0P6q5HghHv94n8K3", "DbXP8DUYGIe5PJWyCwJT", "YR9tV08g62h7FjrqYHDr"]
client_secrets = ["GBfTG8vmuU", "37HyAhWvgE", "ULJapPIC3z"]

url = "https://openapi.naver.com/v1/search/news.json"

model = BertModel.from_pretrained('skt/kobert-base-v1')
kw_model = KeyBERT(model)

stopwords_url = "https://raw.githubusercontent.com/stopwords-iso/stopwords-ko/master/stopwords-ko.txt"
response = requests.get(stopwords_url)
stopwords = response.text.splitlines()

def process_text(extracted_text, client_id, client_secret):
    keywords = get_keywords(kw_model, extracted_text)
    
    all_descriptions = []
    
    for token in keywords:
        if token not in stopwords:
            params = {
                'query': token,
                'display': 100,
                'sort': 'sim'
            }
            headers = {}
            response = request_to_naver(url, headers, params, client_id, client_secret)
            
            data = response.json()
            
            descriptions = [item['description'] for item in data['items']]
            descriptions = [re.sub('<b>', '', description) for description in descriptions]
            descriptions = [re.sub('</b>', '', description) for description in descriptions]
            all_descriptions.extend(descriptions)
    
    all_descriptions_combined = ' '.join(all_descriptions)
    all_descriptions_combined = all_descriptions_combined.replace('[사진]', '')
    all_descriptions_combined = all_descriptions_combined.replace('&quot;', '')
    documents = [all_descriptions_combined, extracted_text]
    
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(documents)
    
    cos_similar = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    
    if cos_similar[0][0] > 0.20:
        result = 1
    elif cos_similar[0][0] > 0.15:
        result = 2
    elif cos_similar[0][0] > 0.10:
        result = 3
    elif cos_similar[0][0] > 0.05:
        result = 4
    else:
        result = 5
    
    return result, cos_similar[0][0]

match_count = 0
total_titles = 0
total_cos_sim = 0

def process_file(file_path, label, pbar, client_id, client_secret, file_results):
    global match_count, total_titles, total_cos_sim
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read().split('\n')
        for j in text:
            result, cos_sim = process_text(j, client_id, client_secret)
            if label == 1 and 0 <= result <= 2:
                match_count += 1
            elif label == 2 and 1 <= result <= 3:
                match_count += 1
            elif label == 3 and 2 <= result <= 4:
                match_count += 1
            elif label == 4 and 3 <= result <= 5:
                match_count += 1
            elif label == 5 and 4 <= result <= 6:
                match_count += 1
            total_titles += 1
            total_cos_sim += cos_sim
            file_results[file_path]['total_titles'] += 1
            file_results[file_path]['total_cos_sim'] += cos_sim
            pbar.update(1)

def print_accuracy(file_results):
    while any(thread.is_alive() for thread in threads):
        if total_titles > 0:
            accuracy = (match_count / total_titles) * 100
            avg_cos_sim = total_cos_sim / total_titles
            print(f"\nCurrent accuracy: {accuracy:.2f}%")
            print(f"Average cosine similarity: {avg_cos_sim:.4f}")
            for file_path, results in file_results.items():
                if results['total_titles'] > 0:
                    file_avg_cos_sim = results['total_cos_sim'] / results['total_titles']
                    print(f"File: {file_path}, Average cosine similarity: {file_avg_cos_sim:.4f}")
        time.sleep(60)

threads = []
pbar = tqdm(total=sum(1 for file_path in data for line in open(file_path, 'r', encoding='utf-8')))

# Initialize a dictionary to store results for each file
file_results = {file_path: {'total_titles': 0, 'total_cos_sim': 0} for file_path in data}

for i, file_path in enumerate(data):
    label = i + 1
    client_id = client_ids[i % len(client_ids)]
    client_secret = client_secrets[i % len(client_secrets)]
    thread = threading.Thread(target=process_file, args=(file_path, label, pbar, client_id, client_secret, file_results))
    threads.append(thread)
    thread.start()

accuracy_thread = threading.Thread(target=print_accuracy, args=(file_results,))
accuracy_thread.start()

for thread in threads:
    thread.join()

accuracy_thread.join()
pbar.close()
print(match_count, "/", total_titles)
print("완료")
input()
