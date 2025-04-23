#!/usr/bin/env python

import logging
from models.player import Player
from models.board import Board
from models.cell import Cell, CellState

# Setup logging
logging.basicConfig(
    filename='hunt_the_king.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.current_player = 1
        self.end = False
        self.winner = None
        self.turns = 0
        logging.info("Game initialized between %s and %s", player1.name, player2.name)

    def setup(self):
        for player in [self.player1, self.player2]:
            print(f"{self.player1.name}'s Board")
            self.player1.board.display()
            print("-" * self.player1.board.size[1] * 2, end="\n\n")
            self.player2.board.display()
            print(f"{self.player2.name}'s Board")

            while not player.ready:
                print(f"{player.name}, place your king on the board.")
                x, y = self._get_coordinates()
                if not player.board.valid_coordinates(x, y) or player.board.get(x, y).is_rock:
                    print("Invalid coordinates. Try again.")
                    logging.warning("%s attempted invalid king placement at (%d, %d)", player.name, x, y)
                    continue
                if player.place_king(x, y):
                    logging.info("%s placed king at (%d, %d)", player.name, x, y)
                    player.ready = True
                else:
                    print("Invalid. Try again.")
                    logging.warning("%s failed to place king at (%d, %d)", player.name, x, y)

            print("\033[H\033[J", end="")  # clear screen

    def switch_player(self):
        self.current_player = 2 if self.current_player == 1 else 1

    def play_turn(self):
        print("\033[H\033[J", end="")  # clear screen
        print(f"Turn {self.turns + 1}")
        print(f"Current Player: {self.current_player}")
        print(f"{self.player1.name}'s Board")
        self.player1.board.display()
        print("-" * self.player1.board.size[1] * 2)
        self.player2.board.display()
        print(f"{self.player2.name}'s Board")

        current_player = self.player1 if self.current_player == 1 else self.player2
        opponent = self.player2 if self.current_player == 1 else self.player1

        print(f"{current_player.name}'s turn.")
        logging.info("Turn %d: %s's turn", self.turns + 1, current_player.name)

        while True:
            x, y = self._get_coordinates()
            if not opponent.board.valid_coordinates(x, y):
                print("Invalid coordinates. Try again.")
                logging.warning("%s attempted invalid hit at (%d, %d)", current_player.name, x, y)
                continue

            hit_result, cell_state = opponent.board.hit(x, y)
            if not hit_result:
                print("Invalid coordinates. Try again.")
                logging.warning("%s attempted repeat or blocked hit at (%d, %d)", current_player.name, x, y)
                continue

            logging.info("%s attacked (%d, %d) - Result: %s", current_player.name, x, y, cell_state.name)

            if cell_state == CellState.KING:
                print(f"{current_player.name} hit the king!")
                logging.info("%s hit the king at (%d, %d) and won!", current_player.name, x, y)
                self.winner = current_player
                self.end = True
            break

        self.turns += 1
        self.switch_player()

    def start(self):
        print("\033[H\033[J", end="")  # clear screen
        print("Welcome to the game!")
        print("Setting up the game...")
        logging.info("Game setup started.")
        self.setup()
        logging.info("Game setup complete.")

        while not self.end:
            self.play_turn()

        if self.winner:
            print("\033[H\033[J", end="")  # clear screen
            print(f"{self.player1.name}'s Board")
            self.player1.board.display()
            print("-" * self.player1.board.size[1] * 2)
            self.player2.board.display()
            print(f"{self.player2.name}'s Board")
            print(f"\n\n\n{self.winner.name} wins!🥳🍾")
            logging.info("Game Over. Winner: %s", self.winner.name)

    def _get_coordinates(self):
        while True:
            try:
                x, y = map(int, input("Enter coordinates (x y): ").split())
                return x - 1, y - 1
            except ValueError:
                print("Invalid input. Enter numbers like: 3 4")
                logging.error("Non-integer coordinates entered.")
