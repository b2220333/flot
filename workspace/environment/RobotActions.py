from Actions import ActionEngine, Action
import RobotControl
import numpy as np
from debug import *

class RobotAction(Action):
    def __init__(self, array, v_t, w): #add teleport thing
        Action.__init__(self, array, v_t, w)

class RobotActionEngine(ActionEngine):
    def __init__(self):
        ActionEngine.__init__(self)
        self.rc = RobotControl.RobotControl()

    def __enterImpl__(self):
        self.rc.__enter__()

    def __exitImpl__(self, type, value, traceback):
        self.rc.__exit__(type, value, traceback)

    def executeActionImpl(self, obs):
        success = True
        try:
            self.rc.setCommand(self.v_t, self.w, self.z)
        except Exception as e:
            success = False
            printError("Failed to send command!")
            if hasattr(e, 'message'):
                printError(e.message)
            else:
                printError(e)

        return success
