import streamlit as st

# Set the title of the web app
st.title("Youtube video downloader")

st.write("Enter the url of the youtube video: ")

# Get text input from the user
user_input = text_input("")
enter = col2.button("Convert")

if enter:
    if user_input:
        st.write(f"You entered: {user_input}")
    else:
        st.write("No input provided.")


