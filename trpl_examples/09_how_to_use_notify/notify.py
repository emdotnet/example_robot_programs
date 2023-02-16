'''
Example 9: notify()
In this example we will be learning about notify(), a notification function that displays a popup window in the robot UI software.
notify(message, warning, error, image_path, timeout):
-message: Message text to display in the popup.
-warning: Set to true if this message is a warning.
-error: Set to true if this message is an error message.
-image_path: Optional path to an image file to displayed in the popup.
-timeout: Optional timeout in seconds.
'''

from robot_command.rpl import *
import math 

set_units("mm", "deg")

'''
We can use notify() outside the main loop or inside, but be care full when using notify inside the main loop.
Remember the main function runs in a loop, so if we run notify() in the main loop without away to stop the notifications or program we might end up with lots of popup messages.
There are ways to stop this from happening.
1) Using conditions: Putting notify() in an "if" condition so that it only happens when a specific event occurs.
2) Specifying notify() type (warning/error): This will pause the program and wait for user input e.g "OK" to continue or "ABORT" to exit program
3) Exit(): This function will stop/exit the program after the main loop has ran once. 
'''
notify("This message is neither a Warning nor an Error type, so the program is still running in the background")

# main runs in a loop
def main():
    notify("This notification has an image attached click OK to continue", image_path="./roboarm(1).png")

    '''
    We can also attach variable data onto the message,
    but remember if the variable data is not a string
    convert it into a string by using python str() function
    '''
    infor = {
     "Notification number": 23,
     "warning": "Yes"
    }
    # Warning type messages pause the program and wait for user input
    notify("Hello World, This is a warning message click OK to continue with the program or ABORT to exit the program: " + str(infor), warning=True)

    # Error type messages pause the program and have ABORT as the only input option
    msg = "Hello World, This is an Error message click ABORT to exit"
    notify(message=msg, error=True)

    exit()  # exit main loop