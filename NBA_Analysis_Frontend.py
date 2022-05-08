import pandas as pd
import streamlit as st

st.title('NBA Player Compensation Analysis')   

@st.cache
def load_data(nrows):
    data = pd.read_csv('output_files/Player_data.csv')
    return data

st.write("NBA DATASET")
data = pd.read_csv('output_files/Player_data.csv')
st.write(data)
