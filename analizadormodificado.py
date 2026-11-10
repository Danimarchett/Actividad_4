def contar_frecuencias(texto):
    """
    Cuenta la frecuencia de cada palabra en un texto, 
    ignorando mayúsculas y signos de puntuación básicos.

    Parametros:
        texto (str): el texto a analizar

    Retorna:
        dict: pares {palabra: frecuencia}
    """
    # 1. Pasamos todo a minúsculas
    texto = texto.lower()
    
    # 2. Reemplazamos los signos de puntuación por espacios vacíos
    for signo in ["¡", "!", "¿", "?", ",", ".", ";", ":"]:
        texto = texto.replace(signo, "")
        
    # 3. Separamos las palabras
    palabras = texto.split()
    
    # 4. Contamos las frecuencias en un diccionario
    frecuencias = {}
    for palabra in palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
        
    return frecuencias