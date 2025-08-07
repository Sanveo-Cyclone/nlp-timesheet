# import requests
# import streamlit as st

# st.title("NLP Timesheet Q&A")

# user_question = st.text_input("Ask your timesheet question:")

# if user_question:
#     payload = {
#         "model": "gemma3",
#         "prompt": user_question
#     }

#     response = requests.post("http://localhost:11434/api/generate", json=payload)
#     result = response.json()["response"]

#     st.write(result)


import streamlit as st
import pandas as pd
 
# Load the CSV
# df = pd.read_csv('timesheet.csv')

df = pd.read_csv('timesheet.csv', encoding='ISO-8859-1')

 
# Preview the data
st.title("Timesheet Dashboard")
st.write("Here's a quick look at the raw timesheet data:")
st.dataframe(df)
 
# Example graph: Total hours by employee
if 'Employee' in df.columns and 'Hours' in df.columns:
    hours_by_emp = df.groupby('Employee')['Hours'].sum().reset_index()
    st.bar_chart(hours_by_emp.set_index('Employee'))
else:
    st.warning("Please make sure your CSV has 'Employee' and 'Hours' columns.")