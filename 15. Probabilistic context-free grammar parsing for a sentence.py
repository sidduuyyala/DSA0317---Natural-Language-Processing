def check_agreement(sentence):
    subject = sentence.split()[0]
    verb = sentence.split()[1]
    if subject.endswith('s') and verb.endswith('es'):
        return True
    return False

sentence = "The dogs chase."
print(check_agreement(sentence))  # True



