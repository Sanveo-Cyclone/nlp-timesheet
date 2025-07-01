import streamlit as st

st.title("NLP-Powered Timesheet Insights")

question = st.text_input("Ask a question about the timesheet data:")

if question:
    st.write("You asked:", question)