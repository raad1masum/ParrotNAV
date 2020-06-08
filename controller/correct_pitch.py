import matplotlib.pyplot as plt
import random
from datetime import datetime

from PID.pid_controller import *
from simulation.sim import *
from states.states import *
from controls import controls

# set constants & gains
kp = pitch_kp
setpoint = pitch_setpoint

# data for plotting
pitch_data = []

# set current date & time
current_datetime = datetime.now()

# pitch up
def pitch_up(correction_rate):
    for i in range(correction_rate):
        control(controls.pitch_up)
        pitch_data.append(float(get_info(pitch_error_state).rstrip('°')))
    for i in range(correction_rate):
        control(controls.pitch_down)
        pitch_data.append(float(get_info(pitch_error_state).rstrip('°')))

# pitch down
def pitch_down(correction_rate):
    for i in range(correction_rate):
        control(controls.pitch_down)
        pitch_data.append(float(get_info(pitch_error_state).rstrip('°')))
    for i in range(correction_rate):
        control(controls.pitch_up)
        pitch_data.append(float(get_info(pitch_error_state).rstrip('°')))

# single incrementation
def increment_single():
    if float(get_info(pitch_error_state).rstrip('°')) < setpoint:
        control(controls.pitch_up)
        control(controls.pitch_down)
        pitch_data.append(float(get_info(pitch_error_state).rstrip('°')))
    if float(get_info(pitch_error_state).rstrip('°')) > setpoint:
        control(controls.pitch_down)
        control(controls.pitch_up)
        pitch_data.append(float(get_info(pitch_error_state).rstrip('°')))

# return if on setpoint
def is_correct():
    if abs(kp * float(get_info(pitch_error_state).rstrip('°'))) == setpoint:
        return True
    else:
        return False

# return error
def get_pitch_error():
    return abs(kp * float(get_info(pitch_error_state).rstrip('°')))

# plot data
def plot_data():
    plt.plot(pitch_data, color='y', label="pitch")
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
    while int(abs(kp * float(get_info(pitch_error_state).rstrip('°')))) != setpoint:
        if float(get_info(pitch_error_state).rstrip('°')) < setpoint:
            pitch_up(int(abs(kp * float(get_info(pitch_error_state).rstrip('°')))))
        if float(get_info(pitch_error_state).rstrip('°')) > setpoint:
            pitch_down(int(abs(kp * float(get_info(pitch_error_state).rstrip('°')))))