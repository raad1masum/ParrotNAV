from simulation import sim
from simulation.sim import *
from controls import controls
from states.states import *
from states.status import status

# control(controls.pitch_up)

while True:
    status()

    while int(yaw_error_state) < 0.0:
        for i in range(2):
            controls.yaw_left
    while int(yaw_error_state) > 0.0:
        for i in range(2):
            controls.yaw_right