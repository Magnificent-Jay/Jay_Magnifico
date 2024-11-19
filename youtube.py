import os
import streamlit as st
from yt_dlp import YoutubeDL

import subprocess

try:
    import yt_dlp
except ModuleNotFoundError:
    print("yt-dlp is not installed. Installing now...")
    subprocess.check_call(["pip", "install", "yt-dlp"])
finally:
    import yt_dlp
    print("yt-dlp is successfully imported!")


def get_resolutions(video_url):
    """Retrieve available resolutions for a given YouTube video."""
    ydl_opts = {'quiet': True}
    with YoutubeDL(ydl_opts) as ydl:
        video_info = ydl.extract_info(video_url, download=False)
        formats = video_info['formats']
        resolutions = {
            f"{f['height']}p": f['format_id']
            for f in formats if f['vcodec'] != 'none' and f['acodec'] != 'none'
        }
        return resolutions, video_info.get('title', 'Unknown Title')

def download_video(video_url, format_id):
    """Download a single video using yt-dlp."""
    download_path = os.path.join(os.getcwd(), "Downloads")
    os.makedirs(download_path, exist_ok=True)  # Ensure the Downloads folder exists

    ydl_opts = {
        'format': format_id,
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
        'quiet': False,
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])
    return download_path

# Streamlit App
st.title("YouTube Downloader")

# Input for YouTube URL
video_url = st.text_input("Enter YouTube video or playlist URL:")

if video_url:
    if st.button("Get Resolutions"):
        try:
            resolutions, title = get_resolutions(video_url)
            st.session_state["resolutions"] = resolutions
            st.session_state["title"] = title
            st.success(f"Available resolutions fetched for: {title}")
        except Exception as e:
            st.error(f"Error fetching resolutions: {e}")

# Display Resolutions Dropdown
if "resolutions" in st.session_state:
    resolution = st.selectbox(
        "Select a resolution:", 
        options=list(st.session_state["resolutions"].keys()),
    )

    if st.button("Download"):
        try:
            format_id = st.session_state["resolutions"][resolution]
            download_path = download_video(video_url, format_id)
            st.success(f"Downloaded '{st.session_state['title']}' to {download_path}")
        except Exception as e:
            st.error(f"Error downloading video: {e}")
