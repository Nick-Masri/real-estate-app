import streamlit as st
from firebase import firebase
firebase = firebase.FirebaseApplication("https://real-estate-1f934-default-rtdb.firebaseio.com")
import pandas as pd
def createPage():
    st.empty()
    st.title("View Listings")
    data = firebase.get("/data", None)
    # st.json(data)
    # st.write(data)
    data = pd.DataFrame(data)
    
    st.dataframe(data.T.reset_index(drop=True))
    return True

createPage()
