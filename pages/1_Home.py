import streamlit as st
import streamlit_authenticator as stauth
from streamlit_extras.switch_page_button import switch_page
import pandas as pd
from dependencies.functions import connectToDatabase
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi




if 'authentication_status' not in st.session_state or st.session_state['authentication_status'] != True:
    switch_page('login')
    
if  "customer_id" not in st.session_state:
    st.session_state['customer_id'] = None

if "customers_data" not in st.session_state:
    st.session_state['customers_data'] = connectToDatabase()#read_dataset("data\\validation_data_synthetic.csv")

pos1, pos2, pos3 = st.columns([3,2,1])
with pos3:
    st.session_state['authenticator'].logout('Logout', 'main', key='logout_button')



def CheckID(id):
    database = st.session_state['customers_data']
    
    validation_data = database["energy_usage_validation"]
    
    records = validation_data.find({'CONS_NO':id})
        
    lenght = 0
    
    for _ in records:
        lenght += 1
        
    return lenght > 0


col1, col2, col3 = st.columns([1,1,1])
with col2:
    st.header("HOME")

st.warning("Enter the Customer ID to begin")

customer_id = st.text_input("Customer ID")

if customer_id != '':
    if CheckID(customer_id):
        if st.button('Submit'):
            st.session_state['customer_id'] = customer_id
            st.session_state['current_customer'] = None
            switch_page('dashboard')
    else:
        st.error('Invalid Customer ID')