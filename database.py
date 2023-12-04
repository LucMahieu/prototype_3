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

    # MongoClient(
    #     host=['ac-j2mlrk4-shard-00-00.sfhs8pe.mongodb.net:27017', 'ac-j2mlrk4-shard-00-02.sfhs8pe.mongodb.net:27017',
    #           'ac-j2mlrk4-shard-00-01.sfhs8pe.mongodb.net:27017'], document_class=dict, tz_aware=False, connect=True,
    #     retrywrites=True, w='majority', authsource='admin', replicaset='atlas-kyejod-shard-0', tls=True,
    #     server_api= < pymongo.server_api.ServerApi
    # object
    # at
    # 0x12ec42760 >)


    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        return client
    except Exception as e:
        print(e)
        return None
