from transformers import MarianTokenizer, MarianMTModel

model_name = "Helsinki-NLP/opus-mt-lv-en"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

def translate_to_english(texts):
    inputs = tokenizer(texts, return_tensors="pt", padding=True, truncation=True)
    translated_tokens = model.generate(**inputs)
    translations = [tokenizer.decode(t, skip_special_tokens=True) for t in translated_tokens]
    return translations

texts_lv = [
    "Labdien! Kā jums klājas?",
    "Es šodien lasīju interesantu grāmatu.",
    "Es tūlit sevi nogalināšu"
]

translations_en = translate_to_english(texts_lv)

for lv, en in zip(texts_lv, translations_en):
    print(f"Latviski: {lv}")
    print(f"Angliski: {en}")
    print()
