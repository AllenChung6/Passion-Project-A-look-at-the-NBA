import pandas as pd
import streamlit as st
   

@st.cache
def load_data(nrows):
    data = pd.read_csv('output_files/Player_data.csv')
    return data

header = st.container()
dataset = st.container()
visuals = st.container()

with header:
    st.title('NBA Player Compensation Analysis') 
    st.markdown('My goal in this project is to analyze data of the top 50 highest paid NBA players and try to determine if they are overpaid, \
    fairly paid, or underpaid vs their playing performance.')

with dataset:   
    st.write("See how I created the NBA Dataset by cleaning and transforming different datasets here: \
         [link](https://share.streamlit.io/mesmith027/streamlit_webapps/main/MC_pi/streamlit_app.py)")
    st.write('NBA Cleaned Dataset')
    st.markdown('The dataset used is from Basketballreference.com')
    data = pd.read_csv('output_files/Player_data.csv')
    data

with visuals:
    st.write('Line Chart:')
    chart_data = pd.DataFrame(
        data=data,
        columns=['Performance','Age',]
    )
    st.line_chart(chart_data)
    
    