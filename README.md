# Classic Snake Game

This repository contains the Python code for a classic rendition of the well-known Snake game, leveraging the Turtle graphics library for a simple and enjoyable graphical user interface.

## Table of Contents

- [Introduction](#introduction)
- [Technologies](#technologies)
- [Files in the Project](#files-in-the-project)
- [Setup](#setup)
- [Gameplay](#gameplay)
- [Developer](#developer)

## Introduction

The Classic Snake Game is a Python-based project that simulates the traditional snake game we all adored. The player controls a snake, guiding it to eat food and grow in size while avoiding walls and its tail. This game saves the high score for each session in `data.txt`, so you can keep track of your progress over time.

## Technologies

Project is created with:
- Python 3.8+
- Turtle Graphics Library

## Files in the Project

- `main.py` - The main game loop that initializes the game window and controls game updates.
- `snake.py` - Contains the Snake class that manages the snake's behavior in the game.
- `food.py` - Contains the Food class that handles the appearance and position of food on the screen.
- `scoreboard.py` - Contains the Scoreboard class that manages the score display and high score tracking.
- `data.txt` - A text file that records the high score between game sessions.

## Setup

To run this game, you'll need a Python interpreter. Clone this repository, navigate to the directory containing the game, and run the following command:

```bash
python main.py
```

## Gameplay


Use the arrow keys (Up, Down, Left, Right) to change the direction of the snake.
Eat food to gain points and grow the snake in length.
Avoid colliding with the wall or the snake's tail.
Try to beat the high score!

## Developer

Ali Jafarbeglou 
