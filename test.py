from konlpy.tag import Okt
import nltk
from collections import Counter
import itertools

# Sample Korean text
text = """
한국어 텍스트에서 키워드를 추출하는 것은 자연어 처리에서 중요한 작업입니다.
텍스트랭크 알고리즘은 그래프 기반의 알고리즘으로, 문서 내의 단어들 간의 연결성을 이용하여 중요한 단어를 추출합니다.
"""

# Initialize the Okt tokenizer
okt = Okt()

# Tokenize the text and extract nouns
tokens = okt.nouns(text)

# Create a frequency distribution of the tokens
freq_dist = Counter(tokens)

# Create a simple co-occurrence matrix
co_occurrence = {}
window_size = 2

for i, token in enumerate(tokens):
    for j in range(i + 1, min(i + window_size, len(tokens))):
        if token != tokens[j]:
            pair = tuple(sorted([token, tokens[j]]))
            if pair in co_occurrence:
                co_occurrence[pair] += 1
            else:
                co_occurrence[pair] = 1

# Rank the words based on their frequency and co-occurrence
ranked_words = sorted(freq_dist.items(), key=lambda x: x[1], reverse=True)

# Extract top N keywords
top_n = 5
keywords = [word for word, freq in ranked_words[:top_n]]

print("Extracted Keywords:", keywords)