from simulation import sim
from simulation.sim import *
from controls import controls
from states.status import status

control(controls.pitch_up)

while True:
    status()