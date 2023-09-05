# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 12:29:59 2023

@author: sebastien.liandrat
"""

import streamlit as st
import time
import numpy as np
from PIL import Image

st.set_page_config(page_title="Courbes", page_icon="📈")

dossier_local = "C:/Users/sebastien.liandrat/Box/Dossier Personnel de Sébastien LIANDRAT/Codes/Projet DataScientest/"


st.markdown("# Présentation de quelques courbes")



img_Fm = Image.open(dossier_local + "Streamlit/Ressources/" + 'Fm.jpeg')
img_mkg     = Image.open(dossier_local + "Streamlit/Ressources/" + 'm(kg).jpeg')



if st.checkbox('Répartition Fm'):
    st.image(img_Fm)
    #st.bar_chart(data['Country'])

if st.checkbox('Répartition m(kg)'):
    st.image(img_mkg)
    #st.bar_chart(data['Country'])

img_hm = Image.open(dossier_local + "Streamlit/Ressources/" + 'heatmap.jpeg')
if st.checkbox('Heat map'):
    st.image(img_hm)
