from info.info import *
from simulation.sim import get_info


def status():
    target_range = get_info(target_range_state)
    x_range = get_info(x_range_state)
    y_range = get_info(y_range_state)
    z_range = get_info(z_range_state)
    roll_error = get_info(roll_error_state)
    roll_rate = get_info(roll_rate_state)
    pitch_error = get_info(pitch_error_state)
    pitch_rate = get_info(pitch_rate_state)
    yaw_error = get_info(yaw_error_state)
    yaw_rate = get_info(yaw_rate_state)

    status_message = f"Target Range: {target_range} \n X Range: {x_range} \n Y Range: {y_range} \n Z Range: {z_range} \n Roll Error: {roll_error} \n Roll Rate: {roll_rate} \n Pitch Error: {pitch_error} \n Pitch Rate: {pitch_rate} \n Yaw Error: {yaw_error} \n Yaw Rate: {yaw_rate} \n"

    print(status_message)
