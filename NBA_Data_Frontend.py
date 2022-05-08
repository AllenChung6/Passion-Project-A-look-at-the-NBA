import pandas as pd
import streamlit as st
import base64
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
       
st.title('A look into NBA Player Stats')

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

# Position Selection
unique_pos = ['PG','SG','SF','PF','C']
selected_pos = st.sidebar.multiselect('Position', unique_pos, unique_pos)

# Filtering Data
df_selected_team = playerstats[(playerstats.Tm == (selected_team)) & (playerstats.Pos.isin(selected_pos))]

st.header('Display Player Stats of Selected Team(s)')
st.success('Dataset queried. Data Dimension: ' + str(df_selected_team.shape[0]) + ' rows and ' + str(df_selected_team.shape[1]) + ' columns.')
# To avoid StreamlitAPIException: ("Eexpected bytes, got a 'int' object", 'Conversion failed for column....'), converted to str
df_selected_team_str = df_selected_team.astype(str)
st.dataframe(df_selected_team_str)
