import streamlit as st

# Set the page config
st.set_page_config(page_title="Student Performance Metrics")

# --- Page definitions ---
# PASTIKAN Anda menyertakan "pages/" di sini
home = "home.py"
performance = "Performance Metrics.py"
objective2 = "obj number 2.py"
objective3 = "obj number 3.py"

# --- Navigation menu ---
page = st.sidebar.radio("Navigate", 
                       ["Homepage", "Objective Number 1", "Objective Number 2", "Objective Number 3"])

# --- Run the selected page ---
if page == "Homepage":
    (open('home.py').read())
    st.write(f"Loading {home}...")
    # You can import and display the contents of home.py here, like:
    # exec(open('pages/home.py').read())

elif page == "Objective Number 1":
    st.write(f"Loading {performance}...")
    # exec(open('pages/Performance Metrics.py').read())

elif page == "Objective Number 2":
    st.write(f"Loading {objective2}...")
    # exec(open('pages/obj number 2.py').read())

elif page == "Objective Number 3":
    st.write(f"Loading {objective3}...")
    # exec(open('pages/obj number 3.py').read())
