'''
Example 11: Using get_pose()
get_pose() returns the current robot pose: Pose(x, y, z, a, b, c).
get_pose(apply_user_frame=True, apply_tool_frame=True):
* apply_user_frame [default True]: Applies the active user frame to the world pose.
* apply_tool_frame [default True]: Applies the active tool frame to the world pose.

'''

from robot_command.rpl import *

set_units("mm", "deg")

def setup_test_user_and_tool_frame():
    # Creating a user frame just above the table to make sure the robot accidentally run in to it.
    set_user_frame("test_user_frame1", position=p[400, -200, 550, 0, 0, 0])
    change_user_frame("test_user_frame1")
    # Creating a tool frame to make sure the z-axis is oriented correctly
    set_tool_frame("test_tool_frame1", orientation=p[0, 0, 0, 180, 0, 0])
    change_tool_frame("test_tool_frame1")


def main():
    setup_test_user_and_tool_frame()
    notify("Using get_pose(), we will get the current Pose of the robot and save it in a variable \"startPose\". Then loop from 0 to 10 and come up with a y-offset and move back and forth from startPose to a new pose with a new y-offset.", warning=True)
    
    movej(Pose(z=-50))  # Move 50mm above current user frame origin

    startPose = get_pose()  # Get current pose and save in "startPose" to be used latter
    for i in range(10):
        xOff = 50  # x offset
        yOff = i * 20  # y offset, changes over time by multiplying 20 to the current index "i" (0...10)
        movej(Pose(x=startPose.x + xOff, y=startPose.y + yOff))  # Move to new point, which is calculated by adding an offset to the startPose
        movej(startPose)  # Go back to start pose
    exit()
