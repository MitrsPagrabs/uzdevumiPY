from transformers import GPT2LMHeadModel, GPT2Tokenizer
from googletrans import Translator
import stanza
import re

stanza.download('lv')
nlp = stanza.Pipeline('lv')

model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

if tokenizer.pad_token_id is None:
    tokenizer.pad_token_id = tokenizer.eos_token_id

prompt_en = "Once upon a time in a distant land"

input_ids = tokenizer.encode(prompt_en, return_tensors="pt")
attention_mask = (input_ids != tokenizer.pad_token_id).long()

output = model.generate(
    input_ids,
    attention_mask=attention_mask,
    max_length=120,
    num_return_sequences=1,
    no_repeat_ngram_size=3,
    top_k=50,
    top_p=0.9,
    temperature=0.8,
    do_sample=True,
    pad_token_id=tokenizer.pad_token_id,
)

generated_text_en = tokenizer.decode(output[0], skip_special_tokens=True)

def clean_generated_text(text):
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'\d+', '', text)
    sentences = text.split('. ')
    unique_sentences = []
    for sentence in sentences:
        sentence = sentence.strip()
        if sentence and sentence not in unique_sentences:
            unique_sentences.append(sentence + '.')
    return ' '.join(unique_sentences[:4])

generated_text_en = clean_generated_text(generated_text_en)

translator = Translator()
try:
    generated_text_lv = translator.translate(generated_text_en, src="en", dest="lv").text
except Exception as e:
    print(f"Tulkošanas kļūda: {e}")
    generated_text_lv = generated_text_en

def stanza_correction(text):
    doc = nlp(text)
    corrected_text = []
    for sentence in doc.sentences:
        tokens = [word.text.capitalize() if i == 0 else word.text for i, word in enumerate(sentence.words)]
        corrected_text.append(' '.join(tokens))
    return ' '.join(corrected_text)

generated_text_lv = stanza_correction(generated_text_lv)

def finalize_text(text):
    doc = nlp(text)
    corrected_tokens = []
    for word in text.split():
        if word.lower() in [entity.text.lower() for entity in doc.entities]:
            corrected_tokens.append(word.capitalize())
        else:
            corrected_tokens.append(word)
    text = ' '.join(corrected_tokens)

    text = re.sub(r'\s+([,.?!:;])', r'\1', text)
    text = re.sub(r'([,.?!:;])(\w)', r'\1 \2', text)
    text = text.strip('. ') + '.'

    text = re.sub(r'"\s+', '"', text)
    text = re.sub(r'\s+"', '"', text)

    open_quotes = text.count('"') % 2
    if open_quotes == 1:
        text += '"'

    return text

generated_text_lv = finalize_text(generated_text_lv)

print("Ģenerētais teksts (latviešu valodā):")
print(generated_text_lv)
#no comments
