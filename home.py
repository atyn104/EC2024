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
        'CGPA': [3.5, 3.2, 3.8, 4.0, 2.9],
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male'],
        'Attendance': ['More than 3 Hours', 'Less than 3 Hours', 'More than 3 Hours', 'More than 3 Hours', 'Less than 3 Hours']
    })


# Set page configuration
st.set_page_config(page_title="🎓 Student Performance Metrics", layout="wide")

# --- KOMPUTASI DATA YANG HILANG ---

# 2. KOMPUTASI: Hitung rata-rata, distribusi gender, dan kehadiran DENGAN MENGGUNAKAN 'data'
average_cgpa = data['CGPA'].mean() # Asumsi nama kolom CGPA adalah 'CGPA'

# Hitung distribusi gender (Asumsi nama kolom adalah 'Gender')
gender_distribution = data['Gender'].value_counts().to_dict()

# Hitung distribusi kehadiran (Asumsi nama kolom adalah 'Attendance')
attendance_distribution = data['Attendance'].value_counts().to_dict()

# --- Sample data for the summary box (Opsional, tapi disimpan) ---
plo_2_value = 3.3
plo_3_value = 3.5
plo_4_value = 4.0

# --- Displaying summary boxes ---
col1, col2, col3 = st.columns(3)

with col1:
    # 3. KOREKSI: Menggunakan variabel yang sudah dihitung
    st.metric(label="Overall CGPA", value=f"{average_cgpa:.2f}")

with col2:
    # 4. KOREKSI: Pastikan kunci 'Male' dan 'Female' ada, lalu hitung totalnya.
    # Menggunakan .get(key, 0) untuk menangani kasus jika kunci tidak ada
    total_gender = gender_distribution.get('Male', 0) + gender_distribution.get('Female', 0)
    st.metric(label="Total Gender Samples", value=total_gender)

with col3:
    # 5. KOREKSI: Menggunakan .get(key, 0) untuk menghindari KeyError jika kategori tidak ada
    attendance_value = attendance_distribution.get('More than 3 Hours', 0)
    st.metric(label="Attendance (>3 Jam)", value=attendance_value)
