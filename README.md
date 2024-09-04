
# 2048 - Simple Game Realisation with Pygame

This is a simple implementation of the popular 2048 game using the Pygame library.

## Game Description:

2048 is a simple puzzle game where the player needs to combine tiles with numbers on a 4x4 grid. The objective is to reach the tile with the number **2048** by sliding and merging tiles with the same value. The game ends when no valid moves are possible, or the player reaches the 2048 tile.

### Game Mechanics:
1. The player uses arrow keys to move the tiles up, down, left, or right.
2. Tiles with the same number merge when they collide, and their values are added.
3. After every move, a new tile (2 or 4) spawns in an empty spot.
4. The goal is to create a tile with the value 2048, but the game can continue past this point.
5. The game ends when no more moves are possible.

## How to start:

1. **Install all requirements**:
   Make sure you have Python and Pygame installed. You can install the required dependencies by running:

   ```bash
   pip install -r requirements.txt
   ```

   (If you don't have a `requirements.txt`, simply install Pygame directly):

   ```bash
   pip install pygame
   ```

2. **Run the game**:
   Once the dependencies are installed, run the game using:

   ```bash
   python main.py
   ```

Enjoy playing 2048!
