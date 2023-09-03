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


st.markdown("# Liste des modèles testés")

dossier_local = "C:/Users/sebastien.liandrat/Box/Dossier Personnel de Sébastien LIANDRAT/Codes/Projet DataScientest/"

X_reduit = pd.read_csv(dossier_local + "Streamlit/Ressources/" + "X_reduit.csv", index_col = 0) 

st.write(X_reduit)


if st.checkbox("Chargement du modèle avec joblib"):
    RFregr=joblib.load(dossier_local + "Streamlit/Ressources/" + 'RFregr.pkl')
    st.write(RFregr)
    
    if st.checkbox("Afficher les paramètres"):
        st.write(RFregr.get_params())

    