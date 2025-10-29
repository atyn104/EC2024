import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# URL for the data file
url = "https://raw.githubusercontent.com/atyn104/EC2024/refs/heads/main/Business_Administration_Department_data.csv"

# Function to load data with caching
@st.cache_data
def load_data(data_url):
    try:
        df = pd.read_csv(data_url)
        return df
    except Exception as e:
        st.error(f"An error occurred while loading the file from the URL: {e}")
        return pd.DataFrame()

Business_Administration_df = load_data(url)

if Business_Administration_df.empty:
    st.stop()
    
st.dataframe(Business_Administration_df.head(), use_container_width=True)
st.header("Objective 2")
st.markdown("---")
st.title("English Skill Rating vs. Overall GPA Analysis")


# 1. Load the data
try:
    df = pd.read_csv("Business_Administration_Department_data.csv")
except FileNotFoundError:
    st.error("Error: The data file 'Business_Administration_Department_data.csv' was not found.")
    st.stop()

# 2. Function to create regression plot
def create_regression_plot(data):
    # Create figure and axes
    fig, ax = plt.subplots(figsize=(8, 6))

    # Plot regression
    sns.regplot(
        x='English',
        y='Overall',
        data=data,
        scatter_kws={'alpha': 0.6},
        line_kws={'color': 'red'},
        ax=ax
    )

    # Set titles and labels
    ax.set_title('Relationship Between English Skill Rating and Overall GPA', fontsize=14)
    ax.set_xlabel('English Skill Rating', fontsize=12)
    ax.set_ylabel('Overall GPA', fontsize=12)
    ax.grid(axis='both', linestyle='--', alpha=0.5)

    plt.tight_layout()
    st.pyplot(fig)

# 3. Run the plot
create_regression_plot(df)

