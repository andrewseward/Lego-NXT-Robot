from time import sleep
from Robot import Robot
from RobotBehaviour import RobotBehaviour
from RobotMode import RobotMode
from RobotSenses import RobotSenses



def Start():
    r'''Connects to a nearby Alpha Rex, then commands it to walk forward and
        then backwards.
    '''

    print("START ROBOT WALK")
    robot = Robot()
    robotSenses = RobotSenses(robot)
    robotBehaviour = RobotBehaviour(robot, robotSenses)
    print("robotSenses.start")
    robotSenses.start()
    print("robotBehaviour.start")
    robotBehaviour.start()

    while(robotBehaviour.Mode != RobotMode.Stop):
        sleep(0.1)
    print("FINISHED")
if __name__ == '__main__':
    Start()

