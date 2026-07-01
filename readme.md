# 🐍 Snake Game

A classic Snake game built with Python's Turtle module, featuring a scoreboard, growing snake, food collisions, and a bordered game area.

Built as part of [Angela Yu's 100 Days of Code](https://www.udemy.com/course/100-days-of-code/) bootcamp (Day 20 project).

## Description

A classic Snake game built with Python's Turtle module. Features smooth keyboard controls, a snake that grows on eating food, a live scoreboard, wall-collision game-over logic, and a bordered play area. Built with clean OOP design across separate modules for the snake, food, and scoreboard — as part of the 100 Days of Code bootcamp.

## Features

- Smooth keyboard controls (Arrow keys or WASD)
- Snake grows every time it eats food
- Live scoreboard that updates on each point
- Game over on wall collision or self-collision
- Thick red border marking the play area

## Controls

| Key | Action |
|-----|--------|
| ↑ / W | Move Up |
| ↓ / S | Move Down |
| ← / A | Move Left |
| → / D | Move Right |

## Project Structure

```
├── main.py         # Game loop, screen setup, collision detection
├── snake.py        # Snake class (movement, growth, direction)
├── food.py         # Food class (random placement)
├── scoreboard.py   # Scoreboard class (score display, game over text)
└── constants.py    # Shared constants (MOVE_DISTANCE, UP, DOWN, LEFT, RIGHT)
```

## Requirements

- Python 3.x
- No external libraries — uses only the built-in `turtle`, `random`, and `time` modules

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/BeingArham/snake-game-turtle.git
   cd snake-game-turtle
   ```
2. Run the game:
   ```bash
   python main.py
   ```

## Author

Arham Tabish
