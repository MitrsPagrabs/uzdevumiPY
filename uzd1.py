import stanza
from collections import Counter

stanza.download('lv')
nlp = stanza.Pipeline('lv', processors='tokenize,lemma')

def word_frequency_analysis(text):
    doc = nlp(text.lower())
    lemmatized_words = [word.lemma for sentence in doc.sentences for word in sentence.words if word.lemma.isalnum()]
    return Counter(lemmatized_words)

text = """
Mākoņainā dienā kaķis sēdēja uz palodzes. Kaķis domāja, kāpēc debesis ir pelēkas. 
Kaķis gribēja redzēt sauli, bet saule slēpās aiz mākoņiem.
"""

result = word_frequency_analysis(text)

for word, count in result.items():
    print(f"{word}: {count}")
