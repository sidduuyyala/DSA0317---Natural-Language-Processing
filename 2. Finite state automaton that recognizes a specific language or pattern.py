class FiniteStateAutomaton:
    def __init__(self):
        self.states = ['q0', 'q1', 'q2']  
        self.alphabet = ['a', 'b']  
        self.transitions = {  
            'q0': {'a': 'q1', 'b': 'q0'},
            'q1': {'a': 'q1', 'b': 'q2'},
            'q2': {'a': 'q1', 'b': 'q2'}
        }
        self.initial_state = 'q0'  
        self.accepting_state = 'q2'  

    def run(self, input_string):
        current_state = self.initial_state
        for char in input_string:
            if char in self.alphabet:
                current_state = self.transitions[current_state][char]
            else:
                return False
        return current_state == self.accepting_state
automaton = FiniteStateAutomaton()
strings = ['ab', 'aab', 'bab', 'bba', 'abcab']
for string in strings:
    result = automaton.run(string)
    print(f"Input: {string}, Accepted: {result}")
