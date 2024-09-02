# This script helps determine a drone's drift during takeoff and movement
# DO NOT RUN THIS SCRIPT WITHOUT READING THROUGH THE ENTIRE THING

# 1. Place the drone on a flat surface
# 2. Run the script and observe the drone's takeoff and landing positions.
# 3. Adjust the trim values and repeat steps 1 and 2 until the drone's landing and takeoff positions are consistent.
#    Record the trim values for your autonomous flight script.
#    Note:
#    - If the drone drifts to the right, set the roll trim to a negative value.
#    - If the drone drifts to the left, set the roll trim to a positive value.
#    - If the drone drifts forward, set the pitch trim to a negative value.
#    - If the drone drifts backward, set the pitch trim to a positive value.

from codrone_edu.drone import *
import time

roll_trim = 0
pitch_trim = 0

drone = Drone()

drone.pair()
drone.reset_sensor()
drone.set_trim(roll_trim, pitch_trim)
time.sleep(3) # Allow 3 seconds for the trim setting to take effect
drone.takeoff()

# The lines of code below are used to test for drift during movement
# COMMENT OUT THE LINE OF CODE THAT YOU ARE NOT USING IT

drone.sendControlWhile(0, 80, 0, 0, 2500) 
# - Place the drone facing forward with lots of clearance ahead
# - The drone will fly forward at 80% power for 2.5 seconds (3 meters)
# - If the drone drifts to the right, the roll trim should be negative; if it drifts to the left, the roll trim should be positive.
# - Adjust the trim values appropriately according to lines 9 - 12


# UNCOMMENT THE LINE BELOW TO TEST FOR SIDEWAYS DRIFT
drone.sendControlWhile(80, 0, 0, 0, 2500)
# - The drone will fly forward at 80% power for 2.5 seconds (3 meters)
# - Place the drone facing forward with lots of clearance ahead
# - Adjust the trim values appropriately according to lines 9 - 12
# - Note that the drone is facing peripindicular to its movement, adjust trim values appropriately

drone.land()
drone.close()
