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

columns_count = 7
lines_count = 5

counter = [1,2,3,4,5,6,7]

# settings
borders_horizontal = True
borders_vertical = True

field_names = [["A1", "A2", "A3", "A4", "A5", "A6", "A7"],
               ["B1", "B", "B3", "B4", "B5", "B6", "B7"],
               ["C1", "C2", "C3", "C4", "C5", "C6", "C7"],
               ["D1", "D2", "D3", "D4", "D5", "D6", "D7"],
               ["E1", "E2", "E3", "E4", "E5", "E6", "E7"],
               ["F1", "F2", "F3", "F4", "F5", "F6", "F7"],
               ["G1", "G2", "G3", "G4", "G5", "G6", "G7"],
               ["H1", "H2", "H3", "H4", "H5", "H6", "H7"]]


# start the main loop
while not ctx.should_close():
    # create a new frame
    ctx.new_frame()

    # setup first win pos and win size
    bimpy.set_next_window_pos(bimpy.Vec2(20, 20), bimpy.Condition.Once)
    bimpy.set_next_window_size(bimpy.Vec2(winWidth - 520, winHeight-40), bimpy.Condition.Once)

    # begin the window
    bimpy.begin("Chess View", flags=bimpy.NoMove | bimpy.NoCollapse) # add more flags like this: | bimpy.NoResize | bimpy.NoTitleBar
    bimpy.columns(columns_count, None, borders_vertical)
    for x in counter:
        counter += 1
        if borders_horizontal and bimpy.get_column_index == 0:
            bimpy.separator()
        bimpy.text("{}".format("a"))
        bimpy.next_column()
    bimpy.columns(1)
    if borders_horizontal:
        bimpy.separator()

    # end the window
    bimpy.end()

    # setup the 2nd window
    bimpy.set_next_window_pos(bimpy.Vec2(800, 20), bimpy.Condition.Once)
    bimpy.set_next_window_size(bimpy.Vec2(winWidth - 820, winHeight-300), bimpy.Condition.Once)
    bimpy.begin("Control Board", flags=bimpy.NoMove | bimpy.NoCollapse)
    bimpy.text("re")
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