from gensim.models import KeyedVectors
import urllib.request
import gzip
import os

LATVIAN_MODEL_URL = "https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.lv.300.vec.gz"
MODEL_PATH = "cc.lv.300.vec"
CACHE_DIR = "cache"
CACHE_MODEL_PATH = os.path.join(CACHE_DIR, "cc.lv.300.kv")

def download_model(url, output_path):
    if not os.path.exists(output_path):
        print("Modeļa lejupielāde...")
        compressed_file = output_path + ".gz"
        urllib.request.urlretrieve(url, compressed_file)
        print("Lejupielāde pabeigta. Izvilkšana...")
        with gzip.open(compressed_file, "rb") as f_in, open(output_path, "wb") as f_out:
            f_out.write(f_in.read())
        os.remove(compressed_file)
        print("Izvilkšana pabeigta.")
    else:
        print("Modelis jau eksistē. Lejupielādes izlaišana.")

def load_model_with_cache(cache_path, vec_path):
    if not os.path.exists(CACHE_DIR):
        os.makedirs(CACHE_DIR)
        print(f"Izveidota kešatmiņas mape: <{CACHE_DIR}>")

    if os.path.exists(cache_path):
        try:
            print("Ielādē modelis no kešatmiņas...")
            model = KeyedVectors.load(cache_path)
            print("Ielāde no kešatmiņas pabeigta.")
            return model
        except Exception as e:
            print(f"Neizdevās ielādēt modeli no kešatmiņas: {e}. Ielādē no vektora faila...")

    print("Ielādē modelis no vektora faila...")
    model = KeyedVectors.load_word2vec_format(vec_path, binary=False)
    print("Modelis ielādēts. Saglabā kešatmiņā...")
    model.save(cache_path)
    print("Modelis saglabāts kešatmiņā.")
    return model

download_model(LATVIAN_MODEL_URL, MODEL_PATH)

model = load_model_with_cache(CACHE_MODEL_PATH, MODEL_PATH)

words_latvian = ["māja", "dzīvoklis", "jūra", "ūdens", "galva", "kek"]

similarities = {
    (w1, w2): model.similarity(w1, w2)
    for i, w1 in enumerate(words_latvian) for w2 in words_latvian[i + 1:]
}

print("\nSemantisks salidzinājums:")
for pair, similarity in similarities.items():
    print(f"{pair}: {similarity:.4f}")
