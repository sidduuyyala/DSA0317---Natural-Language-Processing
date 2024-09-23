import nltk
from nltk.corpus import treebank
from nltk.tag import BigramTagger

train_sents = treebank.tagged_sents()[:3000]
bigram_tagger = BigramTagger(train_sents)
test_sents = treebank.sents()[3000:3010]

for sent in test_sents:
    tagged_sent = bigram_tagger.tag(sent)
    print(tagged_sent)
