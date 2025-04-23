#!/usr/bin/env python
from models.cell import Cell, CellState
import logging

class Board:
    def __init__(self, num_rows, num_cols):
        self.size = (num_rows, num_cols)
        self.king_cell = None
        self.board = [Cell(x, y) for y in range(self.size[1]) for x in range(self.size[0])]

    def valid_coordinates(self, x, y):
        return 0 <= x < self.size[0] and 0 <= y < self.size[1]

    def place_king(self, x, y):
        if not self.valid_coordinates(x, y):
            logging.error(f"Invalid ({x}, {y}) with Board Size({self.size[0]}, {self.size[1]})")
            return False
        
        cell = self.board[x][y]
        if cell.is_king == True:
            return False
        
        cell.place_king()
        self.king_cell = cell
        return True

    def hit(self, x, y):
        if not self.valid_coordinates(x, y):
            logging.error(f"Invalid ({x}, {y}) with Board Size({self.size[0]}, {self.size[1]})")
            return False

        cell = self.board[x][y]
        if cell.is_revealed:
            return False, CellState.REVEALED
        
        cell.reveal()

        if cell.is_king:
            return True, CellState.KING
        else:
            return True, Cell.EMPTY

    def display(self):
        for row in self.board:
            print(" ".join(str(cell) for cell in row))
        print()
    

        