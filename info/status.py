import info
from simulation.sim import get_info


def status():
    target_range = get_info(info.target_range)
    x_range = get_info(info.x_range)
    y_range = get_info(info.y_range)
    z_range = get_info(info.z_range)
    roll_error = get_info(info.roll_error)
    roll_rate = get_info(info.roll_rate)
    pitch_error = get_info(info.pitch_error)
    pitch_rate = get_info(info.pitch_rate)
    yaw_error = get_info(info.yaw_error)
    yaw_rate = get_info(info.yaw_rate)

    status_message = f"Target Range: {target_range} \n X Range: {x_range} \n Y Range: {y_range} \n Z Range: {z_range} \n Roll Error: {roll_error} \n Roll Rate: {roll_rate} \n Pitch Error: {pitch_error} \n Pitch Rate: {pitch_rate} \n Yaw Error: {yaw_error} \n Yaw Rate: {yaw_rate} \n"

    return status_message