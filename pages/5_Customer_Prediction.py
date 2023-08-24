import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import pandas as pd
import plotly.figure_factory as ff
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
import joblib

def AnalyzeRecords(records:list):
    knn_model = joblib.load(open("models/knn_model.pkl", 'rb'))
    random_forest_model = joblib.load(open("models/random_forest_model.pkl",'rb'))
    
    knn_pred = knn_model.predict(records)
    knn_prob = knn_model.predict_proba(records).tolist()[0][1]
    rf_pred = random_forest_model.predict(records)
    rf_prob = random_forest_model.predict_proba(records).tolist()[0][1]
    
    theft_prob = ((knn_prob + rf_prob)/2) * 100

    res = 0
    if knn_pred[0] == rf_pred[0]:
        res = knn_pred
    else:
        res = 1
    
    return (res, theft_prob)

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
    customer = customer.drop(columns=['METER_ID', 'SERVICE_TYPE', 'GEO_LOC', 'DISTRICT', 'TRANS_CON'])

customer.set_index = 'CONS_NO'

customer = customer.T

customer = customer.drop(['CONS_NO'])

st.header("Customer Prediction")

st.write("Analyzing Customer Consumption Patterns...")
results = AnalyzeRecords(customer.T.values.tolist())
model_prediction = results[0]
probability = results[1]
    
if model_prediction == 0:
    st.write("## Prediction: :green[Normal Customer]")
else:
    st.write("### Prediction: :red[Suspicious Customer]")
st.write(f"### Probability of theft: {probability:.2f}%")
    
