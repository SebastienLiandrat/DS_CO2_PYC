# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 12:29:59 2023

@author: sebastien.liandrat
"""

import streamlit as st
import time
import numpy as np
import joblib
import pandas as pd

import sklearn


st.set_page_config(page_title="Modèles", page_icon="📈")


st.markdown("# Modélisation")
st.write('## Liste des modèles testés')

st.markdown('- Lasso')
st.markdown('- Ridge')
st.markdown('- Gradient Boosting Regressor')
st.markdown('- Random Forest Regressor')

dossier_local = "C:/Users/sebastien.liandrat/Box/Dossier Personnel de Sébastien LIANDRAT/Codes/Projet DataScientest/"

X_reduit = pd.read_csv(dossier_local + "Streamlit/Ressources/" + "X_reduit.csv", index_col = 0) 



st.write('### Scores obtenus')

scores = [['Lasso', 0.808],['Ridge', 0.830], ['Gradient Boosting', 0.928],['Random Forest', 0.960]]
df_scores = pd.DataFrame(scores, columns = ['Modèle','Score'])

if st.checkbox('Affichage'):
    st.write(df_scores)


st.write('## Focus sur le Random Forest Regressor')




if st.checkbox("Chargement du modèle avec joblib"):
    RFregr=joblib.load(dossier_local + "Streamlit/Ressources/" + 'RFregr2.pkl')
    st.write(RFregr)
    
    if st.checkbox("Afficher les paramètres"):
        st.write(RFregr.get_params())





df_2 = pd.read_csv(dossier_local + "Streamlit/Ressources/" + "data_500.csv", index_col = 0) 

Country = st.selectbox( label = "Choix de Country", options = df_2["Country"].unique())

Mp = st.selectbox( label = "Choix de Mp", options = df_2[df_2["Country"]==Country]["Mp"].unique())

Cn = st.selectbox( label = "Choix de Cn", options = df_2[(df_2["Mp"] == Mp) 
                                                         & (df_2["Country"]==Country) ]['Cn'].unique())

Ft = st.selectbox( label = "Choix de Ft", options = df_2[(df_2["Mp"] == Mp) 
                                                         & (df_2["Country"]==Country)
                                                         & (df_2["Cn"]==Cn)]['Ft'].unique())




def dataframe_with_selections(df):
    df_with_selections = df.copy()
    df_with_selections.insert(0, "Select", False)

    # Get dataframe row-selections from user with st.data_editor
    edited_df = st.data_editor(
        df_with_selections,
        hide_index=True,
        column_config={"Select": st.column_config.CheckboxColumn(required=True)},
        disabled=df.columns,
    )

    # Filter the dataframe using the temporary column, then drop the column
    selected_rows = edited_df[edited_df.Select]
    return selected_rows.drop('Select', axis=1)


df_display = df_2[(df_2["Country"] == Country) &
   (df_2["Mp"] == Mp) &
   (df_2["Cn"] == Cn) &
   (df_2["Ft"] == Ft)
            ]

df_display = df_display.drop(columns = ["index", "ID"])

selection = dataframe_with_selections(df_display)
st.write("Véhicule sélectionné :")
st.write(selection)

target = selection["Ewltp (g/km)"]
ligne_test = selection[['Country','Mp','T','Mk','Ct','m (kg)','W (mm)','Ft','Fm','ep (KW)','Erwltp (g/km)','Fuel consumption ']]


if st.checkbox("Chargement du modèle MinMaxScaler"):
   scaler = joblib.load(dossier_local + "Streamlit/Ressources/" + 'scaler.pkl')
   st.write(scaler)


   ligne_test_quanti = scaler.transform(ligne_test.select_dtypes(include=['float64']))
   ligne_test_quanti = pd.DataFrame(ligne_test_quanti, columns = ['m (kg)', 'W (mm)', 'ep (KW)', 'Erwltp (g/km)', 'Fuel consumption '])
    
     

   df_global2= pd.concat([ligne_test_quanti,pd.get_dummies(ligne_test.Ct, prefix='categorie').reset_index()],axis =1 )
   df_global2= pd.concat([df_global2 , pd.get_dummies(ligne_test.Fm, prefix='fuel_mode').reset_index()], axis =1)
   df_global2= pd.concat([df_global2 , pd.get_dummies(ligne_test.Country, prefix='Country').reset_index()], axis =1)
   df_global2= pd.concat([df_global2 , pd.get_dummies(ligne_test.Mp, prefix='Mp').reset_index()], axis =1)
   df_global2= pd.concat([df_global2 , pd.get_dummies(ligne_test.Ft, prefix='Ft').reset_index()], axis =1)
    
   df_global2 = df_global2.drop(columns = "index")
    
   empty_df = pd.DataFrame(columns = ['m (kg)', 'W (mm)', 'ep (KW)', 'Erwltp (g/km)', 'Fuel consumption ',
           'categorie_M1', 'categorie_M1G', 'categorie_N1', 'fuel_mode_B',
           'fuel_mode_F', 'fuel_mode_H', 'fuel_mode_M', 'fuel_mode_P',
           'Country_AT', 'Country_BE', 'Country_BG', 'Country_CY', 'Country_CZ',
           'Country_DE', 'Country_DK', 'Country_EE', 'Country_ES', 'Country_FI',
           'Country_FR', 'Country_GR', 'Country_HR', 'Country_HU', 'Country_IE',
           'Country_IS', 'Country_IT', 'Country_LT', 'Country_LU', 'Country_LV',
           'Country_MT', 'Country_NL', 'Country_NO', 'Country_PL', 'Country_PT',
           'Country_RO', 'Country_SE', 'Country_SI', 'Country_SK', 'Mp_BMW',
           'Mp_FORD', 'Mp_HYUNDAI', 'Mp_KIA', 'Mp_MAZDA-SUBARU-SUZUKI-TOYOTA',
           'Mp_MERCEDES-BENZ', 'Mp_RENAULT-NISSAN-MITSUBISHI', 'Mp_STELLANTIS',
           'Mp_VW-SAIC', 'Ft_DIESEL', 'Ft_DIESEL/ELECTRIC', 'Ft_E85', 'Ft_LPG',
           'Ft_NG', 'Ft_NG-BIOMETHANE', 'Ft_PETROL', 'Ft_PETROL/ELECTRIC'])
    
   empty_df = pd.concat([empty_df,df_global2]).fillna(0)


if st.checkbox("Prédiction de la valeur des émissions"):
   emissions = RFregr.predict(empty_df)

   st.write("Prédiction du modèle : ",emissions[0], "g/km")
   st.write("Vraie valeur : ", target.iloc[0], "g/km")