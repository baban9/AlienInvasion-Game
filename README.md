# Alien Invasion Game

Pygame arcade shooter demonstrating object-oriented game design, event-driven loops, and sprite management.

## Problem

Build a playable 2D game that separates configuration, entities, and the main loop so gameplay logic stays testable and extensible.

## Approach

- **Entity model**: `Ship`, `Bullet`, and alien fleet as independent modules
- **Settings centralization**: `settings.py` holds tunable game parameters
- **Event loop**: Input handling isolated from rendering and state updates

## Repository structure

```
Alien_invasion.py   Main game loop and orchestration
settings.py         Screen size, speeds, limits
ship.py             Player ship behavior
bullet.py           Projectile logic
```

## Reproducibility

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
make setup
python Alien_invasion.py
```

## Tech stack

Python 3, Pygame

## Results

Functional arcade game with fleet escalation, lives system, and keyboard controls.

## Limitations and next steps

- Add unit tests for collision detection
- Extract game state into a class for headless simulation
- Add CI smoke test that imports all modules
