from controller import correct_yaw, correct_roll
from data import data

correct_roll.run()
while correct_roll.get_roll_error() != correct_roll.target:
    correct_roll.increment_single()

correct_roll.plot_data()

# correct_yaw.run()
# while correct_yaw.get_yaw_error() != correct_yaw.target:
#     correct_yaw.increment_single()

# data.plot()