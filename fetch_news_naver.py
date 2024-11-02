import requests
import json
import nltk
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from openai import OpenAI

client = OpenAI(
    api_key="None",
    # Change the API base URL to the local interference API
    base_url="http://localhost:1337/v1"  
)

url = "https://raw.githubusercontent.com/stopwords-iso/stopwords-ko/master/stopwords-ko.txt"
response = requests.get(url)
stopwords = response.text.splitlines()
stopwords.append('[')
stopwords.append(']')
nltk.download('punkt')
nltk.download('punkt_tab')

client_id = "iRRD0P6q5HghHv94n8K3"
client_secret = "GBfTG8vmuU"

url = "https://openapi.naver.com/v1/search/news.json"

# Get user input for comparison
input_text = input("분석할 뉴스를 입력하세요: ")

#use OpenAi API to extract keywords
ai_response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": f"Extract the most important 3 words/phrases from the news title separated by commas. However, do not respond other than the extracted words. News title: \"{input_text}\""}],
    stream=False,
)
print("추출된 단어:", ai_response.choices[0].message.content)
input_tokens = ai_response.choices[0].message.content.split(',')
# Initialize an empty list to store all titles
all_titles = []

# Fetch news for each token
for token in input_tokens:
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
        titles = [item['title'] for item in data['items']]
        titles = [re.sub('<b>', '', title) for title in titles]
        titles = [re.sub('</b>', '', title) for title in titles]
        all_titles.extend(titles)

# Tokenize and filter the titles
wordlist = [word for title in all_titles for word in nltk.word_tokenize(title) if word not in stopwords]

# Combine the wordlist into a single string
wordlist_combined = ' '.join(wordlist)

# Create a list of documents to vectorize
documents = [wordlist_combined, input_text]

# Vectorize the documents
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(documents)

# Calculate cosine similarity
cos_similar = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
print("코사인 유사도:", cos_similar[0][0])
if cos_similar[0][0] == 0:
    print("An error occurred.")
elif cos_similar[0][0] > 0.15:
    print("해당 뉴스는 진짜 뉴스입니다.")
else:
    print("해당 뉴스는 가짜 뉴스입니다.")
