import streamlit as st
import pickle
import pandas as pd

pipe=pickle.load(open('pipe.pkl', 'rb'))

teams=['Sunrisers Hyderabad',
 'Mumbai Indians',
 'Royal Challengers Bangalore',
 'Kolkata Knight Riders',
 'Kings XI Punjab',
 'Chennai Super Kings',
 'Rajasthan Royals',
 'Delhi Capitals']

cities=['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
       'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
       'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
       'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
       'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
       'Sharjah', 'Mohali', 'Bengaluru']

st.title("IPL Win Predictor")
st.header("Enter Match Details")
col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox("Select Batting Team", sorted(teams))
with col2:
    bowling_team = st.selectbox("Select Bowling Team", sorted(teams))

selected_city = st.selectbox("Select City", sorted(cities))
target = st.number_input("Target Score", min_value=1)

col3, col4, col5 = st.columns(3)
with col3:
    current_score = st.number_input("Current Score", min_value=0)
with col4:
    overs_done = st.number_input("Overs Completed", min_value=0.1, max_value=19.5, step=0.1)
with col5:
    wickets_out = st.number_input("Wickets Out", min_value=0, max_value=10, step=1)

if st.button("Predict Probability"):
    runs_left = target - current_score
    balls_left = 120 - (overs_done * 6)
    wickets_left = 10 - wickets_out
    crr = current_score / overs_done
    rrr = (runs_left * 6) / balls_left

    input_df = pd.DataFrame({
        'batting_team': [batting_team],
        'bowling_team': [bowling_team],
        'city': [selected_city],
        'runs_left': [runs_left],
        'balls_left': [balls_left],
        'wickets_left': [wickets_left],
        'target': [target],
        'crr': [crr],
        'rrr': [rrr]
    })

    result = pipe.predict_proba(input_df)

    st.write(f"{batting_team} has a {round(result[0][1]*100, 2)}% chance to win the match")
    st.write(f"{bowling_team} has a {round(result[0][0]*100, 2)}% chance to win the match")