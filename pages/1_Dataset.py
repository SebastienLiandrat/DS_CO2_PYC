# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 12:29:15 2023

@author: sebastien.liandrat
"""

import streamlit as st
import time
import numpy as np

import matplotlib as plt
import pandas as pd



st.set_page_config(page_title="Plotting Demo", page_icon="📈")

st.markdown("# Présentation du dataset")
st.sidebar.header("Dataset")
st.write(
    """Jeu de données conséquent : 10 millions de ligne pour une seule année, réduction de l'échantillon à 500000 lignes"""
)



st.sidebar.success("Plan de la présentation.")


dossier_local = "C:/Users/sebastien.liandrat/Box/Dossier Personnel de Sébastien LIANDRAT/Codes/Projet DataScientest/"
fichier = "data2021.csv"

"""
## Présentation du jeu de données global
"""






@st.cache_data
def load_data(adresse):
    data = pd.read_csv(adresse)
    data = data.sample(n = 500000).sort_index()
    return data

#data = load_data(dossier_local + 'Dataset2/' + fichier)


if 'data' not in st.session_state:
    st.session_state.data = load_data(dossier_local + 'Dataset2/' + fichier)
if 'Test' not in st.session_state:
    st.session_state['Test'] = "a"


#read_and_cache_csv = st.cache(pd.read_csv)
#data = read_and_cache_csv(dossier_local + fichier, nrows=500000)


def display_dataframe_quickly(df, max_rows=5000, **st_dataframe_kwargs):
    """Display a subset of a DataFrame or Numpy Array to speed up app renders.
    
    Parameters
    ----------
    df : DataFrame | ndarray
        The DataFrame or NumpyArray to render.
    max_rows : int
        The number of rows to display.
    st_dataframe_kwargs : Dict[Any, Any]
        Keyword arguments to the st.dataframe method.
    """
    n_rows = len(df)
    if n_rows <= max_rows:
        # As a special case, display small dataframe directly.
        st.write(df)
    else:
        # Slice the DataFrame to display less information.
        start_row = st.slider('Start row', 0, n_rows - max_rows)
        end_row = start_row + max_rows
        df = df[start_row:end_row]

        # Reindex Numpy arrays to make them more understadable.
        if type(df) == np.ndarray:
            df = pd.DataFrame(df)
            df.index = range(start_row,end_row)

        # Display everything.
        st.dataframe(df, **st_dataframe_kwargs)
        st.text('Displaying rows %i to %i of %i.' % (start_row, end_row - 1, n_rows))
        
if st.checkbox('Afficher le dataframe global'):
    display_dataframe_quickly(st.session_state.data, max_rows = 50)




"""
## Présentation des variables
"""

if st.checkbox('Variables quantitatives'):
    variables_quanti = pd.read_csv(dossier_local + "/Streamlit/Ressources/Variables_quantitatives.csv")
    display_dataframe_quickly(variables_quanti)

if st.checkbox('Variables qualitatives'):
    variables_quali = pd.read_csv(dossier_local + "/Streamlit/Ressources/Variables_qualitatives.csv")
    display_dataframe_quickly(variables_quali)



  





st.session_state.data["Country"].value_counts(normalize = True).plot(kind = "bar")

