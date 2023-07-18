from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv, find_dotenv
import streamlit as st



def connectToDatabase():
    load_dotenv()
    uri = f"mongodb+srv://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@cluster0.cs7rqja.mongodb.net/?retryWrites=true&w=majority"

    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))
    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)
    

    return client['electricity_usage']

@st.spinner("Submitting...")
def submitReport(customerID, predictedValue, actualValue):
    database = connectToDatabase()
    reports = database['reports']
    
    report = {
        'CONS_NO': customerID,
        'Predicted': predictedValue,
        'Actual': actualValue
    }
    
    reports.insert_one(report)