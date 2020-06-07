from controller import correct_yaw, correct_roll, correct_pitch, correct_horizontal
from data import data
import threading

# yaw_finished = False
# roll_finished = False
# pitch_finished = False

# def yaw():
#     correct_yaw.run()
#     while correct_yaw.get_yaw_error() != correct_yaw.target:
#         correct_yaw.increment_single()
#     yaw_finished = True

# def roll():
#     correct_roll.run()
#     while correct_roll.get_roll_error() != correct_roll.target:
#         correct_roll.increment_single()
#     roll_finished = True

# def pitch():
#     correct_pitch.run()
#     while correct_pitch.get_pitch_error() != correct_pitch.target:
#         correct_pitch.increment_single()
#     pitch_finished = True
#     data.plot_axis() # this should go in the very last function

def horizontal():
    correct_horizontal.run()
    while correct_horizontal.get_horizontal_error() != correct_horizontal.target:
        correct_horizontal.increment_single()

# yaw_run = threading.Thread(target=yaw)
# roll_run = threading.Thread(target=roll)
# pitch_run = threading.Thread(target=pitch)

# yaw_run.start()
# roll_run.start()
# pitch_run.start()
