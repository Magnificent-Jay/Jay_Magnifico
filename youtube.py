import streamlit as st

# Set the title of the web app
st.title("Youtube video downloader")

# Set the columns of the widgets
col1, col2 = st.columns([3, 1])


# Get text input from the user
user_input = col1.text_input("Enter the url of the youtube video:")
enter = col2.button("Convert")

if enter:
    if user_input:
        st.write(f"You entered: {user_input}")
    else:
        st.write("No input provided.")


