"""
    Name: youtube_downloader_audio_cli_1.py
    Author: William A Loring
    Created: 010/31/2024
    Purpose: Use Python pytubefix library to download audion from YouTube
"""

# pip install pytubefox
from pytubefix import YouTube
from pytubefix.cli import on_progress


print(" +----------------------------------+")
print(" |      YouTube Audio Downloader    |")
print(" +----------------------------------+")
# ----------------------- URL ---------------------------------------------#
# Get URL from user
url = input(" Video URL: \n >> ")
you_tube = YouTube(url, on_progress_callback=on_progress)

# ----------------------- EXTRACT AUDIO -----------------------------------#
# Extract the audio stream
video = you_tube.streams.get_audio_only()

# Destination to save file
destination = "./music"

# Download the file to the file system
out_file = video.download(mp3=True, output_path=destination)

print(f" {you_tube.title}  has been successfully downloaded.")
