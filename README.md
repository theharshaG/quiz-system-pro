# quiz-system-pro

Quiz System Pro (Python Project)
## Overview

This project is an advanced command-line Quiz System implemented in Python. It loads questions from a JSON file, applies a timer for each question, evaluates answers, and maintains a leaderboard. The system stores quiz results and ranks users based on their scores.

## Features

Load questions from JSON file
Randomize question order
Timer-based answering system
Validate user input
Calculate score
Leaderboard system (top scores)
Data persistence using JSON files

## Technologies Used

Python
JSON (data storage)
Random module
Time module

## Project Structure

quiz-system-pro/
│
├── main.py
├── questions.json
├── leaderboard.json
└── README.md

## How to Run

install python (VS Code)
Create questions.json file before running
Run the program: quiz system pro.py

## How It Works

Questions are stored in questions.json file
Each question contains question, options, and correct answer

When the program starts:
User enters their name
Questions are shuffled randomly

During quiz:
Each question has a time limit (5 seconds)
If user does not answer in time, the question is skipped
Input is validated to avoid errors

After quiz:
Score is calculated and displayed

Leaderboard system:
User score is saved in leaderboard.json
Scores are sorted in descending order
Top 5 scores are displayed

## Future Improvements

Add difficulty levels
Add category-based quizzes
Store multiple quiz attempts per user
Add negative marking
Convert to GUI application
Develop web version using Flask
Add timer countdown display

## Author
Harsha G
Learning Python | Embedded Systems | IoT
