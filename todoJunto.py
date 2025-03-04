import os
import pdfplumber
import re
import spacy
import nltk
from nltk.corpus import stopwords

# Cargar modelo avanzado de spaCy para español
nlp = spacy.load("es_core_news_lg")

# Descargar stopwords de NLTK (si no lo has hecho ya)
nltk.download('stopwords')
stop_words = set(stopwords.words('spanish'))

# Definir la taxonomía con categorías de TCFD
TAXONOMY = {
    "gobernanza": [
        "consejo administración", "comité de sostenibilidad", "directivos", "responsabilidad",
        "supervisión", "gobernanza", "estrategia corporativa", "decisiones estratégicas",
        "transparencia", "información financiera", "comités de riesgos", "cultura corporativa",
        "junta", "gerencia", "directorio", "remuneración", "periodicidad", "seguimiento"
    ],
    "estrategia": [
        "riesgos climáticos", "oportunidades ambientales", "impacto financiero", "escenarios climáticos",
        "planificación a largo plazo", "transición energética", "resiliencia", "modelos de negocio sostenibles",
        "innovación tecnológica", "adaptación al cambio climático", "estrategias de mitigación", 
        "sostenibilidad", "carbono neto cero", "descarbonización", "riesgos de cambio climático", 
        "riesgos de transición", "riesgos físicos", "préstamos verdes", "clima extremo", "reducción de costos", 
        "impacto", "riesgos reputacionales", "estándares", "estrategia", "uso de tecnología", "energía renovable"
    ],
    "gestion_riesgos": [
        "evaluación de riesgos", "planes de mitigación", "factores de riesgo", "exposición financiera",
        "riesgos físicos", "riesgos transicionales", "gestión de la cadena de suministro", "estrategias de adaptación",
        "gestión de impacto climático", "impacto económico de los riesgos", "seguridad climática", "gestión de desastres",
        "riesgo legal", "riesgo reputacional", "riesgo financiero", "regulación", "acuerdos internacionales",
        "respuesta al riesgo", "materialidad", "precio del carbono", "litigios", "energías renovables", 
        "costos de transición", "sistemas integrados de gestión", "control de gestión de riesgos"
    ],
    "metricas_objetivos": [
        "huella de carbono", "emisiones de CO2", "objetivos de reducción", "indicadores de sostenibilidad",
        "emisiones netas", "información climática", "energías renovables", "medición de huella ecológica",
        "rendimiento sostenible", "reporte de sostenibilidad", "certificación ambiental", "contribución climática",
        "objetivos de sostenibilidad", "reducción de CO2", "emisiones de GEI", "consumo de energía", 
        "consumo de agua", "consumo de combustible", "intensidad"
    ]
}

def clean_text(text):
    # Reemplazar múltiples espacios por uno solo
    text = re.sub(r'\s+', ' ', text)
    # Eliminar líneas vacías
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    # Eliminar líneas que sean solo números (posibles números de página o índices)
    lines = [line for line in lines if not re.fullmatch(r'\d+', line)]
    # Eliminar las URLs
    lines = [re.sub(r'http[s]?://\S+', '', line) for line in lines]
    # Normalizar comillas
    text = "\n".join(lines).replace("“", "\"").replace("”", "\"").replace("’", "'")
    return text

def extract_clean_text(pdf_path):
    text = ""
    # Abrir el PDF
    with pdfplumber.open(pdf_path) as pdf:
        last_header = None  # Guardar encabezado detectado
        last_footer = None  # Guardar pie de página detectado
        total_pages = len(pdf.pages)
        
        # Procesar todas las páginas
        for i, page in enumerate(pdf.pages):
            page_text = page.extract_text()
            if page_text:
                lines = page_text.split("\n")
                
                # Detectar encabezados repetidos
                if last_header is None:
                    last_header = lines[0]
                elif lines[0] == last_header:
                    lines = lines[1:]  # Eliminar encabezado repetido
                
                # Detectar pies de página repetidos
                if last_footer is None:
                    last_footer = lines[-1]
                elif lines[-1] == last_footer:
                    lines = lines[:-1]  # Eliminar pie de página repetido
                
                # Acumular el texto procesado
                text += "\n".join(lines) + "\n"
                
            # Mostrar comentario cada 50 páginas
            if (i + 1) % 50 == 0:
                print(f"Procesando página {i + 1} de {total_pages}...")

    return text

def preprocess_text(text):

    nlp.max_length = 2000000  # Ajusta este valor si el texto es aún más largo

    # Procesar el texto con Spacy
    doc = nlp(text)

    # Tokenización y lematización, eliminando stopwords
    processed_tokens = [
        token.lemma_ for token in doc if token.text.lower() not in stop_words and not token.is_punct and not token.is_space
    ]
    
    # Unir los tokens procesados de nuevo en un texto limpio
    clean_text = " ".join(processed_tokens)
    return clean_text


def search_text_for_tcfd(text, taxonomy):
    results = {category: [] for category in taxonomy.keys()}
    
    for category, keywords in taxonomy.items():
        for keyword in keywords:
            pattern = rf"\b{keyword}\b|\b{keyword.replace(' ', '[_-]?')}\b"
            matches = re.findall(pattern, text, re.IGNORECASE)
            if matches:
                results[category].append((keyword, len(matches)))
                
    return results

# Ajustar estos valores como se quiera!!
def calculate_tcfd_compliance(results):
    scores = {}
    for category, matches in results.items():
        if not matches:
            scores[category] = 0
        elif len(matches) < 3:
            scores[category] = 1
        elif len(matches) < 6:
            scores[category] = 2
        else:
            scores[category] = 3
    return scores

def process_pdf(pdf_path):
    dirty_text = extract_clean_text(pdf_path)
    cleaned_text = clean_text(dirty_text)
    processed_text = preprocess_text(cleaned_text)
    
    matches = search_text_for_tcfd(processed_text, TAXONOMY)
    tcfd_compliance = calculate_tcfd_compliance(matches)
    
    return tcfd_compliance

def main():
    results = []
    
    # Verificar si hay una subcarpeta "pdfs"
    pdf_folder = "pdfs"
    if not os.path.exists(pdf_folder):
        pdf_folder = os.getcwd()  # Si no existe, procesar en el directorio actual
    
    # Obtener todos los archivos .pdf en la carpeta "pdfs"
    pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith(".pdf")]
    
    for pdf_file in pdf_files:
        pdf_path = os.path.join(pdf_folder, pdf_file)
        print(f"Procesando: {pdf_file}")
        
        # Procesar el PDF y obtener resultados de cumplimiento TCFD
        tcfd_compliance = process_pdf(pdf_path)
        
        # Guardar los resultados para cada PDF
        results.append(f"=== RESULTADOS DEL PDF {pdf_file} ===")
        for category, score in tcfd_compliance.items():
            results.append(f"{category.upper()}: {score}/3")
        results.append("\n")

    # Guardar todos los resultados en un archivo
    with open("resultadosCumplimientoTCFD.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(results))

    print("Análisis completado. Resultados guardados en 'resultadosCumplimientoTCFD.txt'.")

if __name__ == "__main__":
    main()
