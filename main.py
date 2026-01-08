import streamlit as st
st.text("The #30daysofAI in SiS (In Streamlit in Snowflake)")
st.title("#30daysofAI in SiS (In Streamlit in Snowflake)")
st.subheader("The coding fish - A lof of IT Stuff")

col1, col2,col3 = st.columns(3)
col1.write("Beingnner levels")

with col1:
    st.badge("Mortal", color="green")

col2.write("Intermedate levels")

with col2:
    st.badge("Hero", color="yellow")

col3.write("Advanced levels")
with col3:
    st.badge("Spartan", color="red")
