import pandas as pd
import streamlit as st
import base64
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
       
st.title('A look at NBA Data')

st.sidebar.header('Filter Search')
selected_year = st.sidebar.selectbox('Year', list(reversed(range(1950,2023))))

@st.cache
def load_data(year):
    url = "https://www.basketball-reference.com/leagues/NBA_" + str(year) + "_per_game.html"
    html = pd.read_html(url, header = 0)
    data = html[0]
    raw=data.drop(data[data.Age == 'Age'].index)
    raw = raw.fillna(0)
    playerstats = raw.drop(['Rk'], axis=1)
    return playerstats
playerstats = load_data(selected_year)

# Team Selection
sorted_unique_team = sorted(playerstats.Tm.unique())
selected_team = st.sidebar.selectbox('Tm', list((x for x in sorted_unique_team)))


