from keybert import KeyBERT
import requests

url = "https://raw.githubusercontent.com/stopwords-iso/stopwords-ko/master/stopwords-ko.txt"
response = requests.get(url)
stopwords = response.text.splitlines()

doc = "대뜸 초인종 눌러 \"물 좀 주세요\"…집까지 찾아온 '도를 아십니까'"
kw_model = KeyBERT()
keywords = kw_model.extract_keywords(doc, keyphrase_ngram_range=(1, 2), top_n=3, stop_words=stopwords)
print(keywords)
keywords = [keyword[0] for keyword in keywords]
print(keywords)