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
st.write(f"Overall Average CGPA: {average_cgpa:.2f}")

# 2. Distribusi Jantina
gender_distribution = data['Gender'].value_counts()
st.subheader("Gender Distribution")
st.write(gender_distribution)

# 3. Distribusi Pendapatan
income_distribution = data['Income'].value_counts()
st.subheader("Family Income Distribution")
st.write(income_distribution)
