import threading

from simulation import sim
from simulation.sim import *
from controls import controls
from states.states import *
from states.status import status

# control(controls.pitch_up)

while True:
    if float(get_info(yaw_error_state).rstrip('°')) < 0.0 and abs(float(get_info(yaw_rate_state).rstrip('°/s'))) < 0.5:
        control(controls.yaw_left)
        # print(float(get_info(yaw_error_state).rstrip('°')))
        print(abs(float(get_info(yaw_rate_state).rstrip('°/s'))))

    if float(get_info(yaw_error_state).rstrip('°')) > 0.0 and abs(float(get_info(yaw_rate_state).rstrip('°/s'))) <= 0.5:
        control(controls.yaw_right)
        # print(float(get_info(yaw_error_state).rstrip('°')))
        print(abs(float(get_info(yaw_rate_state).rstrip('°/s'))))
    