import streamlit as st
import pandas as pd

# Load the CSV
df = pd.read_csv('timesheet.csv', encoding='ISO-8859-1')

# Convert daily_log from 'hh:mm' format to 'hh:mm:ss'
def convert_to_hms(value):
    try:
        # Ensure that the value is a string (if it's a float, convert to string)
        value = str(value)
        
        # Check if the value contains a colon, which indicates a time format
        if ':' in value:
            return f"{value}:00"  # Convert 'hh:mm' to 'hh:mm:ss'
        return value  # Return as is if no colon
    except ValueError:
        return value  # If conversion fails, return the original value

# Apply the conversion to daily_log
df['daily_log'] = df['daily_log'].apply(convert_to_hms)

# Ensure 'user' and 'daily_log' columns exist before processing
if 'user' in df.columns and 'daily_log' in df.columns:
    # Convert to timedelta (hours in total)
    df['daily_log'] = pd.to_timedelta(df['daily_log'], errors='coerce').dt.total_seconds() / 3600

    # Group by user and sum the hours
    hours_by_user = df.groupby('user')['daily_log'].sum().reset_index()

    # Display the bar chart for total hours by user
    st.title("Timesheet Dashboard")
    st.subheader("Total Hours by Employee")
    st.bar_chart(data=hours_by_user, x='user', y='daily_log')

# Total Hours Logged Per Day (Line chart)
df['date'] = pd.to_datetime(df['date'])  # Convert date to datetime

st.subheader("Total Hours Logged Per Day")
hours_by_date = df.groupby('date')['daily_log'].sum().reset_index()
st.line_chart(data=hours_by_date, x='date', y='daily_log')

# Hours Spent per Task Type (Bar chart)
st.subheader("Hours Spent per Task Type")
task_hours = df.groupby('task_type')['daily_log'].sum().sort_values(ascending=False).reset_index()
st.bar_chart(data=task_hours, x='task_type', y='daily_log')

# Sidebar Filters
st.sidebar.header("Filters")
selected_user = st.sidebar.selectbox("Select a User", options=df['user'].unique())

# Filter the dataframe by the selected user
filtered_df = df[df['user'] == selected_user]

# Display filtered data for the selected user
st.write(f"Entries for {selected_user}:")
st.dataframe(filtered_df)
