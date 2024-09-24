import nltk
from nltk.corpus import wordnet as wn
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('punkt')
def get_noun_phrases(sentence):
    words = nltk.word_tokenize(sentence)
    pos_tags = nltk.pos_tag(words)
    noun_phrases = []
    for word, pos in pos_tags:
        if pos.startswith('NN'):              
            noun_phrases.append(word)
    return noun_phrases
def get_meaning(word):
    synsets = wn.synsets(word, pos=wn.NOUN)
    if synsets:
        return synsets[0].definition()
    return None
sentence = "The quick brown fox jumps over the lazy dog."
noun_phrases = get_noun_phrases(sentence)
for noun in noun_phrases:
    meaning = get_meaning(noun)
    if meaning:
        print(f"Noun: {noun} -> Meaning: {meaning}")