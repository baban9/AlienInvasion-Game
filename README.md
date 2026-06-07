# Alien Invasion Game

Complete Pygame arcade shooter with alien fleets, scoring, lives, level progression, and a polished HUD. Built with modular OOP so gameplay logic stays testable without a display.

## Gameplay

- Destroy the alien fleet before they reach the bottom or collide with your ship
- Each cleared wave increases speed and score multiplier
- You have 3 lives; high score persists across runs in the session

## Controls

| Key | Action |
|-----|--------|
| P | Start game (from title screen) |
| A / Left | Move left |
| D / Right | Move right |
| Space | Fire |
| F | Toggle fullscreen |
| R | Restart after game over |
| Q | Quit |

## Architecture

```
game.py           Main loop, state machine, collision handling
settings.py       Tunable constants and difficulty scaling
ship.py           Player ship (procedural sprite, no external assets)
bullet.py         Projectile sprites
alien.py          Alien sprites and fleet manager
game_stats.py     Score, lives, level, high score
hud.py            Scoreboard and overlay screens
collisions.py     Pure collision helpers (unit tested)
Alien_invasion.py Entry point
tests/            Pytest suite
```

## Reproducibility

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
make setup
make run
make test
```

## Design decisions

- **Procedural sprites**: Ship and aliens are drawn with Pygame primitives so the game runs anywhere without missing image files
- **Separated collisions**: Hit detection lives in `collisions.py` for headless testing
- **Difficulty curve**: Speed and points scale per level via `Settings.increase_speed()`
- **Game states**: Title screen, active play, level flash, and game over are explicit UI states

## Tech stack

Python 3, Pygame, pytest

## Future enhancements

- Sound effects and background music
- Power-ups (rapid fire, shield)
- Leaderboard persisted to disk
