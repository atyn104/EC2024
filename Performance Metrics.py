import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# URL for the data file
url = "https://raw.githubusercontent.com/atyn104/EC2024/refs/heads/main/Computer_Science_and_Engineering_data.csv"

# Set page configuration
st.set_page_config(
    page_title="Scientific Visualization",
    layout="wide"
)

st.title(" Objective 1")
st.markdown("""
-To analyze and compare the demographic profiles and socioeconomic backgrounds of students, with a focus on gender distribution within the Computer Science and Engineering department, place of origin, and income level.
""")
st.markdown("---")

# Function to load data with caching
@st.cache_data
def load_data(data_url):
    try:
        df = pd.read_csv(data_url)
        return df
    except Exception as e:
        st.error(f"An error occurred while loading the file from the URL: {e}")
        return pd.DataFrame()

# Load data
Computer_Science_and_Engineering_df = load_data(url)

if Computer_Science_and_Engineering_df.empty:
    st.stop()

# ---NO 1 Plotly Pie Chart (Distribution of Gender) ---
st.subheader("i. Distribution of Gender in Computer Science and Engineering Department ")

if 'Gender' in Computer_Science_and_Engineering_df.columns:
    # Count the occurrences of each gender
    gender_counts_df = Computer_Science_and_Engineering_df['Gender'].value_counts().reset_index()
    gender_counts_df.columns = ['Gender', 'Count']
    
    # Use plotly.express to create a pie chart
    fig_pie = px.pie(
        gender_counts_df, 
        values='Count', 
        names='Gender', 
        title='Gender Distribution',
        hole=0.4, # Optional: makes it a donut chart
        color_discrete_sequence=px.colors.sequential.RdBu # Optional: custom colors
    )
    
    # Update traces to show percentages inside the pie slices
    fig_pie.update_traces(textposition='inside', textinfo='percent+label')
    
    # Display the Plotly chart in Streamlit
    st.plotly_chart(fig_pie, use_container_width=True)
st.markdown("---")

# ---NO 2 Student Count by Hometown and Gender ---

st.subheader(" ii. Student Count by Hometown and Gender ")

# 1. Load the data (assuming the file is available in the app's environment)
try:
    df = pd.read_csv("Computer_Science_and_Engineering_data.csv")
except FileNotFoundError:
    st.error("Error: The data file 'Computer_Science_and_Engineering_data.csv' was not found.")
    st.stop()

# 2. Prepare the data: Group by Hometown and Gender and count occurrences
hometown_gender_counts = df.groupby(['Hometown', 'Gender']).size().unstack(fill_value=0)

# 3. Create the plotting function
def create_hometown_gender_plot(counts):
    # Create the figure and axes explicitly
    # This is critical for Streamlit to know which figure to display
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot the data using pandas plot function on the created axes (ax)
    counts.plot(kind='bar', ax=ax, colormap='viridis')

    # Set titles and labels using the axes object
    ax.set_title('Student Count by Hometown and Gender', fontsize=14)
    ax.set_xlabel('Hometown', fontsize=12)
    ax.set_ylabel('Number of Students', fontsize=12)
    
    # Use ax.tick_params or ax.set_xticklabels for rotations
    ax.tick_params(axis='x', rotation=0) 
    
    ax.legend(title='Gender')
    ax.grid(axis='y', linestyle='--', alpha=0.5)

    plt.tight_layout()

    # Display the plot in Streamlit
    st.pyplot(fig)

# 4. Run the function
create_hometown_gender_plot(hometown_gender_counts)
st.markdown("---")

# ---NO 3 Income Level Distribution by Gender ---

st.subheader(" iii. Income Level Distribution by Gender ")

# 1. Load the data (assuming the file is available in the app's environment)
try:
    df = pd.read_csv("Computer_Science_and_Engineering_data.csv")
except FileNotFoundError:
    st.error("Error: The data file 'Computer_Science_and_Engineering_data.csv' was not found.")
    st.stop()

# 2. Prepare the data: Create cross-tabulation table
# Calculate the percentage distribution of income levels within each gender
gender_income_counts = pd.crosstab(df['Gender'], df['Income'], normalize='index') * 100

# Define the logical order for income levels
income_order = [
    'Low (Below 15,000)',
    'Lower middle (15,000-30,000)',
    'Upper middle (30,000-50,000)',
    'High (Above 50,000)'
]

# Reindex to ensure consistent stacking order (using existing columns)
existing_cols = [col for col in income_order if col in gender_income_counts.columns]
gender_income_counts = gender_income_counts[existing_cols]

# 3. Create the plotting function
def create_stacked_bar_chart(counts):
    # Create the figure and axes explicitly
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot the normalized table as a stacked bar chart using the axes object (ax)
    counts.plot(
        kind='bar',
        stacked=True,
        colormap='viridis',  # Using a different colormap
        ax=ax
    )

    # Set titles and labels using the axes object
    ax.set_title('Income Level Distribution by Gender', fontsize=14)
    ax.set_xlabel('Gender', fontsize=12)
    ax.set_ylabel('Percentage of Students (%)', fontsize=12)
    
    # Set x-tick rotation
    ax.tick_params(axis='x', rotation=0)
    
    # Move legend outside using ax.legend()
    ax.legend(title='Income Level', bbox_to_anchor=(1.05, 1), loc='upper left') 
    
    ax.grid(axis='y', linestyle='--', alpha=0.5)

    plt.tight_layout()
    
    # Display the plot in Streamlit
    st.pyplot(fig)

# 4. Run the function
create_stacked_bar_chart(gender_income_counts)
