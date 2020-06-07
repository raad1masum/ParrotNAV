from controller import correct_yaw, correct_roll
import threading

def yaw():
    correct_yaw.run()
    while correct_yaw.get_yaw_error() != correct_yaw.target:
        correct_yaw.increment_single()
    correct_yaw.plot_data()

def roll():
    correct_roll.run()
    while correct_roll.get_roll_error() != correct_roll.target:
        correct_roll.increment_single()
    correct_roll.plot_data()

yaw_run = threading.Thread(target=yaw)
roll_run = threading.Thread(target=roll)

yaw_run.start()
roll_run.start()