import os
from pytube import YouTube
from moviepy.editor import *
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# Enter the YouTube video URL
url = 'https://www.youtube.com/watch?v=GCgvpwLNvtY'

# Download the video
yt = YouTube(url)
stream = yt.streams.get_highest_resolution()
stream.download()

# Extract the audio
video = VideoFileClip('filename.mp4')
audio = video.audio
audio.write_audiofile('filename.mp3')

# Delete the downloaded video file
os.remove('filename.mp4')
