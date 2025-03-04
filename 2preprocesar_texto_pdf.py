import spacy
from nltk.corpus import stopwords

# Cargar el modelo en español de Spacy
nlp = spacy.load("es_core_news_lg")

# Descargar stopwords de NLTK (si no lo has hecho ya)
import nltk
nltk.download('stopwords')
stop_words = set(stopwords.words('spanish'))

def preprocess_text(text):
    # Procesar el texto con Spacy
    doc = nlp(text)

    # Tokenización y lematización, eliminando stopwords
    processed_tokens = [
        token.lemma_ for token in doc if token.text.lower() not in stop_words and not token.is_punct and not token.is_space
    ]
    
    # Unir los tokens procesados de nuevo en un texto limpio
    clean_text = " ".join(processed_tokens)
    return clean_text

# Cargar el texto limpio que has extraído previamente (deberías ya tener el texto de "clean_text" o "dirty_text")
with open("2020naturgy_clean.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Preprocesar el texto
processed_text = preprocess_text(text)

# Ver los primeros 500 caracteres del texto procesado
print(processed_text[:500])

# Guardar el texto preprocesado en un archivo
with open("2020naturgy_preprocessed.txt", "w", encoding="utf-8") as f:
    f.write(processed_text)
