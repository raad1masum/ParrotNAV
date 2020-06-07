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
    while correct_yaw.get_yaw_error() != correct_yaw.setpoint:
        correct_yaw.increment_single()
    yaw_finished = True

# roll correction
def roll():
    correct_roll.run()
    while correct_roll.get_roll_error() != correct_roll.setpoint:
        correct_roll.increment_single()
    roll_finished = True

# pitch correction
def pitch():
    correct_pitch.run()
    while correct_pitch.get_pitch_error() != correct_pitch.setpoint:
        correct_pitch.increment_single()
    pitch_finished = True

# horizontal correction
def horizontal():
    correct_horizontal.run()
    while correct_horizontal.get_horizontal_error() != correct_horizontal.setpoint:
        correct_horizontal.increment_single()
    horizontal_finished = True
    data.plot() # this should go in the very last function

# axis threads
yaw_thread = threading.Thread(target=yaw)
roll_thread = threading.Thread(target=roll)
pitch_thread = threading.Thread(target=pitch)

horizontal_thread = threading.Thread(target=horizontal)

# axis start
yaw_thread.start()
roll_thread.start()
pitch_thread.start()

horizontal_thread.start()

# wait for axis correction to finish
yaw_thread.join()
roll_thread.join()
pitch_thread.join()

horizontal_thread.join()

# translation threads
# horizontal_thread = threading.Thread(target=horizontal)

# translation start
# horizontal_thread.start()