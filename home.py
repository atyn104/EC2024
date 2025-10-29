import streamlit as st
import pandas as pd

# Muat naik data
file_path = "https://raw.githubusercontent.com/atyn104/EC2024/refs/heads/main/Computer_Science_and_Engineering_data.csv"
data = pd.read_csv(file_path)

# Set page configuration
st.set_page_config(page_title="🎓 Student Performance Metrics", layout="wide")

# --- Sample data for the summary box ---
plo_2_value = 3.3
plo_3_value = 3.5
plo_4_value = 4.0

# --- Displaying summary boxes ---
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Overall", value=f"{average_cgpa:.2f}")
    
with col2:
    male_and_female = gender_distribution['Male'] + gender_distribution['Female']
    st.metric(label="Gender", value=str"(male_and_female)")
    
with col3:
    st.metric(label="Attendance", value=str"(attendance_distribution['More than 3 Hours'])")

