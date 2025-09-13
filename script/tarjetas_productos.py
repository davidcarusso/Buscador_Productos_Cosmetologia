import streamlit as st

# def tarjetas_productos(df_filtrado):
#     for _, row in df_filtrado.iterrows():
#         with st.container():
#             st.subheader(row['productos'])
#             st.write(f"**Presentación:** {row['presentacion']}")
#             st.write(f"**Código:** {row['Código']}")
#             st.write(f"**Precio:** ${row['precio']}")
#             st.divider()


def tarjetas_productos(df_filtrado):
    for _, row in df_filtrado.iterrows():
        with st.container():
            # una fila con columnas para ordenar mejor
            col1, col2 = st.columns([3, 1])

            with col1:
                st.subheader(row["productos"])
                st.write(f"**Presentación:** {row['presentacion']}")
                st.write(f"**Código:** {row['Código']}")
                st.write(f"**Precio:** {row['precio']}")

            with col2:
                st.markdown("🛒")  # lugar para un ícono o botón futuro

            st.divider()  # separador entre productos