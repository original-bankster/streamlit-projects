import streamlit as st
import pandas as pd

# Create a title page
st.title("QAQC Workforce Analytics")

# Add some content to the page
st.write("Human Capital Analytics to show and update QAQC workforce readiness")

# Read the excel file
file_path = "C:/Users/roman/OneDrive/Desktop/HORNE/Production Supervisor/Rosters/QAQC Roster Details_1.18.23.xlsx"
df = pd.read_excel(file_path, sheet_name='CARRL QC Count')

# Select the columns for the first table
first_table = df[['Lead', 'Team #', 'Total Team Members']].dropna()

# Show the first table
st.dataframe(first_table)

# Read the sheet 'CARRL QC Count Totals' from the same excel file
df2 = pd.read_excel(file_path, sheet_name='CARRL QC Count Totals')

# Select the columns for the second table
second_table = df2[['Totals', 'Figures',]].dropna()

# Show the second table
st.dataframe(second_table)



