# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 10:09:59 2023

@author: sebastien.liandrat
"""



import streamlit as st
import matplotlib as plt
import pandas as pd
import numpy as np




#st.sidebar.success("Select a demo above.")


dossier_local = "C:/Users/sebastien.liandrat/Box/Dossier Personnel de Sébastien LIANDRAT/Codes/Projet DataScientest/Dataset2/"
fichier = "data2021.csv"

"""
# Présentation du projet DS CO2

### 5 septembre 2023
"""


"""
## Présentation du sujet

"""
st.write('Prédire les émissions de CO2 (g/km) de véhicules enregistrés en 2021')
st.write('Sébastien Liandrat : Ingénieur Travaux Publics de l’État et Alexandre Teisseire : Géomaticien chez Enedis')
"""
## Enjeux du sujet
"""
st.write('Moyens de transport sont responsables de 25% des émissions de CO2 dans le monde')
st.write('Développement de connaissances dans ce domaine peut accompagner les décideurs privés et publics')
"""
## Base de données
"""
st.write("1ère base de données : ADEME, UTAC en charge de l'homologation des véhicules")
st.write("2ème base de données : AEE, collecte des données des pays de l'UE")



