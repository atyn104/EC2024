import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

# URL for the data file
url = "https://raw.githubusercontent.com/atyn104/EC2024/refs/heads/main/arts_faculty_data.csv"

# Set page configuration
st.set_page_config(
    page_title="Scientific Visualization",
    layout="wide"
)

st.title("Distribution of Gender in Arts Faculty")
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
    
    # --- Data Processing for Charts ---

if 'Gender' in arts_df.columns:
    # Count the occurrences of each gender
    gender_counts_df = arts_df['Gender'].value_counts().reset_index()
    gender_counts_df.columns = ['Gender', 'Count']

    col1, col2 = st.columns(2)

    # --- Plotly Pie Chart (Distribution of Gender) ---

    with col1:
         st.subheader("2.Distribution of Gender in Arts Faculty (Pie Chart)")
    
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

    # --- Plotly Bar Chart (Distribution of Gender) ---

    with col2:
         st.subheader("3. Distribution of Gender in Arts Faculty (Bar Chart)")

    # Use plotly.express to create a bar chart
    fig_bar = px.bar(
        gender_counts_df, 
        x='Gender', 
        y='Count', 
        title='Distribution of Gender in Arts Faculty',
        labels={'Count': 'Count', 'Gender': 'Gender'} # Optional: set axis labels
    )
    
       # Optional: Customize layout for better appearance
    fig_bar.update_layout(
           xaxis_title='Gender', 
           yaxis_title='Count',
           xaxis={'categoryorder': 'total descending'}
       )
    
    # Display the Plotly chart in Streamlit
    st.plotly_chart(fig_bar, use_container_width=True)

else:
    st.error("Could not load data. Please check the URL and your internet connection.")

# --- Example DataFrame creation for testing if needed ---
# data = {'H.S.C or Equivalent study medium': ['Bangla', 'English', 'Bangla', 'English', 'Bangla', 'Bangla']}
# arts_df = pd.DataFrame(data)

st.header("H.S.C or Equivalent Study Medium Analysis")
st.markdown("---")

# Count the occurrences of each study medium
study_medium_counts = arts_df['H.S.C or Equivalent study medium'].value_counts()

# Create the Matplotlib figure and axes
fig, ax = plt.subplots(figsize=(8, 6))

# Create a bar chart on the axes
study_medium_counts.plot(kind='bar', ax=ax)

# Set title and labels
ax.set_title('Distribution of H.S.C or Equivalent Study Medium')
ax.set_xlabel('Study Medium')
ax.set_ylabel('Count')
ax.set_xticklabels(study_medium_counts.index, rotation=45, ha='right')

# Adjust layout to prevent labels from overlapping
plt.tight_layout()

# Display the Matplotlib figure in Streamlit
st.pyplot(fig)

# Assuming 'arts_df' is already loaded as a pandas DataFrame

st.header("Coaching Center Attendance Analysis")
st.markdown("---")

# Count the occurrences of coaching center attendance
coaching_counts = arts_df['Did you ever attend a Coaching center?'].value_counts()

# Create the Matplotlib figure and axes
fig, ax = plt.subplots(figsize=(8, 6))

# Create a bar chart on the axes
coaching_counts.plot(kind='bar', ax=ax)

# Set title and labels
ax.set_title('Distribution of Coaching Center Attendance')
ax.set_xlabel('Attended Coaching Center')
ax.set_ylabel('Count')

# Set x-tick rotation (using ax.set_xticklabels for better control)
# We set the labels explicitly to ensure rotation=0 is applied correctly to the labels
ax.set_xticklabels(coaching_counts.index, rotation=0)

# Adjust layout to prevent labels from overlapping
plt.tight_layout()

# Display the Matplotlib figure in Streamlit
st.pyplot(fig)

# Assuming 'arts_df' is already loaded as a pandas DataFrame

st.header("Arts Program Distribution Analysis")
st.markdown("---")

# Count the occurrences of each Arts Program
arts_program_counts = arts_df['Arts Program'].value_counts()

# Create the Matplotlib figure and axes
fig, ax = plt.subplots(figsize=(8, 6))

# Create a bar chart on the axes
arts_program_counts.plot(kind='bar', ax=ax)

# Set title and labels
ax.set_title('Distribution of Arts Programs')
ax.set_xlabel('Arts Program')
ax.set_ylabel('Count')

# Set x-tick rotation and alignment for the labels
# We use ax.set_xticklabels for better control over alignment ('ha' or horizontalalignment)
ax.set_xticklabels(arts_program_counts.index, rotation=45, ha='right')

# Adjust layout to prevent labels from overlapping
plt.tight_layout()

# Display the Matplotlib figure in Streamlit
st.pyplot(fig)
