import nltk
from nltk import CFG
fopc_grammar = CFG.fromstring("""
    S -> EXPR
    EXPR -> PRED | EXPR 'AND' EXPR | EXPR 'OR' EXPR
    PRED -> NAME '(' VARS ')'
    VARS -> VAR | VAR ',' VARS
    NAME -> 'P' | 'Q' | 'R'
    VAR -> 'x' | 'y' | 'z'
    AND -> 'AND'
    OR -> 'OR'
""")
parser = nltk.ChartParser(fopc_grammar)
def parse_expression(expression):
    try:       
        tokens = expression.replace('(', ' ( ').replace(')', ' ) ').replace(',', ' , ').split()
        trees = list(parser.parse(tokens))
        if trees:
            for tree in trees:
                tree.pretty_print()
        else:
            print("No valid parse found.")
    except ValueError as e:
        print(f"Error: {e}")
expressions = [
    "P(x,y)",
    "Q(x) AND R(y,z)",
    "P(x) OR Q(y) AND R(z)"
]
for expr in expressions:
    print(f"Parsing expression: {expr}")
    parse_expression(expr)
    print()