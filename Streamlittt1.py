import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests
import os
from io import StringIO
import plotly.express as px

# Fonctions pour chaque page

def page_scrap():
    st.title("Données Web_Scrapping")
    st.write("Sélectionnez le jeu de données")
    

    # Sélection du jeu de données dans la barre latérale
    selected_dataset = st.sidebar.selectbox("Choisissez le jeu de données", list(datasets.keys()))

    # Charger les données pour obtenir les colonnes disponibles
    available_columns = pd.read_csv(datasets[selected_dataset]).columns

    # Charger les données
    data = pd.read_csv(datasets[selected_dataset])

    # Afficher les données du jeu sélectionné ici
    st.header(f"Contenu de {selected_dataset}")
    st.write(data)

def page_web():
    st.title("Donnees Web Scrapping")
    st.write("Choisissez le tableau")

    # Charger les données
    chaussures_hom = pd.read_csv("type.csv")
    vet_hom = pd.read_csv("vetment_hom.csv")
    vetements_enfants = pd.read_csv("vetements_enfants.csv")
    chaussure_enfants = pd.read_csv("chaussures_enfant.csv")

    # Afficher les informations
    st.header("chaussures_hom")
    st.write(chaussures_hom)

    st.header("vet_hom")
    st.write(vet_hom)

    st.header("vetements_enfants ")
    st.write(vetements_enfants)

    st.header("chaussure_enfants ")
    st.write(chaussure_enfants)

def page_dash():
    st.title("Dashboard")
    st.write("Sélectionnez le jeu de données")

    # Sélection du jeu de données dans la barre latérale
    selected_dataset = st.sidebar.selectbox("Choisissez le jeu de données", list(datasets.keys()))

    # Charger les données pour obtenir les colonnes disponibles
    available_columns = pd.read_csv(datasets[selected_dataset]).columns

    # Charger les données
    data = pd.read_csv(datasets[selected_dataset])

    # Sélection des colonnes dans la barre latérale
    selected_columns = st.sidebar.multiselect("Sélectionnez les colonnes", available_columns)

    # Filtrer les données en fonction des colonnes sélectionnées
    filtered_data = data[selected_columns]

    # Afficher le DataFrame résultant
    st.write(filtered_data)

    # Laisser l'utilisateur choisir les colonnes X et Y pour les graphiques
    x_column = st.sidebar.selectbox("Sélectionnez la colonne X", filtered_data.columns)
    y_column = st.sidebar.selectbox("Sélectionnez la colonne Y", filtered_data.columns)

    # Line Chart
    st.subheader("Line Chart")
    line_chart = px.line(filtered_data, x=x_column, y=y_column)
    st.plotly_chart(line_chart)

    # Bar Chart
    st.subheader("Bar Chart")
    bar_chart = px.bar(filtered_data, x=x_column, y=y_column)
    st.plotly_chart(bar_chart)

    # Scatter Plot
    st.subheader("Scatter Plot")
    scatter_plot = px.scatter(filtered_data, x=x_column, y=y_column)
    st.plotly_chart(scatter_plot)

    # Pie Chart
    st.subheader("Pie Chart")
    pie_chart = px.pie(filtered_data, names=x_column, values=y_column)
    st.plotly_chart(pie_chart)

    # Box Plot
    st.subheader("Box Plot")
    box_plot = px.box(filtered_data, x=x_column, y=y_column)
    st.plotly_chart(box_plot)

# Liste des jeux de données disponibles
datasets = {
    "Chaussures Hommes": "type.csv",
    "Vêtements Hommes": "vetment_hom.csv",
    "Vêtements Enfants": "vetements_enfants.csv",
    "Chaussures Enfants": "chaussures_enfant.csv",
}

# Sélection de la page dans la barre latérale
selected_page = st.sidebar.radio("Navigation", ["Donnees Web Scrapping", "Dashboard"])

# Afficher la page sélectionnée
if selected_page == "Donnees Web Scrapping":
    page_web()
elif selected_page == "Dashboard":
    page_dash()
elif selected_page == "Donnees Beautifulsoup":
    page_scrap()
