import pdfplumber
import spacy
import re
import json
import argparse
import sys
import time
from unidecode import unidecode

# Cargar modelo de spaCy para reconocimiento de entidades
nlp = spacy.load("es_core_news_lg")

# Etiquetas NER relevantes
etiquetas_validas = {"PER", "ORG", "LOC", "DATE", "GPE", "MONEY", "PRODUCT"}

def mostrar_progreso(actual, total):
    porcentaje = (actual / total) * 100
    barra = "#" * int(porcentaje // 2) + "-" * (50 - int(porcentaje // 2))
    sys.stdout.write(f"\r[{barra}] {porcentaje:.2f}%")
    sys.stdout.flush()

def extraer_texto(pdf_path):
    texto_completo = ""
    with pdfplumber.open(pdf_path) as pdf:
        total_paginas = len(pdf.pages)
        for i, pagina in enumerate(pdf.pages):
            texto_pagina = pagina.extract_text()
            if texto_pagina:
                texto_completo += texto_pagina.replace("\n", " ") + " "
            mostrar_progreso(i + 1, total_paginas) # Mostrar progreso de extracción
    return texto_completo.strip()

def limpiar_texto(texto):
    texto = unidecode(texto)  # Elimina acentos
    texto = re.sub(r"[^a-zA-Z0-9áéíóúÁÉÍÓÚñÑ\s.,;:!?()]", " ", texto)  # Mantiene solo caracteres útiles
    texto = re.sub(r"\s+", " ", texto).strip()  # Reemplaza múltiples espacios por uno solo
    texto = re.sub(r"\b\d+\b", "", texto)  # Elimina números aislados
    return texto

def buscar_palabras(texto, palabras):
    return {palabra: bool(re.search(rf"\b{re.escape(palabra)}\b", texto, re.IGNORECASE)) for palabra in palabras}

def reconocer_entidades(texto):
    doc = nlp(texto)
    entidades_contadas = {}

    for ent in doc.ents:
        if ent.label_ in etiquetas_validas:
            entidad_texto = ent.text.strip().lower()
            entidad_tipo = ent.label_
            if len(entidad_texto) < 3:
                continue
            if entidad_tipo not in entidades_contadas:
                entidades_contadas[entidad_tipo] = {}
            entidades_contadas[entidad_tipo][entidad_texto] = entidades_contadas[entidad_tipo].get(entidad_texto, 0) + 1
    return entidades_contadas

def analizar_pdf(pdf_path, palabras_clave, num_archivo, total_archivos):
    print(f"\n Analizando archivo {num_archivo}/{total_archivos}: {pdf_path}")

    texto = extraer_texto(pdf_path)
    print("\n Extracción completada. Limpiando texto...")

    texto_limpio = limpiar_texto(texto)
    print(" Limpieza completada. Buscando palabras clave...")

    busqueda = buscar_palabras(texto_limpio, palabras_clave)
    print(" Búsqueda completada. Reconociendo entidades...")

    entidades = reconocer_entidades(texto_limpio)
    print(" Análisis de entidades completado.")

    return {
        "archivo": pdf_path,
        "busqueda": busqueda,
        "entidades": entidades
    }

def main():
    parser = argparse.ArgumentParser(description="Análisis de texto en PDFs con búsqueda de palabras clave y NER.")
    parser.add_argument("pdfs", nargs="+", help="Lista de archivos PDF a analizar.")
    parser.add_argument("--palabras", nargs="+", required=True, help="Palabras clave a buscar en los documentos.")

    args = parser.parse_args()
    pdfs = args.pdfs
    palabras_clave = args.palabras

    print(f" Analizando {len(pdfs)} archivos con palabras clave: {palabras_clave}")

    resultados = []
    for i, pdf in enumerate(pdfs):
        resultados.append(analizar_pdf(pdf, palabras_clave, i + 1, len(pdfs)))
        time.sleep(1)  # Pequeña pausa para mejor visualización del progreso

    # Guardar resultados en JSON
    with open("analisis_texto.json", "w", encoding="utf-8") as json_file:
        json.dump(resultados, json_file, indent=4, ensure_ascii=False)

    print("\n Análisis completado. Resultados guardados en 'analisis_texto.json'")

if __name__ == "__main__":
    main()
