from controller import correct_yaw, correct_roll, correct_pitch, correct_horizontal

# generate axis plot
def plot_axis():
    correct_yaw.plot_data()
    correct_roll.plot_data()
    correct_pitch.plot_data()

# generate translation plot
def plot_translation():
    correct_horizontal.plot_data()