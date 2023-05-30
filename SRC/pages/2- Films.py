# Import librairies
import streamlit as st
import pandas as pd
from PIL import Image
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler

#Configuration des dimensions & affichage de la page
st.set_page_config(page_title="Films",
                   page_icon=":clapper:",
                   layout='wide')


#df_films=pd.read_csv('df_films.csv')

# PICKLE pour lire le df compressé et accélérer la page streamlit
# import librairies
import bz2
import pickle
import _pickle as cPickle
# fonction de décompression
def decompress_pickle(file):
 data = bz2.BZ2File(file, 'rb')
 data = cPickle.load(data)
 return data
# décompression du dataframe
df_films = decompress_pickle('SRC/df_films.pbz2')



# Changement d'index
df_films.set_index('title', inplace = True, drop = False )

df_films = df_films[
    df_films['numVotes']>=20000
         ]

# Affichage logo
image = Image.open("C:/Users/murai/OneDrive/Bureau/DATA/PROJET 2/logo.png")
st.image(image)

# Affichage Titre
st.title(':clapper: Notre système de recommandation de films  :movie_camera:')

# Menu déroulant pour choix film
film_base = st.selectbox(
     'A partir de quel film voulez-vous avoir des recommandations ?',
      (df_films['title'].sort_values().drop_duplicates()),
      )

# sous titre exemples
st.caption("Exemples : Les Évadés, La reine des neiges, Il était une fois dans l'Ouest, Le Parrain")


# MACHINE LEARNING

# Selection des colonnes pour le Machine Learning
X = df_films.select_dtypes('number').drop(['isOriginalTitle','numVotes','runtimeMinutes','startYear'],axis=1)

# Prise en compte du choix de film de l'utilisateur
film_a_tester = X.loc[film_base].to_frame().T

# on définit le model
modelNN = NearestNeighbors(n_neighbors=5)

# on entraîne le model
modelNN.fit(X)

# on attribue une variable à chacun des 2 array
neigh_dist, neigh_index = modelNN.kneighbors(film_a_tester, n_neighbors = 11)

# On définit 2 variables pour afficher le titre et le nom du producteur
titre_film_reco = df_films['title']
produc_film_reco = df_films['primaryName']

# On définit 2 variables : titre_film=le titre du film référence, produc_film=le producteur du film référence
titre_film = df_films.loc[film_a_tester.index[0]]['title']
produc_film = df_films.loc[film_a_tester.index[0]]['primaryName']

# On affiche la phrase suivante avec le titre et le producteur du film de référence
st.write("")
st.write(f'## **Voici 10 films qui se rapprochent du film :orange[ {titre_film} ] de :green[ {produc_film} ] :**')
st.write("")

# Boucle permettant d'afficher les 4 films recommandés, le producteur, et le lien vers la page IMDb du film
for i in range(10):
    index_reco = neigh_index[0][i+1]
    st.write("")
    st.markdown(f"### [🎦](https://www.imdb.com/title/{df_films.iloc[neigh_index[0][1:]]['tconst'][i]}/) - **Recommandation {i+1}** : :orange[ {titre_film_reco.iloc[neigh_index[0][i+1]]} ] de :green[ {produc_film_reco.iloc[neigh_index[0][i+1]]} ]")
