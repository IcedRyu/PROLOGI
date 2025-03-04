import tkinter as tk
from tkinter import font as tkFont, PhotoImage
import random
import time
import pygame

# Game parameters
TIME_LIMIT = 30  # 30 seconds to solve as many problems as possible

class MathTimeAttack:
    def __init__(self, parent_window):
        """Initialize the Math Time-Attack window."""
        self.game_window = tk.Toplevel(parent_window)  # Opens in a new window
        self.game_window.title("Math Time Attack")
        self.game_window.geometry("700x500")
        self.game_window.configure(bg="black")

        # Initialize pygame mixer for music
        pygame.mixer.init()

        # Load background image
        try:
            self.bg_image = PhotoImage(file="math_attack_background.png")  # Update with correct path
            bg_label = tk.Label(self.game_window, image=self.bg_image)
            bg_label.place(relwidth=1, relheight=1)  # Full-screen background
            self.game_window.bg_image = self.bg_image  # Prevent garbage collection
        except Exception as e:
            print(f"Warning: Could not load background image: {e}")

        # Load and play background music
        try:
            pygame.mixer.music.load("math_attack_music.mp3")  # Update with correct file path
            pygame.mixer.music.play(-1)
        except Exception as e:
            print(f"Warning: Could not load music: {e}")

        # Font settings
        self.retro_font = tkFont.Font(family="Courier", size=16, weight="bold")

        # Timer and Score Variables
        self.time_left = TIME_LIMIT
        self.score = 0
        self.current_question = ""
        self.correct_answer = 0

        # Create UI elements
        self.setup_ui()

    def setup_ui(self):
        """Create the game interface."""
        # Title Label
        title_text = """
        ███╗   ███╗ █████╗ ████████╗██╗  ██╗
        ████╗ ████║██╔══██╗╚══██╔══╝██║  ██║
        ██╔████╔██║███████║   ██║   ███████║
        ██║╚██╔╝██║██╔══██║   ██║   ██╔══██║
        ██║ ╚═╝ ██║██║  ██║   ██║   ██║  ██║
        ╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝
        """
        self.title_label = tk.Label(self.game_window, text=title_text, font=self.retro_font,
                                    fg="#39FF14", bg="black", justify="center")
        self.title_label.pack(pady=5)

        # Timer Label
        self.timer_label = tk.Label(self.game_window, text=f"Time Left: {self.time_left}s",
                                    font=self.retro_font, fg="red", bg="black")
        self.timer_label.pack()

        # Score Label
        self.score_label = tk.Label(self.game_window, text=f"Score: {self.score}",
                                    font=self.retro_font, fg="yellow", bg="black")
        self.score_label.pack()

        # Math Problem Display
        self.question_label = tk.Label(self.game_window, text="Press 'Start' to begin!",
                                       font=self.retro_font, fg="cyan", bg="black")
        self.question_label.pack(pady=10)

        # Answer Input Field
        self.answer_entry = tk.Entry(self.game_window, font=self.retro_font, bg="white", fg="black")
        self.answer_entry.pack(pady=5)

        # Submit Button
        self.submit_button = tk.Button(self.game_window, text="Submit Answer", font=self.retro_font,
                                       bg="#DC143C", fg="white", command=self.check_answer)
        self.submit_button.pack(pady=5)

        # Start Button
        self.start_button = tk.Button(self.game_window, text="Start Game", font=self.retro_font,
                                      bg="green", fg="black", command=self.start_game)
        self.start_button.pack(pady=5)

        # Exit Button
        self.exit_button = tk.Button(self.game_window, text="Exit", font=self.retro_font,
                                     bg="gray", fg="white", command=self.game_window.destroy)
        self.exit_button.pack(pady=5)

    def generate_question(self):
        """Generate a random math question."""
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        operation = random.choice(["+", "-", "*", "/"])

        # Ensure division results in an integer
        if operation == "/":
            num1 = num2 * random.randint(1, 10)

        self.current_question = f"{num1} {operation} {num2}"
        self.correct_answer = eval(self.current_question)
        self.question_label.config(text=self.current_question)

    def check_answer(self):
        """Check if the user's answer is correct."""
        if self.time_left > 0:
            try:
                user_answer = float(self.answer_entry.get())
                if abs(user_answer - self.correct_answer) < 0.001:  # Allow small float errors
                    self.score += 1
                    self.score_label.config(text=f"Score: {self.score}")
            except ValueError:
                pass  # Ignore non-numeric inputs

            self.answer_entry.delete(0, tk.END)  # Clear input
            self.generate_question()  # Next question

    def start_game(self):
        """Start the timer and generate the first question."""
        self.time_left = TIME_LIMIT
        self.score = 0
        self.score_label.config(text="Score: 0")
        self.start_button.config(state="disabled")  # Disable start button during game
        self.generate_question()
        self.update_timer()

    def update_timer(self):
        """Update the countdown timer."""
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.config(text=f"Time Left: {self.time_left}s")
            self.game_window.after(1000, self.update_timer)  # Call every 1 second
        else:
            self.question_label.config(text="Game Over! Final Score: " + str(self.score))
            self.start_button.config(state="normal")  # Re-enable start button


# Main function to launch the game from another menu
def open_math_attack(parent_window):
    """Open the Math Time Attack game window."""
    MathTimeAttack(parent_window)


# Run the game only if this script is executed directly
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide main window (this is only needed if running standalone)
    open_math_attack(root)
    root.mainloop()
