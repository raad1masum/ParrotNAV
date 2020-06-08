from controller import correct_yaw, correct_roll, correct_pitch, correct_range, correct_vertical, correct_horizontal
from data import data
import threading

# yaw correction
def yaw():
    correct_yaw.run()
    while correct_yaw.get_yaw_error() != correct_yaw.setpoint:
        correct_yaw.increment_single()
    print('ParrotNAV: Yaw Correction Complete!')

# roll correction
def roll():
    correct_roll.run()
    while correct_roll.get_roll_error() != correct_roll.setpoint:
        correct_roll.increment_single()
    print('ParrotNAV: Roll Correction Complete!')

# pitch correction
def pitch():
    correct_pitch.run()
    while correct_pitch.get_pitch_error() != correct_pitch.setpoint:
        correct_pitch.increment_single()
    print('ParrotNAV: Pitch Correction Complete!')

# range correction
def range_correction():
    correct_range.run()
    while correct_range.get_range_error() != correct_range.setpoint:
        correct_range.increment_single()
    print('ParrotNAV: Range Correction Complete!')

# vertical correction
def vertical():
    correct_vertical.run()
    while correct_vertical.get_vertical_error() != correct_vertical.setpoint:
        correct_vertical.increment_single()
    print('ParrotNAV: Vertical Correction Complete!')

# horizontal correction
def horizontal():
    correct_horizontal.run()
    while correct_horizontal.get_horizontal_error() != correct_horizontal.setpoint:
        correct_horizontal.increment_single()
    print('ParrotNAV: Horizontal Correction Complete!')


# create threads
yaw_thread = threading.Thread(target=yaw)
roll_thread = threading.Thread(target=roll)
pitch_thread = threading.Thread(target=pitch)
vertical_thread = threading.Thread(target=vertical)
horizontal_thread = threading.Thread(target=horizontal)
range_thread = threading.Thread(target=range_correction)

# start threads
yaw_thread.start()
roll_thread.start()
pitch_thread.start()
range_thread.start()
vertical_thread.start()
horizontal_thread.start()

# wait for correction to finish
yaw_thread.join()
roll_thread.join()
pitch_thread.join()
range_thread.join()
vertical_thread.join()
horizontal_thread.join()

# plot data
data.plot()