# Import librairies
import streamlit as st
import pandas as pd
from PIL import Image
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler

#Configuration des dimensions & affichage de la page
st.set_page_config(page_title="Documentaires",
                   page_icon=":clapper:",
                   layout='wide')

# Import dataframe
documentaires = pd.read_csv("SRC/pages/documentaires.csv")

# Changement d'index
documentaires.set_index('primaryTitle', inplace = True, drop = False )

# Affichage logo
image = Image.open("SRC/logo.png")
st.image(image)

# Affichage Titre
st.title(':clapper: Notre système de recommandation de documentaires :movie_camera:')

# Menu déroulant pour choix documentaire
docu_base = st.selectbox(
     'A partir de quel documentaire voulez-vous avoir des recommandations ?',
      (documentaires['primaryTitle'].sort_values().drop_duplicates())
      )

# sous titre exemples
st.caption("Exemples : Capitalism: A Love Story, Free Solo, Foo Fighters: Back and Forth")


# MACHINE LEARNING

# Selection des colonnes pour le Machine Learning
X = documentaires.select_dtypes('number').drop('runtimeMinutes',axis=1)

# Prise en compte du choix de documentaire de l'utilisateur
docu_a_tester = X.loc[docu_base].to_frame().T


# SCALER
# initialisation du scaler
scaler = StandardScaler()
# entraînement du scaler
X_scaled = scaler.fit_transform(X)
# film référence avec métriques scalées
docu_a_tester_scaled = scaler.transform(docu_a_tester)


# on définit le model
modelNN = NearestNeighbors(n_neighbors=5)

# on entraîne le model
modelNN.fit(X_scaled)

# on attribue une variable à chacun des 2 array
neigh_dist_scaled, neigh_index_scaled = modelNN.kneighbors(docu_a_tester_scaled, n_neighbors = 6)

# On définit 2 variables pour afficher le titre et le nom du producteur
titre_docu_reco = documentaires['primaryTitle']
produc_docu_reco = documentaires['primaryName']

# On définit 2 variables : titre_docu=le titre du documentaire référence, produc_docu=le producteur du documentaire référence
titre_docu = documentaires.loc[docu_a_tester.index[0]]['primaryTitle']
produc_docu = documentaires.loc[docu_a_tester.index[0]]['primaryName']

# On affiche la phrase suivante avec le titre et le producteur du docu de référence
st.title("")
st.markdown(f'## **Voici 5 documentaires qui se rapprochent de :orange[ {titre_docu} ] de :green[ {produc_docu} ]** : ')
st.title("")

# Boucle permettant d'afficher les 4 docus recommandés, le producteur, et le lien vers la page IMDb du docu
for i in range(5):
    index_reco = neigh_index_scaled[0][i+1]
    st.write("")
    st.markdown(f'### [🎦](https://www.imdb.com/title/{documentaires.iloc[neigh_index_scaled[0][1:]]["tconst"][i]}/) - Recommandation {i+1} : :orange[ **{titre_docu_reco.iloc[neigh_index_scaled[0][i+1]]}** ] de :green[ **{produc_docu_reco.iloc[neigh_index_scaled[0][i+1]]}** ]')

    #st.markdown(f" [:clapper:](https://www.imdb.com/title/{documentaires.iloc[neigh_index_scaled[0][1:]]['tconst'][i]}/)")

    #<p style="font-family:sans-serif; color:Green; font-size: 42px;">
