import streamlit as st
import streamlit_authenticator as stauth
from streamlit_extras.switch_page_button import switch_page
import pandas as pd
import plotly.figure_factory as ff
from dependencies.functions import read_dataset
import numpy as np

if 'authentication_status' not in st.session_state or st.session_state['authentication_status'] != True:
    switch_page('login')

st.header("Customer Analysis")

st.subheader(f"Customer ID: {st.session_state['customer_id']}")


customers_data = st.session_state.customers_data

try:
    customer = customers_data.loc[customers_data['CONS_NO']== st.session_state['customer_id']]
except:
    e= ""    

st.write(customer)

customer.set_index = 'CONS_NO'
# customer = customer.drop(columns=['FLAG'])

customer = customer.T

customer = customer.drop(['CONS_NO'])

st.line_chart(customer)
st.bar_chart(customer)

if st.button("Begin Analysis"):
    st.write("Analyzing Customer Consumption Patterns...")
