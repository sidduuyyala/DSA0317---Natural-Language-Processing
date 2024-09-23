class ParseTree:
    def __init__(self, grammar, start_symbol):
        self.grammar = grammar
        self.start_symbol = start_symbol

    def parse(self, sentence):
        if sentence:
            symbol = self.start_symbol
            production = self.grammar[symbol][0]
            return [symbol, self.parse_sub(production, sentence)]
        return []

    def parse_sub(self, production, sentence):
        result = []
        for symbol in production:
            if symbol in self.grammar:
                result.append([symbol, self.parse_sub(self.grammar[symbol][0], sentence)])
            elif sentence and symbol == sentence[0]:
                result.append(symbol)
                sentence = sentence[1:]
            else:
                return []
        return result

    def print_tree(self, tree, indent=0):
        for node in tree:
            if isinstance(node, list):
                print('  ' * indent + str(node[0]))
                self.print_tree(node[1:], indent + 1)
            else:
                print('  ' * indent + str(node))


# Grammar rules
grammar = {
    'S': [['NP', 'VP']],
    'NP': [['Det', 'N']],
    'VP': [['V', 'NP']],
    'Det': ['the'],
    'N': ['dog', 'cat'],
    'V': ['chases', 'runs']
}


# Start symbol
start_symbol = 'S'


# Sentence
sentence = ['the', 'dog', 'chases', 'the', 'cat']


# Create parse tree
parse_tree = ParseTree(grammar, start_symbol)


# Parse sentence
tree = parse_tree.parse(sentence)


# Print parse tree
parse_tree.print_tree(tree)
