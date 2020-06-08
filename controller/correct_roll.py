import matplotlib.pyplot as plt
import random
from datetime import datetime

from PID.pid_controller import *
from simulation.sim import *
from states.states import *
from controls import controls

# set constants & gains
kp = roll_kp
setpoint = roll_setpoint

# data for plotting
roll_data = []

# set current date & time
current_datetime = datetime.now()

# roll left
def roll_left(correction_rate):
    for i in range(correction_rate):
        control(controls.roll_left)
        roll_data.append(float(get_info(roll_error_state).rstrip('°')))
    for i in range(correction_rate):
        control(controls.roll_right)
        roll_data.append(float(get_info(roll_error_state).rstrip('°')))

# roll right
def roll_right(correction_rate):
    for i in range(correction_rate):
        control(controls.roll_right)
        roll_data.append(float(get_info(roll_error_state).rstrip('°')))
    for i in range(correction_rate):
        control(controls.roll_left)
        roll_data.append(float(get_info(roll_error_state).rstrip('°')))

# single incrementation
def increment_single():
    if float(get_info(roll_error_state).rstrip('°')) < setpoint:
        control(controls.roll_left)
        control(controls.roll_right)
        roll_data.append(float(get_info(roll_error_state).rstrip('°')))
    if float(get_info(roll_error_state).rstrip('°')) > setpoint:
        control(controls.roll_right)
        control(controls.roll_left)
        roll_data.append(float(get_info(roll_error_state).rstrip('°')))

# return if on setpoint
def is_correct():
    if abs(kp * float(get_info(roll_error_state).rstrip('°'))) == setpoint:
        return True
    else:
        return False

# return error
def get_roll_error():
    return abs(kp * float(get_info(roll_error_state).rstrip('°')))

# plot data
def plot_data():
    plt.plot(roll_data, color='g', label="roll")
    plt.style.use('seaborn-bright')
    plt.axhline(linewidth=4, color='b')
    plt.title('Vehicle Error in Degrees Over Time in Seconds', fontsize=14)
    plt.legend(loc='upper right')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Error (°)')
    plt.grid()
    plt.savefig(f'data/plots/data_{current_datetime.strftime("%d-%m-%Y_%H:%M:%S")}.png')

# run correction loop
def run():
    while int(abs(kp * float(get_info(roll_error_state).rstrip('°')))) != setpoint:
        if float(get_info(roll_error_state).rstrip('°')) < setpoint:
            roll_left(int(abs(kp * float(get_info(roll_error_state).rstrip('°')))))
        if float(get_info(roll_error_state).rstrip('°')) > setpoint:
            roll_right(int(abs(kp * float(get_info(roll_error_state).rstrip('°')))))