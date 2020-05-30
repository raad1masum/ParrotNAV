import threading

from simulation import sim
from simulation.sim import *
from controls import controls
from states.states import *
from states.status import status

def move_left():
    for i in range(3): 
        control(controls.yaw_left)
    for i in range(3): 
        control(controls.yaw_right)


def move_right():
    for i in range(3): 
        control(controls.yaw_right)
    for i in range(3): 
        control(controls.yaw_left)

while True:
    while float(get_info(yaw_error_state).rstrip('°')) != 0.0:
        if float(get_info(yaw_error_state).rstrip('°')) < 0.0:
            move_left()
        if float(get_info(yaw_error_state).rstrip('°')) > 0.0:
            move_right()
