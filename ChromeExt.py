from flask import Flask, request, jsonify
from flask_cors import CORS
from newsdataapi import NewsDataApiClient
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

# API key authorization, Initialize the client with your API key

api = NewsDataApiClient(apikey="pub_5792240c0c63be345810def276d2c4add312f")

# You can paginate till last page by providing "page" parameter

page=None

titles = []
while True:

    response = api.latest_api(page = page, country="kr")

    if response['status'] == 'success':
        # Extract titles
        titles = [article['title'] for article in response['results']]

        # Print the titles
        for title in titles:
            titles.append(title)
    else:
        print(response['message'])
        break
    page = response.get('nextPage',None)

    if not page:

        break

with open('titles.txt', 'w') as file:
    for title in titles:
        file.write(title + '\n')

app = Flask(__name__)
CORS(app)

@app.route('/generate_selector', methods=['POST'])
def generate_selector():
    extracted_text = request.get_json().get("text", "")
    print(extracted_text)
    data = [i for i in nltk.word_tokenize(extracted_text) if i not in stopwords]
    print(data)
    #q=' '.join(data), 
    # ai_response = client.chat.completions.create(
    #     model="gpt-4o-mini",
    #     messages=[{"role": "user", "content": f"Based on these news titles, check if input news is fake or not. Input news: \"{extracted_text}\" News titles: \"{news_titles}\""}],
    #     stream=False,
    # )
    # return ai_response.choices[0].message.content

app.run(port=5050)
