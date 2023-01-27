import streamlit as st
import pandas as pd

# Create a title page
st.title("Compact QAQC Roster")

# Add some content to the page
st.write("For historical roster updates refer to Expansive QAQC Roster Option from the Home Screen ")

# Read the excel file
file_path = "C:/Users/roman/OneDrive/Desktop/HORNE/Production Supervisor/Rosters/QAQC Roster Details_1.18.23.xlsx"
df = pd.read_excel(file_path, sheet_name='CARRL Compact Roster')

# Show the data in a table
st.write("Last updated 1/26/2023 at 11:30 am PST", key='last_updated', align='right')
table = st.dataframe(df)

# Create a sidebar
st.sidebar.title("Roster Filters")

# Get the unique options from the dataframe
unique_project_roles = df['Project Role'].unique()
unique_qc_teams = df['QC Team'].unique()
unique_companies = df['Company'].unique()

# Create a drop-down box in the sidebar to select the column to filter by
filter_options = ["All"] + list(unique_project_roles) + list(unique_qc_teams) + list(unique_companies)
selected_filter = st.sidebar.selectbox("Select a filter:", filter_options)

# Create a button to execute the filter
if st.sidebar.button("Apply Filter"):
    if selected_filter != "All":
        table.dataframe(df[(df['Project Role'] == selected_filter) | (df['QC Team'] == selected_filter) | (df['Company'] == selected_filter)])
    else:
        table.dataframe(df)
