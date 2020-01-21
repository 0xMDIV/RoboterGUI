import os
from graphics import *
#from world import *
import json

win = GraphWin("Roboter Steuerung", 1280, 720)
# draw the chessboard
chessGrid = Rectangle(win, Point(10,150), Point(10,150))
mouseClick = win.getMouse() # pause for click in window
win.close()

