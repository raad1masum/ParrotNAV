from controller import correct_yaw
from data import data

correct_yaw.run()

while correct_yaw.get_yaw_error() != correct_yaw.target:
    correct_yaw.increment_single()

data.plot()