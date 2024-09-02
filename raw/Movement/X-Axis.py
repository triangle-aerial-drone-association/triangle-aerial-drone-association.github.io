from codrone_edu.drone import *
import time

drone = Drone()

def fly_2_x(max_time:10, x_ini,x_dst, y_pos,z_pos,velocity,direction):
    print("------------Flying toward coordinates with incremental instruction",x_ini,x_dst,y_pos,z_pos,direction)
    time_sec = max_time
    time_start = time.perf_counter()
    x_target = x_ini

    while (time.perf_counter() - time_start) < time_sec:
        pos_data = drone.get_position_data()
        print(pos_data)
        if direction == "forward":
            # move 1/20 of the flying speed each time
            x_target = x_target + velocity*0.05
            if pos_data[1] >= x_dst:
                break
        else:
            # move 1/20 of the flying speed each time
            x_target = x_target - velocity*0.05
            if pos_data[1] <= x_dst:
                break
        drone.send_absolute_position(x_target, y_pos, z_pos,velocity, 0, 0)
        time.sleep(0.01)

    dur = time.perf_counter() - time_start
    print("*********Time spent:", dur)
