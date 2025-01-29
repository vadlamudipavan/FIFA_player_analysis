# FIFA Player Position Predictor

## Overview
The FIFA Player Position Predictor is a web-based application developed using Streamlit. It utilizes the FIFA 2021 dataset and machine learning techniques to classify football players into one of three position classes: attackers, defenders, or midfielders. This project offers valuable insights into player attributes and their significance, providing a useful tool for football coaches, scouts, and enthusiasts.

## Features
- **Player Position Prediction**: Predicts whether a player is an attacker, defender, or midfielder using a **Random Forest Classifier**.
- **Interactive Input Interface**: Users can input player attributes such as attacking, defending, skill, movement, mentality, and goalkeeping via sliders.
- **Visualizations**: Displays feature importance through bar graphs and pie charts for better interpretability.
- **Practical Insights**: Aids in talent identification, team optimization, and strategic planning.

## Dataset
The project uses the FIFA 2021 dataset sourced from [Kaggle](https://www.kaggle.com/datasets/yagunnersya/fifa-21-messy-raw-dataset-for-cleaning-exploring/code). The dataset includes:
- Player ratings and potential
- Skill sets and physical characteristics
- Nationality, age, preferred foot, and club affiliation

## Machine Learning Model
Six machine learning algorithms were evaluated on the dataset with the following accuracy results:
- **Random Forest**: 95.30% (Best-performing model)
- K-Nearest Neighbors: 95.05%
- Logistic Regression: 94.82%
- Support Vector Machine: 94.64%
- Decision Tree: 94.64%
- Naïve Bayes: 73.47% (Least suitable)

Based on the results, the **Random Forest Classifier** was chosen for its superior accuracy and reliability in classifying player positions.

### Feature Selection
Key features used for prediction include:
- **Attacking**
- **Defending**
- **Skill**
- **Movement**
- **Mentality**
- **Goalkeeping**

The target variable is the **Position Class**, categorized as attacker, defender, or midfielder.

## Setup Instructions
Follow these steps to set up and run the application:

1. **Install Required Packages**  
   Ensure the following Python packages are installed:

2. **Extract Project Files**  
Download and extract the project files. Locate the `phase3.py` file in the `dhanushr_harzeena_pavanven_phase_3` folder.

3. **Run the Application**  
Open a terminal, navigate to the directory containing `phase3.py`, and execute:
This will launch the application in your default web browser.

4. **Interact with the Application**  
- Input player attributes using the sliders.
- Click "Predict" to classify the player's position.
- View feature importance visualizations in bar graph and pie chart formats.

## Recommendations
- The tool is designed to assist in player scouting, recruitment, and team optimization.
- Insights into feature importance help franchises focus on critical traits for specific positions, enabling data-driven decision-making.

## Future Enhancements
- **Player Comparison Tools**: Add features for side-by-side player comparisons.
- **Real-Time Updates**: Integrate real-time performance data for live predictions.
- **Customization**: Provide tailored solutions for various leagues and teams.
- **Scalability**: Expand functionality to support diverse user needs and larger datasets.

## Conclusion
This project showcases the power of machine learning in football analytics. By leveraging a Random Forest Classifier and an intuitive web interface, the FIFA Player Position Predictor simplifies complex decision-making processes for team strategies and scouting. It empowers users to make informed decisions, enhancing team composition and overall performance.

## References
- [FIFA 2021 Dataset](https://www.kaggle.com/datasets/yagunnersya/fifa-21-messy-raw-dataset-for-cleaning-exploring/code)
- [Streamlit Documentation](https://streamlit.io/)
- [Scikit-Learn Documentation](https://scikit-learn.org/stable/)
