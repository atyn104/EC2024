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
def create_gpa_job_gender_violin_plot(df: pd.DataFrame):
    """
    Generates a split violin plot visualizing the distribution of Overall GPA
    based on Job Status ('Job') and split by 'Gender'.

    Args:
        df (pd.DataFrame): The DataFrame containing 'Job', 'Overall', and 'Gender' columns.
                           'Job' should be categorical (e.g., Yes/No),
                           'Overall' should be the GPA score (numeric),
                           'Gender' should be categorical (e.g., Male/Female).
    """
    # Set the size of the plot
    plt.figure(figsize=(14, 6))

    # Create the split violin plot
    sns.violinplot(
        x='Job',
        y='Overall',
        hue='Gender',
        data=df,
        palette={'Male': 'skyblue', 'Female': 'lightcoral'},
        split=True,
        inner='quartile' # Adds lines for quartile and median
    )

    # Add titles and labels
    plt.title('Overall GPA Distribution by Job Status and Gender', fontsize=16, fontweight='bold')
    plt.xlabel('Has a Job', fontsize=14)
    plt.ylabel('Overall GPA', fontsize=14)
    plt.legend(title='Gender', fontsize=10, title_fontsize='12')
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)

    # Add a grid for better readability
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Adjust layout to prevent labels from overlapping
    plt.tight_layout()
    
    # Display the plot
    plt.show()
    
    # Optionally, save the plot to a file (uncomment to use)
    # plt.savefig('overall_gpa_job_gender_violin.png', dpi=300)


if __name__ == '__main__':
    # --- Data Loading Placeholder ---
    # NOTE: Replace this with your actual data loading mechanism (e.g., from a CSV)
    # This is a dummy DataFrame for demonstration purposes.
    data = {
        'Overall': [3.5, 3.8, 3.2, 2.9, 4.0, 3.1, 3.6, 3.3, 3.0, 3.9],
        'Job': ['Yes', 'Yes', 'No', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No'],
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Female', 'Male', 'Female', 'Male']
    }
    df_example = pd.DataFrame(data)

    print("Generating violin plot...")
    create_gpa_job_gender_violin_plot(df_example)
    print("Plot display finished.")
