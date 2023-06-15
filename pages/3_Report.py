import streamlit as st
import streamlit_authenticator as stauth
from streamlit_extras.switch_page_button import switch_page
import pandas as pd
import plotly.figure_factory as ff
from dependencies.functions import read_dataset
import numpy as np

if 'authentication_status' not in st.session_state or st.session_state['authentication_status'] != True:
    switch_page('login')
    
st.header("Report")

with st.form("Report Form"):
    meter_id = st.text_input("Customer ID", key="customer_id")
    predicted_value = st.selectbox("Predicted Value", options=["Suspicious", "Normal Customer"], key="pvalue")
    actual_value = st.selectbox("Actual Value", options=["Suspicious", "Normal Customer"], key="avalue")
    
    st.form_submit_button()
    
    

