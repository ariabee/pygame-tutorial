# Pygame Tutorial Team Assignment
Language, Action, and Perception; Week 3

We used the Python Pygame tutorial provided by https://coderslegacy.com/python/python-pygame-tutorial/ to build a small Pygame application, with an additional feature.

## Additional Features: Multiplayer cars + Up/Down motion
The standard car-avoids-enemy-cars game is now a two-player endeavor. A second player controls a car using the *a* and *d* keys for left and right motion. Both cars must avoid collision with the enemy vehicles, and with each other, in order to keep the game going.

Both players can now move up and down in addition to left and right. Player1 moves up and down via the *up* and *down* keys. Player2 moves up and down via the *w* and *s* keys.

Code updates:

- In Game.py, we added a Player2 class, including Player2 image.
- Player2 uses a-d-w-s keys to move left-right-up-down.
- Player1 uses left, right, up, and down keys to move similarly.
- Both players begin in positions on opposite sides of the display.
- The players share an enemy sprite group (the enemy cars that move towards the players).
- Collisions are checked between players and their enemies, and between players themselves.

## How to Use (Development)
- Have python installed. Check https://www.pygame.org/wiki/GettingStarted for details.
- Have pygame installed. Check https://www.pygame.org/wiki/GettingStarted for details.

## How to Use (to Play!)
- Be sure to have python and pygame installed. Check https://www.pygame.org/wiki/GettingStarted for details.
- Download the project files or clone the project locally.
- Using terminal or other command line interface launch `python3 Game.py`. 

## References
- Pygame tutorial used here: https://coderslegacy.com/python/python-pygame-tutorial/
- Pygame documentation: https://www.pygame.org/docs/ref/draw.html
