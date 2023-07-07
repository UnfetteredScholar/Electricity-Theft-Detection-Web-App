import streamlit as st
import streamlit_authenticator as stauth
from streamlit_extras.switch_page_button import switch_page
import pandas as pd
import plotly.figure_factory as ff
from dependencies.functions import read_dataset
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
import pickle
import joblib


def AnalyzeRecords(records:list):
    knn_model = joblib.load(open("models/knn_model.pkl", 'rb'))
    random_forest_model = joblib.load(open("models/random_forest_model.pkl",'rb'))
    
    knn_pred = knn_model.predict(records)
    rf_pred = random_forest_model.predict(records)
    
    res = 0
    if knn_pred[0] == rf_pred[0]:
        res = knn_pred
    else:
        res = 1
    
    return res
    
if 'authentication_status' not in st.session_state or st.session_state['authentication_status'] != True:
    switch_page('login')

st.header("Customer Analysis")

st.subheader(f"Customer ID: {st.session_state['customer_id']}")


database = st.session_state['customers_data']
    
validation_data = database["energy_usage_validation"]
    
record = validation_data.find({'CONS_NO':st.session_state['customer_id']})[0]
customer = pd.DataFrame(data=[record])
customer = customer.drop(columns='_id')

st.write(customer)


#Plot Charts
customer.set_index = 'CONS_NO'
customer = customer.drop(columns=['FLAG'])

customer = customer.T

customer = customer.drop(['CONS_NO'])

st.line_chart(customer)
st.bar_chart(customer)



if st.button("Begin Analysis"):
    st.write("Analyzing Customer Consumption Patterns...")
    model_prediction = AnalyzeRecords(customer.T.values.tolist())
    
    st.header("Prediction")
    if model_prediction == 0:
        st.write("Normal Customer")
    else:
        st.write("Suspicious Customer")
    
    
    

