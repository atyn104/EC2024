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

plt.figure(figsize=(10, 6))

sns.violinplot(
    x='Job',
    y='Overall',
    hue='Gender',
    data=df,
    palette={'Male': 'skyblue', 'Female': 'lightcoral'},
    split=True,
    inner='quartile'
    ax=ax
)

ax.plt.title('Overall GPA Distribution by Job Status and Gender', fontsize=14)
ax.plt.xlabel('Has a Job', fontsize=12)
ax.plt.ylabel('Overall GPA', fontsize=12)
ax.plt.legend(title='Gender')
ax.plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()


