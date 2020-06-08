import matplotlib.pyplot as plt
import random
from time import sleep
from datetime import datetime

from PID.pid_controller import *
from simulation.sim import *
from states.states import *
from controls import controls

# set constants & gains
kp = range_kp
setpoint = range_setpoint
delay = 1

# data for plotting
range_data = []

# set current date & time
current_datetime = datetime.now()

# translate forward
def translate_forward(correction_rate):
    for i in range(correction_rate):
        control(controls.translate_forward)
        range_data.append(float(get_info(x_range_state).rstrip(' m')))
    sleep(delay)
    for i in range(correction_rate):
        control(controls.translate_backward)
        range_data.append(float(get_info(x_range_state).rstrip(' m')))

# translate backward
def translate_backward(correction_rate):
    for i in range(correction_rate):
        control(controls.translate_backward)
        range_data.append(float(get_info(x_range_state).rstrip(' m')))
    sleep(delay)
    for i in range(correction_rate):
        control(controls.translate_forward)
        range_data.append(float(get_info(x_range_state).rstrip(' m')))

# single incrementation
def increment_single():
    if float(get_info(x_range_state).rstrip(' m')) < setpoint:
        control(controls.translate_forward)
        sleep(delay)
        control(controls.translate_backward)
        range_data.append(float(get_info(x_range_state).rstrip(' m')))
    if float(get_info(x_range_state).rstrip(' m')) > setpoint:
        control(controls.translate_backward)
        sleep(delay)
        control(controls.translate_forward)
        range_data.append(float(get_info(x_range_state).rstrip(' m')))

# return if on setpoint
def is_correct():
    if abs(kp * float(get_info(x_range_state).rstrip(' m'))) == setpoint:
        return True
    else:
        return False

# return error
def get_range_error():
    return abs(kp * float(get_info(x_range_state).rstrip(' m')))

# plot data
def plot_data():
    plt.plot(range_data, color='b', label="range")
    plt.style.use('seaborn-bright')
    plt.title('Vehicle Error in Degrees Over Time in Seconds', fontsize=14)
    plt.legend(loc='upper right')
    plt.axhline(linewidth=4, color='b')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Error (°)')
    plt.grid()
    plt.savefig(f'data/plots/data_{current_datetime.strftime("%d-%m-%Y_%H:%M:%S")}.png')

# run correction loop
def run():
    while int(abs(kp * float(get_info(x_range_state).rstrip(' m')))) != setpoint:
        if float(get_info(x_range_state).rstrip(' m')) < setpoint:
            translate_forward(int(abs(kp * float(get_info(x_range_state).rstrip(' m')))))
        if float(get_info(x_range_state).rstrip(' m')) > setpoint:
            translate_backward(int(abs(kp * float(get_info(x_range_state).rstrip(' m')))))