import streamlit as st
from firebase import firebase
from pages import listings
import webbrowser
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(initial_sidebar_state="collapsed")

firebase = firebase.FirebaseApplication("https://real-estate-1f934-default-rtdb.firebaseio.com")

st.title("Login")
username = st.text_input("Username", key=3413)
password = st.text_input("Password", type="password", key="password")
if st.button("Submit", key=1):
  if username == "admin" and password == "1234":
    # listings.createPage()
    # webbrowser.open("http://localhost:8501/listings", new=0)
    
    switch_page("listings")

  else:
    st.error("Incorrect username or password")

