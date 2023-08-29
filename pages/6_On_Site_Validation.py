import streamlit as st
import streamlit_authenticator as stauth
from streamlit_extras.switch_page_button import switch_page
import pandas as pd
import plotly.figure_factory as ff
from dependencies.functions import connectToDatabase, submitReport
import numpy as np

if 'authentication_status' not in st.session_state or st.session_state['authentication_status'] != True:
    switch_page('login')
    
if "customer_id" not in st.session_state or st.session_state['customer_id'] == None:
    switch_page("Home")
    
if 'model_prediction' not in st.session_state or st.session_state['model_prediction'] is None:
    switch_page("dashboard")
    
if 'submitted' not in st.session_state:
    st.session_state['submitted'] = False
    
    
left, _, _ = st.columns([1,5,1])

with left:
    if st. button("Previous", key='P1'):
        switch_page("customer prediction")
    
st.header("On Site Validation")


# customer_id = st.text_input("Customer ID", key="customer_id", )
customer_id = st.session_state.customer_id
st.write(f"**Customer ID:** {customer_id}")


predicted_value = st.session_state['model_prediction']
st.write(f"**Model Prediction:** {predicted_value}")

actual_value = st.selectbox("Actual Value", options=["Theft Case", "Normal Usage"], key="avalue")
    
if st.button(label="Submit"):
    try:
        submitReport(customerID=customer_id, predictedValue=predicted_value, actualValue=actual_value)
    except Exception:
        st.write("Unable to submit report")
    else:
        st.session_state['submitted'] = True

if st.session_state['submitted']:
    if st.button("Return to Home"):
        st.session_state['submitted'] = False
        switch_page("home")
            