'''
Example 8: Pause example
'''
from robot_command.rpl import *
set_units("mm", "deg")  # set units
# A function to move in a rectangular formation
def draw_rect(x=0, y=0, w=100, h=100):
    movej(p[x,y,0,0,0,0])
    movel(p[x+w,0,0,0,0,0])
    movel(p[x+w,y+h,0,0,0,0])
    movel(p[x,y+h,0,0,0,0])

def setup_test_user_and_tool_frame():
    # Creating a user frame just above the table to make sure the robot accidentally run in to it.
    set_user_frame("test_user_frame1", position=p[400, -200, 550, 0, 0, 0])
    change_user_frame("test_user_frame1")
    # Creating a tool frame to make sure the z-axis is oriented correctly
    set_tool_frame("test_tool_frame1", orientation=p[0, 0, 0, 180, 0, 0])
    change_tool_frame("test_tool_frame1")

def main():
    setup_test_user_and_tool_frame()
    '''
    pause() is different from sleep() function in that it requires user input from the system UI to resume the program.
    Also you can make a pause optional by setting the "optional" parameter to true (pause(optional=True)).
    Optional pauses will be skipped unless you activate them by clicking "OPTIONAL PAUSE" button in the system UI.
    '''
    notify("This program demonstrates the pause() command.  It draws one rectangle, then pauses, waiting for cycle start to resume.", warning=True)
    draw_rect()
    notify("The program is now paused, click \"CYCLE START\" to resume")
    pause()  # Once the program reaches this point it will be paused till you click "CYCLE START" again to resume the program
    draw_rect()  # Draw a rectangle
    notify("The robot will draw two more rectangles, with an optional pause in between.  If \"OPTIONAL PAUSE\" is enabled the program will pause, otherwise it will draw both rectangles immediately.", warning=True)
    draw_rect()  # Draw a rectangle
    pause(optional=True)    # This pause will be skipped (activate it by clicking "OPTIONAL PAUSE" in the system UI)
    draw_rect()  # Draw a rectangle
    exit()  # Exit main loop