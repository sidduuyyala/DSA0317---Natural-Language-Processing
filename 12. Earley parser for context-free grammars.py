def earley_parse(grammar, start_symbol, input_string):
    def predict(state):
        symbol, dot, production = state
        if dot < len(production):
            next_symbol = production[dot]
            if next_symbol in grammar:
                return [(next_symbol, 0, grammar[next_symbol][0])]
        return []

    def scan(state, token):
        symbol, dot, production = state
        if dot < len(production):
            next_symbol = production[dot]
            if next_symbol == token:
                return [(symbol, dot + 1, production)]
        return []

    def complete(state, start):
        symbol, dot, production = state
        if dot == len(production):
            return [(symbol, start, production)]
        return []

    chart = [[] for _ in range(len(input_string) + 1)]
    chart[0].append((start_symbol, 0, grammar[start_symbol][0]))

    for i in range(len(input_string) + 1):
        for state in chart[i]:
            chart[i] += predict(state)
            if i < len(input_string):
                chart[i + 1] += scan(state, input_string[i])
            chart[i] += complete(state, i)

    return chart[-1]


# Grammar rules
grammar = {
    'S': [['A', 'B']],
    'A': [['a', 'A'], []],
    'B': [['b', 'B'], []]
}


# Start symbol
start_symbol = 'S'


# Test input string
input_string = "aabbb"


# Parse input string
result = earley_parse(grammar, start_symbol, input_string)


# Print result
if result:
    print(f"'{input_string}' is accepted by the grammar.")
else:
    print(f"'{input_string}' is not accepted by the grammar.")

