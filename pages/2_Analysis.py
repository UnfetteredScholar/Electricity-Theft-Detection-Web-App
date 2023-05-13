import streamlit as st
import streamlit_authenticator as stauth
from streamlit_extras.switch_page_button import switch_page
import pandas as pd
import plotly.figure_factory as ff
from dependencies.functions import read_dataset
import numpy as np

st.header("Customer Analysis")

st.subheader(f"Meter ID: {st.session_state['meter_id']}")

path = "C:\\Users\\atoto\\Documents\\Final Year Project\\ElectricityTheftDetection\\data\\data_features_reduced.csv"

customers_data = read_dataset(path)

try:
    customer = customers_data.loc[customers_data['CONS_NO']== st.session_state['meter_id']]
except:
    e= ""    

st.write(customer)

customer.set_index = 'CONS_NO'
customer = customer.drop(columns=['FLAG'])

customer = customer.T

customer = customer.drop(['CONS_NO'])

st.line_chart(customer)
st.bar_chart(customer)

if st.button("Begin Analysis"):
    st.write("Analyzing Customer Consumption Patterns...")
