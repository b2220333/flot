import AirSimControl
from Actions import ActionEngine
import numpy as np
from debug import *

class AirSimAction():
    def __init__(self, v_t):
        self.



class AirSimActionEngine(ActionEngine):
    def __init__(self, act_dim=11, max_v_t=1.0, max_w=1.0):
        ActionEngine.__init__(self, act_dim, max_v_t, max_w)
        self.asc = AirSimControl.AirSimControl()

    def __enterImpl__(self):
        self.asc.__enter__()

    def __exitImpl__(self, type, value, traceback):
        self.asc.__exit__(type, value, traceback)

    def reset(self, pose=None):
        if pose is not None:
            self.home_pose = pose
        self.asc.setPose(self.home_pose)

    def executeActionImpl(self, obs):
        success = True
        try:
            if obs.serializable['hasCollided'].val:
                self.reset()
            self.asc.setCommand(self.v_t, self.w)
            # print(self.v_t, self.w)
        except:
            success = False
            printError("Failed to execute command in AirSim!")
        return success
