from nltk.tokenize import word_tokenize
import string

def calculate_word_overlap(text1, text2):
    words1 = set(word.lower().strip(string.punctuation) for word in word_tokenize(text1))
    words2 = set(word.lower().strip(string.punctuation) for word in word_tokenize(text2))
    
    common_words = words1 & words2
    
    total_unique_words = len(words1 | words2)
    overlap_percentage = (len(common_words) / total_unique_words) * 100 if total_unique_words > 0 else 0
    
    return common_words, overlap_percentage

text1 = "Rudens lapas ir dzeltenas un oranžas. Lapas klāj zemi un padara to krāsainu."
text2 = "Krāsainas rudens lapas krīt zemē. Lapas ir oranžas un dzeltenas."

common_words, overlap_percentage = calculate_word_overlap(text1, text2)

print(f"Kopīgie vārdi: {', '.join(common_words)}")
print(f"Sakritības līmenis: {overlap_percentage:.2f}%")
