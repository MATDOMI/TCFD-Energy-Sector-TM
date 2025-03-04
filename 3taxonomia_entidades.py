import spacy
import re
from collections import defaultdict

# Cargar modelo avanzado de spaCy para español
nlp = spacy.load("es_core_news_lg")

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


def search_text_for_tcfd(text, taxonomy):
    results = {category: [] for category in taxonomy.keys()}
    
    for category, keywords in taxonomy.items():
        for keyword in keywords:
            pattern = rf"\b{keyword}\b|\b{keyword.replace(' ', '[_-]?')}\b"
            matches = re.findall(pattern, text, re.IGNORECASE)
            if matches:
                results[category].append((keyword, len(matches)))
                
    return results

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

# Cargar el texto preprocesado
with open("2020naturgy_preprocessed.txt", "r", encoding="utf-8") as f:
    processed_text = f.read()

# Buscar menciones de términos clave TCFD
matches = search_text_for_tcfd(processed_text, TAXONOMY)

# Calcular el índice de cumplimiento basado en las reglas definidas
tcfd_compliance = calculate_tcfd_compliance(matches)

# Guardar los resultados en un archivo
with open("tcfd_compliance_results.txt", "w", encoding="utf-8") as f:
    f.write("=== RESULTADOS DEL ANÁLISIS DE CUMPLIMIENTO TCFD ===\n")
    for category, score in tcfd_compliance.items():
        f.write(f"{category.upper()}: {score}/3\n")

print("\nAnálisis completado. Resultados guardados en 'tcfd_compliance_results.txt'.")
