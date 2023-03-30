import os
import time
import numpy as np
import tkinter as tk
from tkinter import *
from PIL import Image
from gtts import gTTS
from moviepy.editor import *
from tkinter import filedialog
from moviepy.video.io.VideoFileClip import VideoFileClip
from functionnalities import copy,paste,app_width,app_height,cmpt,entries
from functionnalities import on_enter,on_leave,on_enter2,on_leave2,cmpt,entries

def on_enter(e):
    video_button.config(cursor="hand2")
def on_leave(e):
    video_button.config(cursor="")
def on_enter2(e):
    script_button.config(cursor="hand2")
def on_leave2(e):
    script_button.config(cursor="")
def add__widget():
    global cmpt
    global entries
    if (cmpt!=8): # 7 is the max number of widgets in the window
        entry = tk.Text(frame, height=2, width=50, font=("Arial", 13),name=str(cmpt), bg="#FFC300")
        entries.append(entry)
        cmpt = cmpt + 1
        entry.pack(ipadx=5, ipady=5, padx=5, pady=5)

# Function to read the text and create an MP4 file
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

# Create a Tkinter window
root = tk.Tk()
root.title('Video Maker BOT')
root.iconbitmap('./logo/icon.ico')
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
script_button = Button(button_frame, text="Ajouter une Parole", command=add__widget , bg="#FF5733", fg="#F2F2F2")
script_button.pack(side=LEFT, padx=5)
button_frame.pack(pady=10)

# Create an entry widget
frame = Frame(root, bd=5, bg="#FFC300")#for text output
frame.pack(ipadx=5, ipady=5, padx=5, pady=5)
entry = tk.Text(frame, height=2, width=50, font=("Arial", 13),name=str(cmpt), bg="#FFC300")
entries.append(entry)
cmpt = cmpt + 1
# Create a scrollbar and attach it to the Text widget
entry.pack(ipadx=5, ipady=5, padx=5, pady=5)

video_button.bind("<Enter>", on_enter)
video_button.bind("<Leave>", on_leave)
script_button.bind("<Enter>", on_enter2)
script_button.bind("<Leave>", on_leave2)
entry.bind("<Control-c>", copy)
entry.bind("<Control-v>", paste)
root.mainloop()