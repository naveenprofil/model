import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model = joblib.load('usps_mail_volume_predictor.sav')

st.title("USPS Mail Volume Predictor")
st.write("Enter details to predict mail volume for the next day.")

# User input
zone = st.selectbox('Geographic Zone', ['Zone 1', 'Zone 2', 'Zone 3', 'Zone 4'])
delivery_time = st.number_input('Delivery Time (hours)', min_value=1.0, max_value=12.0, step=0.1)
mail_volume_last_week = st.number_input('Mail Volume Last Week', min_value=50, max_value=500, step=1)
current_mail_volume = st.number_input('Current Mail Volume', min_value=50, max_value=500, step=1)

# Mapping zone to numeric value
zone_mapping = {'Zone 1': 1, 'Zone 2': 2, 'Zone 3': 3, 'Zone 4': 4}
zone_numeric = zone_mapping[zone]

# Prediction
if st.button('Predict Mail Volume'):
    input_data = pd.DataFrame([[zone_numeric, delivery_time, mail_volume_last_week, current_mail_volume]],
                              columns=['geographic_zone', 'delivery_time', 'mail_volume_last_week', 'current_mail_volume'])
    prediction = model.predict(input_data)
    st.success(f"Predicted Mail Volume for Next Day: {prediction[0]:.2f}")
