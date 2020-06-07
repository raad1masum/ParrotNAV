import matplotlib.pyplot as plt
import numpy as np
import random
from datetime import datetime

from simulation.sim import *
from states.states import *
from controls import controls

kp = 0.5
target = 0.0

pitch_data = []

current_datetime = datetime.now()

def pitch_left(correction_rate):
    for i in range(correction_rate):
        control(controls.pitch_left)
        pitch_data.append(float(get_info(pitch_error_state).rstrip('°')))
    for i in range(correction_rate):
        control(controls.pitch_right)
        pitch_data.append(float(get_info(pitch_error_state).rstrip('°')))

def pitch_right(correction_rate):
    for i in range(correction_rate):
        control(controls.pitch_right)
        pitch_data.append(float(get_info(pitch_error_state).rstrip('°')))
    for i in range(correction_rate):
        control(controls.pitch_left)
        pitch_data.append(float(get_info(pitch_error_state).rstrip('°')))

def increment_single():
    if float(get_info(pitch_error_state).rstrip('°')) < target:
        control(controls.pitch_left)
        control(controls.pitch_right)
        pitch_data.append(float(get_info(pitch_error_state).rstrip('°')))
    if float(get_info(pitch_error_state).rstrip('°')) > target:
        control(controls.pitch_right)
        control(controls.pitch_left)
        pitch_data.append(float(get_info(pitch_error_state).rstrip('°')))

def is_correct():
    if abs(kp * float(get_info(pitch_error_state).rstrip('°'))) == target:
        return True
    else:
        return False

def get_pitch_error():
    return abs(kp * float(get_info(pitch_error_state).rstrip('°')))

def plot_data():
    plt.plot(pitch_data, color='y')
    plt.style.use('seaborn-bright')
    plt.axhline(linewidth=4, color='b')
    plt.xlabel('Time (seconds)', fontsize=16)
    plt.ylabel('Error (°)', fontsize=16)
    plt.grid()
    plt.savefig(f'data/all/data_{current_datetime.strftime("%d-%m-%Y_%H:%M:%S")}.png')

def run():
    while int(abs(kp * float(get_info(pitch_error_state).rstrip('°')))) != target:
        if float(get_info(pitch_error_state).rstrip('°')) < target:
            pitch_left(int(abs(kp * float(get_info(pitch_error_state).rstrip('°')))))
        if float(get_info(pitch_error_state).rstrip('°')) > target:
            pitch_right(int(abs(kp * float(get_info(pitch_error_state).rstrip('°')))))