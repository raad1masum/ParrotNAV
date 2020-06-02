import matplotlib.pyplot as plt
import numpy as np

from simulation import sim
from simulation.sim import *
from controls import controls
from states.states import *
from states.status import status

kp = 1.5

list = []


def move_left(correction_rate):
    list.append(correction_rate)
    print(correction_rate)
    if correction_rate == 0:
        control(controls.yaw_left)
        control(controls.yaw_right)
    else:
        for i in range(correction_rate):
            control(controls.yaw_left)
        for i in range(correction_rate):
            control(controls.yaw_right)
    print(list)


def move_right(correction_rate):
    list.append(correction_rate)
    print(correction_rate)
    if correction_rate == 0:
        control(controls.yaw_right)
        control(controls.yaw_left)
    else:
        for i in range(correction_rate):
            control(controls.yaw_right)
        for i in range(correction_rate):
            control(controls.yaw_left)
    print(list)


while True:
    if float(get_info(yaw_error_state).rstrip('°')) < 0.0:
        move_left(int(abs(kp * float(get_info(yaw_error_state).rstrip('°')))))
    if float(get_info(yaw_error_state).rstrip('°')) > 0.0:
        move_right(
            int(abs(kp * float(get_info(yaw_error_state).rstrip('°')))))
