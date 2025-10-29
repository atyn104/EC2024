import streamlit as st
import pandas as pd

# Muat naik data
file_path = "https://raw.githubusercontent.com/atyn104/EC2024/refs/heads/main/Computer_Science_and_Engineering_data.csv"
data = pd.read_csv(file_path)

# Tajuk untuk dashboard
st.title("🎓 Student Performance Metrics")

# 1. Purata CGPA
average_cgpa = data['Overall'].mean()
st.subheader("Average GPA")
st.metric(label="Overall Average CGPA: ", value=f"{average_cgpa:.2f}")

# 2. Distribusi Jantina
gender_distribution = data['Gender'].value_counts()
st.metric(label="Gender Distribution", value=str(gender_distribution['Male']))

# 3. Distribusi Pendapatan
income_distribution = data['Income'].value_counts()
st.metric(label="Family Income Distribution", value=str(income_distribution['High']))
