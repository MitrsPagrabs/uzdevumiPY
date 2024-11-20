import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from collections import Counter

nltk.download('punkt')

def summarize_text(text, num_sentences=2):
    sentences = sent_tokenize(text)
    words = word_tokenize(text.lower())

    words = [word for word in words if word.isalnum()]

    word_freq = Counter(words)

    sentence_scores = {}
    for sentence in sentences:
        sentence_word_count = word_tokenize(sentence.lower())
        sentence_score = sum(word_freq[word] for word in sentence_word_count if word in word_freq)
        sentence_scores[sentence] = sentence_score

    summarized_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]
    return ' '.join(summarized_sentences)

article = """
Latvija ir valsts Baltijas reģionā. Tās galvaspilsēta ir Rīga, kas ir slavena ar savu vēsturisko centru un skaistajām ēkām.
Latvija robežojas ar Lietuvu, Igauniju un Krieviju, kā arī tai ir piekļuve Baltijas jūrai. Tā ir viena no Eiropas Savienības dalībvalstīm.
"""

summary = summarize_text(article, num_sentences=2)
print("Rezumējums:", summary)
