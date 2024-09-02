from codrone_edu.drone import *
import time

drone = Drone()

def fly_2_y(max_time:10, x_pos,y_pos,z_pos,velocity,direction):
    print("------------Flying toward coordinate", x_pos, y_pos, z_pos,direction)
    time_sec = max_time
    time_start = time.perf_counter()

    while (time.perf_counter() - time_start) < time_sec:
        pos_data = drone.get_position_data()
        print(pos_data)
        if direction == "left":
            if pos_data[2] >= y_pos:
                break
        else:
            if pos_data[2] <= y_pos:
                break

        drone.send_absolute_position(x_pos, y_pos, z_pos,velocity, 0, 0)
        time.sleep(0.01)

    dur = time.perf_counter() - time_start
    print("*********Time spent:", dur)
