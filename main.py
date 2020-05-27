from simulation import sim
from simulation.sim import *
from controls import controls
from info import info

control(controls.pitch_up)

while True:
    print(get_info(info.pitch_error))