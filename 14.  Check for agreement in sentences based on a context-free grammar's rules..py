class ContextFreeGrammar:
    def __init__(self, rules):
        self.rules = rules

    def check_agreement(self, sentence):
        tokens = sentence.split()
        for rule in self.rules:
            if self.match_rule(rule, tokens):
                return True
        return False

    def match_rule(self, rule, tokens):
        if len(rule) != len(tokens):
            return False
        for i, token in enumerate(tokens):
            if token not in rule[i]:
                return False
        return True


# Define context-free grammar rules
rules = [
    ['DT', 'JJ', 'NN', 'VBZ', 'DT', 'JJ', 'NN'],  # The big dog chases the small cat.
    ['DT', 'JJ', 'NN', 'VBZ', 'DT', 'JJ', 'NN', 'PP'],  # The big dog chases the small cat with a stick.
    ['PRP', 'VBZ', 'DT', 'JJ', 'NN'],  # He chases the big dog.
]

# Define token tags
token_tags = {
    'DT': ['the', 'a', 'an'],
    'JJ': ['big', 'small', 'happy'],
    'NN': ['dog', 'cat', 'stick'],
    'VBZ': ['chases', 'runs', 'jumps'],
    'PRP': ['he', 'she', 'it'],
    'PP': ['with', 'in', 'on']
}

# Create grammar
grammar = ContextFreeGrammar(rules)


# Test sentences
sentences = [
    "The big dog chases the small cat.",
    "The big dog chases the small cat with a stick.",
    "He chases the big dog.",
    "The big dog chases the cat.",  # Disagreement
]


# Check agreement
for sentence in sentences:
    tokens = sentence.split()
    tagged_tokens = []
    for token in tokens:
        for tag, values in token_tags.items():
            if token.lower() in values:
                tagged_tokens.append(tag)
                break
    agreement = grammar.check_agreement(' '.join(tagged_tokens))
    print(f"Sentence: {sentence}, Agreement: {agreement}")
