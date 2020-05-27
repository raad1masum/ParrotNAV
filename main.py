from simulation import sim
from simulation.sim import *
from controls import controls
from info import info
from info.status import status

control(controls.pitch_up)

while True:
    status()