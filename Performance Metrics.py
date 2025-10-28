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

# Function to load data with caching
@st.cache_data
def load_data(data_url):
    try:
        df = pd.read_csv(url)
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
    gender_counts_df = Business_Administration_df['Gender'].value_counts().reset_index()
    gender_counts_df.columns = ['Gender', 'Count']
    
    fig_pie = px.pie(
        gender_counts_df, 
        values='Count', 
        names='Gender', 
        title='Gender Distribution',
        hole=0.4,
        color_discrete_sequence=px.colors.sequential.RdBu
    )
    
    fig_pie.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig_pie, use_container_width=True)

st.markdown("---")

# --- HSC Score vs. Overall GPA ---
st.subheader("3. HSC Score vs. Overall GPA")
required_cols = ['HSC', 'Overall']

if not Business_Administration_df.empty and all(col in Business_Administration_df.columns for col in required_cols):
    fig, ax = plt.subplots(figsize=(8, 6))

    sns.regplot(
        x='HSC',
        y='Overall',
        data=Business_Administration_df,
        scatter_kws={'alpha':0.6},
        line_kws={'color':'red'},
        ax=ax
    )

    ax.set_title('Relationship Between HSC Score and Overall GPA', fontsize=14)
    ax.set_xlabel('HSC Score', fontsize=12)
    ax.set_ylabel('Overall GPA', fontsize=12)
    ax.grid(axis='both', linestyle='--', alpha=0.5)
    plt.tight_layout()
    st.pyplot(fig, use_container_width=True)

st.markdown("---")

# --- CORRECTED: Overall GPA Distribution by Job Status and Gender ---
# Alternative: Using Plotly for the violin plot (add this after the HSC vs GPA plot)
st.subheader("4. Overall GPA Distribution by Job Status and Gender")

required_cols = ['Job', 'Overall', 'Gender']

if not Business_Administration_df.empty and all(col in Business_Administration_df.columns for col in required_cols):
    
    # Using Plotly for interactive violin plot
    fig = px.violin(
        Business_Administration_df,
        x='Job',
        y='Overall',
        color='Gender',
        box=True,
        points=False,
        title='Overall GPA Distribution by Job Status and Gender'
    )
    
    fig.update_layout(
        xaxis_title='Job Status',
        yaxis_title='Overall GPA'
    )
    
    st.plotly_chart(fig, use_container_width=True)
        
    except Exception as e:
        st.error(f"Error creating violin plot: {e}")
        
        # Alternative: Use a boxplot instead
        st.info("Trying alternative visualization (Boxplot)")
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.boxplot(
            x='Job',
            y='Overall',
            hue='Gender',
            data=Business_Administration_df,
            palette={'Male': 'skyblue', 'Female': 'lightcoral'}
        )
        ax.set_title('Overall GPA Distribution by Job Status and Gender (Boxplot)')
        ax.set_xlabel('Job Status')
        ax.set_ylabel('Overall GPA')
        plt.tight_layout()
        st.pyplot(fig, use_container_width=True)

else:
    missing_cols = [col for col in required_cols if col not in Business_Administration_df.columns]
    st.error(f"Missing required columns: {missing_cols}")
    st.info(f"Available columns: {list(Business_Administration_df.columns)}")
