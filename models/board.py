#!/usr/bin/env python

from models.cell import Cell, CellState
from config import BOARD_ROWS, BOARD_COLS
import random
from math import floor

class Board:
    def __init__(self, size=(BOARD_ROWS, BOARD_COLS), rocks=None):
        self.size = size
        self.board  = [[Cell(x, y) for y in range(size[1])] for x in range(size[0])]
        self.king_cell = None
        self.rocks_count = floor(self.size[0] * self.size[1] * 0.15) if rocks is None else rocks
        self._place_rocks()

    def get(self, x, y):
        return self.board[x][y]

    def valid_coordinates(self, x, y):
        return 0 <= x < self.size[0] and 0 <= y < self.size[1]

    def place_king(self, x, y):
        if self.valid_coordinates(x, y):
            if self.board[x][y].is_king:
                return False
            self.board[x][y].place_king()
            self.king_cell = self.board[x][y]
            return True
        else:
            raise ValueError("Invalid coordinates for placing the king.")


    def _place_rocks(self):
        count = 0
        while count < self.rocks_count:
            x, y = random.randint(0, self.size[0] - 1), random.randint(0, self.size[1] - 1)
            if not self.board[x][y].is_rock and not self.board[x][y].is_king:
                self.board[x][y].is_rock = True
                count += 1

    def hit(self, x, y):
        if not self.valid_coordinates(x, y):
            return ValueError("Invalid coordinates for hitting a cell.")
        cell = self.board[x][y]

        if cell.is_revealed:
            return False, CellState.REVEALED
        
        if cell.is_rock:
            return False, CellState.ROCK

        cell.reveal()

        if cell.is_king:
            return True, CellState.KING
        return True, CellState.EMPTY

    def display(self):
        for row in self.board:
            print(" ".join(str(cell) for cell in row))
        print()

