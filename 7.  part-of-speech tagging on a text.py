import nltk

# Try downloading the necessary NLTK models in the script itself
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')

# Perform POS tagging
def pos_tagging(text):
    words = nltk.word_tokenize(text)
    pos_tags = nltk.pos_tag(words)
    for word, tag in pos_tags:
        print(f"Word: {word}, POS Tag: {tag}")

# Example usage
text = "John is playing football in the park with his friends."
pos_tagging(text)
