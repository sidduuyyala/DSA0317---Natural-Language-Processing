class PluralFSM:
    def __init__(self):
        self.states = ['SINGULAR', 'PLURAL']
        self.alphabet = ['y', 'ies', 'es', 's']
        self.transitions = {
            'SINGULAR': {
                'y': ('PLURAL', 'ies'),
                'ies': ('PLURAL', 'ies'),
                'es': ('PLURAL', 'es'),
                's': ('PLURAL', 's')
            }
        }
        self.initial_state = 'SINGULAR'
        self.current_state = self.initial_state

    def pluralize(self, word):
        self.current_state = self.initial_state
        if word.endswith('y'):
            return word[:-1] + 'ies'
        elif word.endswith('is') or word.endswith('ch') or word.endswith('sh'):
            return word + 'es'
        elif word.endswith('s') or word.endswith('x') or word.endswith('z'):
            return word + 'es'
        else:
            return word + 's'
plural_fsm = PluralFSM()
words = ['cat', 'city', 'brush', 'box', 'quiz']
for word in words:
    plural = plural_fsm.pluralize(word)
    print(f"{word} -> {plural}")


