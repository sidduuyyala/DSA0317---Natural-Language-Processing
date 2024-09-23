words = ['dog', 'chases', 'big']
pos_tags = ['NN', 'VB', 'JJ']

# Define emission probabilities
emission_prob = {
    'NN': {'dog': 0.8},
    'VB': {'chases': 0.9},
    'JJ': {'big': 0.7}
}

# Initialize POS tags sequence
pos_tags_sequence = []

# Assign POS tags
for word in words:
    max_prob = 0
    max_tag = None
    for tag in pos_tags:
        prob = emission_prob[tag].get(word, 0)
        if prob > max_prob:
            max_prob = prob
            max_tag = tag
    pos_tags_sequence.append(max_tag)

# Print POS tags sequence
print('POS Tags Sequence:', pos_tags_sequence)
