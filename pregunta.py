"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd
from fuzzywuzzy import fuzz, process


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")

    #
    # Inserte su código aquí
    #

    
    df.sexo = df.sexo.astype('category').str.lower()
    df.tipo_de_emprendimiento = df.tipo_de_emprendimiento.astype('category').str.lower()
    df.idea_negocio = df.idea_negocio.astype('category').str.lower()
    df.barrio = df.barrio.astype('category').str.lower()
    df.estrato = df.estrato.astype('category')
    df.comuna_ciudadano = df.comuna_ciudadano.astype(int).astype('category')
    df.fecha_de_beneficio = pd.to_datetime(df.fecha_de_beneficio, dayfirst=True)
    df.línea_credito = df.línea_credito.str.lower().astype('category')
 
    

    df.monto_del_credito = df.monto_del_credito.str.strip("$")
    df.monto_del_credito = df.monto_del_credito.str.replace(',','')
    df.monto_del_credito = df.monto_del_credito.astype(float).astype(int)

    df.línea_credito = df.línea_credito.str.replace(' ', '_')


    #Linea de formato de tipo despues de las correcciones
    df.línea_credito = df.línea_credito.str.lower().astype('category')

   
    #df = df.drop_duplicates(inplace=True)

    valid_lineas = ["agropecuaria", "ayacucho_formal", "credioportuno", "empresarial_ed.", "juridica_y_cap.semilla", "microempresarial", "solidaria", "fomento_agropecuario"]

    df.línea_credito_ = df.línea_credito.copy()

    #
    # Valor mínimo de similitud para hacer el cambio
    #
    min_threshold = 80

    #
    # Estructuta básica
    #
    for valid_linea in valid_lineas:

        potential_matches = process.extract(
            valid_linea,
            df.línea_credito,
            limit=df.shape[0],
        )

        for potential_match in potential_matches:

            if potential_match[1] >= min_threshold:

                df.loc[df.línea_credito == potential_match[0], "línea_credito_"] = valid_linea

    #print(df[~df.línea_credito.isin({'microempresarial','juridica_y_cap.semilla','fomento_agropecuario','agropecuaria', 'ayacucho_formal', 'empresarial_ed.','creditoportuno','solidaria'})])
    #print(set(df.línea_credito).difference(valid_linea))
    print(df)
    return df

if __name__ == "__main__":
    print(clean_data())
