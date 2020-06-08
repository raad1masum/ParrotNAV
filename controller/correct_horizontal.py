import matplotlib.pyplot as plt
import random
from time import sleep
from datetime import datetime

from PID.pid_controller import *
from simulation.sim import *
from states.states import *
from controls import controls

# set constants & gains
kp = horizontal_kp
setpoint = horizontal_setpoint

# data for plotting
horizontal_data = []

# set current date & time
current_datetime = datetime.now()

# translate left
def translate_left(correction_rate):
    for i in range(correction_rate):
        control(controls.translate_left)
        horizontal_data.append(float(get_info(y_range_state).rstrip(' m')))
        sleep(2)
    for i in range(correction_rate):
        control(controls.translate_right)
        horizontal_data.append(float(get_info(y_range_state).rstrip(' m')))

# translate right
def translate_right(correction_rate):
    for i in range(correction_rate):
        control(controls.translate_right)
        horizontal_data.append(float(get_info(y_range_state).rstrip(' m')))
        sleep(2)
    for i in range(correction_rate):
        control(controls.translate_left)
        horizontal_data.append(float(get_info(y_range_state).rstrip(' m')))

# single incrementation
def increment_single():
    if float(get_info(y_range_state).rstrip(' m')) < setpoint:
        control(controls.translate_right)
        sleep(2)
        control(controls.translate_left)
        horizontal_data.append(float(get_info(y_range_state).rstrip(' m')))
    if float(get_info(y_range_state).rstrip(' m')) > setpoint:
        control(controls.translate_left)
        sleep(2)
        control(controls.translate_right)
        horizontal_data.append(float(get_info(y_range_state).rstrip(' m')))

# return if on setpoint
def is_correct():
    if abs(kp * float(get_info(y_range_state).rstrip(' m'))) == setpoint:
        return True
    else:
        return False

# return error
def get_horizontal_error():
    return abs(kp * float(get_info(y_range_state).rstrip(' m')))

# plot data
def plot_data():
    plt.plot(horizontal_data, color='m', label="horizontal")
    plt.style.use('seaborn-bright')
    plt.axhline(linewidth=4, color='b')
    plt.legend(loc="upper right")
    plt.xlabel('Time (seconds)', fontsize=16)
    plt.ylabel('Error (°)', fontsize=16)
    plt.grid()
    plt.savefig(f'data/plots/data_{current_datetime.strftime("%d-%m-%Y_%H:%M:%S")}.png')

# run correction loop
def run():
    while int(abs(kp * float(get_info(y_range_state).rstrip(' m')))) != setpoint:
        if float(get_info(y_range_state).rstrip(' m')) < setpoint:
            translate_right(int(abs(kp * float(get_info(y_range_state).rstrip(' m')))))
        if float(get_info(y_range_state).rstrip(' m')) > setpoint:
            translate_left(int(abs(kp * float(get_info(y_range_state).rstrip(' m')))))