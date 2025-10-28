import streamlit as st

st.set_page_config(page_title="Student Performance Metrics")

# Page definitions
home = st.Page("home.py", title="Homepage", icon=":material/home:", default=True)
visualise = st.Page("Performance Metrics.py", title="Objective Number 2", icon=":material/analytics:")

# Navigation menu
pg = st.navigation({
    "Menu": [home],
    "🎓 Student Performance Metrics": [visualise],
})

pg.run()
