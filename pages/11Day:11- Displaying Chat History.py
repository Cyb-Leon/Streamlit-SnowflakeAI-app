import streamlit as st
import json
from snowflake.snowpark.fucntions import ai_complete


st.title("I am now a genius on Streamlit")

#we connect to Snowflake with a session
try:
    # Works in Streamlit in Snowflake
    from snowflake.snowpark.context import get_active_session
    session = get_active_session()
except:
    # Works locally and on Streamlit Community Cloud
    from snowflake.snowpark import Session
    session = Session.builder.configs(st.secrets["connections"]["snowflake"]).