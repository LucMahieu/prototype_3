import bcrypt
import streamlit as st

def hash_password(password):
    encoded_password = password.encode('utf-8')
    return bcrypt.hashpw(encoded_password, bcrypt.gensalt())

def init_session_state():
    if 'authentication_status' not in st.session_state:
        st.session_state.authentication_status = False

