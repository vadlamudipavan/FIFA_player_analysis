import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns

ff_training_df = pd.read_csv("fifa21_raw_data.csv", low_memory=False)

attacking_positions = ['ST', 'CF', 'LW', 'RW', 'LM', 'RM']
defending_positions = ['CB', 'LB', 'RB', 'LWB', 'RWB']
central_positions = ['CAM', 'CM', 'CDM']

def classify_position(position):
    if position in attacking_positions:
        return 'Attacker'
    elif position in defending_positions:
        return 'Defender'
    elif position in central_positions:
        return 'Midfielder'
    else:
        return 'Midfielder'

ff_training_df['PositionClass'] = ff_training_df['Best Position'].apply(classify_position)

features_var = ['Attacking', 'Defending', 'Skill', 'Movement', 'Mentality', 'Goalkeeping']
target_var = 'PositionClass'
X = ff_training_df[features_var]
y = ff_training_df[target_var]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = RandomForestClassifier()
clf.fit(X_train, y_train)

st.title("Football Player Position Predictor")
st.image("fifa_world_cup_logo.png", width=550)

player_name = st.sidebar.text_input("Enter player's name:")
player_age = st.sidebar.text_input("Enter player's Age:")
player_weight = st.sidebar.text_input("Enter player's Weight(kgs):")
player_height = st.sidebar.text_input("Enter player's Height(in cm):")
st.sidebar.header("Input Features")
attacking = st.sidebar.slider("Attacking", min_value=50, max_value=500, value=50)
defending = st.sidebar.slider("Defending", min_value=50, max_value=300, value=50)
skill = st.sidebar.slider("Skill", min_value=50, max_value=500, value=50)
movement = st.sidebar.slider("Movement", min_value=50, max_value=500, value=50)
mentality = st.sidebar.slider("Mentality", min_value=50, max_value=500, value=50)
goalkeeping = st.sidebar.slider("Goalkeeping", min_value=50, max_value=500, value=50)

if st.sidebar.button("Predict"):
    prediction = clf.predict([[attacking, defending, skill, movement, mentality, goalkeeping]])

    st.subheader("Player Details & Prediction")
    prediction_text = "The predicted position class is: " + prediction[0]
    st.write(prediction_text)

    st.write("Player's Name:", player_name)
    st.write("Player's Age:", player_age)
    st.write("Player's Weight(kgs):", player_weight)
    st.write("Player's Height(in cm):", player_height)

    st.subheader("Feature Importances")
    importances = clf.feature_importances_
    importance_df = pd.DataFrame({'Feature': features_var, 'Importance': importances})
    
    plt.figure(figsize=(14, 12))
    sns.barplot(x='Importance', y='Feature', data=importance_df, palette="viridis")
    plt.title("Feature Importances")
    plt.xlabel("Importance")
    plt.ylabel("Feature")
    st.pyplot(plt)

    plt.figure(figsize=(15, 15))
    plt.pie(importances, labels=features_var, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title('Contribution of Each Feature')
    st.pyplot(plt)