import os
import tkinter as tk
from tkinter import filedialog
from pygame import mixer

# Initialize the mixer
mixer.init()

# Create the main application window
root = tk.Tk()
root.title("Music Player")
root.geometry("400x400")

# Define functions for music controls
def play_music():
    mixer.music.load(track)
    mixer.music.play()

def pause_music():
    mixer.music.pause()

def unpause_music():
    mixer.music.unpause()

def stop_music():
    mixer.music.stop()

def load_music():
    global track
    track = filedialog.askopenfilename()
    track_name.set(os.path.basename(track))

# Create GUI elements
track_name = tk.StringVar()
track_label = tk.Label(root, textvariable=track_name)
track_label.pack(pady=10)

load_button = tk.Button(root, text="Load", command=load_music)
load_button.pack(pady=10)

play_button = tk.Button(root, text="Play", command=play_music)
play_button.pack(pady=10)

pause_button = tk.Button(root, text="Pause", command=pause_music)
pause_button.pack(pady=10)

unpause_button = tk.Button(root, text="Unpause", command=unpause_music)
unpause_button.pack(pady=10)

stop_button = tk.Button(root, text="Stop", command=stop_music)
stop_button.pack(pady=10)

# Run the application
root.mainloop()
