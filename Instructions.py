import tkinter as tk
from tkinter import filedialog, font as tkFont, PhotoImage
import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Create Instructions Window
instructions_window = tk.Tk()
instructions_window.title("Instructions")
instructions_window.geometry("700x500")
instructions_window.configure(bg="black")  # Retro terminal background

# Retro pixel-style font
instr_font = tkFont.Font(family="Courier", size=16, weight="bold")

# Instructions text (formatted for better readability)
instructions_text = """
         ███╗   ██╗██╗   ██╗███╗   ███╗██████╗ ██╗   ██╗███████╗
         ████╗  ██║██║   ██║████╗ ████║██╔══██╗██║   ██║██╔════╝
         ██╔██╗ ██║██║   ██║██╔████╔██║██████╔╝██║   ██║███████╗
         ██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██╗██║   ██║╚════██║
         ██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║╚██████╔╝███████║
         ╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝
             
           Welcome to NumRush!
      Solve math problems and test your skills!  

      ▶ Normal Mode: Solve a fixed number of problems.  
      ▶ Time-Attack: Solve as many as possible before time runs out.  
      ▶ Earn points and try to beat the high score!

"""

# Create a frame for text
frame = tk.Frame(instructions_window, bg="black", bd=5)
frame.place(relx=0.5, rely=0.5, anchor="center")

# Display instructions with retro color style
instr_label = tk.Label(frame, text=instructions_text, font=instr_font,
                       fg="#39FF14", bg="black", justify="center")
instr_label.pack(pady=10)

# Exit button (Retro Red)
exit_button = tk.Button(frame, text="▶ Back to Menu", font=instr_font,
                        bg="#DC143C", fg="white", activebackground="#8B0000",
                        activeforeground="white", command=instructions_window.destroy)
exit_button.pack(pady=10)

# Run the window
instructions_window.mainloop()


