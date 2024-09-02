from codrone_edu.drone import *
import time

drone = Drone()

def identify_color_mat():
    print('Identifying Color Mat...')
    colorsensor = drone.get_color_data()
    while drone.get_color_data() == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]:
        colorsensor = drone.get_color_data()
    colors = {
        "Red": (255, 0, 0, 255),
        "Green": (0, 255, 0, 255),
        "Blue": (0, 0, 255, 255),
        "Black": (0,0,255,255)
    }
    for i in range(10):
        drone.set_drone_LED(*colors[colorsensor[9].name])
    time.sleep(0.5)