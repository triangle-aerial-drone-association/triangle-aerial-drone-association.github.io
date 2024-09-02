from codrone_edu.drone import *
import time

# Trim Values
roll_trim = 0
pitch_trim = 0

drone = Drone()

# Pre-flight preparation function
def pre_flight_preparation(roll_trim, pitch_trim):
    print('Pre Flight Preparation...')
    drone.reset_sensor()
    drone.reset_move()
    drone.set_trim(roll_trim, pitch_trim)
    drone.set_initial_pressure()
    time.sleep(3) # Give 3 sec for the above action to finish
    battery_level = drone.get_battery()
    if battery_level < 90: 
        print('Need a freshly charged battery')
        exit(10) # Closes out the program with an error code
