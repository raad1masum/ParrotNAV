from controller import correct_yaw, correct_roll, correct_pitch, correct_range, correct_vertical, correct_horizontal

# plot data
def plot():
    correct_yaw.plot_data()
    correct_roll.plot_data()
    correct_pitch.plot_data()
    correct_range.plot_data()
    correct_vertical.plot_data()
    correct_horizontal.plot_data()