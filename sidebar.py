import streamlit as st

st.set_page_config(page_title="Student Performance Metrics")

# Define pages
home = st.Page("home.py", title="Homepage", icon=":material/home:", default=True)
visualise = st.Page("Student Performance Metrics/Objective Number 2.py",
                    title="Objective Number 2", icon=":material/analytics:")

# Group under a parent section
pg = st.navigation({
    "Menu": [home],
    "🎓 Student Performance Metrics": [visualise],
})

pg.run()
