import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image
from moviepy.video.io.VideoFileClip import VideoFileClip
import numpy as np
from gtts import gTTS
from moviepy.editor import *
import os
import time

# global variables
cmpt = 1
entries = []

def add__widget():
    global cmpt
    global entries
    entry = tk.Text(frame, height=2, width=50, font=("Arial", 13),name=str(cmpt), bg="#FFC300")
    entries.append(entry)
    cmpt = cmpt + 1
    entry.pack(ipadx=5, ipady=5, padx=5, pady=5)

# Define a function to read the text aloud and create an MP4 file
def create_video2():
    global cmpt
    global entries
    clips = []
    for entry in entries:
        for j in range(1,cmpt):
            if (entry.winfo_name() == str(j)):
                text = entry.get("1.0", tk.END)
                filename = 'audio'+str(j)+'.mp3'
                # Generate the audio file
                tts = gTTS(text=text, lang='fr')
                tts.save(filename)
    # Load the image
    for j in range(1,cmpt):
        img_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
        image = Image.open(img_path)
        resized_image = image.resize((640, 480))
        img_array = np.array(resized_image)
        img = ImageClip(img_array)
        # Load the audio
        audio_path ='audio'+str(j)+'.mp3'
        audio = AudioFileClip(audio_path)
        # Set the duration of the video to be the same as the audio
        duration = audio.duration
        # Combine the image and audio into a video
        video = img.set_audio(audio).set_duration(duration)
        # Save the video to disk
        video_path = 'video'+str(j)+'.mp4'
        video.write_videofile(video_path, fps=24)
        clip = VideoFileClip(video_path)
        clips.append(clip)
    final_clip = concatenate_videoclips(clips)
    final_clip.write_videofile("./outputVideos/video.mp4")
    # a loop to delete cache audios
    for j in range(1,cmpt):
        time.sleep(2)
        filename = 'audio'+str(j)+'.mp3'
        os.remove(filename)
    # a loop to delete cache videos
    for j in range(1,cmpt):
        time.sleep(2)
        video_path = 'video'+str(j)+'.mp4'
        os.remove(video_path)

def copy(event):
    event.widget.event_generate("<<Copy>>")

def paste(event):
    event.widget.event_generate("<<Paste>>")

# Create a Tkinter window
root = tk.Tk()
root.title('Video Maker BOT')
root.iconbitmap('./logo/icon.ico')
# Designate Height and Width of our app
app_width = 550
app_height = 520

# The Height and Width of our pc screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2 ) - (app_height / 2)
root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
root.resizable(False,False)
FirstBackGroung = Label(root,width="550",height="285",bg="#003DA5")
FirstBackGroung.place(x=0,y=0)

button_frame = Frame(root,bg="#003DA5")
video_button = Button(button_frame, text="Créer la vidéo", command=create_video2 , bg="#FF5733", fg="#F2F2F2")
video_button.pack(side=LEFT, padx=5)
script_button = Button(button_frame, text="Ajouter Script", command=add__widget , bg="#FF5733", fg="#F2F2F2")
script_button.pack(side=LEFT, padx=5)
button_frame.pack(pady=10)

# Create an entry widget
frame = Frame(root, bd=5, bg="#FFC300")#for text output
frame.pack(ipadx=5, ipady=5, padx=5, pady=5)
entry = tk.Text(frame, height=2, width=50, font=("Arial", 13),name=str(cmpt), bg="#FFC300")
entries.append(entry)

cmpt = cmpt + 1
# Create a scrollbar and attach it to the Text widget
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
scrollbar.config(command=entry.yview)
entry.pack(ipadx=5, ipady=5, padx=5, pady=5)

entry.bind("<Control-c>", copy)
entry.bind("<Control-v>", paste)
root.mainloop()