class TopDownParser:
    def __init__(self, grammar):
        self.grammar = grammar
        self.start_symbol = list(grammar.keys())[0]

    def parse(self, input_string):
        return self.parse_recursive(self.start_symbol, input_string)

    def parse_recursive(self, symbol, input_string):
        productions = self.grammar[symbol]

        for production in productions:
            result = self.match_production(production, input_string)

            if result:
                return True

        return False

    def match_production(self, production, input_string):
        if len(production) == 1 and production[0] == input_string:
            return True

        index = 0
        for symbol in production:
            if symbol in self.grammar:
                if not self.parse_recursive(symbol, input_string[index:]):
                    return False
                index += len(input_string[index:].split(symbol)[0]) + 1
            elif symbol != input_string[index]:
                return False
            else:
                index += 1

        return index == len(input_string)


# Define context-free grammar
grammar = {
    'S': [['A', 'B'], ['B', 'A']],
    'A': [['a', 'A'], ['a']],
    'B': [['b', 'B'], ['b']]
}


# Create parser
parser = TopDownParser(grammar)


# Test parser
input_strings = ["aabbb", "ababa", "baaab"]


for input_string in input_strings:
    result = parser.parse(input_string)

    if result:
        print(f"'{input_string}' is accepted by the grammar.")
    else:
        print(f"'{input_string}' is not accepted by the grammar.")

