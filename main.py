# main.py
from app.translator import Translator
from app.nlp_model import NLPModel

def main():
    translator = Translator()
    nlp_model = NLPModel()

    while True:
        text = input("Enter the text to translate or type 'exit' to quit: ")
        if text.lower() == 'exit':
            break

        target_language = input("Enter the target language code (e.g., 'fr' for French): ")
        translated_text = translator.translate(text, target_language)
        nlp_translated_text = nlp_model.translate(text, target_language)

        print("Translated Text (Transformer):", translated_text)
        print("Translated Text (NLP Model):", nlp_translated_text)

if __name__ == "__main__":
    main()
