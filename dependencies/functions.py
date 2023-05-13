import pandas as pd
import streamlit as st

@st.cache_data(show_spinner=False)
def read_dataset(path:str):
    df = pd.read_csv(path)
    
    return df