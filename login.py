import streamlit as st
import streamlit_authenticator as stauth

import database

def login_module():

    @st.cache_data(ttl=600)
    def get_data():
        client = database.init_connection(**st.secrets["mongo"])
        db = client.LearnLoop
        # List  all collections
        items = db.users.find()
        items = list(items)  # make hashable for st.cache_data

        # Format items into { key: { "username": username, "password": password } }
        items = {"usernames":
                     { item["username"]: item for item in items }
                 }

        # Revert username field to name
        for username, item in items["usernames"].items():
            item["name"] = item.pop("username")
            item["password"] = item.pop("password")

        return items

    items = get_data()

    cookie_name = 'LearnLoopLogin'
    cookie_key = 'LearnLoopKey'
    cookie_expiry = 0
    preauthorized_users = []

    authenticator = stauth.Authenticate(
        items,
        cookie_name,
        cookie_key,
        cookie_expiry,
        preauthorized_users,
    )

    authenticator.login('Login', 'main')

    if st.session_state["authentication_status"]:
        st.write(f'Welkom *{st.session_state["name"]}*, je bent nu ingelogd. \n Hiermee houden we jouw vooruitgang bij, veel succes met studeren!')
        authenticator.logout('Or log out...', 'main', key='unique_key')
    elif st.session_state["authentication_status"] is False:
        st.error('Username/password is incorrect')
    elif st.session_state["authentication_status"] is None:
        st.warning('Please enter your username and password')