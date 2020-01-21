#Nicht klauen ihr Schlingels
from graphics import *
from time import *
import asyncio
import enum

class Direction(enum.Enum):
    North = 1
    East = 2
    West = 3
    South = 4

class Pointer:
    __direction = Direction
    def __init__(self, direction, x, y):
        self.__x = x
        self.__y = y
        self.__direction = direction

class ChessBoard:
    def __init__(self, win, counter, lines):
        self.win = win
        self.lineCounter = 0
        self.columns = counter
        self.rows = lines

        while(self.lineCounter != lines):
            self.lineCounter += 1
            createLine(self.win, counter, self.lineCounter)

def createRectangle(win,pointer1,pointer2):
    rect = Rectangle(pointer1,pointer2)
    rect.setWidth(2)
    rect.setFill("white")
    rect.draw(win)
    rect = None

def createLine(win, counter, lineNumber):
    lineCounter = 0
    while(lineCounter != counter):
        lineCounter += 1
        createRectangle(win, Point((60*lineCounter), (60*lineNumber)), Point(60*(1+lineCounter), (60*(1+lineNumber))))

if __name__ == "__main__":
    win = GraphWin("Tester", 800, 500)
    newChessBoard = ChessBoard(win, 7, 5)
    print(newChessBoard.columns)
    win.getMouse()
    win.close()