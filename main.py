import streamlit as st


st.title("My First WebApp")
st.divider()

col1, col2 = st.columns(2)
with col1:
    st.button("Left Button")
with col2:
    st.button("Right Button")
