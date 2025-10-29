import streamlit as st
st.set_page_config(page_title="Student Performance Metrics")

# --- Page definitions ---
# PASTIKAN Anda menyertakan "pages/" di sini
home = st.Page("pages/home.py", title="Homepage", icon=":material/home:", default=True)
performance = st.Page("pages/Performance Metrics.py", title=" Objective Number 1 ", icon=":material/insights:")
objective2 = st.Page("pages/obj number 2.py", title=" Objective Number 2 ", icon=":material/insights:")
objective3 = st.Page("pages/obj number 3.py", title=" Objective Number 3 ", icon=":material/insights:")

# --- Navigation menu ---
pg = st.navigation({ 
    "Menu": [home],
    "📊 Visualization Pages": [performance, objective2, objective3], 
})

# --- Run the selected page ---
pg.run() # Baris ini sekarang seharusnya bekerja
