import streamlit as st
import streamlit_authenticator as stauth

import database

def login_module():

    @st.cache_data(ttl=600)
    def get_user_data():
        """Caches the login data for all users for 10 minutes in a accessible format."""
        # Connect to database
        client = database.init_connection(**st.secrets["mongo"])
        db = client.LearnLoop

        # List  all collections in db
        collections = list(db.users.find()) # make hashable for st.cache_data

        # Format collections into { key: { "username": username, "password": password } }
        items = {"usernames":
                     { item["username"]: item for item in collections }
                 }

        # Revert username field to name
        for username, item in items["usernames"].items():
            item["name"] = item.pop("username")
            item["password"] = item.pop("password")

        return items
    
    login_user_data = get_user_data()

    cookie_name = 'LearnLoopLogin'
    cookie_key = 'LearnLoopKey'
    cookie_expiry = 0
    preauthorized_users = []

    authenticator = stauth.Authenticate(
        login_user_data,
        cookie_name,
        cookie_key,
        cookie_expiry,
        preauthorized_users,
    )

    authenticator.login('Login', 'main')

    if st.session_state["authentication_status"]:
        st.header('Account')
        st.write(f'{st.session_state.username}')
        authenticator.logout('Log out', 'main', key='unique_key')
    elif st.session_state["authentication_status"] is False:
        st.error('Username or password is incorrect')
    elif st.session_state["authentication_status"] is None:
        pass