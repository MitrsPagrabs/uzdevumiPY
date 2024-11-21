import stanza
from googletrans import Translator

stanza.download('en')
nlp = stanza.Pipeline('en')

translator = Translator()

text_lv = "Valsts prezidents Egils Levits piedalījās pasākumā, ko organizēja Latvijas Universitāte. Toms Kolpakovs atrodas Latvijā."

text_en = translator.translate(text_lv, src='lv', dest='en').text

doc = nlp(text_en)

def capitalize_proper_nouns(text):
    words = text.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)

print("\nIdentificētās vienības:")
for sentence in doc.sentences:
    for entity in sentence.ents:
        entity_lv = translator.translate(entity.text, src='en', dest='lv').text
        entity_lv_capitalized = capitalize_proper_nouns(entity_lv)
        entity_type = "PER" if entity.type == "PERSON" else entity.type
        print(f"{entity_lv_capitalized}: {entity_type}")
