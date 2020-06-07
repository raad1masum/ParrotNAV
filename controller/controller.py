from controller import correct_yaw, correct_roll, correct_pitch
from data import data
import threading

def yaw():
    correct_yaw.run()
    while correct_yaw.get_yaw_error() != correct_yaw.target:
        correct_yaw.increment_single()

def roll():
    correct_roll.run()
    while correct_roll.get_roll_error() != correct_roll.target:
        correct_roll.increment_single()

def pitch():
    correct_pitch.run()
    while correct_pitch.get_pitch_error() != correct_pitch.target:
        correct_pitch.increment_single()
    data.plot() # this should go in the very last function

yaw_run = threading.Thread(target=yaw)
roll_run = threading.Thread(target=roll)

yaw_run.start()
roll_run.start()