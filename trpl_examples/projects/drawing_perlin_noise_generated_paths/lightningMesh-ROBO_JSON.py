import json
from robot_command.rpl import *

SAFE_HEIGHT = 50
NUM_BATCH_LENGTH = 5  # Maximum number of paths in each batch
JSON_FILE_PATH = "paths/pathsMap_extract_cat.json"

def get_existing_JSON():
    notify("Getting paths from JSON")
    with open(JSON_FILE_PATH, "r") as openFile:
        json_data = json.load(openFile)
    return json_data["paths"]

# divco() will divide a list into batches (divide and conquer)
def divco(list):
    if len(list) <= NUM_BATCH_LENGTH:
        return [list]
    else:
        mid = len(list) // 2
        left = list[:mid]
        right = list[mid:]
        return divco(left) + divco(right)


all_paths = get_existing_JSON()


def init_setup():
    notify("Setting frames")
    change_tool_frame("tool_frame1")
    change_user_frame("sadiq_1")
    movej(p[0,0,SAFE_HEIGHT,0,0,0])


def start(_paths):
    if not _paths:
        notify("No c_paths")
        exit()
    x = 0
    y = 0
    set_path_blending(True, 0)
    for c_path in _paths:  # For every path  in c_paths[] list
        if not c_path:
            notify("No c_path")
            exit()
        for point in c_path:
            x = point[0]
            y = point[1]
            movel(p[x, y, 0, 0, 0, 0])
        movel(p[x, y, SAFE_HEIGHT, 0, 0, 0])

    sync()
    set_path_blending(False)
    set_path_blending(False)

def blend_n_run(batches):
    for batch in batches:
        start(batch)
    # When done, move to home
    movej(p[0,0, SAFE_HEIGHT, 0, 0, 0])

def main():
    init_setup()
    blend_n_run(divco(all_paths))
    exit()
