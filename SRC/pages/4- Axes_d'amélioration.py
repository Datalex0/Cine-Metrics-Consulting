#Import des modules nécessaires
import streamlit as st
import pandas as pd
from PIL import Image
#from streamlit_option_menu import option_menu
from sklearn.neighbors import NearestNeighbors


#Configuration des dimensions & affichage de la page
st.set_page_config(page_title="Axes d'amélioration", 
                   page_icon="🎬", 
                   layout='wide')


#Affichage du texte clignotant

import streamlit as st

def main():
    st.markdown(
        """
        <style>
        
        @keyframes blink {
            0% { opacity: 1; }
            50% { opacity: 0; }
            100% { opacity: 1; }
        }

        .blink-text {
            animation: blink 1s infinite;
        }
        
        </style>

        """,
        unsafe_allow_html=True
    )

    st.markdown('<font size = 50><p class="blink-text"> Ciné Métrics Consulting - tu veux un film ? Et BING ! </p></font>', unsafe_allow_html=True)

if __name__ == '__main__':
    main()



#Affichage des textes
st.title("Axes d'améliorations :rocket:")
st.divider()

# checkbox
# check if the checkbox is checked
# title of the checkbox is 'Show/Hide'
check1=st.checkbox("#1")
if check1:

	# display the text if the checkbox returns True value
	st.header("Intégrer l'affiche et la bande annonce pour chaque film")



st.divider()
check2=st.checkbox("#2")
if check2:
    st.header("Intégrer les acteurs au système de recommandations")



st.divider()
check3=st.checkbox("#3")
if check3:
    st.header("Trier par pays pour avoir des thématiques nationales")  



st.divider()   
check4=st.checkbox("#4")
if check4:
    st.header("Créer un système de notation après visionnage d'un film via le compte client en ligne")





