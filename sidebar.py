import streamlit as st

st.set_page_config(
    page_title="Student Performance Metrics "
)

# 1. Definisi Halaman (Pastikan fail 'Performance Metrics.py', 'Objective 2.py', dan 'Objective 3.py' wujud)
home = st.Page('home.py', title='Homepage', default=True, icon=":material/home:")
visualise = st.Page('Performance Metrics.py', title='Student Performance Metrics', icon=":material/school:")
objective2 = st.Page('obj number 2.py', title='Objective 2', icon=":material/ads_click:")
objective3 = st.Page('obj number 3.py', title='Objective 3', icon=":material/ads_click:")

# 2. Tambahkan semua halaman ke dalam navigasi
# Semua halaman dalam senarai akan dipaparkan di bawah tajuk 'Menu'
pg = st.navigation(
        {
            "Menu": [home, visualise, objective2, objective3]
        }
    )

pg.run()
