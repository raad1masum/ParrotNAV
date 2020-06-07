import matplotlib.pyplot as plt
import numpy as np
import random
from datetime import datetime

from simulation.sim import *
from states.states import *
from controls import controls

kp = 1
target = 0.0

yaw_data = []

current_datetime = datetime.now()

def yaw_left(correction_rate):
    for i in range(correction_rate):
        control(controls.yaw_left)
        yaw_data.append(float(get_info(yaw_error_state).rstrip('°')))
    for i in range(correction_rate):
        control(controls.yaw_right)
        yaw_data.append(float(get_info(yaw_error_state).rstrip('°')))

def yaw_right(correction_rate):
    for i in range(correction_rate):
        control(controls.yaw_right)
        yaw_data.append(float(get_info(yaw_error_state).rstrip('°')))
    for i in range(correction_rate):
        control(controls.yaw_left)
        yaw_data.append(float(get_info(yaw_error_state).rstrip('°')))

def increment_single():
    if float(get_info(yaw_error_state).rstrip('°')) < target:
        control(controls.yaw_left)
        control(controls.yaw_right)
        yaw_data.append(float(get_info(yaw_error_state).rstrip('°')))
    if float(get_info(yaw_error_state).rstrip('°')) > target:
        control(controls.yaw_right)
        control(controls.yaw_left)
        yaw_data.append(float(get_info(yaw_error_state).rstrip('°')))

def is_correct():
    if abs(kp * float(get_info(yaw_error_state).rstrip('°'))) == target:
        return True
    else:
        return False

def get_yaw_error():
    return abs(kp * float(get_info(yaw_error_state).rstrip('°')))

def plot_data():
    plt.plot(yaw_data, color='r')
    plt.style.use('seaborn-bright')
    plt.axhline(linewidth=4, color='b')
    plt.xlabel('Time (seconds)', fontsize=16)
    plt.ylabel('Error (°)', fontsize=16)
    plt.grid()
    plt.savefig(f'data/yaw/yaw_data_{current_datetime.strftime("%d-%m-%Y_%H:%M:%S")}.png')

def run():
    while int(abs(kp * float(get_info(yaw_error_state).rstrip('°')))) != target:
        if float(get_info(yaw_error_state).rstrip('°')) < target:
            yaw_left(int(abs(kp * float(get_info(yaw_error_state).rstrip('°')))))
        if float(get_info(yaw_error_state).rstrip('°')) > target:
            yaw_right(int(abs(kp * float(get_info(yaw_error_state).rstrip('°')))))