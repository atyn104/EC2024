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
        return pd.Dataframe()

Business_Administration_df = load_data(url)

if Business_Administration_df.empty:
    st.stop()
    
st.subheader("1.Raw Data Preview")
st.dataframe(Business_Administration_df.head(), use_container_width=True)
st.markdown("---")

    # --- Plotly Pie Chart (Distribution of Gender) ---

st.subheader("2.Distribution of Gender in Business Administration Department")
    
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

                # --- Visualization ---

# Example Context (assuming the previous code structure)
    
st.subheader("3. HSC Score vs. Overall GPA")
required_cols = ['HSC', 'Overall'] # <--- MUST ALIGN WITH THE LINE ABOVE
if not Business_Administration_df.empty and all(col in Business_Administration_df.columns for col in required_cols):
            
            # 1. Initialize Figure and Axes
            fig, ax = plt.subplots(figsize=(8, 6))

            sns.regplot(
                x='HSC',
                y='Overall',
                data=Business_Administration_df, # Use your defined DataFrame
                scatter_kws={'alpha':0.6},
                line_kws={'color':'red'},
                ax=ax # IMPORTANT: Plot on the defined Axes
            )

            ax.set_title('Relationship Between HSC Score and Overall GPA', fontsize=14)
            ax.set_xlabel('HSC Score', fontsize=12)
            ax.set_ylabel('Overall GPA', fontsize=12)
            ax.grid(axis='both', linestyle='--', alpha=0.5)

            plt.tight_layout()
            st.pyplot(fig, use_container_width=True)

     # --- Visualization ---

st.subheader("3. Overall GPA Distribution by Job Status and Gender")
required_cols = ['Job', 'Overall', 'Gender'] # <--- MUST ALIGN WITH THE LINE ABOVE
if not Business_Administration_df.empty and all(col in Business_Administration_df.columns for col in required_cols):
    
           plt.figure(figsize=(14, 6))

        sns.violinplot(
           x='Job_Status',
           y='Overall_GPA',
           hue='Student_Gender',
           df=Business_Administration_df,
           palette={'Male': 'skyblue', 'Female': 'lightcoral'},
           split=True,
           inner='quartile',# Adds lines for quartile and median
           ax=ax
        )
            
           ax.set_title('Overall GPA Distribution by Job Status and Gender', fontsize=14)
           ax.set_xlabel('Has a Job', fontsize=12)
           ax.set_ylabel('Overall GPA', fontsize=12)
           ax.legend(title='Gender')
           ax.grid(axis='y', linestyle='--', alpha=0.7)

           plt.tight_layout()
           st.pyplot(fig, use_container_width=True)

    
