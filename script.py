import tkinter as tk
from tkinter import *
from gtts import gTTS
from moviepy.editor import *
# Create a Tkinter window
root = tk.Tk()



root.title('Speaker BOT')
# Designate Height and Width of our app
app_width = 450
app_height = 220
# The Height and Width of our pc screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2 ) - (app_height / 2)
root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
root.resizable(False,False)

FirstBackGroung = Label(root,width="550",height="285",bg="#183444")
FirstBackGroung.place(x=0,y=0)

# Create an entry widget
frame = Frame(root, bd=5, bg="#EEECCC")#for text output
frame.pack(ipadx=5, ipady=5, padx=5, pady=5)
# entry = tk.Entry(frame,width=82,font=("Arial", 13))

entry = tk.Text(frame, height=5, width=82, font=("Arial", 13))

# Create a scrollbar and attach it to the Text widget
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
entry.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=entry.yview)

entry.pack(side=TOP)

# Define a function to read the text aloud and create an MP4 file
def create_video2():
    text = entry.get()
    filename = 'output.mp3'
    
    # Generate the audio file
    tts = gTTS(text=text, lang='fr')
    tts.save(filename)

    # Load the image
    img_path = 'image.jpg'
    img = ImageClip(img_path)

    # Load the audio
    audio_path = 'output.mp3'
    audio = AudioFileClip(audio_path)

    # Set the duration of the video to be the same as the audio
    duration = audio.duration

    # Combine the image and audio into a video
    video = img.set_audio(audio).set_duration(duration)

    # Save the video to disk
    video_path = 'video.mp4'
    video.write_videofile(video_path, fps=24)

# Create a button to create the video
button = tk.Button(root, text="Créer la vidéo", command=create_video2)

# Pack the widgets into the GUI
entry.pack()
button.pack()

root.mainloop()