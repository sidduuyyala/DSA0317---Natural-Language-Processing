from nltk.corpus import stopwords, wordnet
from nltk.tokenize import word_tokenize
from nltk.wsd import lesk
import string
def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    tokens = [token for token in tokens if token not in string.punctuation and token not in stopwords.words('english')]
    return tokens
def perform_wsd(word, sentence):
    best_sense = lesk(sentence, word)
    return best_sense
sentence = "He went to the bank to deposit his money."
word = "bank"
preprocessed_sentence = preprocess_text(sentence)
sense = perform_wsd(word, preprocessed_sentence)
if sense:
    print(f"Word: {word}")
    print(f"Sentence: {sentence}")
    print(f"Best Sense: {sense.name()} - {sense.definition()}")
else:
    print(f"No suitable sense found for '{word}' in then context.")