# Passion-Project-A-look-at-NBA-Data

PART I - Stat Collector

In this project, I will be gathering data from the data source www.basketball-reference.com via webscraping and presenting it to the user. The user can filter through different criteria and the data will be presented to the user. The user can then print out this data into a csv file. 

I will then build a datapipeline that will load the csv file data into a sql database. 

I will be using Python, Pandas, Seaborn, Streamlit, and Apache Airflow for this part.


PART II - Adhoc Analysis, Player salary vs Perfomrance

Determining how much an NBA player is worth salary-wise is on the mind of NBA team owners everywhere. Once a player contract is up, an owner can do 1 of 3 things. They can either:

1. Overpay them to keep them
2. Pay them a fair contract hoping they will resign
3. Let them walk without a deal.

It is often not an easy task to navigate. Oftentimes even, NBA fanatics will debate whether a player is overpaid or not depending on their performance.
My goal in this project is to analyze data of the top 50 highest paid NBA players and try to determine if they are overpaid, fairly paid, or underpaid vs their playing performance.

For this project, I will be using Python, Pandas, Jupyter Notebook/Deepnote. I will be gathering data from different sources (api, csv files), cleaning the data, and analyzing the data. I will create data visualizations representing my findings as well.

<b>Worflow Diagram</b>
<img width="1440" alt="Data Pipeline Workflow" src="https://user-images.githubusercontent.com/99351833/168076195-f6e41b04-9a1c-4935-b23d-9135d205eaf3.png">

<b>NBA Stat Hub Application:</br>
![NBA Stat Hub](https://user-images.githubusercontent.com/99351833/168205454-283b4120-a604-4a47-b8a9-2423d8b3afab.png)


<b>Tableau Visualizations: </b>
![Dashboard 1](https://user-images.githubusercontent.com/99351833/167270070-ed7f2e9a-933a-44e8-8c78-2fa6fbc55d62.png)
![Player Salary vs Performance](https://user-images.githubusercontent.com/99351833/167270020-cf837695-4bc1-4e07-8957-78acac743532.png)
![Player Salary by Category](https://user-images.githubusercontent.com/99351833/167270022-a03274bd-1a2d-41c0-a9e6-d1c92ffd7572.png)
![Top 50 Player Performance](https://user-images.githubusercontent.com/99351833/167270027-8211ad84-6859-4795-8b9c-35bb14760f00.png)
![Age vs Usage % and TOV %](https://user-images.githubusercontent.com/99351833/167270030-4b420bde-1df0-4916-8a4d-369cbee5dc86.png)

Backlog:

-Finish building out Data Pipeline by loading csv file into SQL Database. Will use Docker + Airflow to achieve this. <br>
-Build out more seaborn visualizations for Stat Collector dataframes.
-Web scrape and display more datasets (such as Team data)
-Add more search criteria.
-Customize dataframe styling (for better looking dataframes)
-Deploy to Heroku.

