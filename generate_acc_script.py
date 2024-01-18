import string
import random
import streamlit as st
from streamlit_authenticator.hasher import Hasher
import database


def generate_account_names_and_passwords(num_accounts, password_length):
    accounts = []
    possible_names = ['banana', 'apple', 'tree', 'river', 'mountain', 'flower', 'sky', 'ocean', 'forest', 'stone']
    # animal_names = [
    #     "Lion", "Tiger", "Elephant", "Giraffe", "Zebra", 
    #     "Panda", "Kangaroo", "Koala", "Rhino", "Hippo", 
    #     "Cheetah", "Leopard", "Wolf", "Bear", "Monkey", 
    #     "Gorilla", "Chimpanzee", "Camel", "Ostrich", "Flamingo"
    # ]

    for i in range(num_accounts):
        # animal_name = random.choice(animal_names)

        # Select a name from the list and add a number to make it unique
        account_name = possible_names[i % len(possible_names)] + ''.join(random.choices(string.digits, k=4))

        # Generate a password
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=password_length))

        accounts.append((account_name, password))

    return accounts

# Generate 10 accounts with passwords of length 8
AMOUNT_OF_ACCOUNTS = 10
accounts = generate_account_names_and_passwords(AMOUNT_OF_ACCOUNTS, 8)

def upload_accounts():
    client = database.init_connection(**st.secrets["mongo"])
    db = client.LearnLoop

    for account in accounts:
        # Hash password
        hashed_password = Hasher([account[1]]).generate()[0]
        db.users.insert_one({'username': account[0], 'password': hashed_password})
        print('Username:', account[0], '| Password:', account[1])


if __name__ == "__main__":
    accounts = generate_account_names_and_passwords(3, 8)



