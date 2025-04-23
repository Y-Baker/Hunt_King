#!/usr/bin/env python

from models.board import Board

class Player:
    def __init__(self, name):
        self.name = name
        self.board = Board()
        self.ready = False
    
    def place_king(self, x, y):
        return self.board.place_king(x, y)

    def surrender(self):
        self.board.display()
        self.ready = False
        