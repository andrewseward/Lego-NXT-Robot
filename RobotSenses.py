import threading
from time import sleep
from EventHook import EventHook
MIN_DRIVE_FORWARDS_DISTANCE = 40
MIN_STOP_TURNING_DISTANCE = 80
REFRESH_FREQUENCY = 0.2

class RobotSenses(threading.Thread):
    def __init__(self, robot):
        self.robot = robot
        self.OnTooClose = EventHook()
        self.OnAllClear = EventHook()
        self.OnStop = EventHook()
        self.Running = True
        threading.Thread.__init__ ( self )

    def CheckIsObstructionPresent(self, distanceFromObstacle, obstructionPresent):
        if (distanceFromObstacle < MIN_DRIVE_FORWARDS_DISTANCE and obstructionPresent == False):
            print("obstructionPresent")
            obstructionPresent = True
            self.OnTooClose.fire()
        return obstructionPresent

    def CheckIsObstructionClear(self, distanceFromObstacle, obstructionPresent):
        if (distanceFromObstacle > MIN_STOP_TURNING_DISTANCE and obstructionPresent == True):
            print("no obstructionPresent")
            obstructionPresent = False
            self.OnAllClear.fire()
        return obstructionPresent

    def IsStopButtonPressed(self):
        print("IsStopButtonPressed")
        pressed = self.robot.IsButtonPressed()
        print("IsStopButtonPressed: " + str(pressed))
        if (pressed == 1):
            print("StopButtonPressed")
            self.Running = 0
            self.OnStop.fire()

    def run ( self ):
        obstructionPresent =False
        while(self.Running==1):
            sleep(REFRESH_FREQUENCY)
            distanceFromObstacle = self.robot.getDistanceFromObstacle()
            print("distanceFromObstacle:" + str(distanceFromObstacle))
            obstructionPresent = self.CheckIsObstructionPresent(distanceFromObstacle, obstructionPresent)
            obstructionPresent = self.CheckIsObstructionClear(distanceFromObstacle, obstructionPresent)
            self.IsStopButtonPressed()