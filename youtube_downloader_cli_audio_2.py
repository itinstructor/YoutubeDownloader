"""
    Name: youtube_downloader_audio_cli_2.py
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

while True:
    # ----------------------- URL ------------------------------------------#
    # Get URL from user
    url = input(" Video URL: \n >> ")
    you_tube = YouTube(url)

    # ----------------------- EXTRACT AUDIO --------------------------------#
    # Extract the audio stream
    video = you_tube.streams.filter(only_audio=True).first()

    # Destination to save file
    destination = "./music"

    # Download the file to memory
    # The audio file is in mp4 format
    out_file = video.download(output_path=destination)

    # Save the file to the file system
    # Split the file into to parts, the filename and the extension
    file_name, file_extension = os.path.splitext(out_file)
    # Concatenate the filename with an .mp3 file extension
    new_file = file_name + '.mp3'

    # Rename the mp4 file to an mp3 file extension
    os.rename(out_file, new_file)

    print(f" {you_tube.title}  has been successfully downloaded.")

    menuchoice = input("Download another? \n(N to quit, Enter to continue)")
    if menuchoice.upper() == "N":
        break
