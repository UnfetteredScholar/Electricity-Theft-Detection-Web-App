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


left, _, right = st.columns([1,5,1])

with left:
    if st. button("Previous", key='P1'):
        switch_page("energy data")

with right:
    if st. button("Next", key="N1"):
        switch_page("customer prediction")
        

st.header("ENERGY USAGE PLOT")

#Plot Charts
customer.set_index = 'CONS_NO'
# customer = customer.drop(columns=)

customer = customer.T

customer = customer.drop(['CONS_NO'])

customer['Day'] = range(1, 91)

customer.columns = ["Usage/kWh", "Day"]

st.write("**Daily Usage Line Chart**")
st.line_chart(customer, x='Day', y='Usage/kWh')

st.write("**Daily Usage Bar Chart**")
st.bar_chart(customer, x='Day', y='Usage/kWh')



left, _, right = st.columns([1,5,1])

with left:
    if st. button("Previous", key='P2'):
        switch_page("energy data")

with right:
    if st. button("Next", key="N2"):
        switch_page("customer prediction")
    
