class TransformationBasedTagger:
    def __init__(self, rules):
        self.rules = rules

    def tag(self, sentence):
        tokens = sentence.split()
        tagged_tokens = []

        for token in tokens:
            tagged = False
            for rule in self.rules:
                if rule['pattern'] == token:
                    tagged_tokens.append((token, rule['tag']))
                    tagged = True
                    break

            if not tagged:
                tagged_tokens.append((token, 'Unknown'))

        return tagged_tokens


# Define transformation rules
rules = [
    {'pattern': 'dog', 'tag': 'NN'},
    {'pattern': 'chases', 'tag': 'VB'},
    {'pattern': 'big', 'tag': 'JJ'},
    {'pattern': 'the', 'tag': 'DT'},
    {'pattern': 'small', 'tag': 'JJ'},
    {'pattern': 'cat', 'tag': 'NN'}
]


# Create tagger
tagger = TransformationBasedTagger(rules)


# Test tagger
sentence = "The big dog chases the small cat."
tagged_sentence = tagger.tag(sentence)


# Print tagged sentence
for token, tag in tagged_sentence:
    print(f"{token}: {tag}")
