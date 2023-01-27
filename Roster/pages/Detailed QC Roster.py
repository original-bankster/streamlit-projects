import streamlit as st
import pandas as pd

# Create a title page
st.title("Expansive QAQC Roster")

# Add some content to the page
st.write("You can also use the 'Name' search feature to improve your results")

# Read the excel file
file_path = "C:/Users/roman/OneDrive/Desktop/HORNE/Production Supervisor/Rosters/QAQC Roster Details_1.18.23.xlsx"
df = pd.read_excel(file_path, sheet_name='CARRL Expansive Roster')

# Show the data in a table
table = st.dataframe(df)

# Create a sidebar
st.sidebar.title("Roster Filters")

# Get the unique options from the dataframe
unique_project_roles = df['Role'].unique()
unique_qc_teams = df['Team'].unique()
unique_companies = df['Company'].unique()

# Create a drop-down box in the sidebar to select the column to filter by
filter_options = ["All"] + list(unique_project_roles) + list(unique_qc_teams) + list(unique_companies)
selected_filter = st.sidebar.selectbox("Select a filter:", filter_options)

# Create a button to execute the filter
if st.sidebar.button("Apply Filter"):
    if selected_filter != "All":
        table.dataframe(df[(df['Role'] == selected_filter) | (df['Team'] == selected_filter) | (df['Company'] == selected_filter)])
    else:
        table.dataframe(df)

# Create a search toolbar
name_search = st.text_input("Enter a name:")

# Create a button to execute the search
if st.button("Search"):
    if name_search:
        filtered_df = df[df['Name'].str.contains(name_search, case=False, na=False)]
        table.dataframe(filtered_df)
    else:
        table.dataframe(df)
