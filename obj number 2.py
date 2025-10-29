import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

st.header("Objective 2")
st.markdown("---")
st.title("1. Relationship Between English Skill Rating vs. Overall GPA Analysis")

# 1. Load the data
try:
    df = pd.read_csv("Computer_Science_and_Engineering_data.csv")
except FileNotFoundError:
    st.error("Error: The data file 'Computer_Science_and_Engineering_data.csv' was not found.")
    st.stop()

# 2. Function to create regression plot
def create_regression_plot(data):
    # Create figure and axes
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot regression
    sns.regplot(
        x='English',
        y='Overall',
        data=data,
        scatter_kws={'alpha': 0.6},
        line_kws={'color': 'red'},
        ax=ax
    )
    # Set titles and labels
    ax.set_title('Relationship Between English Skill Rating and Overall GPA', fontsize=14)
    ax.set_xlabel('English Skill Rating', fontsize=12)
    ax.set_ylabel('Overall GPA', fontsize=12)
    ax.grid(axis='both', linestyle='--', alpha=0.5)

    plt.tight_layout()
    st.pyplot(fig)

# 3. Run the plot
create_regression_plot(df)

###

st.title("2. Overall GPA Distribution by Semester Analysis")

# 1. Load the data (assuming the file is available in the app's environment)
try:
    df = pd.read_csv("Computer_Science_and_Engineering_data.csv")
except FileNotFoundError:
    st.error("Error: The data file 'Computer_Science_and_Engineering_data.csv' was not found.")
    st.stop()

# 2. Define custom order for semesters (optional but recommended for clarity)
semester_order = ['3rd', '4th', '6th', '7th']
# Filter for existing semesters in case the list is incomplete
existing_semesters = [s for s in semester_order if s in df['Semester'].unique()]

# 3. Create the plotting function
def create_violin_plot(data, order):
    # Create the figure and axes explicitly (replacing plt.figure())
    fig, ax = plt.subplots(figsize=(10, 6))

    # Create the violin plot using the axes object (ax)
    sns.violinplot(
        x="Semester",
        y="Overall",
        data=data,
        order=order, # Use the defined order
        inner='quartile', # Adds lines for quartile and median
        ax=ax
    )

    # Set titles and labels using the axes object
    ax.set_title('Overall GPA Distribution by Semester', fontsize=14)
    ax.set_xlabel('Semester', fontsize=12)
    ax.set_ylabel('Overall GPA', fontsize=12)
    
    # Set grid and layout
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    
    # Display the plot in Streamlit (replacing plt.show())
    st.pyplot(fig)

# 4. Run the function
create_violin_plot(df, existing_semesters)

####

st.title("3. Overall GPA Distribution by Extra Curricular Activity Status")

# 1. Load the data (assuming the file is available in the app's environment)
try:
    df = pd.read_csv("Computer_Science_and_Engineering_data.csv")
except FileNotFoundError:
    st.error("Error: The data file 'Computer_Science_and_Engineering_data.csv' was not found.")
    st.stop()

# 2. Create the plotting function
def create_violin_plot_extra(data):
    # Create the figure and axes explicitly (replacing plt.figure())
    fig, ax = plt.subplots(figsize=(10, 6))

    # Create the violin plot using the axes object (ax)
    # The 'No' category will not appear if there are no 'No' entries.
    sns.violinplot(
        x="Extra",
        y="Overall",
        data=data,
        inner='quartile', # Adds lines for quartile and median
        ax=ax
    )

    # Set titles and labels using the axes object
    ax.set_title('Overall GPA Distribution by Extra Curricular Activity Status', fontsize=14)
    ax.set_xlabel('Involved in Extra Curricular Activities', fontsize=12)
    ax.set_ylabel('Overall GPA', fontsize=12)
    
    # Set grid and layout
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    
    # Display the plot in Streamlit (replacing plt.show())
    st.pyplot(fig)

# 3. Run the function
create_violin_plot_extra(df)

# Optional: Add a note about the data distribution
if 'No' not in df['Extra'].unique():
    st.info("Note: All students in the uploaded dataset reported 'Yes' for Extra Curricular Activities, so the plot only displays one distribution.")
