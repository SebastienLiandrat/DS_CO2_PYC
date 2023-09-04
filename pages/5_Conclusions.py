# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 12:29:59 2023

@author: sebastien.liandrat
"""

import streamlit as st
import time
import numpy as np

st.set_page_config(page_title="page 2", page_icon="📈")

st.title('Analyse des résultats du modèle')

st.write('## Features importance')

st.write("graphe à rajouter")

st.write('## Interprétabilité du modèle')

st.write('Les résultats semblent être cohérents. Importance des variables relatives à la puissance du moteur, à la masse du véhicule, à la consommation de carburant ou encore les véhicules fonctionnant au pétrole')

st.write('Les variables moins influentes : Variables dichotomisées (pays,pool de fabricants), quelques variables quantitatives (taille des roues)')

st.write('Facilement interprétables (régression multiple)')

st.write('A priori pas de problèmes ethiques')

st.write('## Évolution du modèle')

st.write("Fusion de certaines modalités pour diminuer le nombre de features")

st.write("Hyperoptimisation")
