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

st.title("🎓 Student Performance Metrics ")
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

# ---NO 1 Plotly Pie Chart (Distribution of Gender) ---
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

# ---NO 2 Student Count by Hometown and Gender ---

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
st.markdown("---")

        # ---NO 3 Income Level Distribution by Gender  ---

st.title("Income Level Distribution by Gender")

# 1. Load the data (assuming the file is available in the app's environment)
try:
    df = pd.read_csv("Business_Administration_Department_data.csv")
except FileNotFoundError:
    st.error("Error: The data file 'Business_Administration_Department_data.csv' was not found.")
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

# ---OBJ Number 2  ---

try:
    # Attempt to load the data file. Since this is a combined script, 
    # we assume the file 'Business_Administration_Department_data.csv' is present.
    # If the file is not available, the app will still run but the plot will be skipped.
    df = pd.read_csv("Business_Administration_Department_data.csv")
    data_loaded = True
except FileNotFoundError:
    # Create a placeholder DataFrame for running the app without the file
    df = pd.DataFrame({
        'English': [3, 4, 5, 2, 4],
        'Overall': [3.1, 3.8, 4.0, 2.5, 3.5]
    })
    data_loaded = False
    
# --- Plotting Function for Obj Number 2 ---
def create_regression_plot(data):
    """Generates and displays the English Skill Rating vs. Overall GPA Regression Plot."""
    
    # Check if the necessary columns exist before plotting
    if 'English' not in data.columns or 'Overall' not in data.columns:
        st.error("Data error: Required columns ('English' and 'Overall') not found in the dataset.")
        return

    # Create the figure and axes explicitly
    fig, ax = plt.subplots(figsize=(8, 6))

    # Create the regression plot
    sns.regplot(
        x='English',
        y='Overall',
        data=data,
        scatter_kws={'alpha':0.6, 'color': '#2C5D6F'}, # Blue/Teal color
        line_kws={'color':'#E54B4B', 'linewidth': 2}, # Red regression line
        ax=ax
    )

    # Set titles and labels
    ax.set_title('Relationship Between English Skill Rating and Overall GPA', fontsize=16, fontweight='bold')
    ax.set_xlabel('English Skill Rating (Input)', fontsize=13)
    ax.set_ylabel('Overall GPA (Outcome)', fontsize=13)
    
    # Customize appearance
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.grid(axis='y', linestyle=':', alpha=0.7)
    
    plt.tight_layout()
    
    # Display the plot in Streamlit
    st.pyplot(fig)
