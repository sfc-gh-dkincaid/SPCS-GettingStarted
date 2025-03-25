import streamlit as st
from snowflake.snowpark import Session
from snowflake.snowpark import functions as f
import spcs_helpers
import datetime
import json
import os

# Make connection to Snowflake and cache it
@st.cache_resource
def connect_to_snowflake():
    return spcs_helpers.session()

session = connect_to_snowflake()

#Fetch data from Snowflake
@st.cache_data
def users(_sess: Session):
    return _sess.table('SPCS_PLAYGROUND.PUBLIC.SERVICE_USERS').to_pandas()

service = os.environ["service_name"]

# Write directly to the app - purely cosmetic headers
st.title("My Example Streamlit App")
st.write("Running all within Snowpark Container Services")
st.write(f"My Env Variable={service}")

st.markdown('------') 

df = users(session)
st.dataframe(df)