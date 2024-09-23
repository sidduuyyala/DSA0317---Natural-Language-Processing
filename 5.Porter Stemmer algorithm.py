from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
words = ["running", "jumping", "happiness", "computers", "generous"]
stemmed_words = [stemmer.stem(word) for word in words]
print(stemmed_words)
