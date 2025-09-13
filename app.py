import streamlit as st


from script.datos import importar_datos
from script.normalizar_texto import normalizar

df = importar_datos()

st.title("Buscador de Productos")

buscador =  st.text_input("¿Qué estás buscando?")

if buscador:
    buscador_normalizado = normalizar(buscador)
    df["productos_normalizado"] = df['productos'].apply(normalizar)
    query_buscador = "productos_normalizado.str.contains(@buscador_normalizado)"
    df_filtrado = df.query( query_buscador , engine="python")

    st.write(buscador_normalizado)
    st.dataframe(df_filtrado[['productos', 'Código', 'precio']],  hide_index=True )

else:
    st.write("Ingresa un término para buscar.")



