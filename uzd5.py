import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')

def clean_and_normalize_text(text):
    text = text.lower()
    
    text = ' '.join(word for word in text.split() if not word.startswith(('http', '@')))
    
    text = text.replace('!!!', '!').replace('!!', '!')
    text = text.replace('??', '?').replace('???', '?')
    
    tokens = word_tokenize(text)
    
    tokens = [token for token in tokens if token.isalnum() or token in ['!', '?', '.', ',']]
    
    return ' '.join(tokens).replace(' !', '!').replace(' ?', '?').replace(' .', '.')

raw_text = "@John: Šis ir lielisks produkts##@!!!!!! Vai ne? 👏 👏 👏 http://example.com"

cleaned_text = clean_and_normalize_text(raw_text)

print("Oriģinālais teksts:", raw_text)
print("Tīrs teksts:", cleaned_text)
