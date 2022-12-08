import streamlit as st
from firebase import firebase
import json

firebase = firebase.FirebaseApplication("https://real-estate-1f934-default-rtdb.firebaseio.com")



def upload():
    st.title("Upload a new listing")
    st.markdown('# Insert New Data')
    # new_data = st.text_input("Enter new data", key="new_data")
    price = st.number_input("Property Price Estimate")
    city = st.text_input("City of Location")
    state = st.text_input("State")
    data = {}
    
    if st.button("Submit", key=2):
        data['city'] = city
        data['state'] = state
        data['price'] = price

        firebase.post("/data", data)

upload()
