import streamlit as st


from script.datos import importar_datos


df = importar_datos()

st.title("Buscador de Productos")

buscador =  st.text_input("¿Qué estás buscando?").lower()

query_buscador = f"productos.str.lower().str.contains('{buscador}')"
df_filtrado = df.query( query_buscador , engine="python")

if buscador:
    st.dataframe(df_filtrado,  hide_index=True )

else:
    st.write("Ingresa un término para buscar.")



