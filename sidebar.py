import streamlit as st

st.set_page_config(
    page_title="Student Performance Metrics"
)

visualise = st.Page('Performance Metrics.py', title='Student Performance Metrics', icon=":material/school:")

home = st.Page('home.py', title='Homepage', default=True, icon=":material/home:")

pg = st.navigation(
        {
            "Menu": [home, visualise]
        }
    )

pg.run()

with st.sidebar.expander("🎓 Student Performance Metrics", expanded=False):
    if st.button("Objective Number 2"):
        st.session_state.page = "Objective 2"
