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

        print(items)

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
        authenticator.logout('Logout', 'main', key='unique_key')
        st.write(f'Welcome *{st.session_state["name"]}*')
        st.title('Some content')
    elif st.session_state["authentication_status"] is False:
        st.error('Username/password is incorrect')
    elif st.session_state["authentication_status"] is None:
        st.warning('Please enter your username and password')