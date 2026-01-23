import streamlit as st
st.text("The #30daysofAI SiS (In Streamlit in Snowflake)")
st.title("#30daysofAI in SiS (In Streamlit in Snowflake)")
st.subheader("The coding fish - A lof of IT Stuff")

col1, col2,col3 = st.columns(3)
col1.write("Beingnner levels")

with col1:
    st.badge("Mortal", color="green")
    st.page_link("pages/Day:1- Connect To Snowflake.py")
    st.page_link("pages/Day:2- Run LLM (Cortex AI ) In Snowflake.py")
    st.page_link("pages/Day:6- Status UI for Long-Running Task.py")
    st.page_link("pages/Day:14- Adding Avatars and Error Handling.py")
    st.page_link("pages/Day:13- Adding a System Prompt.py")
    st.page_link("pages/Day:11- Displaying Chat History.py")

col2.write("Intermedate levels")

with col2:
    st.badge("Hero", color="yellow")
    st.page_link("pages/Day:3- Write streams.py")
    st.page_link("pages/Day:4- Caching the App.py")
    st.page_link("pages/Day:5- Post Generator App.py")
    st.page_link("pages/Day:8- Meet the Chat Elements.py")
    st.page_link("pages/Day:15- Model Comparison Arena.py")
    st.page_link("pages/Day:21- RAG with Cortex Search.py")
    st.page_link("pages/Day:22- Chat with Your Documents.py")

col3.write("Advanced levels")
with col3:
    st.badge("Spartan", color="red")
    st.page_link("pages/Day:7- Theming and Layout.py")
    st.page_link("pages/Day:10- StreamlitxSnowflake Chatbot.py")
    st.page_link("pages/Day:9- Understanding Session State.py")
    st.page_link("pages/Day:12- Streaming Responses.py")
    st.page_link("pages/Day:16- Batch Document Text Extractor for RAG.py")
    st.page_link("pages/Day:17- Loading and Transforming Customer Reviews for RAG.py")
    st.page_link("pages/Day:18 - Generating Embeddings for Customer Reviews.py")
    st.page_link("pages/Day:19- Creating Cortex Search for Customer Reviews.py")
    st.page_link("pages/Day:20- Querying Cortex Search.py")


st.caption("#30DayOfAI StreamLit x Snowflake.")
