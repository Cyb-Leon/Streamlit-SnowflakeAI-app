import streamlit as st
st.text("The #30daysofAI SiS (In Streamlit in Snowflake)")
st.title("#30daysofAI in SiS (In Streamlit in Snowflake)")
st.subheader("The coding fish - A lof of IT Stuff")

col1, col2,col3 = st.columns(3)
col1.write("Beingnner levels")

with col1:
    st.badge("Mortal", color="green")
    st.page_link("pages/1Day:1- Connect To Snowflake.py")
    st.page_link("pages/2Day:2- Run LLM (Cortex AI ) In Snowflake.py")
    st.page_link("pages/6Day:6- Status UI for Long-Running Task.py")
    st.page_link("pages/14Day:14- Adding Avatars and Error Handling.py")
    st.page_link("pages/13Day:13- Adding a System Prompt.py")

col2.write("Intermedate levels")

with col2:
    st.badge("Hero", color="yellow")
    st.page_link("pages/3Day:3- Write streams.py")
    st.page_link("pages/4Day:4- Caching the App.py")
    st.page_link("pages/5Day:5- Post Generator App.py")
    st.page_link("pages/8Day:8- Meet the Chat Elements.py")
col3.write("Advanced levels")
with col3:
    st.badge("Spartan", color="red")
    st.page_link("pages/7Day:7- Theming and Layout.py")
    st.page_link("pages/10Day:10- StreamlitxSnowflake Chatbot.py")
    st.page_link("pages/9Day:9- Understanding Session State.py")
    st.page_link("pages/11Day:11- Displaying Chat History.py")
    st.page_link("pages/12Day:12- Streaming Responses.py")


st.caption("#30DayOfAI StreamLit x Snowflake.")
