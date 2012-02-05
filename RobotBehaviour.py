import random
import threading
from time import sleep

from RobotMode import RobotMode

MOVE_SPEED = 100
TURN_ANGLE=150
REFRESH_FREQUENCY = 0.1
__author__ = 'Mike'

class RobotBehaviour(threading.Thread):
    def __init__(self, robot, robotSenses):
        self.robot = robot
        self.robotSenses = robotSenses
        self.robotSenses.OnTooClose += self.OnTooClose
        self.robotSenses.OnAllClear += self.OnAllClear
        self.robotSenses.OnStop += self.OnStop
        self.Mode = RobotMode.Forward
        threading.Thread.__init__ ( self )

    def OnTooClose(self):
        print("RobotMode Turn")
        self.Mode = random.choice([RobotMode.Left, RobotMode.Right])
        self.robot.WarningNoise()

    def OnAllClear(self):
        print(" RobotMode.Forward")
        self.Mode = RobotMode.Forward
        self.robot.OkNoise()

    def OnStop(self):
        print("RobotMode Stop")
        self.Mode = RobotMode.Stop

    def run (self):
        self.robot.StopWalk()
        print("RobotStart")
        while(self.Mode != RobotMode.Stop):
            while(self.Mode == RobotMode.Forward):
                self.robot.StartWalk(MOVE_SPEED)
                sleep(REFRESH_FREQUENCY)
            while(self.Mode == RobotMode.Left or self.Mode == RobotMode.Right):
                self.robot.turn(self.Mode, TURN_ANGLE)
        self.robot.StopWalk()
        print("RobotStopping")