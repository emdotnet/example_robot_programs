# Generating Paths with Perlin noise and drawing them
The Perlin noise function is great at creating some cool looking noise patterns, so this project will be using that cool feature to generate paths. Which then will be given to the robot to draw. Since there are so many points being generated, the path blending process over works the computer and the motor drivers which end up exiting the program. So a divide and conquer solution was implemented, hence `divco()` function in the script. This solution brakes down the paths into smaller batches of paths and the computer blends a single batch at a time. This doesn't solve the issue, but it gives better control of avoiding the problem, meaning you can adjust the number of paths, path length, and batch size.
The most consistent "divide and conquer" configuration was,  
```
MAX_PATH_LENGTH = 100   # Maximum number of points in each path
NUM_BATCH_LENGTH = 5    # Maximum number of paths in each batch
```
 After Every batch there is a wait period, meaning the next batch is getting processed. When the robot is done drawing, the "CYCLE START" button indicator will stop showing green.

To influence how the paths look you will have to play around with the `noise_z_frame`, `curve_factor`, `rnd` variables in the `lightingMesh_preview.py` or `lightingMesh-ROBO_DIVCO.py` scripts. There are some experimental values that are commented out. You could try uncommenting them and see what results look like. 
#
### WARNING: If you are experimenting with new ways to generate paths I recommend do so in the `lightingMesh_preview.py` script.
#
Script files with `_ROBO_` are meant to control the robot
There are three script files:
* `lightningMesh_preview.py` --> You can run this file without the need for the robot. Its purpose is to help test, preview and generate paths that will be saved in a JSON file `./path/pathMap_extract.json` (this file will be overwritten, so if you plan on reusing the generated paths, change the JSON file name or change the file path in the script on the `SAVE_JSON_FILE_PATH` variable)
* `lightningMesh_ROBO_JSON.py` --> This will make the robot draw paths from a given JSON file (default: `./path/pathMap_extract.json`)
* `lightningMesh_ROBO_DIVCO.py` This script does both generating paths and making the robot draw them. You won't be able to preview the generated paths until the robot is done drawing them.

To get started with this project we will need to install the perlin-noise and pygam packages. This is mainly for the preview script. 
Before we install any packages we need to set up a virtual environment for this project.
For those new to this, a virtual environment/venv helps isolate our project packages/dependencies from the rest of the system (The last thing we need is to install a package that will break other packages that are not related to this project).
#
## Creating a virtual environment
### macOS/Linux
#### You may need to run `sudo apt-get install python3-venv` first on Debian-based OSs
Command: `python3 -m venv .venv`

### Windows
Command: `python -m venv .venv`

You can also use `py -3 -m venv .venv`

The commands above will create a virtual environment in a folder called ".venv", you can name it whatever you.

## Activating the virtual environment:
### Widows
Command: `.env\Scripts\activate.bat`
### Linux
Command: `source .env/bin/activate`

## Deactivating virtual environment
Command: `deactivate`

## Installing packages in a virtual environment
### Linux
Command: `python3 -m pip install package-name`
### Windows
Command: `python -m pip install package-name` 
OR
Command: `py -m pip install package-name`

```
# Perlin noise installation
(windows): python -m pip install perlin-noise
OR
(linux): python3 -m pip install perlin-noise

# pygam installation
(windows): python -m pip install pygam
OR
(linux): python3 -m pip install pygam

```
#
## Learn about venv:
* [Using Python environments in VS Code](https://code.visualstudio.com/docs/python/environments)

* [Virtual Environments and Packages](https://docs.python.org/3/tutorial/venv.html)

* [Installing packages using pip and virtual environments](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)


## Learn more about the Tormach Robot Programming Language (TRPL):
https://tormach.atlassian.net/wiki/spaces/ROBO/pages/1930690719/Tormach+Robot+Programming+Language


