import streamlit as st
import pickle
import pandas as pd
import numpy as np
import xgboost
from xgboost import XGBRegressor

pipe = pickle.load(open('/Users/mihir/Desktop/Projects/t20 wc score predictor/pipe.pkl','rb'))

teams = ['Australia',
    'India',
    'Bangladesh',
    'West Indies',
    'Nepal',
    'Scotland',
    'Netherlands',
    'Canada',
    'England',
    'South Africa',
    'Oman',
    'Pakistan',
    'New Zealand',
    'Afghanistan',
    'Ireland',
    'Sri Lanka',
    'United States of America',
    'Papua New Guinea',
    'Uganda',
    'Namibia']

cities = ['Dubai',
 'Abu Dhabi',
 'Colombo',
 'Al Amarat',
 'Sharjah',
 'Johannesburg',
 'Mirpur',
 'Auckland',
 'Sydney',
 'Lahore',
 'London',
 'Durban',
 'Dublin',
 'Nottingham',
 'Melbourne',
 'Pallekele',
 'Cape Town',
 'Dhaka',
 'Belfast',
 'Bridgetown',
 'Lauderhill',
 'St Lucia',
 'Hamilton',
 'Chittagong',
 'Gros Islet',
 'Centurion',
 'Southampton',
 'Christchurch',
 'Karachi',
 'Wellington',
 'Kirtipur',
 'Barbados',
 'Hobart',
 'Perth',
 'Brisbane',
 'Mount Maunganui',
 'Manchester',
 "St George's",
 'Chandigarh',
 'Windhoek',
 'Adelaide',
 'Ahmedabad',
 'Kolkata',
 'The Hague',
 'Birmingham',
 'North Sound',
 'Bristol',
 'Edinburgh',
 'Lucknow',
 'Houston',
 'Mumbai',
 'Providence',
 'Delhi',
 'Cardiff',
 'New York',
 'Dharamsala',
 'Tarouba',
 'Nagpur',
 'Kingston',
 'Napier',
 'Rajkot',
 'Bangalore',
 'Kingstown']

st.title('Cricket Score Predictor')

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select batting team',sorted(teams))
with col2:
    bowling_team = st.selectbox('Select bowling team', sorted(teams))

city = st.selectbox('Select city',sorted(cities))

col3,col4,col5 = st.columns(3)

with col3:
    current_score = st.number_input('Current Score')
with col4:
    overs = st.number_input('Overs done(works for over>5)')
with col5:
    wickets = st.number_input('Wickets out')

last_five = st.number_input('Runs scored in last 5 overs')

if st.button('Predict Score'):
    balls_left = 120 - (overs*6)
    wickets_left = 10 -wickets
    crr = current_score/overs

    input_df = pd.DataFrame(
     {'batting_team': [batting_team], 'bowling_team': [bowling_team],'city':city, 'current_score': [current_score],'balls_left': [balls_left], 'wickets_left': [wickets], 'crr': [crr], 'last_five': [last_five]})
    result = pipe.predict(input_df)
    st.header("Predicted Score - " + str(int(result[0])))
