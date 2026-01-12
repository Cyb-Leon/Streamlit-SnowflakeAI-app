import streamlit as st
st.text("The #30daysofAI in SiS (In Streamlit in Snowflake)")
st.title("#30daysofAI in SiS (In Streamlit in Snowflake)")
st.subheader("The coding fish - A lof of IT Stuff")

col1, col2,col3 = st.columns(3)
col1.write("Beingnner levels")

with col1:
    st.badge("Mortal", color="green")
    st.text("Day:1- Connect To Snowflake")
    st.text("Day:2- Run LLM (Cortex AI ) In Snowflake ")
    st.text("Day:6- Status UI for Long-Running Task")

col2.write("Intermedate levels")

with col2:
    st.badge("Hero", color="yellow")
    st.text("Day:3- Write streams")
    st.text("Day:4- Caching the App")
    st.text("Day:5- Post Generator App")
    st.text("Day:8- Meet the Chat Elements")
col3.write("Advanced levels")
with col3:
    st.badge("Spartan", color="red")
    st.text("Day:7- Theming and Layout")
    st.text("Day:10- StreamlitxSnowflake Chatbot")
    st.text("Day:9- Understanding Session State")
    st.text("Day:11- Displaying Chat History")

Day 11: #30DayOfAI Displaying Chat History.



If you are or aspire to be a data scientist/analyst, I'd highly advise you to take on this challenge - the tools are available for you.



head to Snowflake Developers or Streamlit to get more details about this. Get fontend up and running, Snowflake platform setup for data to play with. 