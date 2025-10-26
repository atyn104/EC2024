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

Business_Administration_df = load_data(url)

if Business_Administration_df.empty:
    st.stop()
    
st.subheader("1.Raw Data Preview")
st.dataframe(Business_Administration_df.head(), use_container_width=True)

if 'Gender' in Business_Administration_df.columns:
    # Count the occurrences of each gender
    gender_counts_df = Business_Administration_df['Gender'].value_counts().reset_index()
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

# Initialize the figure
plt.figure(figsize=(8, 6))

# sns.regplot includes the scatter plot and the linear regression line
sns.regplot(
    x='HSC',
    y='Overall',
    df=Business_Administration_df,
    scatter_kws={'alpha':0.6},  # Transparency for data points
    line_kws={'color':'red'},    # Color for the regression line
    ax=ax
)

# Apply titles and labels
ax.set.title('Relationship Between HSC Score and Overall GPA', fontsize=14)
ax.set.xlabel('HSC Score', fontsize=12)
ax.set.ylabel('Overall GPA', fontsize=12)
ax.set.grid(axis='both', linestyle='--', alpha=0.5)
plt.tight_layout()
st.pyplot(fig)
