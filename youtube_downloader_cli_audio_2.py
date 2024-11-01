"""
    Name: youtube_downloader_audio_cli_2.py
    Author: William A Loring
    Created: 10/31/2024
    Purpose: Use Python pytubefix library to download audion from YouTube
"""

# pip install pytubefix
from pytubefix import YouTube
from pytubefix.cli import on_progress

print(" +----------------------------------+")
print(" |      YouTube Audio Downloader    |")
print(" +----------------------------------+")

while True:
    # ----------------------- URL ------------------------------------------#
    # Get URL from user
    url = input(" Video URL: \n >> ")
    you_tube = YouTube(url, on_progress_callback=on_progress)

    # ----------------------- EXTRACT AUDIO --------------------------------#
    # Extract the audio stream
    video = you_tube.streams.get_audio_only()

    # Destination to save file
    destination = "./music"

    # Download the file to the file system
    out_file = video.download(mp3=True, output_path=destination)

    print(f" {you_tube.title}  has been successfully downloaded.")

    menuchoice = input("Download another? \n(N to quit, Enter to continue)")
    if menuchoice.upper() == "N":
        break
