import streamlit as st
import pandas as pd
from notebooks.distance_utils import calculate_distance 
import pickle


# Load model
with open("model_xg.pkl", "rb") as file:
    model = pickle.load(file)


st.title('Taxi Trip Duration')

# -------Inputs----------
pickup_datetime  = st.datetime_input(label = "Enter datetime of  journey")

pickup_latitude  = st.number_input(
    label = 'Enter pickup latitude ',
    placeholder= 'Enter pickup latitude',
    value=34.712234, format="%.6f",
    min_value=34.712234,
    max_value= 51.881084)

pickup_longitude = st.number_input(
    label = 'Enter pickup longitude',
    placeholder= 'Enter pickup longitude',
    value=-121.933342,format="%.6f",
    min_value= -121.933342,
    max_value=-72.074333)

dropoff_latitude = st.number_input(
    label = 'Enter drop latitude',
    placeholder = 'Enter drop latitude',
    value=32.181141,format="%.6f",
    min_value=32.181141,
    max_value=43.921028	)

dropoff_longitude = st.number_input(
    label = 'Enter drop longitude',
    placeholder= 'Enter drop longitude',
    value=-121.933304,format="%.6f",
    min_value = -121.933304,
    max_value = -72.022408)

## creating dataframe 
X_test = pd.DataFrame({'pickup_latitude':[float(pickup_latitude)],
                        'pickup_longitude':[float(pickup_longitude)], 
                        'dropoff_latitude':[float(dropoff_latitude)],
                        'dropoff_longitude':[float(dropoff_longitude)]})

                       # 'pickup_month', 'pickup_day_of_week',
       #'pickup_day_of_month', 'pickup_hour', 'pickup_minute', 'distance(km)'})


##---- EXTRACTING DATE FEATURES 
def extract_date_features(date):

    
    X_test['pickup_month']= date.month ## extract date
    X_test['pickup_day_of_week'] = date.weekday()## Extract day 
    X_test['pickup_day_of_month'] = date.day##Extract date
    X_test['pickup_hour']  = date.hour  ## Extract pick Hour of the trip
    X_test['pickup_minute'] = date.minute ## Extract pick minutes 


extract_date_features(pickup_datetime)

## Calculating distance
if st.button('Find Distance'):
  
    st.session_state.distance = calculate_distance(pickup_latitude,pickup_longitude,dropoff_latitude,dropoff_longitude)
    st.write('Total Approximate Distance(km)',st.session_state.distance)
    ## adding distance feature to DataFrame
    

 ## model predictions 
if st.button('Calculate Trip Duration'):
    if 'distance' in st.session_state:

        X_test['distance(km)'] = st.session_state.distance

        trip_duration = model.predict(X_test)

        duration_min = int(trip_duration[0] / 60)

        st.success(f'Estimated Trip Duration: {duration_min} minutes')

    else:
        st.warning(
            'Please calculate the distance first.'
        )



