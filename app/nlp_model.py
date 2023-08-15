# app/nlp_model.py
import torch
from transformers import MarianMTModel, MarianTokenizer

class NLPModel:
    def __init__(self, model_name="Helsinki-NLP/opus-mt-en-ROMANCE"):
        self.model = MarianMTModel.from_pretrained(model_name)
        self.tokenizer = MarianTokenizer.from_pretrained(model_name)

    def translate(self, text, target_language):
        input_text = f"en2{target_language}: {text}"
        input_ids = self.tokenizer.encode(input_text, return_tensors="pt")
        translated_ids = self.model.generate(input_ids)
        translated_text = self.tokenizer.decode(translated_ids[0], skip_special_tokens=True)
        return translated_text
