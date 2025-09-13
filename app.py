import streamlit as st


from script.datos import importar_datos
from script.normalizar_texto import normalizar
from script.tarjetas_productos import tarjetas_productos



df = importar_datos()

st.title("Buscador de Productos")


col1, col2 = st.columns([3,1])

with col1:
    buscador =  st.text_input("¿Qué estás buscando?")

with col2:
    vista = st.radio("Modo de visualización:", ["Tabla", "Tarjetas"])

if buscador:

    buscador_normalizado = normalizar(buscador)
    productos_normalizado = df['productos'].apply(normalizar)
    mask = productos_normalizado.str.contains(buscador_normalizado)
    df_filtrado = df[mask]

    st.write(f"Estas buscando: {buscador_normalizado}")

    if vista == "Tabla":
        st.dataframe(df_filtrado,  hide_index=True )

    elif vista == "Tarjetas":
        tarjetas_productos(df_filtrado)
  

else:
    st.write("Ingresa un término para buscar.")



