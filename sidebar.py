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

with st.sidebar:
    st.header("Objective Number 2")
    
    # --- Top-Level Item 1: Homepage ---
    if st.button("🏠 Homepage", key="nav_home", use_container_width=True):
        st.session_state.page = "Homepage"

    st.markdown("---")
    
