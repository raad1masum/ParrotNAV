from controller import correct_yaw, correct_roll, correct_pitch, correct_horizontal
from data import data
import threading

# set correction finished to false
yaw_finished = False
roll_finished = False
pitch_finished = False
horizontal_finished = False

# yaw correction
def yaw():
    correct_yaw.run()
    while correct_yaw.get_yaw_error() != correct_yaw.target:
        correct_yaw.increment_single()
    yaw_finished = True

# roll correction
def roll():
    correct_roll.run()
    while correct_roll.get_roll_error() != correct_roll.target:
        correct_roll.increment_single()
    roll_finished = True

# pitch correction
def pitch():
    correct_pitch.run()
    while correct_pitch.get_pitch_error() != correct_pitch.target:
        correct_pitch.increment_single()
    pitch_finished = True
    data.plot_axis() # this should go in the very last axis function

# horizontal correction
def horizontal():
    correct_horizontal.run()
    while correct_horizontal.get_horizontal_error() != correct_horizontal.target:
        correct_horizontal.increment_single()
    horizontal_finished = True
    data.plot_translation() # this should go in the very last translation function

# axis threads
yaw_thread = threading.Thread(target=yaw)
roll_thread = threading.Thread(target=roll)
pitch_thread = threading.Thread(target=pitch)

# axis start
yaw_thread.start()
roll_thread.start()
pitch_thread.start()

# translation threads
horizontal_thread = threading.Thread(target=horizontal)

# translation start
if yaw_finished and roll_finished and pitch_finished:
    horizontal_thread.start()