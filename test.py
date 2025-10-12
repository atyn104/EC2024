import streamlit as st
import pandas as pd
import plotly.express as px

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
    
st.subheader("Raw Data Preview")
st.dataframe(arts_df.head(), use_container_width=True)
    
    # --- Data Processing for Charts ---

if 'Gender' in arts_df.columns:
    # Count the occurrences of each gender
    gender_counts_df = arts_df['Gender'].value_counts().reset_index()
    gender_counts_df.columns = ['Gender', 'Count']

    col1, col2 = st.columns(2)

    # --- Plotly Pie Chart (Distribution of Gender) ---

    with col1:
         st.subheader("Distribution of Gender in Arts Faculty (Pie Chart)")
    
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
         st.subheader("Distribution of Gender in Arts Faculty (Bar Chart)")

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
