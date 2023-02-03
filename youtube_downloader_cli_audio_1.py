"""
    Name: youtube_downloader_audio_cli_1.py
    Author: William A Loring
    Created: 02/02/2023
    Purpose: Use Python pytube library to download audion from YouTube
"""

# pip install pytube
from pytube import YouTube
import os

print(" +----------------------------------+")
print(" |      YouTube Audio Downloader    |")
print(" +----------------------------------+")
# ----------------------- URL ---------------------------------------------#
# Get URL from user
url = input(" Video URL: \n >> ")
you_tube = YouTube(url)
  
# ----------------------- EXTRACT AUDIO -----------------------------------#
# Extract the audio stream
video = you_tube.streams.filter(only_audio=True).first()

# Destination to save file
destination = "./music"

# Download the file to memory
out_file = video.download(output_path=destination)

# Save the file to the file system
file_name, file_extension = os.path.splitext(out_file)
new_file = file_name + '.mp3'

os.rename(out_file, new_file)

print(f" {you_tube.title}  has been successfully downloaded.")
