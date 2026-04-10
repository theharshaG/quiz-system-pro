# before run the program you should create "questions.json" file 

import json
import random
import time

#  Load questions
def load_questions():
    with open("questions.json", "r") as f:
        return json.load(f)


# Timer input
def timed_input(prompt, timeout=5):
    print(f"You have {timeout} seconds...")
    start = time.time()

    answer = input(prompt)

    end = time.time()

    if end - start > timeout:
        print(" Time's up!")
        return None

    return answer


# Run quiz
def run_quiz(questions):
    score = 0

    for q in questions:
        print("\n" + q["question"])

        for i, option in enumerate(q["options"], start=1):
            print(f"{i}. {option}")

        choice = timed_input("Enter option: ", 5)

        if choice is None:
            print("Skipped!")
            continue

        if not choice.isdigit():
            print("Invalid input")
            continue

        index = int(choice) - 1

        if index < 0 or index >= len(q["options"]):
            print("Invalid choice")
            continue

        selected = q["options"][index]

        if selected == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print("wrong! Answer:", q["answer"])

    return score


# Load leaderboard
def load_leaderboard():
    try:
        with open("leaderboard.json", "r") as f:
            return json.load(f)
    except:
        return []


#Save leaderboard
def save_leaderboard(data):
    with open("leaderboard.json", "w") as f:
        json.dump(data, f, indent=4)


#  Update leaderboard
def update_leaderboard(name, score):
    data = load_leaderboard()

    data.append({"name": name, "score": score})

    # Sort highest score first
    data = sorted(data, key=lambda x: x["score"], reverse=True)

    save_leaderboard(data)


# Show leaderboard
def show_leaderboard():
    data = load_leaderboard()

    print("\n LEADERBOARD")
    for i, user in enumerate(data[:5], start=1):
        print(f"{i}. {user['name']} - {user['score']}")


# MAIN PROGRAM
def main():
    name = input("Enter your name: ")

    questions = load_questions()
    random.shuffle(questions)

    score = run_quiz(questions)

    print(f"\n {name}, your score: {score}/{len(questions)}")

    update_leaderboard(name, score)
    show_leaderboard()


#  Run
if __name__ == "__main__":
    main()
