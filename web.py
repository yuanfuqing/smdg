import streamlit as st
from gsheetsdb import connect
# Create a connection object.
conn = connect()
# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(ttl=600)
def run_query(query):
    rows = conn.execute(query, headers=1)
    rows = rows.fetchall()
    return rows
st.write("Hello")
sheet_url = st.secrets["public_gsheets_url"]
rows = run_query(sheet_url)
st.write(sheet_url)
