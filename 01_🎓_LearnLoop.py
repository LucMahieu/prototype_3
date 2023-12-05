import openai
from PyPDF2 import PdfReader
import streamlit as st
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.prompts import (SystemMessagePromptTemplate, HumanMessagePromptTemplate,
                               ChatPromptTemplate)
from langchain.chat_models import ChatOpenAI
from langchain.chains.summarize import load_summarize_chain
from langchain.callbacks import get_openai_callback
from langchain.chains.openai_functions.extraction import create_extraction_chain
from dotenv import load_dotenv
import os
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA

import database
import utils

load_dotenv()
utils.init_session_state()
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.set_page_config(page_title="LearnLoop", layout="centered")
st.title("🎓 LearnLoop")
st.subheader("Bèta Prototype")

"""
Met de uiteindelijke versie van LearnLoop kun je de stof uit de hoorcolleges op een effectieve manier leren doordat LearnLoop automatisch de 
onderwerpen uit de hoorcolleges haalt, deze aanvult en fact-checked met het boek en over die kennis een interactief, gepersonaliseerd
en adaptief leertraject maakt.

Dit is het eerste prototype en het doel hiervan is om te testen of directe feedback op je antwoorden waarde toevoegt aan je studeerervaring. 
Met jouw feedback gaan we het prototype verbeteren en nieuwe functionaliteiten toevoegen zodat het uiteindelijk een volledig interactief, 
gepersonaliseerd en adaptief leertraject wordt waarmee je op een veel leukere en effectievere manier kunt studeren.

Stappen:
1. Login met je ontvangen gebruikersnaam en wachtwoord
2. Selecteer je vak
3. Start met leren!
"""

## Load login page
from login import login_module
login_module()
