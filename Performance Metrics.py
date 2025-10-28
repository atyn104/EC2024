import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# URL for the data file
url = "https://raw.githubusercontent.com/atyn104/EC2024/refs/heads/main/Business_Administration_Department_data.csv"

# Set page configuration
st.set_page_config(
    page_title="Scientific Visualization",
    layout="wide"
)

st.title("Student Performance Metrics ")
st.markdown("---")

col1, col2, col3 = st.columns(3)
   
col1.metric(label="PLO 2", value=f"3.3", help="PLO 2: Cognitive Skill", border=True)
col2.metric(label="PLO 3", value=f"3.5", help="PLO 3: Digital Skill", border=True)
col3.metric(label="PLO 4", value=f"4.0", help="PLO 4: Interpersonal Skill", border=True)
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

Business_Administration_df = load_data(url)

if Business_Administration_df.empty:
    st.stop()
    
st.subheader("1. Raw Data Preview")
st.dataframe(Business_Administration_df.head(), use_container_width=True)
st.markdown("---")

# --- Plotly Pie Chart (Distribution of Gender) ---
st.subheader("2. Distribution of Gender in Business Administration Department")
    
if 'Gender' in Business_Administration_df.columns:
    # Count the occurrences of each gender
    gender_counts_df = Business_Administration_df['Gender'].value_counts().reset_index()
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


st.title("Student Count by Hometown and Gender")

# 1. Load the data (assuming the file is available in the app's environment)
try:
    df = pd.read_csv("Business_Administration_Department_data.csv")
except FileNotFoundError:
    st.error("Error: The data file 'Business_Administration_Department_data.csv' was not found.")
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
