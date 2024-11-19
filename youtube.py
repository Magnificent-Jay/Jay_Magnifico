import streamlit as st
import os
from pytube import Playlist, Youtube

def display_res(yt):
    """Display available resolutions for a given YouTube video."""
    print("\nAvailable resolutions:")
    streams = yt.streams.filter(progressive=True, file_extension="mp4")

    resolutions = []
    for i, stream in enumerate(streams):
        print(f"{i + 1}. {stream.resolution}")
        resolutions.append(stream)

    # Return list of available streams
    return resolutions







# Set the title of the web app
st.title("Youtube video downloader")

st.write("Enter the url of the youtube video: ")

# Get text input from the user
user_input = st.text_input("")
enter = st.button("Convert")

if enter:
    if user_input:
        st.write(f"You entered: {user_input}")
    else:
        st.write("No input provided.")


