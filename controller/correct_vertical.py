import matplotlib.pyplot as plt
import random
from time import sleep
from datetime import datetime

from PID.pid_controller import *
from simulation.sim import *
from states.states import *
from controls import controls

# set constants & gains
kp = vertical_kp
setpoint = vertical_setpoint

# data for plotting
vertical_data = []

# set current date & time
current_datetime = datetime.now()

# translate up
def translate_up(correction_rate):
    for i in range(correction_rate):
        control(controls.translate_up)
        vertical_data.append(float(get_info(z_range_state).rstrip(' m')))
        sleep(1)
    for i in range(correction_rate):
        control(controls.translate_down)
        vertical_data.append(float(get_info(z_range_state).rstrip(' m')))

# translate down
def translate_down(correction_rate):
    for i in range(correction_rate):
        control(controls.translate_down)
        vertical_data.append(float(get_info(z_range_state).rstrip(' m')))
        sleep(1)
    for i in range(correction_rate):
        control(controls.translate_up)
        vertical_data.append(float(get_info(z_range_state).rstrip(' m')))

# single incrementation
def increment_single():
    if float(get_info(z_range_state).rstrip(' m')) < setpoint:
        control(controls.translate_up)
        sleep(1)
        control(controls.translate_down)
        vertical_data.append(float(get_info(z_range_state).rstrip(' m')))
    if float(get_info(z_range_state).rstrip(' m')) > setpoint:
        control(controls.translate_down)
        sleep(1)
        control(controls.translate_up)
        vertical_data.append(float(get_info(z_range_state).rstrip(' m')))

# return if on setpoint
def is_correct():
    if abs(kp * float(get_info(z_range_state).rstrip(' m'))) == setpoint:
        return True
    else:
        return False

# return error
def get_vertical_error():
    return abs(kp * float(get_info(z_range_state).rstrip(' m')))

# plot data
def plot_data():
    plt.plot(vertical_data, color='c', label="vertical")
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
    while int(abs(kp * float(get_info(z_range_state).rstrip(' m')))) != setpoint:
        if float(get_info(z_range_state).rstrip(' m')) < setpoint:
            translate_up(int(abs(kp * float(get_info(z_range_state).rstrip(' m')))))
        if float(get_info(z_range_state).rstrip(' m')) > setpoint:
            translate_down(int(abs(kp * float(get_info(z_range_state).rstrip(' m')))))