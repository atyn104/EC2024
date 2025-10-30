import streamlit as st
import pandas as pd

# 1. MUAT DATA: Variabel DataFrame sudah bernama 'data'
file_path = "https://raw.githubusercontent.com/atyn104/EC2024/refs/heads/main/Computer_Science_and_Engineering_data.csv"
try:
    data = pd.read_csv(file_path) # Data dimuat ke variabel 'data'
except Exception as e:
    st.error(f"Gagal memuat data dari GitHub: {e}")
    # Inisialisasi data dummy jika gagal memuat
    data = pd.DataFrame({
        'HSC': [4.75, 4.42, 4.50, 3.32, 3.33],
        'SSC': [4.05, 5.00, 4.81, 4.50, 4.95],
        'Overall': [3.5, 3.2, 3.8, 4.0, 2.9],
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male']
    })

# Set page configuration
st.set_page_config(page_title="🎓 Student Performance Metrics", layout="wide")

# --- KOMPUTASI DATA YANG HILANG ---

# 2. KOMPUTASI: Hitung rata-rata HSC dan SSC
hsc_ssc_avg = (data['HSC'] + data['SSC']) / 2  # Menggabungkan nilai HSC dan SSC
average_hsc_ssc = hsc_ssc_avg.mean()

# Hitung distribusi gender (Asumsi nama kolom adalah 'Gender')
gender_distribution = data['Gender'].value_counts().to_dict()

# --- Displaying summary boxes ---
col1, col2, col3 = st.columns(3)

with col1:
    # 3. KOREKSI: Menggunakan variabel yang sudah dihitung
    st.metric(label="Purata HSC dan SSC", value=f"{average_hsc_ssc:.2f}")

with col2:
    # 4. KOREKSI: Pastikan kunci 'Male' dan 'Female' ada, lalu hitung totalnya.
    total_gender = gender_distribution.get('Male', 0) + gender_distribution.get('Female', 0)
    st.metric(label="Total Gender Samples", value=total_gender)

with col3:
    # Menampilkan Overall GPA
    average_cgpa = data['Overall'].mean()  # Menghitung purata GPA
    st.metric(label="Overall GPA", value=f"{average_cgpa:.2f}")

st.divider()
