from controller import correct_yaw

while not correct_yaw.is_correct:
    correct_yaw.increment_single()

correct_yaw.plot_data()
