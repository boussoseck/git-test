# # Simuler des données pour le tableau de bord

    # # Créer un DataFrame
    # df = pd.read_csv("Vente_Locations_Villas.csv")
    # da = pd.read_csv("Appartements.csv")
    # # Créer le diagramme camembert pour la variable "prix"
    # st.subheader("prix/adresse")
    # villa_counts = df['Type_annonce'].value_counts()

    # # Diagramme camembert directement dans la page
    # fig, ax = plt.subplots()
    # ax.pie(villa_counts.head(2), labels=villa_counts.head(2).index, autopct='%1.1f%%',
    #        startangle=90, colors=sns.color_palette('pastel'), wedgeprops=dict(width=0.4))
    # ax.axis('equal')
    # st.pyplot(fig)

    # st.subheader("prix/adresse")

    # fi, ax = plt.subplots()

    # # Utiliser l'axe pour créer un nuage de points
    # sns.regplot(data=da, x='Nombre_pieces', y='Prix',
    #             color='blue', scatter_kws={'s': 100})

    # # Personnaliser l'axe et le graphique
    # ax.set_xlabel('Nombre de Pièces')
    # ax.set_ylabel('Prix')
    # ax.set_title('Courbe de Régression Nombre de Pièces/Prix')

    # # Afficher le graphique avec Streamlit
    # st.pyplot(fi)


# Barre de navigation