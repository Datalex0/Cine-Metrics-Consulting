
# Import librairies
import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

#Configuration des dimensions & affichage de la page
st.set_page_config(page_title="Thématiques",
                   page_icon=":clapper:",
                   layout='wide')

# Import dataframes
documentaires = pd.read_csv("SRC/pages/documentaires.csv")
films = pd.read_csv("SRC/pages/sam.csv")

films=films[
    films['numVotes']>=20000
            ]

# Renommage colonnes en français
documentaires = documentaires.rename({'tconst':'Référence', 'titleType':'Format', 'primaryTitle':'Titre', 'startYear':'Sortie', 'runtimeMinutes':'Durée', 'genres':'Genres','averageRating':'Note moyenne','numVotes':'Nb Votes','primaryName':'Producteur'}, axis='columns')
films = films.rename({'tconst':'Référence', 'titleType':'Format', 'title':'Titre', 'startYear':'Sortie', 'runtimeMinutes':'Durée', 'genres':'Genres','averageRating':'Note moyenne','numVotes':'Nb Votes','primaryName':'Producteur'}, axis='columns')

#Ajout colonne 'lien IMDB'
documentaires['lien IMDb']='https://www.imdb.com/title/'+documentaires['Référence']
films['lien IMDb']='https://www.imdb.com/title/'+films['Référence']



# Titre Sidebar
st.sidebar.title("**Faites votre sélection** :")

st.sidebar.markdown("***")


# Boutons Radio choix Films ou Documentaires
df_search = st.sidebar.radio(
    "Que voulez-vous rechercher ?",
    ('Des Films', 'Des Documentaires'))



st.sidebar.markdown("***")


# FILMS

if df_search== 'Des Films' :
 
    # Définition du texte à afficher
    texte = "Films"
    # Configuration de la vitesse de défilement (en pixels par seconde)
    vitesse = 10
    # Génération du code HTML pour le texte défilant
    html_code = f"""<marquee scrollamount="{vitesse}"> {texte} </marquee>"""
    # Mise en forme taille = 150 pixels
    st.markdown("""<style>
            .big-font {
                font-size:150px
            }
            </style>""", unsafe_allow_html=True)
    # Affichage du texte défilant
    st.markdown(f'<p class="big-font"><font face="Brush Script MT">{html_code}</font></p>', unsafe_allow_html=True)
    #Brush Script MT
    #Courier
    #Impact
    #Trebuchet MS
    #Tahoma
    #Arial Black
    
    # Boutons Radio choix Recherche : Genre, Producteur ou Année
    choix = st.sidebar.radio(
        "Comment voulez-vous filtrer ?",
        ('Par Genre', 'Par Producteur', 'Par Année'))

    st.sidebar.markdown("***")

    # Si choix = genre
    if choix == 'Par Genre':
        
        #Titre films genre
        st.title(":popcorn: Recherche de Films par Genre :popcorn:")
        st.title("\n")
        
        # Menu déroulant des différents genres
        liste_genres =['Action', 'Actualité', 'Animation', 'Aventure', 'Biographie', 'Comédie', 'Crime', 'Documentaire Court', 'Drame', 'Familial', 'Fantaisie', 'Guerre', 'Historique', 'Horreur', 'Musical', 'Musique', 'Mystère', 'Policier', 'Romance', 'Science Fiction', 'Sport', 'Western']
        genre = st.sidebar.selectbox(
        'Quel genre voulez-vous afficher ?', liste_genres
        )

        # traduction des genres en anglais pour correspondre au df
        if genre=='Aventure':
            genre='Adventure'
        elif genre=='Biographie':
            genre='Biography'
        elif genre=='Comédie':
            genre='Comedy'
        elif genre=='Drame':
            genre='Drama'
        elif genre=='Familial':
            genre='Family'
        elif genre=='Fantaisie':
            genre='Fantasy'
        elif genre=='Historique':
            genre='History'
        elif genre=='Horreur':
            genre='Horror'
        elif genre=='Musique':
            genre='Music'
        elif genre=='Mystère':
            genre='Mystery'
        elif genre=='Actualité':
            genre='News'
        elif genre=='Science Fiction':
            genre='Sci-Fi'
        elif genre=='Documentaire Court':
            genre='Short'
        elif genre=='Policier':
            genre='Thriller'
        elif genre=='Guerre':
            genre='War'

        # Double Curseur durée
        min_duree_genre, max_duree_genre = st.sidebar.slider(
        'Selectionner une durée en min :',
        min_value = 0, 
        max_value = 240, 
        value = (0,240), 
        step = 10)
        
        # Affichage du dataframe filtré selon le genre et la durée choisis
        st.dataframe(data = films[
            (films.Genres.str.contains(genre)) & (films['Durée']<=max_duree_genre) & (films['Durée']>=min_duree_genre)
            ][['Référence','Titre','Sortie','Durée','Genres','Note moyenne','Nb Votes','Producteur','lien IMDb']].sort_values('Nb Votes', ascending=False),
                     width=2000
            )



    # Si choix = producteur
    elif choix == 'Par Producteur':
        
        #Titre films producteur
        st.title(":popcorn: Recherche de Films par Producteur :popcorn:")
        st.title("\n")
        
        # Menu déroulant producteurs
        prod_deroul = st.sidebar.selectbox(
            'Quel producteur voulez-vous afficher ?',
            (films['Producteur'].sort_values().drop_duplicates()))
        
        # Double Curseur durée
        min_duree_prod, max_duree_prod = st.sidebar.slider(
        'Selectionner une durée en min :',
        min_value = 0,
        max_value = 240,
        value = (0,240),
        step =10)

        # Affichage du dataframe filtré selon le producteur et la durée choisis
        st.dataframe(films[
        (films.Producteur.str.contains(prod_deroul)) & (films['Durée']<=max_duree_prod) & (films['Durée']>=min_duree_prod)
        ][['Référence','Titre','Sortie','Durée','Genres','Note moyenne','Nb Votes','Producteur','lien IMDb']].sort_values('Nb Votes',ascending=False)
        )


    # Si choix = année
    elif choix == 'Par Année':
        
        #Titre films année
        st.title(":popcorn: Recherche de Films par Année :popcorn:")
        st.title("\n")
        
        # Double Curseur durée
        min_annee, max_annee = st.sidebar.slider(
        "Selectionner l'année de sortie",
        min_value = 1910,
        max_value = 2023,
        value = (1910,2023)
        )
        
        # Double Curseur année de sortie
        min_duree_annee, max_duree_annee = st.sidebar.slider(
        'Selectionner une durée en min :',
        min_value = 0, 
        max_value = 240,
        value = (0,240), 
        step = 10)
        
        # Affichage du dataframe filtré selon l'année de sortie et la durée choisies
        st.dataframe(films[
        (films['Sortie']<=max_annee) & (films['Sortie']>=min_annee) & (films['Durée']<=max_duree_annee) & (films['Durée']>=min_duree_annee)
        ][['Référence','Titre','Sortie','Durée','Genres','Note moyenne','Nb Votes','Producteur','lien IMDb']].sort_values('Nb Votes',ascending=False)
        )
        
    else:
        st.write("Vous n'avez rien sélectionné")













# DOCUMENTAIRES

elif df_search== 'Des Documentaires' :
    
    # Définition du texte à afficher
    texte = "Documentaires"
    # Configuration de la vitesse de défilement (en pixels par seconde)
    vitesse = 10
    # Génération du code HTML pour le texte défilant
    html_code = f"""<marquee scrollamount="{vitesse}"> {texte} </marquee>"""
    # Mise en forme taille = 150 pixels
    st.markdown("""<style>
            .big-font {
                font-size:150px
            }
            </style>""", unsafe_allow_html=True)
    # Affichage du texte défilant
    st.markdown(f'<p class="big-font"><font face="Brush Script MT">{html_code}</font></p>', unsafe_allow_html=True)
    #Brush Script MT
    #Courier
    #Impact
    #Trebuchet MS
    #Tahoma
    #Arial Black
    
    # Bouton Radio choix Recherche : Genre, Producteur ou Année
    choix = st.sidebar.radio(
        "Comment voulez-vous filtrer ?",
        ('Par Genre', 'Par Producteur', 'Par Année'))
    st.sidebar.title("\n")


    # Si choix = genre
    if choix == 'Par Genre':
        
        # Titre Documentaires par Genre
        st.title(":popcorn: Recherche de Documentaires par Genre :popcorn:")
        st.title("\n")
        
        # Menu déroulant des différents genres
        liste_genres =['Action', 'Actualité', 'Animation', 'Aventure', 'Biographie', 'Comédie', 'Crime', 'Documentaire Court', 'Drame', 'Familial', 'Fantaisie', 'Guerre', 'Historique', 'Horreur', 'Musical', 'Musique', 'Mystère', 'Policier', 'Romance', 'Science Fiction', 'Sport', 'Western']
        genre = st.sidebar.selectbox(
        'Quel genre voulez-vous afficher ?', liste_genres
        )

        # traduction des genres en anglais pour correspondre au df
        if genre=='Aventure':
            genre='Adventure'
        elif genre=='Biographie':
            genre='Biography'
        elif genre=='Comédie':
            genre='Comedy'
        elif genre=='Drame':
            genre='Drama'
        elif genre=='Familial':
            genre='Family'
        elif genre=='Fantaisie':
            genre='Fantasy'
        elif genre=='Historique':
            genre='History'
        elif genre=='Horreur':
            genre='Horror'
        elif genre=='Musique':
            genre='Music'
        elif genre=='Mystère':
            genre='Mystery'
        elif genre=='Actualité':
            genre='News'
        elif genre=='Science Fiction':
            genre='Sci-Fi'
        elif genre=='Documentaire Court':
            genre='Short'
        elif genre=='Policier':
            genre='Thriller'
        elif genre=='Guerre':
            genre='War'

        # Double Curseur durée
        min_duree_genre, max_duree_genre = st.sidebar.slider(
        'Selectionner une durée en min :',
        min_value = 0, 
        max_value = 240, 
        value = (0,240), 
        step = 10)
        
        # Affichage du dataframe filtré selon le genre et la durée choisis
        st.dataframe(data = documentaires[
            (documentaires.Genres.str.contains(genre)) & (documentaires['Durée']<=max_duree_genre) & (documentaires['Durée']>=min_duree_genre)
            ][['Référence','Titre','Sortie','Durée','Genres','Note moyenne','Nb Votes','Producteur','lien IMDb']].sort_values('Nb Votes', ascending=False)
            )



    # Si choix = producteur
    elif choix == 'Par Producteur':
        
        # Titre Documentaires par Producteur
        st.title(":popcorn: Recherche de Documentaires par Producteur :popcorn:")
        st.title("\n")
        
        # Menu déroulant producteurs
        prod_deroul = st.sidebar.selectbox(
            'Quel producteur voulez-vous afficher ?',
            (documentaires['Producteur'].sort_values().drop_duplicates()))
        
        # Double Curseur durée
        min_duree_prod, max_duree_prod = st.sidebar.slider(
        'Selectionner une durée en min :',
        min_value = 0, 
        max_value = 240, 
        value = (0,240), 
        step =10)

        # Affichage du dataframe filtré selon le producteur et la durée choisis
        st.dataframe(documentaires[
        (documentaires.Producteur.str.contains(prod_deroul)) & (documentaires['Durée']<=max_duree_prod) & (documentaires['Durée']>=min_duree_prod)
        ][['Référence','Titre','Sortie','Durée','Genres','Note moyenne','Nb Votes','Producteur','lien IMDb']].sort_values('Nb Votes',ascending=False)
        )



    # Si choix = année
    elif choix == 'Par Année':
        
        # Titre Documentaires par Année
        st.title(":popcorn: Recherche de Documentaires par Année :popcorn:")
        st.title("\n")
        
        # Double Curseur Année
        min_annee, max_annee = st.sidebar.slider(
        "Selectionner l'année de sortie",
        min_value = 1920,
        max_value = 2023,
        value = (1920,2023)
        )
        
        # Double Curseur durée
        min_duree_annee, max_duree_annee = st.sidebar.slider(
        'Selectionner une durée en min :',
        min_value = 0, 
        max_value = 240, 
        value = (0,240), 
        step = 10)
        
        # Affichage du dataframe filtré selon l'Année de sortie et la durée choisies
        st.dataframe(documentaires[
        (documentaires['Sortie']<=max_annee) & (documentaires['Sortie']>=min_annee) & (documentaires['Durée']<=max_duree_annee) & (documentaires['Durée']>=min_duree_annee)
        ][['Référence','Titre','Sortie','Durée','Genres','Note moyenne','Nb Votes','Producteur','lien IMDb']].sort_values('Nb Votes',ascending=False)
        )
        
    else:
        st.write("Vous n'avez rien sélectionné")
