# Asteroids Game

A classic Asteroids arcade game built with Python and Pygame. Navigate your spaceship through an asteroid field, shoot asteroids to break them apart, and survive as long as possible.

## Prerequisites

- Python 3.13 or higher
- Pygame 2.6.1

## Installation

Clone the repository:
```bash
git clone https://github.com/JansenMitchell/asteroids.git
cd asteroids
```

Install dependencies:
```bash
pip install -e .
```

Or install pygame directly:
```bash
pip install pygame==2.6.1
```

## How to Run

```bash
python main.py
```

## Controls

- Arrow keys or WASD to move and rotate
- Spacebar to shoot
- Close the window to exit

## Gameplay

- Avoid colliding with asteroids
- Shoot asteroids to break them into smaller pieces
- Survive as long as you can

## Project Structure

```
asteroids/
├── main.py           # Game entry point and main loop
├── player.py         # Player spaceship class
├── asteroid.py       # Asteroid object class
├── asteroidfield.py  # Asteroid spawning system
├── shot.py           # Projectile class
├── circleshape.py    # Base class for circular game objects
├── constants.py      # Game configuration constants
├── logger.py         # Event and state logging system
└── pyproject.toml    # Project dependencies
```

## License

This project is open source and available for educational purposes.