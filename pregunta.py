"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd

def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col=0)

    #Se modifican las columnas para un formato correcto
    #Sexo
    df.sexo = df.sexo.str.lower()
    #tipo_de_emprendimiento
    df.tipo_de_emprendimiento = df.tipo_de_emprendimiento.str.lower()
    #idea_negocio
    df.idea_negocio = df.idea_negocio.str.lower()
    df.idea_negocio = df.idea_negocio.str.replace(' ', '_')
    df.idea_negocio = df.idea_negocio.str.replace('-', '_')
    #barrio
    df.barrio = df.barrio.str.lower()
    df.barrio = df.barrio.str.replace(' ', '_')
    df.barrio = df.barrio.str.replace('-', '_')
    #comuna_ciudadano
    df.comuna_ciudadano = df.comuna_ciudadano.astype(int)
    #fecha_de_beneficio
    df.fecha_de_beneficio = pd.to_datetime(df.fecha_de_beneficio, dayfirst=True)
    #monto_del_credito
    df.monto_del_credito = df.monto_del_credito.str.strip("$")
    df.monto_del_credito = df.monto_del_credito.str.replace(',','')
    df.monto_del_credito = df.monto_del_credito.astype(float)
    #línea_credito
    df.línea_credito = df.línea_credito.str.lower()
    df.línea_credito = df.línea_credito.str.replace(' ', '_')
    df.línea_credito = df.línea_credito.str.replace('-', '_')

    #Se eliminan las filas duplicadas y las columnas de los datos nan o faltantes
    df.dropna(axis = 0, inplace = True)
    df.drop_duplicates(inplace = True)

    return df

if __name__ == "__main__":
    print(clean_data())
