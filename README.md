# T20-Score-Predictor
Project Overview
This project focuses on predicting the innings score of a T20 cricket match using machine learning techniques. The model predicts the final score of the batting team based on various factors such as the runs scored, wickets lost, overs passed, the opponent team, and the stadium where the match is played.

Problem Statement
In T20 cricket, predicting the final score of an innings is a complex task due to the dynamic nature of the game. The goal of this project is to build a machine learning model that can accurately predict the final score of the batting team based on the current match conditions.

Data Preprocessing
The dataset was preprocessed to handle both categorical and numerical features:

Categorical Features: The categorical features like batting_team, bowling_team, and city were encoded using OneHotEncoder. This approach converts categorical variables into a format that can be provided to ML algorithms to do a better job in prediction.
Numerical Features: Numerical features were standardized using StandardScaler to ensure that all features contribute equally to the prediction model.
Model Development
The model development involved the following steps:

Train-Test Split: The dataset was split into training and testing sets using an 80-20 ratio. This allowed for training the model on a large portion of the data while reserving a subset for evaluating its performance.
Pipeline Creation: A machine learning pipeline was created to streamline the preprocessing and modeling steps. The pipeline included:
OneHotEncoding for categorical features.
StandardScaling for numerical features.
XGBRegressor as the primary model for prediction.
Model Training: The XGBRegressor was chosen for its ability to handle large datasets with high accuracy. It was trained using 1000 estimators, a learning rate of 0.2, and a max depth of 12 to capture complex relationships in the data.
Model Evaluation: The model was evaluated using the R-squared score and Mean Absolute Error (MAE). The R-squared score was 0.99, indicating that the model explained 99% of the variance in the target variable, and the MAE was 1.62, showing that the average prediction error was 1.62 runs.
Results
The model demonstrated a high level of accuracy in predicting the innings score of the batting team. The low MAE and high R-squared score reflect the model's effectiveness in capturing the dynamics of T20 cricket and making precise score predictions.

Conclusion
This project showcases the application of machine learning in sports analytics, particularly in predicting outcomes in T20 cricket. The model's success highlights the potential of data-driven approaches in enhancing decision-making and strategy formulation in sports.

Future Work
Future improvements could involve:

Incorporating additional features such as player performance data, weather conditions, and pitch type.
Exploring ensemble models or deep learning techniques to further enhance prediction accuracy.
Expanding the model to predict other aspects of the game, such as win probabilities or individual player scores.
