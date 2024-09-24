import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet
def explore_word_meanings(word):
    synsets = wordnet.synsets(word)
    if not synsets:
        print(f"No meanings found for '{word}' in WordNet.")
        return
    for synset in synsets:
        print(f"Meaning ({synset.pos()}) - {synset.definition()}")
        print(f"Example: {synset.examples()}")
        print()
word_to_explore = "bank"
explore_word_meanings(word_to_explore)