import matplotlib.pyplot as plt
import random
from datetime import datetime

from simulation.sim import *
from states.states import *
from controls import controls

# set constants & gains
kp = 0.4
setpoint = 0.0

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
    plt.plot(pitch_data, color='y')
    plt.style.use('seaborn-bright')
    plt.axhline(linewidth=4, color='b')
    plt.xlabel('Time (seconds)', fontsize=16)
    plt.ylabel('Error (°)', fontsize=16)
    plt.grid()
    plt.savefig(f'data/axis/data_{current_datetime.strftime("%d-%m-%Y_%H:%M:%S")}.png')

# run correction loop
def run():
    while int(abs(kp * float(get_info(pitch_error_state).rstrip('°')))) != setpoint:
        if float(get_info(pitch_error_state).rstrip('°')) < setpoint:
            pitch_up(int(abs(kp * float(get_info(pitch_error_state).rstrip('°')))))
        if float(get_info(pitch_error_state).rstrip('°')) > setpoint:
            pitch_down(int(abs(kp * float(get_info(pitch_error_state).rstrip('°')))))