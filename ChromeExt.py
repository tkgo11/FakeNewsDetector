from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import requests
import nltk

client = OpenAI(
    api_key="None",
    # Change the API base URL to the local interference API
    base_url="http://localhost:1337/v1"  
)

url = "https://raw.githubusercontent.com/stopwords-iso/stopwords-ko/master/stopwords-ko.txt"
response = requests.get(url)
stopwords = response.text.splitlines()
nltk.download('punkt')
nltk.download('punkt_tab')

news_url = 'https://newsapi.org/v2/everything'

app = Flask(__name__)
CORS(app)

@app.route('/generate_selector', methods=['POST'])
def generate_selector():
    extracted_text = request.get_json().get("text", "")
    print(extracted_text)
    news = []
    data = [i for i in nltk.word_tokenize(extracted_text) if i not in stopwords]
    print(data)
    params = {
        #'q': ' '.join(data),
        'language': 'ko',
        'apiKey': '258be7177d7142788c50ed9b5718073e'
    }
    news_response = requests.get(news_url, params=params)
    news_data = news_response.json()
    print(news_data)
    if news_data['status'] == 'ok':
        for article in news_data['articles']:
            news.append(article['title'])
    # Convert the list of news titles to a single string
    news_titles = ' '.join(news)
    print(news_titles)
    ai_response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": f"Based on these news titles, check if input news is fake or not. Input news: \"{extracted_text}\" News titles: \"{news_titles}\""}],
        stream=False,
    )
    return ai_response.choices[0].message.content

app.run(port=5050)
