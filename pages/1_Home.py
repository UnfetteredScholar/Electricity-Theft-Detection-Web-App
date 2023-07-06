import streamlit as st
import streamlit_authenticator as stauth
from streamlit_extras.switch_page_button import switch_page
import pandas as pd
from dependencies.functions import read_dataset


if 'authentication_status' not in st.session_state or st.session_state['authentication_status'] != True:
    switch_page('login')
    
if  "customer_id" not in st.session_state:
    st.session_state['customer_id'] = None

if "customers_data" not in st.session_state:
    st.session_state['customers_data'] = read_dataset("data\\validation_data_synthetic.csv")

pos1, pos2, pos3 = st.columns([3,2,1])
with pos3:
    st.session_state['authenticator'].logout('Logout', 'main', key='logout_button')





col1, col2, col3 = st.columns([1,1,1])
with col2:
    st.header("HOME")

st.warning("Enter the Customer ID to begin")

customer_id = st.text_input("Customer ID")

if customer_id != '':
    if customer_id in st.session_state.customers_data['CONS_NO'].values:
        st.session_state['customer_id'] = customer_id
        if st.button('Submit'):
            switch_page('analysis')
    else:
        st.error('Invalid Customer ID')