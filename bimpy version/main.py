import bimpy # grpahic lib
import json # for configs
import world # import the world classes
import serial

# serial schnittstell
#movementController = serial.Serial('/dev/ttyUSB0')
# create a window context
ctx = bimpy.Context()
# initialize main window
ctx.init(1280,720, "Robotter Steuerung")
# set window width and height
winHeight = ctx.height()
winWidth = ctx.width()

menu_tab = 1

columns_count = 7
lines_count = 5

counter = [1,2,3,4,5,6,7]

# settings
borders_horizontal = True
borders_vertical = True

field_names = ["A1", "A2", "A3", "A4", "A5", "A6", "A7",
               "B1", "B", "B3", "B4", "B5", "B6", "B7",
               "C1", "C2", "C3", "C4", "C5", "C6", "C7",
               "D1", "D2", "D3", "D4", "D5", "D6", "D7",
               "E1", "E2", "E3", "E4", "E5", "E6", "E7",
               "F1", "F2", "F3", "F4", "F5", "F6", "F7",
               "G1", "G2", "G3", "G4", "G5", "G6", "G7",
               "H1", "H2", "H3", "H4", "H5", "H6", "H7"]


def drawMainTab(columns_count=7, lines_count=5):
    bimpy.columns(columns_count, None, borders_vertical)
    i = 0
    col_c = 0
    while col_c > lines_count:
        col_c += 1
    while i != columns_count:
        if borders_horizontal and bimpy.get_column_index == 0:
            bimpy.separator()
        #bimpy.text("{}".format("a"))
        bimpy.button(field_names[i], bimpy.Vec2(100,100))
        bimpy.next_column()
        i += 1
    columns_count = 0
    bimpy.columns(1)
    if borders_horizontal:
        bimpy.separator()

def drawPathFinder(columns_count=7, lines_count=5):
    bimpy.columns(columns_count, None, borders_vertical)
    i = 0
    while i != columns_count:
        i += 1
        if borders_horizontal and bimpy.get_column_index == 0:
            bimpy.separator()
        #bimpy.text("{}".format("a"))
        bimpy.button("Auto Path", bimpy.Vec2(100,100))
        bimpy.next_column()
    bimpy.columns(1)
    if borders_horizontal:
        bimpy.separator()
        
# menu functions
def move_forward():
    print("Move Forward")
    #movementController.write("move_forward")

def move_backwards():
    print("Move Backward")
    #movementController.write("move_backward")
    
def turn_left():
    print("Turned Left 90°")
    #movementController.write("move_turn_left")

def turn_right():
    print("Turned Right -90°")
    #movementController.write("turn_right")

def spinMe():
    print("Hui")
            
# start the main loop
while not ctx.should_close():
    # create a new frame
    ctx.new_frame()

    # setup first win pos and win size
    bimpy.set_next_window_pos(bimpy.Vec2(20, 20), bimpy.Condition.Once)
    bimpy.set_next_window_size(bimpy.Vec2(winWidth - 520, winHeight-40), bimpy.Condition.Once)

    # begin the window
    bimpy.begin("Chess View", flags=bimpy.NoMove | bimpy.NoCollapse) # add more flags like this: | bimpy.NoResize | bimpy.NoTitleBar
    if bimpy.button("General", bimpy.Vec2(150, 25)):
        menu_tab = 1
    bimpy.same_line()
    if bimpy.button("Path Finder", bimpy.Vec2(150, 25)):
        menu_tab = 2  
    
    if menu_tab == 1:
        drawMainTab()
    elif menu_tab == 2:
        drawPathFinder()
    # end the window
    bimpy.end()

    # setup the 2nd window
    bimpy.set_next_window_pos(bimpy.Vec2(800, 20), bimpy.Condition.Once)
    bimpy.set_next_window_size(bimpy.Vec2(winWidth - 820, winHeight-300), bimpy.Condition.Once)
    bimpy.begin("Control Board", flags=bimpy.NoMove | bimpy.NoCollapse)
    bimpy.columns(3, None, False)
    bimpy.next_column()
    if bimpy.button("Forward", bimpy.Vec2(140,80)):
        move_forward()
    bimpy.next_column()
    bimpy.next_column()
    if bimpy.button("Left", bimpy.Vec2(140,80)):
        turn_left()
    bimpy.next_column()
    bimpy.next_column()
    if bimpy.button("Right", bimpy.Vec2(140,80)):
        turn_right()
    bimpy.next_column()
    bimpy.next_column()
    if bimpy.button("Back", bimpy.Vec2(140,80)):
        move_backwards()
    bimpy.columns(1)
    bimpy.new_line()
    if bimpy.button("Spin Me", bimpy.Vec2(150,50)):
        spinMe()
    bimpy.end()

#    setup the 3rd window
    bimpy.set_next_window_pos(bimpy.Vec2(800, 460), bimpy.Condition.Once)
    bimpy.set_next_window_size(bimpy.Vec2(winWidth - 820, winHeight-480), bimpy.Condition.Once)
    bimpy.begin("Window Settings", flags=bimpy.NoMove | bimpy.NoCollapse)
    bimpy.text("Borders")
    #bimpy.checkbox("horizontal", borders_horizontal)
    #bimpy.same_line()
    #bimpy.checkbox("vertical", borders_vertical)
    bimpy.end()
    bimpy.show_demo_window()
    # render the context window
    ctx.render()