import time
import json
import random
import tkinter as tk
from tkinter import messagebox, PhotoImage, font as tkFont
import pygame
import subprocess
import os
import sys

# Initialize pygame mixer for background music
pygame.mixer.init()
pygame.mixer.music.load("menu_song.mp3")  # Ensure you have a valid music file
pygame.mixer.music.play(-1)

# Initialize Tkinter
root = tk.Tk()
root.title("NumRush")
root.geometry("500x500")
root.configure(bg="#000000")

# Load GIF frames properly
gif_path = r"C:\Users\redic\Desktop\pygame_app\menu_bg.gif"
frames = []
frame_index = 0

# Load GIF frames safely
try:
    while True:
        frame = PhotoImage(file=gif_path, format=f"gif - {len(frames)}")
        frames.append(frame)
except tk.TclError:
    pass  # End of GIF reached

if not frames:
    print("Error: Could not load GIF frames. Check file path or format.")
    root.quit()  # Exit if GIF isn't loading properly

# Function to animate GIF
def update_gif():
    global frame_index
    frame_index = (frame_index + 1) % len(frames)
    bg_label.configure(image=frames[frame_index])
    root.after(100, update_gif)

# Display first frame
bg_label = tk.Label(root, image=frames[0])
bg_label.place(relwidth=1, relheight=1)  # Full screen background
update_gif()  # Start animation

# Create frames
menu_frame = tk.Frame(root, bg="#5A5A5A")
menu_frame.place(relx=0.5, rely=0.5, anchor="center")  # Center menu frame

retro_font = tkFont.Font(family="Courier", size=30, weight="bold")
button_font = tkFont.Font(family="Courier", size=16, weight="bold")

# Title Label
menu_label = tk.Label(menu_frame, text="NUMRUSH", font=retro_font, bg="#5A5A5A", fg="#39FF14")
menu_label.pack(pady=10)

difficulty_var = tk.StringVar(value="easy")
tk.Radiobutton(menu_frame, text="Easy", variable=difficulty_var, value="easy", font=button_font,
               bg="#5A5A5A", fg="#FFD700", selectcolor="#000000").pack()
tk.Radiobutton(menu_frame, text="Medium", variable=difficulty_var, value="medium", font=button_font,
               bg="#5A5A5A", fg="#FFD700", selectcolor="#000000").pack()
tk.Radiobutton(menu_frame, text="Hard", variable=difficulty_var, value="hard", font=button_font,
               bg="#5A5A5A", fg="#FFD700", selectcolor="#000000").pack()

# Center buttons by making them wider and using pack with padx and pady
btn_width = 15

# Function to open external Python files safely
def open_file(file_path):
    if os.path.exists(file_path):  # Check if the file exists
        try:
            subprocess.Popen([sys.executable, file_path])  # Uses the correct Python executable
        except Exception as e:
            messagebox.showerror("Error", f"Could not open file:\n{str(e)}")
    else:
        messagebox.showerror("Error", f"File not found:\n{file_path}")

# Function to open the instructions window (runs instructions.py)
def open_instructions():
    subprocess.Popen([sys.executable, "instructions.py"])

# Buttons
tk.Button(menu_frame, text="START GAME", font=button_font,
          bg="#FF4500", fg="#FFFFFF", width=btn_width, 
          command=lambda: open_file("start_game.py")).pack(pady=5)

tk.Button(menu_frame, text="TIME-ATTACK", font=button_font,
          bg="#1E90FF", fg="#FFFFFF", width=btn_width, 
          command=lambda: open_file("time_attack_game.py")).pack(pady=5)

tk.Button(menu_frame, text="HIGH SCORES", font=button_font,
          bg="#32CD32", fg="#FFFFFF", width=btn_width, 
          command=lambda: open_file("high_scores.py")).pack(pady=5)

tk.Button(menu_frame, text="INSTRUCTIONS", font=button_font,
          bg="#8A2BE2", fg="#FFFFFF", width=btn_width, 
          command=open_instructions).pack(pady=5)  # Calls instructions.py

tk.Button(menu_frame, text="EXIT", font=button_font,
          bg="#DC143C", fg="#FFFFFF", width=btn_width, 
          command=root.quit).pack(pady=5)

root.mainloop()
