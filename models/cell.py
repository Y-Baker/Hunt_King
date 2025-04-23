#!/usr/bin/env python
from enum import Enum

class CellState(Enum):
    EMPTY = 0
    KING = 1
    REVEALED = 2
    ROCK = 3

class Cell:
    def __init__(self, x, y, is_king=False, is_revealed=False, is_rock=False):
        self.x = x
        self.y = y
        self.is_king = is_king
        self.is_revealed = is_revealed
        self.is_rock = False
    
    def place_king(self):
        self.is_king = True
    
    def reveal(self):
        if self.is_revealed:
            return False
        
        self.is_revealed = True
        return True


    def __repr__(self):
        if self.is_king and self.is_revealed:
            return "👑"
        elif self.is_rock:
            return "🪨 "
        elif self.is_revealed:
            return "❌"
        else:
            return "⬜️"

