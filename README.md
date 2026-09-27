NYC Taxi Trip Duration Prediction

**Project Overview**

This project uses machine learning to predict NYC taxi trip duration based on trip-related and date/time features.

**Objective**

To build a regression model that can accurately predict taxi trip duration and deploy it as an interactive web application.

📊 Dataset

The model was trained on approximately 457K+ NYC taxi trip records.

The dataset contains information related to:

- Pickup date and time

- Drop-off date and time

- Pickup and drop-off locations

- Passenger count

- Trip-related information

The target variable is taxi trip duration.

🛠️ **Tech Stack**

- Python

- Pandas – Data manipulation and analysis

- NumPy – Numerical operations

- Scikit-learn – Machine learning and feature selection

- XGBoost – Gradient boosting regression

- Streamlit – Web application and model deployment

- Git & GitHub – Version control


🔍 Exploratory Data Analysis

The analysis focused on understanding:

    Trip duration distribution

    Pickup and drop-off patterns

    Time-of-day effects

    Day-of-week patterns

    Relationship between trip characteristics and duration

    Potential outliers and data-quality issues

⚙️ Feature Engineering

Date/time information was transformed into useful features such as:

    Pickup hour

    Pickup day

    Pickup month

    Day of week

    Other relevant time-based features

Trip-related features were also processed to provide the models with more meaningful information.
🧠 Feature Selection

To identify useful predictors and reduce unnecessary features, the project used:

    SelectKBest

    Mutual Information Regression

These techniques were evaluated as part of the model-development process.
Models Used

Linear Regression

Decision Tree

Random Forest

Lasso Regression

XGBoost

📈 Final Model & Results

Final Model: Tuned XGBoost Regressor

Primary Metric: MSE

Metric	Score

    R²	0.775
    
    MSE	31,715.30 seconds 
    
    RMSE 178.09 seconds 
    
    MAE	2.18 minutes 
    
🌐 Streamlit Application

The trained model is integrated with a Streamlit application for interactive taxi trip-duration prediction.

▶️ How to Run

    git clone https://github.com/Nandini3-g/NYC_taxi_trip_duration.git
    
    cd NYC_taxi_trip_duration
    
    pip install -r requirements.txt
    
    streamlit run app.py

**Application link:**

https://nyc-taxitrip-duration-s.streamlit.app/

👩‍💻 Author

Nandini

GitHub: https://github.com/Nandini3-g
