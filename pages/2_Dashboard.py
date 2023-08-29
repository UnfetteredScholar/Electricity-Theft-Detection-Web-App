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


st.header("DASHBOARD")
st.subheader("Customer Info")

st.write(f"**Customer ID:** {customer['CONS_NO'][0]}")
if "METER_ID" in customer:
    st.write(f"**Meter ID:** {customer['METER_ID'][0]}")
    st.write(f"**Service Type:** {customer['SERVICE_TYPE'][0]}")
    st.write(f"**Geo Location:** {customer['GEO_LOC'][0]}")
    st.write(f"**District:** {customer['DISTRICT'][0]}")
    st.write(f"**Transformer Connection:** {customer['TRANS_CON'][0]}")

col1, col2 = st.columns(2)

with col1:
    # st.image(open("./images/Table.jpeg"))
    st.image(image="images/table.jpg",width=200)
    if st.button("View Energy Data"):
        switch_page("energy data")
    st.image(image="images/plot.jpg",width=200)
    if st.button("View Graphical Data"):
        switch_page("graph data")
    
with col2:
    st.image(image="images/predict.jpg",width=200)
    if st.button("Load and Predict Activity"):
        switch_page("customer prediction")
    st.image(image="images/report.jpg",width=200)
    if st.button("On Site Validation"):
        switch_page("on site validation")

