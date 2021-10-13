

https://user-images.githubusercontent.com/5693518/135105777-0103dc42-a90a-4432-8062-2a771571c7a6.mp4


# Saving Probed Values to CSV File
This program contains an example of using the probel() command to probe a series of points (in this example it's the top of a machinist's vise).  From three points a new user frame/work offset is created.  Then all the values (three probed points + the new user frame) are appended to a CSV file.

This example is discussed on the Tormach user forums here: https://forums.tormach.com/t/example-program-probing-points-creating-a-new-user-frame-from-the-probed-points-and-saving-values-to-a-csv-file/49

## Prerequisites
A touch probe must be connected to the robot's tool flange for this example to work as written.  Make sure to test the polarity and function of the probe before running this code.

This program expects that you have created a user frame/work offset named "temp_offset".  It will probe three points, one directly below the XYZ origin of "temp_offset", one 50mm away in Y, and one 50mm away in X.
## Libraries Used
CSV (https://docs.python.org/3/library/csv.html)
