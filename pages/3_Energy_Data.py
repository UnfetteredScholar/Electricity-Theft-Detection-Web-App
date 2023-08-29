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

if "METER_ID" in customer:
    customer = customer.drop(columns=['METER_ID', 'SERVICE_TYPE', 'GEO_LOC', 'DISTRICT', 'SUPPLY_TYPE', 'TRAFFO_NAME'])

#Plot Charts
customer.set_index = 'CONS_NO'
# customer = customer.drop(columns=)

customer = customer.T

customer = customer.drop(['CONS_NO'])


left, _, right = st.columns([1,5,1])

with left:
    if st. button("Previous", key='P1'):
        switch_page("dashboard")

with right:
    if st. button("Next", key="N1"):
        switch_page("graph data")

st.header("ENERGY CONSUMPTION DATA")
st.markdown("**Last 3 Months Consumption**")

st.write(f"**Customer ID:** {st.session_state.customer_id}")

st.write("**Unit: Kilowatt-hour/ kWh**")


col1, col2, col3 = st.columns(3)

month1 = customer[0:30]
month2 = customer[30:60]
month3 = customer[60:90]

month1.columns = ["Daily Consumption/ kWh"]
month2.columns = ["Daily Consumption/ kWh"]
month3.columns = ["Daily Consumption/ kWh"]

with col1:
    st.subheader("Month 1")
    st.write(month1)
    
with col2:
    st.subheader("Month 2")
    st.write(month2)
    
with col3:
    st.subheader("Month 3")
    st.write(month3)


left, _, right = st.columns([1,5,1])

with left:
    if st. button("Previous", key='P2'):
        switch_page("dashboard")

with right:
    if st. button("Next", key="N2"):
        switch_page("graph data")
    