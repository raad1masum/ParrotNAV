from controller import correct_yaw

correct_yaw.run()

while correct_yaw.get_yaw_error() != 0.0:
    correct_yaw.increment_single()

correct_yaw.plot_data()
