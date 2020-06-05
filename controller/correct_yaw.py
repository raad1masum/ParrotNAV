import matplotlib.pyplot as plt
import numpy as np
import random
from datetime import datetime

from simulation.sim import *
from states.states import *
from controls import controls

kp = 1

yaw_data = []

current_datetime = datetime.now()

def move_left(correction_rate):
    for i in range(correction_rate):
        control(controls.yaw_left)
        yaw_data.append(float(get_info(yaw_error_state).rstrip('°')))
    for i in range(correction_rate):
        control(controls.yaw_right)
        yaw_data.append(float(get_info(yaw_error_state).rstrip('°')))

def move_right(correction_rate):
    for i in range(correction_rate):
        control(controls.yaw_right)
        yaw_data.append(float(get_info(yaw_error_state).rstrip('°')))
    for i in range(correction_rate):
        control(controls.yaw_left)
        yaw_data.append(float(get_info(yaw_error_state).rstrip('°')))

def increment_single():
    if float(get_info(yaw_error_state).rstrip('°')) < 0.0:
        control(controls.yaw_left)
        control(controls.yaw_right)
    if float(get_info(yaw_error_state).rstrip('°')) > 0.0:
        control(controls.yaw_right)
        control(controls.yaw_left)

def is_correct():
    if int(abs(kp * float(get_info(yaw_error_state).rstrip('°')))) == 0.0:
        return True
    else:
        return False

while int(abs(kp * float(get_info(yaw_error_state).rstrip('°')))) != 0.0:
    if float(get_info(yaw_error_state).rstrip('°')) < 0.0:
        move_left(int(abs(kp * float(get_info(yaw_error_state).rstrip('°')))))
    if float(get_info(yaw_error_state).rstrip('°')) > 0.0:
        move_right(int(abs(kp * float(get_info(yaw_error_state).rstrip('°')))))

def plot_data():
    plt.plot(yaw_data, color='r')
    plt.style.use('seaborn-bright')
    plt.axhline(linewidth=4, color='b')
    plt.xlabel('Time (seconds)', fontsize=16)
    plt.ylabel('Error (°)', fontsize=16)
    plt.grid()
    plt.savefig(f'data/yaw/yaw_data_{current_datetime.strftime("%d-%m-%Y_%H:%M:%S")}.png')
