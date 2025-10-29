import streamlit as st

st.set_page_config(page_title="Student Performance Metrics")

# --- Page definitions ---
home = st.Page("home.py", title="Homepage", icon=":material/home:", default=True)
objective2 = st.Page("Performance Metrics.py", title="Objective Number 2", icon=":material/analytics:")

# --- Navigation menu ---
pg = st.navigation({
    "Menu": [home],
    "📊 This page visualizes graphs based on objectives": [],
    "🎓 Student Performance Metrics": [objective2],
})

pg.run()
