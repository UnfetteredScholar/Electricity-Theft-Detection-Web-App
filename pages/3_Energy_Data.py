import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import pandas as pd

if 'authentication_status' not in st.session_state or st.session_state['authentication_status'] != True:
    switch_page('login')
    
if "customer_id" not in st.session_state or st.session_state['customer_id'] == None:
    switch_page("Home")


if 'current_customer' in st.session_state and st.session_state.current_customer is not None:
    customer = st.session_state.current_customer
else:
    database = st.session_state['customers_data']
    
    validation_data = database["energy_usage_validation"]
    
    record = validation_data.find({'CONS_NO':st.session_state['customer_id']})[0]
    customer = pd.DataFrame(data=[record])
    customer = customer.drop(columns=['_id','FLAG'])
    st.session_state['current_customer']= customer

st.header("ENERGY USAGE DATA")

st.write(f"**Customer ID:** {customer['CONS_NO'][0]}")

st.write("**Unit: Kilowatt-hour/ kWh**")
st.write(customer)
