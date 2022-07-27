import streamlit as st
from gsheetsdb import connect
# Create a connection object.
conn = connect()
# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
st.write("Hello")
sheet_url = st.secrets["public_gsheets_url"]
rows = conn.execute(query, headers=1)
st.write(sheet_url)
