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