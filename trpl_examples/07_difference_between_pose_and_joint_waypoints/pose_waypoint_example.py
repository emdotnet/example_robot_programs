'''
Example 7: Pose()/p[]
This example will be showing how Pose() differs from Joints()/j[]
After reading this continue to the joint_waypoint_example.py in the current folder to see how Joints() differs from Pose()/p[]
'''
from robot_command.rpl import *

set_units("mm", "deg")  # set units

# A function to move in a rectangular formation, Using Pose() waypoints (p[x, y, z, a, b, c])
def draw_rect_with_pose_waypoints(x=0, y=0, w=100, h=100):
    movej(p[x,y,0,0,0,0])
    movel(p[x+w,0,0,0,0,0])
    movel(p[x+w,y+h,0,0,0,0])
    movel(p[x,y+h,0,0,0,0])
    movel(p[x,y,0,0,0,0])

#  main() runs in a loop
def main():
    notify("This example is one of two examples that will be demonstrating the difference between Joint()/j[] and Pose()/p[].\n\nThis example focuses on Pose()/p[]. With Pose() you control the positioning of the robot end effector using xyz coordinates and ABC rotations (A-rotation on x, B-on y, C-on z) relative to the robots origin(located at the base of the robot) or created user frame.\nThis program will create a user frame and then draw a rectangle. Then it will create another user frame similar to the last one but rotated 90 degrees and it will draw a rectangle.\nYou will notice that the robot will act differently on the last test because since we are changing user frames and we are using Pose()/p[] the robot end effector will move relative to the current user frame. This wont be the case if we used Joint()/j[].", warning=True)
    '''
    The main difference is that Pose() is affected by user frames and tool frames.
    And with Pose() you control the end effector in cartesian coordinates e.g p[x, y, z, a, b, c]/Pose(x=0, y=0, z=0, a=0, b=0, c=0)

    * A user frame is an offset space that the robot will perform tasks in.
    * The user frame will be offset relative to the origin point of the robot located at the base of the arm.

    This script will show how user frames affect the robot's movements.
    Below you will notice that we create two user frames, one is horizontal and the other is vertical.
    '''
    set_tool_frame("tool_frame1", orientation=p[0,0,0,180,0,0])  # Create a tool frame rotated 180 degrees on the x-axis (this will make sure the end effector movements are not flipped)
    change_tool_frame("tool_frame1")  # Use the created tool frame

    # Horizontal user frame
    set_user_frame("home_frame1", position=p[400,-200,550,0,0,0])  # Create first  user frame (this user frame is created just above Joint 2 of the robot)
    change_user_frame("home_frame1")  # Use the created user frame
    notify("Horizontal user frame is active")
    draw_rect_with_pose_waypoints()  # draw a rectangle

    # Vertical user frame
    set_user_frame("home_frame2", position=p[400,-200,550,0,0,0], orientation=p[0,0,0,90,0,0])  # Create second user frame
    change_user_frame("home_frame2")
    notify("Vertical user frame is active")
    draw_rect_with_pose_waypoints()  # draw a rectangle

    exit()  # exit main loop
