import pandas as pd

def importar_datos():
    sheet_id = "1ytGK55mhfm-GmGpj7-rAU9ue0DKcizlA"
    sheet_name = "AGOSTO%202025"
    URL_PATH = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

    df = pd.read_csv(URL_PATH)

    df = df[["SKINCARE FACIAL LIMPIEZA Descripción general", "Código", "Precio"]]
    df = df.rename(columns={"SKINCARE FACIAL LIMPIEZA Descripción general": "productos"})
    df = df.rename(columns={"Precio": "precio"})
    df["productos"] = df["productos"].str.title()
   

    return df





