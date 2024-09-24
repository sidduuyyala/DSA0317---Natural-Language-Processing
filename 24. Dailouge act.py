import nltk
from nltk.tokenize import word_tokenize
dialog = ["Hi, how are you?", "I'm good, thank you!", "What's your name?", "My name is John."]
def recognize_dialog_act(utterance):
    tokens = word_tokenize(utterance.lower())
    if tokens[0] in ['hi', 'hello']:
        return 'Greeting'
    elif tokens[-1] == '?':
        return 'Question'
    elif tokens[0] in ['thanks', 'thank']:
        return 'Thanks'
    else:
        return 'Statement'
for utterance in dialog:
    act = recognize_dialog_act(utterance)
    print(f"Utterance: '{utterance}' => Dialog Act: {act}")