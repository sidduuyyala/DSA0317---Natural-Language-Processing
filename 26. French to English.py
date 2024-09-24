from translate import Translator
def translate_to_french(text):
    translator = Translator(to_lang="fr")
    translation = translator.translate(text)
    return translation
def main():
    while True:
        english_text = input("Enter English text to translate to French (or type 'exit' to quit): ")
        if english_text.lower() == 'exit':
            break
        french_text = translate_to_french(english_text)
        print(f'French: {french_text}')
if __name__ == "__main__":
    main()