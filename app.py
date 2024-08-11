import streamlit as st
import csv
import pandas as pd
import numpy as py

nameArr = []
descArray = []
amountArray = []
pictureArray = []

df = pd.read_csv('sprint1items.csv')

for i in range(38):
    nameArr.append(df.iloc[i][0])
    descArray.append(df.iloc[i][1])
    amountArray.append(df.iloc[i][2])
    pictureArray.append(df.iloc[i][3])
    



with st.container():
    st.subheader("Sprint 1 Shop")
    col1, col2 = st.columns(2)

    def button_state(*args, key=None, **kwargs):
        if key is None:
            raise ValueError("Must pass key")
        
        if key not in st.session_state:
            st.session_state[key] = False

        if st.button(*args, **kwargs):
            st.session_state[key] = not st.session_state[key]

        return st.session_state[key]
    
    with col1:
        for i in range(0,38,2):
            if button_state(nameArr[i], key="interesting_button" + str(i)):
                st.write(descArray[i])
                st.write("Amount: " + str(amountArray[i]))
                st.image(pictureArray[i])
    
    with col2:
        for j in range(1,39,2):
            if button_state(nameArr[j], key ="pleaseWork" + str(j)):
                st.write(descArray[j])
                st.write("Amount: " + str(amountArray[j]))
                st.image(pictureArray[j])

            

    
            

    
