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

# --- Dummy Data for Demonstration ---
# Since gender_counts_total is not defined, we'll create a dummy variable.
# In your actual app, this variable will come from your dataset processing.
data = {'Male': 150, 'Female': 180}
gender_counts_total = pd.Series(data)
# --- End of Dummy Data ---

st.title("Student Gender Distribution Dashboard")
st.subheader("Count by Gender (Total Dataset)")

# Display the raw counts
st.dataframe(gender_counts_total.rename('Count').to_frame().T)

# Create the Matplotlib figure
fig, ax = plt.subplots(figsize=(6, 4))

# Create the bar plot using Seaborn on the specified axes (ax)
sns.barplot(
    x=gender_counts_total.index, 
    y=gender_counts_total.values, 
    ax=ax # IMPORTANT: Pass the axes object to Seaborn
)

# Set the title and labels for the plot
ax.set_title('Student Count by Gender (Total Dataset)')
ax.set_xlabel('Gender')
ax.set_ylabel('Number of Students')

# Show the plot in Streamlit using st.pyplot()
st.pyplot(fig)
