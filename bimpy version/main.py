import bimpy # grpahic lib
import json # for configs
import world # import the world classes

# create a window context
ctx = bimpy.Context()
# initialize main window
ctx.init(1280,720, "Robotter Steuerung")
# set window width and height
winHeight = ctx.height()
winWidth = ctx.width()

def toggleMenu():
    print("Menu Toggled")
    return 1
# start the main loop
while not ctx.should_close():
    # create a new frame
    ctx.new_frame()

    # setup first win pos and win size
    bimpy.set_next_window_pos(bimpy.Vec2(20, 20), bimpy.Condition.Once)
    bimpy.set_next_window_size(bimpy.Vec2(winWidth - 520, winHeight-40), bimpy.Condition.Once)

    # begin the window
    bimpy.begin("Chess View", flags=bimpy.NoMove) # add more flags like this: | bimpy.NoResize | bimpy.NoTitleBar
    bimpy.text("placeholder")
    # end the window
    bimpy.end()
    
    # setup the 2nd window
    bimpy.set_next_window_pos(bimpy.Vec2(800, 20), bimpy.Condition.Once)
    bimpy.set_next_window_size(bimpy.Vec2(winWidth - 820, winHeight-40), bimpy.Condition.Once)
    bimpy.begin("Control Board")
    bimpy.text("re")
    bimpy.end()

    # render the context window
    ctx.render()