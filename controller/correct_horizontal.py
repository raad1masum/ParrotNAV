import matplotlib.pyplot as plt
import random
from datetime import datetime

from simulation.sim import *
from states.states import *
from controls import controls

# set constants & gains
kp = 2.1
setpoint = 0.0

# data for plotting
horizontal_data = []

# set current date & time
current_datetime = datetime.now()

# translate left
def translate_left(correction_rate):
    for i in range(correction_rate):
        control(controls.translate_left)
        horizontal_data.append(float(get_info(y_range_state).rstrip(' m')))
    for i in range(correction_rate):
        control(controls.translate_right)
        horizontal_data.append(float(get_info(y_range_state).rstrip(' m')))

# translate right
def translate_right(correction_rate):
    for i in range(correction_rate):
        control(controls.translate_right)
        horizontal_data.append(float(get_info(y_range_state).rstrip(' m')))
    for i in range(correction_rate):
        control(controls.translate_left)
        horizontal_data.append(float(get_info(y_range_state).rstrip(' m')))

# single incrementation
def increment_single():
    if float(get_info(y_range_state).rstrip(' m')) < setpoint:
        control(controls.translate_right)
        control(controls.translate_left)
        horizontal_data.append(float(get_info(y_range_state).rstrip(' m')))
    if float(get_info(y_range_state).rstrip(' m')) > setpoint:
        control(controls.translate_left)
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
    plt.plot(horizontal_data, color='y')
    plt.style.use('seaborn-bright')
    plt.axhline(linewidth=4, color='b')
    plt.xlabel('Time (seconds)', fontsize=16)
    plt.ylabel('Error (°)', fontsize=16)
    plt.grid()
    plt.savefig(f'data/all/data_{current_datetime.strftime("%d-%m-%Y_%H:%M:%S")}.png')

# run correction loop
def run():
    while int(abs(kp * float(get_info(y_range_state).rstrip(' m')))) != setpoint:
        if float(get_info(y_range_state).rstrip(' m')) < setpoint:
            translate_right(int(abs(kp * float(get_info(y_range_state).rstrip(' m')))))
        if float(get_info(y_range_state).rstrip(' m')) > setpoint:
            translate_left(int(abs(kp * float(get_info(y_range_state).rstrip(' m')))))