from textblob import TextBlob
from googletrans import Translator
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk

nltk.download('punkt')
nltk.download('stopwords')

LATVIAN_STOPWORDS = set(["ir", "un", "vai", "es", "tu", "viņš", "viņa", "mēs", "jūs", "viņi", "tas", "tā", "ka", "par", "ar", "no", "uz", "pie", "zem", "virs", "kā", "tik", "to", "šis", "šī", "šos", "šīs", "bet", "lai", "kur", "kad", "kamēr", "tad", "tas", "tie", "tās", "tur", "šeit", "tādēļ", "tāpēc", "jo", "kāpēc", "ļoti"])

translator = Translator()

def analyze_sentiment_latvian(sentence):
    neutral_phrases = ["neitrāls", "nekas īpašs", "parasts", "vidējs"]

    if any(phrase in sentence.lower() for phrase in neutral_phrases):
        return "Neitrāls"

    tokens = word_tokenize(sentence.lower())
    filtered_tokens = [word for word in tokens if word not in LATVIAN_STOPWORDS]

    if not filtered_tokens:
        return "Neitrāls"

    translation = translator.translate(" ".join(filtered_tokens), src='lv', dest='en')
    translated_text = translation.text

    blob = TextBlob(translated_text)
    polarity = blob.sentiment.polarity

    if -0.3 <= polarity <= 0.3:
        return "Neitrāls"
    elif polarity > 0.3:
        return "Pozitīvs"
    else:
        return "Negatīvs"

sentences = [
    "Šis produkts ir lielisks, esmu ļoti apmierināts!",
    "Esmu vīlies, produkts neatbilst aprakstam.",
    "Neitrāls produkts, nekas īpašs.",
    "Labs produkts!",
    "Ļoti slikts produkts!",
    "Vidēji"
]

for i, sentence in enumerate(sentences, 1):
    sentiment = analyze_sentiment_latvian(sentence)
    print(f"Teikums {i}: '{sentence}' -> Noskaņojums: {sentiment}")
