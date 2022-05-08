import pandas as pd
import streamlit as st
   

@st.cache
def load_data(nrows):
    data = pd.read_csv('output_files/Player_data.csv')
    return data

header = st.beta_container()
dataset = st.beta_container()

with header:
    st.title('NBA Player Compensation Analysis') 
    st.markdown('My goal in this project is to analyze data of the top 50 highest paid NBA players and try to determine if they are overpaid, \
    fairly paid, or underpaid vs their playing performance.')

with dataset:   
    st.write("NBA Clean Dataset")
    st.write("The datasets are from Basketballreference.com")
    
data = pd.read_csv('output_files/Player_data.csv')
