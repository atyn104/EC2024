import streamlit as st

# Set up page configuration
st.set_page_config(page_title="Student Performance Metrics", layout="wide")

# --- Define pages ---
home = "Home Page"
performance = "Performance Metrics"
objective2 = "Objective Number 2"
objective3 = "Objective Number 3"

# --- Navigation menu ---
page = st.sidebar.selectbox(
    "Select a page",
    [home, performance, objective2, objective3]
)

# --- Display content based on the selected page ---
if page == home:
    st.title("Homepage")
    st.write("Welcome to the homepage of the Student Performance Metrics dashboard.")
    
elif page == performance:
    st.title("Performance Metrics")
    st.write("Here we display the performance metrics of the students.")

elif page == objective2:
    st.title("Objective Number 2")
    st.write("Details for Objective Number 2.")

elif page == objective3:
    st.title("Objective Number 3")
    st.write("Details for Objective Number 3.")
