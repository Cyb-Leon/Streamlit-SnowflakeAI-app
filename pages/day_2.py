import streamlit as st
from snowflake.snowpark.functions import ai_complete
import json

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

# Model and prompt
model = "claude-3-5-sonnet"
prompt = st.text_input("Enter your prompt:")

# Run LLM inference
if st.button("Generate Response"):
    df = session.range(1).select(
        ai_complete(model=model, prompt=prompt).alias("response")
    )
    
    # Get and display response
    response_raw = df.collect()[0][0]
    response = json.loads(response_raw)
    st.write(response)

# Footer
st.divider()
st.caption("Day 2: Hello, Cortex! | 30 Days of AI")