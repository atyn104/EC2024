import streamlit as st

st.set_page_config(page_title="Student Performance Metrics")

# --- Page definitions ---
home = st.Page("home.py", title="Homepage", icon=":material/home:", default=True)
objective2 = st.Page("Performance Metrics.py", title="Objective Number 2", icon=":material/analytics:")

# --- Navigation menu (pages setup) ---
pg = st.navigation({
    "Menu": [home],
    "🎓 Student Performance Metrics"
    [objective2],
})
# --- Run selected page ---
pg.run()
