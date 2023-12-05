import string
import random

import streamlit as st
from streamlit_authenticator.hasher import Hasher

import database


AMOUNT_OF_ACCOUNTS = 10

def generate_account_names_and_passwords_v2(num_accounts, password_length):
    accounts = []
    possible_names = ['banana', 'apple', 'tree', 'river', 'mountain', 'flower', 'sky', 'ocean', 'forest', 'stone']

    for i in range(num_accounts):
        # Select a name from the list and add a number to make it unique
        account_name = possible_names[i % len(possible_names)] + ''.join(random.choices(string.digits, k=4))

        # Generate a password
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=password_length))

        accounts.append((account_name, password))

    return accounts

# Generate 10 accounts with passwords of length 8
accounts_v2 = generate_account_names_and_passwords_v2(AMOUNT_OF_ACCOUNTS, 8)

# Upload accounts
client = database.init_connection(**st.secrets["mongo"])
db = client.LearnLoop

for account in accounts_v2:
    # Hash password
    hashed_password = Hasher([account[1]]).generate()[0]
    # print(hashed_password)
    db.users.insert_one({'username': account[0], 'password': hashed_password})
    print('Username:', account[0], '| Password:', account[1])



