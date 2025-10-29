import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns


st.title("1. Student Count by Attendance Rate and Gender")

# 1. Load the data (assuming the file is available in the app's environment)
try:
    df = pd.read_csv("Computer_Science_and_Engineering_data.csv")
except FileNotFoundError:
    st.error("Error: The data file 'Computer_Science_and_Engineering_data.csv' was not found.")
    st.stop()

# 2. Prepare the data
# Define the desired order of attendance categories
attendance_order = ['Below 40%', '40%-59%', '60%-79%', '80%-100%']

# Group by both 'Attendance' and 'Gender' and count the size of each group
attendance_gender_counts = df.groupby(['Attendance', 'Gender']).size().reset_index(name='Count')

# Convert 'Attendance' to a Categorical type with the specified order
attendance_gender_counts['Attendance'] = pd.Categorical(
    attendance_gender_counts['Attendance'],
    categories=attendance_order,
    ordered=True
)

# Sort the DataFrame by the new categorical column
attendance_gender_counts = attendance_gender_counts.sort_values('Attendance')

# 3. Create the plotting function
def create_grouped_attendance_plot(data):
    # Create the figure and axes explicitly (replaces plt.figure())
    fig, ax = plt.subplots(figsize=(10, 6))

    # Use seaborn's barplot with the 'hue' parameter, passing 'ax=ax'
    sns.barplot(
        data=data,
        x='Attendance',
        y='Count',
        hue='Gender',  # Separates men and women
        palette='Set2', # A contrasting palette
        ax=ax          # Plot onto the explicit axes object
    )

    # Set titles and labels using the axes object (ax)
    ax.set_title('Student Count by Attendance Rate and Gender', fontsize=14)
    ax.set_xlabel('Attendance Rate', fontsize=12)
    ax.set_ylabel('Number of Students', fontsize=12)
    ax.legend(title='Gender') 
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Set x-tick rotation
    ax.tick_params(axis='x', rotation=0)

    plt.tight_layout()
    
    # 4. Display the plot in Streamlit (replaces plt.show())
    st.pyplot(fig)

# 5. Run the function
create_grouped_attendance_plot(attendance_gender_counts)

# Add a note based on the specific data
if '80%-100%' in df['Attendance'].unique() and len(df['Attendance'].unique()) == 1:
    st.info("Note: All students in the dataset fall into the **80%-100%** attendance category.")

# --- Streamlit App Code ---

st.title("2. Student Count by Attendance Rate and Hometown")

# 1. Load the data (assuming the file is available in the app's environment)
try:
    df = pd.read_csv("Computer_Science_and_Engineering_data.csv")
except FileNotFoundError:
    st.error("Error: The data file 'Computer_Science_and_Engineering_data.csv' was not found.")
    st.stop()

# 2. Prepare the data: Create cross-tabulation table
# Group by Attendance and Hometown and count occurrences
attendance_hometown_counts = df.groupby(['Attendance', 'Hometown']).size().unstack(fill_value=0)

# Define the desired order of attendance categories
attendance_order = ['Below 40%', '40%-59%', '60%-79%', '80%-100%']

# Reindex to ensure consistent ordering of attendance categories
# Note: For your current data (all '80%-100%'), only that bar will appear.
attendance_hometown_counts = attendance_hometown_counts.reindex(attendance_order).fillna(0) # Fill NaN from reindex with 0

# 3. Create the plotting function
def create_grouped_hometown_plot(counts):
    # Create the figure and axes explicitly (replacing plt.figure())
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot the data using pandas plot method on the created axes (ax)
    counts.plot(
        kind='bar',
        ax=ax,
        colormap='viridis'
    )

    # Set titles and labels using the axes object
    ax.set_title('Student Count by Attendance Rate and Hometown', fontsize=14)
    ax.set_xlabel('Attendance Rate', fontsize=12)
    ax.set_ylabel('Number of Students', fontsize=12)
    
    # Set x-tick rotation
    ax.tick_params(axis='x', rotation=0) 
    
    ax.legend(title='Hometown')
    ax.grid(axis='y', linestyle='--', alpha=0.5)

    plt.tight_layout()
    
    # 4. Display the plot in Streamlit (replacing plt.show())
    st.pyplot(fig)

# 5. Run the function
create_grouped_hometown_plot(attendance_hometown_counts)

# Add a note based on the specific data
if '80%-100%' in df['Attendance'].unique() and len(df['Attendance'].unique()) == 1:
    st.info("Note: All students in the dataset fall into the **80%-100%** attendance category.")
