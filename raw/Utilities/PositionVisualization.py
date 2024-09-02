# This script tracks and visualizes the drone's position over time using 2D and 3D plots while flying
import math
from time import sleep
import time
import threading
from codrone_edu.drone import *
from codrone_edu.protocol import *

# This is an external library for plotting, use "pip install matplotlib" in your terminal to install it
import matplotlib.pyplot as plt

# Initialize trim values
roll_trim = 0
pitch_trim = 0

# Create a Drone object
drone = Drone()
drone.open()
drone.pair()
drone.reset_sensor()
drone.set_trim(roll_trim, pitch_trim)

# Allow 3 seconds for the trim setting to take effect
time.sleep(3)

# Lists to use for graphing data
t_list = []
x_list = []
y_list = []

# Determining the initial time value
t_init = time.time()
t_now = 0
capture_data_flag = True

# Function to capture data
def capture_data():
    global t_now, capture_data_flag
    while capture_data_flag:
        t_now = time.time() - t_init
        x = drone.get_pos_x()
        y = drone.get_pos_y()
        print(x, ",", y, ",", t_now)
        x_list.append(x)
        y_list.append(y)
        t_list.append(t_now)
        time.sleep(0.01)  

drone.takeoff()

# Starts data capture parallel to drone movement
data_capture_thread = threading.Thread(target=capture_data)
data_capture_thread.start()


# PUT YOUR COMMANDS HERE BELOW THIS LINE
drone.send_absolute_position(0.4, 0, 0.7, 0.5, 0, 180)
# DO NOT PUT CODE BEYOND THIS LINE


# Land the drone and stop data capture
print("landing")
drone.land()
drone.emergency_stop()
capture_data_flag = False  # Stop the data capture

data_capture_thread.join()  # Synthesizing Data

# Setting up the 2D graph
plt.xlim(-50, 50)  # Set x-axis limits
plt.ylim(-50, 50)  # Set y-axis limits
plt.plot(x_list, y_list, 'go')  # Plot x and y data points
plt.ylabel('x (cm)')  # Label for y-axis
plt.xlabel('y (cm)')  # Label for x-axis
plt.show()  # Display the 2D plot

# Setting up the 3D graph
fig = plt.figure()  
axis = plt.axes(projection='3d')  
plt.xlim(-50, 50)  # Set x-axis limits for the 3D plot
plt.ylim(-50, 50)  # Set y-axis limits for the 3D plot

# Scatter plot for 3D data, coloring points based on their t value
axis.scatter3D(x_list, y_list, t_list, c=t_list, cmap='viridis')
plt.show()  # Display the 3D plot

time.sleep(1)
drone.close()
