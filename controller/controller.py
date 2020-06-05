from controller import correct_yaw

correct_yaw.run()

while True:
    correct_yaw.increment_single()

correct_yaw.plot_data()
