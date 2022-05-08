import pandas as pd
import streamlit as st
import base64
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

header = st.container()
dataset = st.container()
visuals = st.container()
features = st.container()

with header:       
    st.title('A look into NBA Player Stats')
    st.write('You can follow and get an overview of my github project here: \
         [link](https://github.com/AllenChung6/Passion-Project-A-look-at-the-NBA)')
    st.write('Data here was gathered from www.basketball-reference.com')

# Create sidebar to filter year
st.sidebar.header('Filter Search')
selected_year = st.sidebar.selectbox('Year', list(reversed(range(1950,2023))))

# Load Data from Data source: www.basketball-reference.com
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

with features:
    # Team Selection. Sort by unique team name and add elements to selected_team.
    sorted_by_unique_team = sorted(playerstats.Tm.unique())
    selected_team = st.sidebar.selectbox('Tm', list((x for x in sorted_by_unique_team)))

    # Position Selection
    uniq_pos = ['PG','SG','SF','PF','C']
    sel_pos = st.sidebar.multiselect('Position', uniq_pos, uniq_pos)

    #def download_file(data);
    #    csv = data.to_csv



with dataset:
    # Filtering Data
    df_selected_team = playerstats[(playerstats.Tm == (selected_team)) & (playerstats.Pos.isin(sel_pos))]

    st.write('Display Player Stats below:')
    try:
    # To avoid StreamlitAPIException: ("Eexpected bytes, got a 'int' object", 'Conversion failed for column....'), converted to str
        df_selected_team_str = df_selected_team.astype(str)
        st.dataframe(df_selected_team_str)
    except Exception as e:
        st.error('There was an error. Please reload app')
    else:
        st.success('Dataset queried. Data Dimension: ' + str(df_selected_team.shape[0]) + ' rows and ' + str(df_selected_team.shape[1]) + ' columns.')


