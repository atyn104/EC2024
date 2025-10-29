import streamlit as st

st.set_page_config(page_title="Student Performance Metrics")

# --- Page definitions ---
home = st.Page("home.py", title="Homepage", icon=":material/home:", default=True)
performance = st.Page("Performance Metrics.py", title="Performance Metrics", icon=":material/analytics:")
objective2 = st.Page("obj number 2.py", title="Objective Number 2", icon=":material/insights:")

# --- Navigation menu ---
pg = st.navigation({
    "Menu": [home],
    "📊 Visualization Pages": [performance, objective2],
})
# --- Run the selected page ---
pg.run()
