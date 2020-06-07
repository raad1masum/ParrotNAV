import matplotlib.pyplot as plt
import random
from datetime import datetime

from PID.pid_controller import *
from simulation.sim import *
from states.states import *
from controls import controls

# set constants & gains
kp = yaw_kp
setpoint = yaw_setpoint

# data for plotting
yaw_data = []

# set current date & time
current_datetime = datetime.now()

# yaw left
def yaw_left(correction_rate):
    for i in range(correction_rate):
        control(controls.yaw_left)
        yaw_data.append(float(get_info(yaw_error_state).rstrip('°')))
    for i in range(correction_rate):
        control(controls.yaw_right)
        yaw_data.append(float(get_info(yaw_error_state).rstrip('°')))

# yaw right
def yaw_right(correction_rate):
    for i in range(correction_rate):
        control(controls.yaw_right)
        yaw_data.append(float(get_info(yaw_error_state).rstrip('°')))
    for i in range(correction_rate):
        control(controls.yaw_left)
        yaw_data.append(float(get_info(yaw_error_state).rstrip('°')))

# single incrementation
def increment_single():
    if float(get_info(yaw_error_state).rstrip('°')) < setpoint:
        control(controls.yaw_left)
        control(controls.yaw_right)
        yaw_data.append(float(get_info(yaw_error_state).rstrip('°')))
    if float(get_info(yaw_error_state).rstrip('°')) > setpoint:
        control(controls.yaw_right)
        control(controls.yaw_left)
        yaw_data.append(float(get_info(yaw_error_state).rstrip('°')))

# return if on setpoint
def is_correct():
    if abs(kp * float(get_info(yaw_error_state).rstrip('°'))) == setpoint:
        return True
    else:
        return False

# return error
def get_yaw_error():
    return abs(kp * float(get_info(yaw_error_state).rstrip('°')))

# plot data
def plot_data():
    plt.plot(yaw_data, color='r')
    plt.style.use('seaborn-bright')
    plt.axhline(linewidth=4, color='b')
    plt.xlabel('Time (seconds)', fontsize=16)
    plt.ylabel('Error (°)', fontsize=16)
    plt.grid()
    plt.savefig(f'data/plots/data_{current_datetime.strftime("%d-%m-%Y_%H:%M:%S")}.png')

# run correction loop
def run():
    while int(abs(kp * float(get_info(yaw_error_state).rstrip('°')))) != setpoint:
        if float(get_info(yaw_error_state).rstrip('°')) < setpoint:
            yaw_left(int(abs(kp * float(get_info(yaw_error_state).rstrip('°')))))
        if float(get_info(yaw_error_state).rstrip('°')) > setpoint:
            yaw_right(int(abs(kp * float(get_info(yaw_error_state).rstrip('°')))))