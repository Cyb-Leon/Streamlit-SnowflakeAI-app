import streamlit as st

st.set_page_config(layout="wide")
st.text("The #30daysofAI SiS (In Streamlit in Snowflake)")
st.title("#30daysofAI in SiS (In Streamlit in Snowflake)")
st.subheader("The coding fish - A lof of IT Stuff")

col1, col2,col3 = st.columns(3)
col1.write("Beingnner levels")

with col1:
    st.badge("Mortal", color="green")
    st.page_link("pages/1Day 1: Connect To Snowflake.py")
    st.page_link("pages/2Day 2: Run LLM (Cortex AI ) In Snowflake.py")
    st.page_link("pages/6Day 6: Status UI for Long-Running Task.py")
    st.page_link("pages/14Day 14: Adding Avatars and Error Handling.py")
    st.page_link("pages/13Day 13: Adding a System Prompt.py")
    st.page_link("pages/11Day 11: Displaying Chat History.py")

col2.write("Intermedate levels")

with col2:
    st.badge("Hero", color="yellow")
    st.page_link("pages/3Day 3: Write streams.py")
    st.page_link("pages/4Day 4: Caching the App.py")
    st.page_link("pages/5Day 5: Post Generator App.py")
    st.page_link("pages/8Day 8: Meet the Chat Elements.py")
    st.page_link("pages/15Day 15: Model Comparison Arena.py")
    st.page_link("pages/21Day 21: RAG with Cortex Search.py")
    st.page_link("pages/22Day 22: Chat with Your Documents.py")
    st.page_link("pages/24Day 24: Working with Images (Multimodality).py")
    st.page_link("pages/26Day 26: Introduction to Cortex Agents.py")

col3.write("Advanced levels")
with col3:
    st.badge("Spartan", color="red")
    st.page_link("pages/7Day 7: Theming and Layout.py")
    st.page_link("pages/10Day 10: StreamlitxSnowflake Chatbot.py")
    st.page_link("pages/9Day 9: Understanding Session State.py")
    st.page_link("pages/12Day 12: Streaming Responses.py")
    st.page_link("pages/16Day 16: Batch Document Text Extractor for RAG.py")
    st.page_link("pages/17Day 17: Loading and Transforming Customer Reviews for RAG.py")
    st.page_link("pages/18Day 18: Generating Embeddings for Customer Reviews.py")
    st.page_link("pages/19Day 19: Creating Cortex Search for Customer Reviews.py")
    st.page_link("pages/20Day 20: Querying Cortex Search.py")
    st.page_link("pages/23Day 23: LLM Evaluation & AI Observability.py")
    st.page_link("pages/25Day 25: Voice Interface.py")


st.caption("#30DayOfAI StreamLit x Snowflake.")
