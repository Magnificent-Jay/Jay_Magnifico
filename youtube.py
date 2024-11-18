import streamlit as st

# Set the title of the web app
st.title("Youtube video downloader")

# Get text input from the user
user_input = st.text_input("Enter the url of the youtube video:")

# Display the input back to the user
if user_input:
    st.write(f"You entered: {user_input}")
