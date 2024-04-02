import streamlit as st
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image



@st.cache(allow_output_mutation=True)
def load():
    model_path = "best_model.h5"
    model = load_model(model_path, compile=False)
    return model

# Chargement du model
model = load()

# Ajout des informations sur le nom, le prénom, le lien et l'hommage pour le professeur
st.sidebar.title("Informations")
nom="NOBIME"
prenom = "Tanguy Adonis"
whatssap = "+22951518759"
lien = "www.linkedin.com/in/tanguy-adonis-nobime-078166200"
hommage = '''Cette application est une oeuvre de l'application du cours de Kevin degila. Mes profondes gratitudes pour ces actions à l'égard de l'IA dans l'écosysteme du Bénin et en Afrique francophone, ci-dessous je vous invite à faire un tour sur son compte youtube.'''
ressource = "https://www.youtube.com/results?search_query=kevin+degila"





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
    

    c1.image(Image.open(upload))
    if rec == 1:
        c2.write(f"Je pense que l'objet est recyclable")
    else:
        c2.write(f"Je ne crois pas que l'objet soit recyclable")

# Affichage des informations dans la barre latérale
st.sidebar.write(f"Nom: {nom}")
st.sidebar.write(f"Prénom: {prenom}")
st.sidebar.write(f"Link: {lien}")
st.sidebar.write(f"Remerciement: {hommage}")
st.sidebar.write(f"Ressource utilisée: {ressource}")
