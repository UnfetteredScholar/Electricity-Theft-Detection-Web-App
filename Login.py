import streamlit as st
import streamlit_authenticator as stauth
from streamlit_extras.switch_page_button import switch_page
import yaml
from yaml.loader import SafeLoader

with open('resources/config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

st.session_state['authenticator'] = authenticator

name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status:
    switch_page('home')

elif authentication_status == False:
    st.error('Username/password is incorrect. Try again!')

elif authentication_status is None:
    st.warning('Please enter your username and password')