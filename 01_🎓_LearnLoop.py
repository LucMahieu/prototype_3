import openai
import streamlit as st
from dotenv import load_dotenv
import os
import database
import utils

load_dotenv()
utils.init_session_state()
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.set_page_config(page_title="LearnLoop", layout="centered")
st.title("🎓 LearnLoop")
st.subheader("Bèta Prototype")

"""
Wat goed dat je het prototype gaat testen! Jouw feedback is waardevol en gaan we gebruiken om LearnLoop te verbeteren. Het is het eerste prototype waarmee we het leertraject en de directe feedback functie willen testen. We zijn benieuwd hoe je deze manier van studeren ervaart en vooral wat er beter aan kan! Je kunt al je feedback direct anoniem met ons delen via de '💬 Feedback' pagina.

Het langetermijndoel is dat LearnLoop automatisch de onderwerpen uit de hoorcolleges en andere studiematerialen haalt, deze aanvult en fact-checked met het boek en over die kennis een interactief, gepersonaliseerd en adaptief leertraject maakt.

Maar voor nu zijn we vooral benieuwd naar jouw ervaring en je suggesties voor veranderingen!

**Stappen:**
1. **Inloggen:** Gebruik de gegeven gebruikersnaam en wachtwoord.
2. **Kies Leertraject:** 'Leren en Geheugen' en het hoorcollege.
3. **Studeren & Feedback:** Volg het leertraject en geef tussentijds feedback.
4. **Feedback Formulier:** Laat je mening achter via het formulier (einde van het leertraject).

Alvast heel erg bedankt en succes met het studeren!
"""

## Load login page
from login import login_module
login_module()
