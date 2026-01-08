import streamlit as st
st.title("Hi i am stupid")
# Auto-detect environment and connect
try:
    from snowflake.snowpark.context import get_active_session
    session = get_active_session()
except:
    from snowflake.snowpark import Session
    session = Session.builder.configs(st.secrets["connections"]["snowflake"]).create()


# Query Snowflake version
version = session.sql("SELECT CURRENT_VERSION()").collect()[0][0]