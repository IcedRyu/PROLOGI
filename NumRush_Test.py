import time
import random
import json

HIGH_SCORE_FILE = "high_scores.json"


def load_high_scores():
    try:
        with open(HIGH_SCORE_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"normal": 0, "time_attack": 0}


def save_high_scores(scores):
    with open(HIGH_SCORE_FILE, "w") as file:
        json.dump(scores, file)


def generate_problem(difficulty):
    if difficulty == "easy":
        a, b = random.randint(1, 10), random.randint(1, 10)
    elif difficulty == "medium":
        a, b = random.randint(10, 50), random.randint(10, 50)
    else:
        a, b = random.randint(50, 100), random.randint(50, 100)
    operator = random.choice(["+", "-", "*"])
    question = f"{a} {operator} {b}"
    answer = eval(question)
    return question, answer


def play_game(mode):
    scores = load_high_scores()
    difficulty = input("Choose difficulty (easy/medium/hard): ").lower()
    score = 0

    if mode == "normal":
        rounds = 5
        for _ in range(rounds):
            question, answer = generate_problem(difficulty)
            user_answer = input(f"Solve: {question} = ")
            if user_answer.isdigit() and int(user_answer) == answer:
                print("Correct!")
                score += 10
            else:
                print(f"Wrong! The correct answer was {answer}.")

    elif mode == "time_attack":
        time_limit = 30
        start_time = time.time()
        while time.time() - start_time < time_limit:
            question, answer = generate_problem(difficulty)
            user_answer = input(f"Solve: {question} = ")
            if user_answer.isdigit() and int(user_answer) == answer:
                print("Correct!")
                score += 10 + int(10 - (time.time() - start_time) % 10)
            else:
                print(f"Wrong! The correct answer was {answer}.")

    print(f"Final Score: {score}")
    if score > scores[mode]:
        print("New High Score!")
        scores[mode] = score
        save_high_scores(scores)


def view_high_scores():
    scores = load_high_scores()
    print(f"High Scores:\nNormal Mode: {scores['normal']}\nTime-Attack Mode: {scores['time_attack']}")


def show_instructions():
    print("""
    Welcome to NumRush!
    - Choose a mode: Normal or Time-Attack.
    - Solve math problems correctly to earn points.
    - In Normal mode, you solve a set number of questions.
    - In Time-Attack mode, solve as many as you can before time runs out.
    - Try to beat the high score!
    """)


def main():
    while True:
        print("\nNumRush Main Menu")
        print("1. Start Game")
        print("2. Time-Attack Mode")
        print("3. View High Scores")
        print("4. Instructions")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            play_game("normal")
        elif choice == "2":
            play_game("time_attack")
        elif choice == "3":
            view_high_scores()
        elif choice == "4":
            show_instructions()
        elif choice == "5":
            print("Thanks for playing NumRush!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()