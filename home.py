import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# URL for the data file
url = "https://raw.githubusercontent.com/atyn104/EC2024/refs/heads/main/Computer_Science_and_Engineering_data.csv"

# Set page configuration
st.set_page_config(
    page_title="Scientific Visualization",
    layout="wide"
)

st.title("🎓 Student Performance Metrics ")
st.markdown("---")

# Function to load data with caching
@st.cache_data
def load_data(data_url):
    try:
        df = pd.read_csv(data_url)
        return df
    except Exception as e:
        st.error(f"An error occurred while loading the file from the URL: {e}")
        return pd.DataFrame()

# Load data
Computer_Science_and_Engineering_df = load_data(url)

if Computer_Science_and_Engineering_df.empty:
    st.stop()

# Clean and convert 'HSC' and 'SSC' columns to numeric, handling errors or missing data
Computer_Science_and_Engineering_df['HSC'] = pd.to_numeric(Computer_Science_and_Engineering_df['HSC'], errors='coerce')
Computer_Science_and_Engineering_df['SSC'] = pd.to_numeric(Computer_Science_and_Engineering_df['SSC'], errors='coerce')

# Replace NaN values with the column mean (optional, can replace with 0 or other value)
Computer_Science_and_Engineering_df['HSC'].fillna(Computer_Science_and_Engineering_df['HSC'].mean(), inplace=True)
Computer_Science_and_Engineering_df['SSC'].fillna(Computer_Science_and_Engineering_df['SSC'].mean(), inplace=True)

# --- KOMPUTASI DATA YANG HILANG ---

# 2. KOMPUTASI: Hitung rata-rata HSC dan SSC
hsc_ssc_avg = (Computer_Science_and_Engineering_df['HSC'] + Computer_Science_and_Engineering_df['SSC']) / 2  # Menggabungkan nilai HSC dan SSC
average_hsc_ssc = hsc_ssc_avg.mean()

# Hitung distribusi gender (Asumsi nama kolom adalah 'Gender')
gender_distribution = Computer_Science_and_Engineering_df['Gender'].value_counts().to_dict()
male_count = gender_distribution.get('Male', 0)
female_count = gender_distribution.get('Female', 0)

# --- Displaying summary boxes ---
# Create 3 columns for a clean, organized summary box
col1, col2, col3 = st.columns(3)  # 3 columns for summary box

with col1:
    # 3. KOREKSI: Menggunakan variabel yang sudah dihitung
    st.metric(label="Purata HSC dan SSC", value=f"{average_hsc_ssc:.2f}",border=True)

with col2:
    # Kira jumlah lelaki dan perempuan secara berasingan
    male_count = gender_distribution.get('Male', 0)
    female_count = gender_distribution.get('Female', 0)
    
    # Kira jumlah keseluruhan pelajar
    total_students = male_count + female_count
    
    # Gabungkan ketiga-tiga maklumat dalam satu string untuk ditampilkan dalam kotak
    gender_summary = f"Lelaki: {male_count} | Perempuan: {female_count}"
    
    # Gunakan st.metric untuk memaparkan dalam satu kotak yang sederhana
    st.metric(label="Total Student",\nvalue=f"{total_students}", delta=gender_summary, border=True)


with col3:
    # Menampilkan Overall GPA
    average_cgpa = Computer_Science_and_Engineering_df['Overall'].mean()  # Menghitung purata GPA
    st.metric(label="Overall GPA", value=f"{average_cgpa:.2f}",border=True)

# Show raw data preview
st.subheader("1. Raw Data Preview")
st.dataframe(Computer_Science_and_Engineering_df.head(), use_container_width=True)
st.markdown("---")
