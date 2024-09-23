import spacy

# Load the SpaCy model
nlp = spacy.load("en_core_web_sm")

def perform_ner(text):
    # Process the text using SpaCy NLP pipeline
    doc = nlp(text)
    
    # Extract and print named entities
    for ent in doc.ents:
        print(f"Entity: {ent.text}, Label: {ent.label_}")

# Example usage
text = "Apple is looking at buying U.K. startup for $1 billion. Elon Musk is the CEO of SpaceX."

perform_ner(text)
