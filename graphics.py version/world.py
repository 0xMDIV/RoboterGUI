import sqlite3
from graphics import * #just better tkinter

class Chessboard():
    def __init__(self, window, row, col):
        self.window = window
        self.row = row
        self.column = col

        chessGrid = Rectangle(Point(10,150), Point(10,150))
        i = 0
        while i != row:
            i += 1
            print(i)


class WorldObject():
    def __init__(self, window, size_x, size_y):
        self.window = window
        self.x = size_x # left right
        self.y = size_y # height


class useful():
    def countUp(self, counterEnd):



