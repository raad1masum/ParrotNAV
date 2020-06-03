import matplotlib.pyplot as plt
import numpy as np
import random
from datetime import datetime

from simulation.sim import control
from controls import controls
from states.states import *
from states.status import status

kp = 1

list = []

current_datetime = datetime.now()

def move_left(correction_rate):
    for i in range(correction_rate):
        control(controls.yaw_left)
        list.append(float(get_info(yaw_error_state).rstrip('°')))
    for i in range(correction_rate):
        control(controls.yaw_right)
        list.append(float(get_info(yaw_error_state).rstrip('°')))
    print(list)


def move_right(correction_rate):
    for i in range(correction_rate):
        control(controls.yaw_right)
        list.append(float(get_info(yaw_error_state).rstrip('°')))
    for i in range(correction_rate):
        control(controls.yaw_left)
        list.append(float(get_info(yaw_error_state).rstrip('°')))
    print(list)

while int(abs(kp * float(get_info(yaw_error_state).rstrip('°')))) != 0.0:
    if float(get_info(yaw_error_state).rstrip('°')) < 0.0:
        move_left(int(abs(kp * float(get_info(yaw_error_state).rstrip('°')))))
    if float(get_info(yaw_error_state).rstrip('°')) > 0.0:
        move_right(int(abs(kp * float(get_info(yaw_error_state).rstrip('°')))))

plt.plot(list, color='r')
plt.style.use('seaborn-bright')
plt.axhline(linewidth=4, color='b')
plt.xlabel('Time (seconds)', fontsize=16)
plt.ylabel('Error (degrees)', fontsize=16)
plt.grid()
plt.savefig(f'data/yaw/yaw_data_{current_datetime.strftime("%d-%m-%Y_%H:%M:%S")}.png')
