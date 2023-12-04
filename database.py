from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pymongo
import streamlit as st

@st.cache_resource
def init_connection(username, password, host):
    uri = f"mongodb+srv://{username}:{password}@{host}/?retryWrites=true&w=majority"
    print(uri)
    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))
    # client = pymongo.MongoClient(**st.secrets["mongo"])
    print(client)

    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        return client
    except Exception as e:
        print(e)
        return None