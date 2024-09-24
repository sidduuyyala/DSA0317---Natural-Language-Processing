import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
import string
nltk.download('punkt')
nltk.download('stopwords')
def preprocess_text(text):
    stop_words = set(stopwords.words('english') + list(string.punctuation))
    tokens = word_tokenize(text.lower())
    return [word for word in tokens if word not in stop_words]
def lexical_cohesion_score(tokens):
    score = 0
    seen_tokens = set()
    for token in tokens:
        if token in seen_tokens:
            score += 1
        seen_tokens.add(token)
    return score / len(tokens) if tokens else 0
text = "John went to the store. He bought some milk. The store was busy."
tokens = preprocess_text(text)
cohesion_score = lexical_cohesion_score(tokens)
print("Text: ", text)
print("Lexical Cohesion Score: ", cohesion_score)  