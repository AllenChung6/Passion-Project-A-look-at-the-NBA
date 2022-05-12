import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import base64
import seaborn as sns



st.set_page_config(layout="wide", page_title="NBA Stat Hub", page_icon='🖖')

header = st.container()
dataset = st.container()
visuals = st.container()
features = st.container()
adhoc = st.container()


with header:
    NBA = Image.open('/Users/allenc/PyCharmProjects/JupyterProjects/Passion-Project-A-look-at-the-NBA/Images/basketball_banner3.png')
    st.image(NBA, width = 1400)       
    st.write('You can follow and get an overview of my github project here: \
         [link](https://github.com/AllenChung6/Passion-Project-A-look-at-the-NBA)')
    st.write('Data here was gathered from www.basketball-reference.com')
    st.header('Stat Collector')
    st.write('You can view or collect NBA player stats to view or download here.')

# Create sidebar to filter year
st.sidebar.header('Filter Search')
selected_year = st.sidebar.selectbox('Year', list(reversed(range(1950,2023))))

# Load Data from Data source: www.basketball-reference.com
@st.cache
def load_data(year):
        url = "https://www.basketball-reference.com/leagues/NBA_" + str(year) + "_per_game.html"
        html = pd.read_html(url, header = 0) 
        data = html[0]
        raw_data=data.drop(data[data.Age == 'Age'].index)
        raw_data= raw_data.fillna(0)
        raw_data= raw_data.rename(columns={'Tm': 'Team'})
        playerstats = raw_data.drop(['Rk'], axis=1)
        return playerstats
playerstats = load_data(selected_year)

@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

@st.cache
def load_data():
    data = pd.read_csv('output_files/Player_data.csv')
    return data

def sidebar(image):
    sidebar_fmt = 'jpeg'

    st.markdown(
        f"""
      <style>
      [data-testid="stSidebar"] > div:first-child {{
          background: url(data:image/{sidebar_fmt};base64,{base64.b64encode(open(image, "rb").read()).decode()});
          background-size: cover;
      }}
      </style>
      """,
        unsafe_allow_html=True,
    )

image = '/Users/allenc/PyCharmProjects/JupyterProjects/Passion-Project-A-look-at-the-NBA/Images/basketball_sidebar.jpeg'
sidebar(image)

# Adding backgrounf image
#@st.cache
# def get_base64_of_bin_file(bin_file):
#     with open(bin_file, 'rb') as f:
#         data = f.read()
#     return base64.b64encode(data).decode()

# def set_png_as_page_bg(jpeg_file):
#     bin_str = get_base64_of_bin_file(jpeg_file)
#     page_bg_img = '''
#     <style>
#     .stApp{
#         background-image: url("data:image/jpeeg;base64,%s");
#         background-size: cover;
#     }
#     </style>
#     ''' % bin_str
    
#     st.markdown(page_bg_img, unsafe_allow_html=True)
#     return

# set_png_as_page_bg('/Users/allenc/PyCharmProjects/JupyterProjects/Passion-Project-A-look-at-the-NBA/Images/hardwood_court2.jpeg')

#st.sidebar.image("/Users/allenc/PyCharmProjects/JupyterProjects/Passion-Project-A-look-at-the-NBA/Images/hardwood_court2.jpeg", use_column_width=True)

with features:
    # Team Selection. Sort by unique team name and add elements to selected_team.
    sorted_by_unique_team = sorted(playerstats.Team.unique())
    selected_team = st.sidebar.selectbox('Team', list((x for x in sorted_by_unique_team)))

    # Position Selection
    uniq_pos = ['PG','SG','SF','PF','C']
    sel_pos = st.sidebar.multiselect('Position', uniq_pos)


with dataset:
    # Filtering Data
    df_selected_team = playerstats[(playerstats.Team == (selected_team)) & (playerstats.Pos.isin(sel_pos))]

    st.write('Display Player Stats below:')
    try:
    # To avoid StreamlitAPIException: ("Eexpected bytes, got a 'int' object", 'Conversion failed for column....'), converted to str
        player_df = df_selected_team.astype(str)
        st.dataframe(player_df)
    except Exception as e:
        st.error('There was an error. Please reload app')
    else:
        st.success('Dataframe Dimensions ' + str(df_selected_team.shape[0]) + ' rows and ' + str(df_selected_team.shape[1]) + ' columns.')

    # # Dataframe styling:
    # player_df.head(20).style.set_table_styles(
    # [{'selector': 'th',
    #     'props': [('background', '#7CAE00'),
    #               ('color', 'white'),
    #               ('font-family', 'verdana')]},

    # {'selector': 'td',
    #      'props': [('font-family', 'verdana')]},

    # {'selector': 'tr:nth-of-type(odd)',
    #      'props': [('background', '#DCDCDC')]},

    # {'selector': 'tr:nth-of-type(even)',
    #      'props': [('background', 'white')]},
    # ]
    # ).hide_index()


    # Download data as csv file
    csv = convert_df(player_df)
    st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name= f'{selected_team}_Player_data.csv',
    mime='text/csv',
    )

    #Download data as xls file
    xls = convert_df(player_df)
    st.download_button(
    label="Download data as XLS",
    data=xls,
    file_name= f'{selected_team}_Player_data.xls',
    mime='application/vnd.ms-excel',
    )

    # Seaborn Line Plot
    if st.button('Bar Plot (PlayerPts per game)'):
        st.header('Bar Plot: Player Pt Average Per Game')
        df_selected_team.to_csv(f'/Users/allenc/PyCharmProjects/JupyterProjects/Passion-Project-A-look-at-the-NBA/output_files/player_df.csv',index=False)
        df = pd.read_csv(f'/Users/allenc/PyCharmProjects/JupyterProjects/Passion-Project-A-look-at-the-NBA/output_files/player_df.csv')
        fig = plt.figure(figsize=(20,8))
        sns.barplot(x= df['PTS'], y= df['Player'], data=pd.melt(df, ['Player']))
        st.pyplot(fig)

with adhoc:
    # Import CSV file
    st.header('Ad-hoc Analysis: Player Salary vs Performance')
    st.write('Raw data sets were pulled from csv files on the basketballreference.com website')
    st.write('Raw Dataset: Salaries:')
    raw_salary = Image.open('/Users/allenc/PyCharmProjects/JupyterProjects/Passion-Project-A-look-at-the-NBA/Images/Raw_df_salary.png')
    st.image(raw_salary)  
    st.write('Raw Dataset: Advanced Stats:')
    raw_adv_stats = Image.open('/Users/allenc/PyCharmProjects/JupyterProjects/Passion-Project-A-look-at-the-NBA/Images/Raw_df_stats.png')
    st.image(raw_adv_stats)  
    st.write('Removed all players that played less than 50 games as they skewed data. Also removed the players with no advanced stats recorded.')
    st.write('I created a formula to calculate performance:')
    perf_formula = Image.open('/Users/allenc/PyCharmProjects/JupyterProjects/Passion-Project-A-look-at-the-NBA/Images/performance_formula.png')
    st.image(perf_formula) 
    st.write('Here are the percentiles I used for player salary:')
    salary_percentile = Image.open('/Users/allenc/PyCharmProjects/JupyterProjects/Passion-Project-A-look-at-the-NBA/Images/Salary_percentile.png')
    st.image(salary_percentile) 
    st.write('Here are the percentiles I used for player salary:')
    salary_percentile = Image.open('/Users/allenc/PyCharmProjects/JupyterProjects/Passion-Project-A-look-at-the-NBA/Images/Salary_percentile.png')
    st.image(salary_percentile)
    st.write('Here are the percentiles I used for player performance:')
    perf_percentile = Image.open('/Users/allenc/PyCharmProjects/JupyterProjects/Passion-Project-A-look-at-the-NBA/Images/perf_percentile.png')
    st.image(perf_percentile)  
    st.write('I applied the formula calculation to all players in the dataframe:')
    analysis = Image.open('/Users/allenc/PyCharmProjects/JupyterProjects/Passion-Project-A-look-at-the-NBA/Images/Analysis_code.png')
    st.image(analysis) 
    st.write('NBA Cleaned Dataset')
    data = pd.read_csv('output_files/Player_data.csv').drop(['Rank'], axis=1)

    def color(val):
        color = 'red' if val=='Overpaid' else 'orange' if val=='Fairly Paid' else 'green'
        return f'background-color: {color}'
    
    st.dataframe(data.style.applymap(color, subset=['Analysis']))
    #st.dataframe(data.style.format({"2021-22 Salaries ($)":"{:.2%}", "PER":"{:.2%}", "TS%":"{:.2%}","AST%":"{:.2%}","STL%":"{:.2%}","BLK%":"{:.2%}","TOV%":"{:.2%}","USG%":"{:.2%}","WS":"{:.2%}","WS/48":"{:.2%}", \
    #"BPM":"{:.2%}", "VORP":"{:.2%}","Performance":"{:.2%}"}))
  
    st.write('Tableau Data Visualizations')
    dashboard = Image.open('/Users/allenc/PyCharmProjects/JupyterProjects/Passion-Project-A-look-at-the-NBA/Images/Dashboard 1.png')
    st.image(dashboard) 


