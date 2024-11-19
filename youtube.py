import streamlit as st

# Set the title of the web app
st.title("Youtube video downloader")

st.write("Enter the url of the youtube video: ")

# Set the columns of the text widget
col1, col2 = st.columns([3, 1])

# Get text input from the user
user_input = col1.text_input("")
oi = col2.write("")
enter = col2.button("Convert")

if enter:
    if user_input:
        st.write(f"You entered: {user_input}")
    else:
        st.write("No input provided.")


