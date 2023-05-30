
#:movie_camera:

#Import des modules nécessaires
import streamlit as st
import pandas as pd
from PIL import Image
from sklearn.neighbors import NearestNeighbors
import streamlit.components.v1 as components
import bz2
import pickle
import _pickle as cPickle
from sklearn.preprocessing import StandardScaler

#Configuration des dimensions & affichage de la page
st.set_page_config(page_title="Home-Ciné Metrics Consulting", 
                   page_icon=":clapper:", 
                   layout='wide')


# Initialisation du fond d'écran
import base64
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('SRC/img_home.png')  



# TITRE DEFILANT
# Définition du texte à afficher
texte = "Ciné Metrics Consulting"
# Configuration de la vitesse de défilement (en pixels par seconde)
vitesse = 20
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
    
    

st.markdown('<html><h3 align="center">Nous mettons à votre disposition une sélection rapide et appropriée de films en prévision de vos programmations futures.</h3></html>', unsafe_allow_html=True) 

st.markdown('<html><h3 align="center">Des sélections thématiques sont également mises à votre disposition.</h3></html>', unsafe_allow_html=True)

 
st.markdown('<h3 align="center"><p style="color:#3358FF"><font size="24">UNE SELECTION A PORTEE DE DOIGTS.</font></p></h3>', unsafe_allow_html=True)
st.title('📵 🚭') 
                  
#st.image(image)


# NEWSLETTER
# Insertion d'un formulaire de contact
with st.container():
    st.write("---")
    st.header("Inscrivez-vous à notre newsletter ! :mailbox: ")
    st.write("Vous ne raterez aucune semaine thématique :eyes: ! ")
    st.write("##")
# Inputs
name = st.text_input('Nom: ')
email = st.text_input('Email :')
# Fonction permettant l'envoi d'un mail informant d'une nouvelle inscription
formulaire_contact = f"""
<form action="https://formsubmit.co/simon.projet.2@gmail.com" method="POST">
     <name>
     <email>
     <input type="hidden" name="_captcha" value="false">
     <button type="submit">Envoyer</button>
</form> 
"""
#<input type="text" name="name" placeholder="Votre nom" required>
#<input type="email" name="email" placeholder="Votre Email" required>
#<input type="hidden" name="_autoresponse" value="Merci pour votre inscription ! A bientôt dans nos salles ! ">
# Lecture du csv
data = pd.read_csv("listletter.csv")
data.set_index('Name')
# Ajouter les nouvelles données au DataFrame existant
if email and name:
                st.write("")
                st.write("Voici le CSV qui s'auto-incrémente avec les coordonnées client :")
                new_data = pd.DataFrame({"Name": [name], "Mail": [email]})
                data = pd.concat([data, new_data])
                # Sauvegarder les données dans le fichier CSV
                data.to_csv("listletter.csv", columns=['Name','Mail'])
                st.success("Inscription réussie !")
                st.dataframe(data[['Name','Mail']])
else:
                st.warning("Veuillez remplir tous les champs.")
# Envoi du mail informant d'une nouvelle inscription
st.markdown(formulaire_contact, unsafe_allow_html=True)
#Lire le fichier style.css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)   
local_css("SRC/pages/style.css") 
