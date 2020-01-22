import os
from graphics import *
#from world import *
import json

# wir drawen eine linie mit 7 Rechtecken
# dann 5 dieser Linien
#
#
#

def drawRectangle(window, point1, point2):
    rectangle = Rectangle(point1, point2)
    rectangle.setWidth(2)
    rectangle.setFill("white")
    rectangle.draw(window)

class ChessBoard:
    def __init__(self, window, columns, lines):
        self.window = window
        self.columns = columns
        self.lines = lines
        self.counter = 0
        self.counter2 = 0
        self.x_start = 20
        self.x2_start = 80
        self.y_start = 20
        self.y_start2 = 80

        # immer 60 mehr
        # 1 linie, davon brauchen wir aber 5
        while self.counter != columns:
            drawRectangle(self.window, Point(self.x_start,20), Point(self.x2_start,80))
            self.counter += 1
            self.x_start += 60
            self.x2_start += 60
        self.x_start = 20
        self.x2_start = 80
        self.counter = 0
        while self.counter != columns:
            drawRectangle(self.window, Point(self.x_start,80), Point(self.x2_start,140))
            self.counter += 1
            self.x_start += 60
            self.x2_start += 60
        self.x_start = 20
        self.x2_start = 80
        self.counter = 0
        while self.counter != columns:
            drawRectangle(self.window, Point(self.x_start,140), Point(self.x2_start,200))
            self.counter += 1
            self.x_start += 60
            self.x2_start += 60
        self.x_start = 20
        self.x2_start = 80
        self.counter = 0
        while self.counter != columns:
            drawRectangle(self.window, Point(self.x_start,200), Point(self.x2_start,260))
            self.counter += 1
            self.x_start += 60
            self.x2_start += 60
        self.x_start = 20
        self.x2_start = 80
        self.counter = 0
        while self.counter != columns:
            drawRectangle(self.window, Point(self.x_start,260), Point(self.x2_start,320))
            self.counter += 1
            self.x_start += 60
            self.x2_start += 60

        #drawRectangle(window, Point(20,20), Point(80,80))
        #drawRectangle(window, Point(80,20), Point(140,80))
        #drawRectangle(window, Point(140,20), Point(200,80))



class WorldObject():
    def __init__(self, window):
        self.window = window
        self.x = size_x # left right
        self.y = size_y # height


count = 0
columns = 7
lines = 5

window = GraphWin("Roboter Steuerung", 1280, 720)
# draw the chessboard
chessbord = ChessBoard(window, columns, lines)
mouseClick = window.getMouse() # pause for click in window
#win.close()

