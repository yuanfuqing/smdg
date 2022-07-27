import streamlit as st
from gsheetsdb import connect
# Create a connection object.
conn = connect()
public_gsheets_url = "https://docs.google.com/spreadsheets/d/1pCrJ9O3T6le6ptl-xUbbdGLhJ_J3SK6zgldJ5MJw6pA/edit?usp=sharing"
# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(ttl=600)
def run_query(query):
    rows = conn.execute(query, headers=1)
    rows = rows.fetchall()
    return rows
st.write("Hello")
sheet_url = st.secrets["public_gsheets_url"]
rows = run_query(f'SELECT * FROM "{sheet_url}"')
