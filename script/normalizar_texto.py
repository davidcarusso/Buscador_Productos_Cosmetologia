import unicodedata

def normalizar(texto):
    if isinstance(texto, str):
        texto = unicodedata.normalize('NFKD', texto)
        texto = texto.encode('ASCII', 'ignore').decode('utf-8')
        return texto.lower()
    return ""
