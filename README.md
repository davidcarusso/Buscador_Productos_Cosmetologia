# Buscador de Productos

Esta aplicación está desarrollada con **Streamlit** y permite buscar productos dentro de un DataFrame de forma flexible, ignorando tildes y mayúsculas. Es ideal para catálogos de productos donde los usuarios pueden escribir términos de búsqueda sin preocuparse por acentos o capitalización.

## Características

- Búsqueda por texto en la columna `productos`.
- Normalización del texto para eliminar tildes y convertir a minúsculas.
- Uso de `pandas.query()` con `engine='python'` para realizar el filtrado.
- Visualización de los resultados en una tabla con las columnas: `productos`, `Código` y `precio`.
- Ocultación del índice en la tabla para una presentación más limpia.

## Funcionamiento

1. El usuario ingresa un término en el campo de búsqueda.
2. El término se normaliza mediante la función `normalizar`, que elimina acentos y convierte el texto a minúsculas.
3. La columna `productos` del DataFrame también se normaliza.
4. Se realiza una consulta con `df.query()` para filtrar los productos que contienen el término buscado.
5. Se muestran los resultados en una tabla interactiva.

## Función de normalización

```python
import unicodedata

def normalizar(texto):
    if isinstance(texto, str):
        texto = unicodedata.normalize('NFKD', texto)
        texto = texto.encode('ASCII', 'ignore').decode('utf-8')
        return texto.lower()
    return ""



## Requisitos
- Python 3.8+
- Streamlit
- Pandas

## Ejecución

streamlit run app.py
