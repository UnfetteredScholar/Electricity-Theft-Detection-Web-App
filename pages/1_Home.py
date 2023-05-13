import streamlit as st
import streamlit_authenticator as stauth
from streamlit_extras.switch_page_button import switch_page
import pandas as pd
from dependencies.functions import read_dataset


if 'authentication_status' not in st.session_state or st.session_state['authentication_status'] != True:
    switch_page('login')
    
if  "meter_id" not in st.session_state:
    st.session_state['meter_id'] = None

pos1, pos2, pos3 = st.columns([3,2,1])
with pos3:
    st.session_state['authenticator'].logout('Logout', 'main', key='logout_button')


path = "C:\\Users\\atoto\\Documents\\Final Year Project\\ElectricityTheftDetection\\data\\data_features_reduced.csv"

customers_data = read_dataset(path)

col1, col2, col3 = st.columns([1,1,1])
with col2:
    st.header("HOME")

st.warning("Enter the meter ID to begin")

meter_id = st.text_input("Meter ID")

if meter_id != '':
    if meter_id in customers_data['CONS_NO'].values:
        st.session_state['meter_id'] = meter_id
        if st.button('Submit'):
            switch_page('analysis')
    else:
        st.error('Invalid Customer ID')