# app/translator.py
import transformers
from transformers import pipeline

class Translator:
    def __init__(self, model_name="Helsinki-NLP/opus-mt-en-ROMANCE"):
        self.translator = pipeline("translation", model=model_name)

    def translate(self, text, target_language):
        translated_text = self.translator(text, target_lang=target_language)[0]['translation_text']
        return translated_text
