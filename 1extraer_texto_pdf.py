import pdfplumber
import re

def clean_text(text):
    # Reemplazar múltiples espacios por uno solo
    text = re.sub(r'\s+', ' ', text)
    # Eliminar líneas vacías
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    # Eliminar líneas que sean solo números (posibles números de página o índices)
    lines = [line for line in lines if not re.fullmatch(r'\d+', line)]
    # Eliminar solo las URLs, pero no toda la línea
    lines = [re.sub(r'http[s]?://\S+', '', line) for line in lines]
    # Normalizar comillas y caracteres raros
    text = "\n".join(lines).replace("“", "\"").replace("”", "\"").replace("’", "'")
    return text

def extract_clean_text(pdf_path):
    text = ""
    # Abrir el PDF
    with pdfplumber.open(pdf_path) as pdf:
        last_header = None  # Guardar encabezado detectado
        last_footer = None  # Guardar pie de página detectado
        total_pages = len(pdf.pages)  # Total de páginas en el PDF
        
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

    # Limpiar el texto extraído
    return text

pdf_path = "2020naturgy.pdf"
output_clean_txt = "2020naturgy_clean.txt"
output_dirty_txt = "2020naturgy_dirty.txt"

# Extraer texto de todas las páginas
dirty_text = extract_clean_text(pdf_path)

# Limpiar el texto extraído
cleaned_text = clean_text(dirty_text)

# Guardar el texto "sucio" sin limpiar
with open(output_dirty_txt, "w", encoding="utf-8") as f:
    f.write(dirty_text)

# Guardar el texto limpio
with open(output_clean_txt, "w", encoding="utf-8") as f:
    f.write(cleaned_text)

print(f"Texto sucio del PDF guardado en {output_dirty_txt}")
print(f"Texto limpio del PDF guardado en {output_clean_txt}")
