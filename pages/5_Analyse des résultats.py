# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 12:29:59 2023

@author: sebastien.liandrat
"""

import streamlit as st
import time
import numpy as np
import pandas as pd
from PIL import Image

st.set_page_config(page_title="Analyse des résultats")

st.title('Analyse des résultats du modèle')

st.write('## Features importance')

dossier_local = "C:/Users/sebastien.liandrat/Box/Dossier Personnel de Sébastien LIANDRAT/Codes/Projet DataScientest/"
img_FI = Image.open(dossier_local + "Streamlit/Ressources/" + 'feature_importance.jpeg')

if st.checkbox('Affichage'):
    st.image(img_FI)
    #st.bar_chart(data['Country'])


st.write('## Interprétabilité du modèle')

inter = {'Feature'  : ['fuel_mode_P','ep (KW)','Fuel consumption','m (kg)','W (mm)','Country_IT','Ft_PETROL/ELECTRIC','fuel_mode_H','Country_PL','Ft_PETROL','Mp_MAZDA-SUBARU-SUZUKI-TOYOTA','Erwltp (g/km)','Ft_DIESEL','Country_ES','fuel_mode_M','Mp_BMW'], 'Importance'    : [0.524253,0.214388,0.085094,0.079045,0.022122,0.017216,0.011440,0.006584,0.005430,0.005176,0.004104,0.002650,0.002425,0.002275,0.001773,0.001716]}
df_inter = pd.DataFrame(inter)
st.dataframe(df_inter)

st.write('Les résultats semblent être cohérents. Importance des variables relatives à la puissance du moteur, à la masse du véhicule, à la consommation de carburant ou encore les véhicules fonctionnant au pétrole')

st.write('Les variables moins influentes : Variables dichotomisées (pays,pool de fabricants), quelques variables quantitatives (taille des roues)')

st.write('Facilement interprétables (régression multiple)')

st.write('A priori pas de problèmes ethiques')

st.write('## Évolution du modèle')

st.write('Fusion de certaines modalités pour diminuer le nombre de features')

st.write("Hyperoptimisation avec un GridSearchCV")

# Number of trees in random forest
n_estimators = [int(x) for x in np.linspace(start = 100, stop = 2000, num = 5)]
# Number of features to consider at every split
max_features = ['auto', 'sqrt']
# Maximum number of levels in tree
max_depth = [int(x) for x in np.linspace(10, 110, num = 5)]
max_depth.append(None)
# Minimum number of samples required to split a node
min_samples_split = [2, 5, 10]
# Minimum number of samples required at each leaf node
min_samples_leaf = [1, 2, 4]
# Method of selecting samples for training each tree
bootstrap = [True, False]

forest_params_2 = {'n_estimators': n_estimators,
               'max_features': max_features,
               'max_depth': max_depth,
               'min_samples_split': min_samples_split,
               'min_samples_leaf': min_samples_leaf,
               'bootstrap': bootstrap}

if st.checkbox('Paramètres testés'):
    st.write(forest_params_2)
