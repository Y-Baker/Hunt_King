# 🎯 Game: Hunt the King

## 🧠 Game Concept
Hunt the King is a two-player strategy game where each player places a King on a hidden board. Players take turns attacking coordinates to try to locate and "hit" the opponent's King.

---

## 📋 Rules

1. Each player has a board (e.g., 8x8 grid).
2. Each player hides their King at a secret cell.
3. Random rocks are placed on the board at initialization to block cells.
4. Players take turns calling out a coordinate to attack.
5. The game evaluates the result of each attack:
   - `Hit`: The opponent's King is found.
   - `Miss`: Empty cell.
   - `Invalid`: Already attacked or a blocked cell.
6. The first to hit the opponent's King wins!

---

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/Y-Baker/Hunt_King
    cd Hunt_King
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the game:
    ```bash
    python main.py
    ```

4. Follow the on-screen instructions to play the game.
5. Enjoy the game!
