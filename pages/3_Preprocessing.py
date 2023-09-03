# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 12:29:59 2023

@author: sebastien.liandrat
"""

import streamlit as st
import time
import numpy as np
import pandas as pd


### Fonctions

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


st.set_page_config(page_title="Étapes de préprocessing", page_icon="📈")

st.markdown("# Étapes de préprocessing")

"""
## Sélection des features
"""

selected_features = ['Country','Mp','T','Mk','Ct','m (kg)','Ewltp (g/km)','W (mm)','Ft','Fm','ep (KW)','Erwltp (g/km)','Fuel consumption ']

if st.checkbox('Liste des features conservées'):

    options = st.multiselect(
    'Colonnes à afficher',
    st.session_state.data.columns, selected_features)
    
    #st.write(options)
    display_dataframe_quickly(st.session_state.data[options], max_rows = 50)

    

  



"""
## Traitement des variables qualitatives
"""
st.write("Variable Mp : Supression des véhicules TESLA")

st.write("Variable T : Finalement, trop de modalités et donc suppression de la colonne")

st.write("Variable Mk : Finalement, trop de modalités et donc suppression de la colonne")

st.write("Variable Ct : Suppression des modalités très peu présentes (quelques lignes sur 10 millions)")

st.write("Variable Ft : Suppression des modalités correspondant aux véhicules électriques, à hydrogène et UNKNOWN")


"""
## Traitement des variables quantitatives
"""
st.write("Suppression des NA : remplacement par la médiane")





