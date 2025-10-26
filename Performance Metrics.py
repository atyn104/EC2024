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

st.title("Distribution of Gender in Business Administration Department")
st.markdown("---")

# Function to load data with caching
@st.cache_data
def load_data(data_url):
    try:
        df = pd.read_csv(url)
        return df
    except Exception as e:
        st.error(f"An error occurred while loading the file from the URL: {e}")
        return pd.Dataframe()

arts_df = load_data(url)

if arts_df.empty:
    st.stop()
    
st.subheader("1.Raw Data Preview")
st.dataframe(arts_df.head(), use_container_width=True)

if 'Gender' in arts_df.columns:
    # Count the occurrences of each gender
    gender_counts_df = arts_df['Gender'].value_counts().reset_index()
    gender_counts_df.columns = ['Gender', 'Count']

    col1, col2 = st.columns(2)

    # --- Plotly Pie Chart (Distribution of Gender) ---

    with col1:
         st.subheader("2.Distribution of Gender in Business Administration Department")
    
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

                # --- Visualization ---
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# --- 1. Define the correct file path ---
# Use a relative path assuming the CSV is in a 'data' folder
csv_file_path = os.path.join('data', 'ResearchInformation3.csv')

# Load the CSV file
# Use try-except to handle potential file not found or decoding errors
try:
    df = pd.read_csv(csv_file_path)
except FileNotFoundError:
    print(f"Error: The file was not found at {csv_file_path}")
    exit() # Stop execution if data isn't loaded
except UnicodeDecodeError:
    print("Error: Could not decode the file. Try specifying an encoding (e.g., encoding='latin-1').")
    exit()

# --- 2. Create and Save the Visualization ---

plt.figure(figsize=(10, 6))

sns.violinplot(
    x='Job',
    y='Overall',
    hue='Gender',
    data=df,
    palette={'Male': 'skyblue', 'Female': 'lightcoral'},
    split=True,
    inner='quartile'
)

plt.title('Objective 1: Overall GPA Distribution by Job Status and Gender', fontsize=14)
plt.xlabel('Has a Job', fontsize=12)
plt.ylabel('Overall GPA', fontsize=12)
plt.legend(title='Gender')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# --- 3. Save the output image file ---
# Create an 'images' directory if it doesn't exist
output_dir = 'images'
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, 'overall_gpa_job_gender_violinplot.png')

# Save the plot to the file path
plt.savefig(output_path)
plt.close() # Close the plot to free up memory

print(f"Visualization successfully generated and saved to: {output_path}")
