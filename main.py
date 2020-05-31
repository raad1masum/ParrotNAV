from simulation import sim
from simulation.sim import *
from controls import controls
from states.states import *
from states.status import status


kp = 1.5

def move_left(correction_rate):
    print(correction_rate)
    for i in range(correction_rate):
        control(controls.yaw_left)
    for i in range(correction_rate):
        control(controls.yaw_right)


def move_right(correction_rate):
    print(correction_rate)
    for i in range(correction_rate):
        control(controls.yaw_right)
    for i in range(correction_rate):
        control(controls.yaw_left)


while True:
    while float(get_info(yaw_error_state).rstrip('°')) != 0.0:
        if float(get_info(yaw_error_state).rstrip('°')) < 0.0:
            move_left(int(abs(kp * float(get_info(yaw_error_state).rstrip('°')))))
        if float(get_info(yaw_error_state).rstrip('°')) > 0.0:
            move_right(int(abs(kp * float(get_info(yaw_error_state).rstrip('°')))))
