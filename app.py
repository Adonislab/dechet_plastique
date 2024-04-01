import streamlit as st
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
from tensorflow.keras.preprocessing.image import img_to_array, load_img


@st.cache(allow_output_mutation=True)
def load():
    model_path = "best_model.h5"
    model = load_model(model_path, compile=False)
    return model

# Chargement du model
model = load()

# Ajout des informations sur le nom, le prénom, le lien et l'hommage pour le professeur
st.sidebar.title("Informations")
nom = st.sidebar.text_input("Nom", value="NOBIME")
prenom = st.sidebar.text_input("Prénom", value="Tanguy Adonis")
whatssap = st.sidebar.text_input("Contact", value="+22951518759")
lien = st.sidebar.text_input("Link", value="www.linkedin.com/in/tanguy-adonis-nobime-078166200")
hommage = st.sidebar.text_area("Hommage au professeur", value="Cette application est une oeuvre de l'application du cours de Kevin degila. Mes profondes gratuites à lui pour ce cours, ci-dessous je vous invite à faire un tour sur son compte youtube.")
ressource = st.sidebar.text_input("Ressource", value="https://www.youtube.com/results?search_query=kevin+degila")





def predict(upload):
    img = Image.open(upload)
    img = np.asarray(img)
    img_resize = np.array(Image.fromarray(img).resize((224, 224)))
    img_resize = np.expand_dims(img_resize, axis=0)
    pred = model.predict(img_resize)
    rec = pred[0][0]
    return rec




st.title("Poubelle Intelligente : Détection d'un objet recyclable")

upload = st.file_uploader("Chargez l'image de votre objet", type=['png', 'jpeg', 'jpg'])

c1, c2 = st.columns(2)

if upload:
    rec = predict(upload)
    prob_recyclable = rec * 100      
    prob_organic = (1-rec)*100

    c1.image(Image.open(upload))
    if prob_recyclable > 50:
        c2.write(f"Nous sommes certain à {prob_recyclable:.2f} % que l'objet est recyclable")
    else:
        c2.write(f"Nous sommes certain à {prob_organic:.2f} % que l'objet n'est pas recyclable")

# Affichage des informations dans la barre latérale
st.sidebar.write(f"Nom: {nom}")
st.sidebar.write(f"Prénom: {prenom}")
st.sidebar.write(f"Link: {lien}")
st.sidebar.write(f"Remerciement: {hommage}")
st.sidebar.write(f"Ressource utilisée: {ressource}")
