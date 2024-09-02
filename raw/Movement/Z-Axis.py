from codrone_edu.drone import *
import time

drone = Drone()


def fly_2_z(height, power):
    HT = drone.get_pos_z()
    print('  ', HT, 'to', height)

    if HT < height:
        drone.set_throttle(power)
        while HT < height:
            drone.move(.075)
            print('up')
            print(str(HT)+"target height"+str(height))
            HT = drone.get_pos_z()
    else:
        drone.set_throttle(-1*power)
        while HT > height:
            drone.move(.075)
            print("Down")
            print(str(HT) + "target height" + str(height))
            HT = drone.get_pos_z()

    print("  Reached Target Height & hover at ",HT)
