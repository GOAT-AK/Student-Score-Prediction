import streamlit as st
import pandas as pd
import numpy as np
import pickle


with open("Student Score Prediction/exam_score_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("Student Score Prediction/scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

with open("Student Score Prediction/encoders.pkl", "rb") as f:
    encoders = pickle.load(f)


st.title("📘 Student Exam Score Predictor")
st.write("Enter the details below to estimate the student's exam score:")

# Two-column layout
col1, col2 = st.columns(2)

# Categorical
with col1:
    parental_involvement = st.selectbox("Parental Involvement", ["Low", "Medium", "High"])
    access_to_resources = st.selectbox("Access to Resources", ["Low", "Medium", "High"])
    extracurricular = st.selectbox("Extracurricular Activities", ["Yes", "No"])
    motivation = st.selectbox("Motivation Level", ["Low", "Medium", "High"])
    internet_access = st.selectbox("Internet Access", ["Yes", "No"])
    family_income = st.selectbox("Family Income", ["Low", "Medium", "High"])
    teacher_quality = st.selectbox("Teacher Quality", ["Low", "Medium", "High"])
    peer_influence = st.selectbox("Peer Influence", ["Negative", "Neutral", "Positive"])
    learning_disability = st.selectbox("Learning Disabilities", ["Yes", "No"])


# Numeric
with col2:
    parent_education = st.selectbox("Parental Education Level", ["High School", "College", "Postgraduate"])
    distance_home = st.selectbox("Distance from Home", ["Near", "Moderate", "Far"])
    hours_studied = st.number_input("Hours Studied per Week", min_value=0, max_value=80, value=10)
    attendance = st.slider("Attendance (%)", 0, 100, 85)
    sleep_hours = st.slider("Sleep Hours per Night", 3, 12, 7)
    previous_scores = st.number_input("Previous Average Score", min_value=0, max_value=100, value=70)
    tutoring_sessions = st.number_input("Tutoring Sessions per Month", min_value=0, max_value=20, value=2)
    physical_activity = st.number_input("Physical Activity Hours per Week", min_value=0, max_value=20, value=3)


# Prepare Input Data
input_data = pd.DataFrame([{
    "Hours_Studied": hours_studied,
    "Attendance": attendance,
    "Parental_Involvement": parental_involvement,
    "Access_to_Resources": access_to_resources,
    "Extracurricular_Activities": extracurricular,
    "Sleep_Hours": sleep_hours,
    "Previous_Scores": previous_scores,
    "Motivation_Level": motivation,
    "Internet_Access": internet_access,
    "Tutoring_Sessions": tutoring_sessions,
    "Family_Income": family_income,
    "Teacher_Quality": teacher_quality,
    "Peer_Influence": peer_influence,
    "Physical_Activity": physical_activity,
    "Learning_Disabilities": learning_disability,
    "Parental_Education_Level": parent_education,
    "Distance_from_Home": distance_home
}])

# Ensure correct column order (same as training)
expected_features = [
    "Hours_Studied",
    "Attendance",
    "Parental_Involvement",
    "Access_to_Resources",
    "Extracurricular_Activities",
    "Sleep_Hours",
    "Previous_Scores",
    "Motivation_Level",
    "Internet_Access",
    "Tutoring_Sessions",
    "Family_Income",
    "Teacher_Quality",
    "Peer_Influence",
    "Physical_Activity",
    "Learning_Disabilities",
    "Parental_Education_Level",
    "Distance_from_Home"
]
input_data = input_data[expected_features]

# Encode categorical features
for col, le in encoders.items():
    if col in input_data.columns:
        input_data[col] = le.transform(input_data[col])

# Scale numeric features
input_scaled = scaler.transform(input_data)

# Prediction
if st.button("Predict Exam Score"):
    prediction = model.predict(input_scaled)[0]
    st.success(f"📊 Predicted Exam Score: **{prediction:.2f}**")
